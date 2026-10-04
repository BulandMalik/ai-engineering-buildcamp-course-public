from pathlib import Path

from gitsource import chunk_documents
from minsearch import Index

import json

from dotenv import load_dotenv
from openai import AzureOpenAI
from pydantic import BaseModel, Field
from typing import Literal


import os

load_dotenv()

instructions = """
You're a course assistant, your task is to answer the QUESTION from the
course students using the provided CONTEXT
"""

prompt_template = """
<QUESTION>
{question}
</QUESTION>

<CONTEXT>
{context}
</CONTEXT>
""".strip()

HERE = Path(__file__).resolve().parent
TEXT_DIR = HERE / "books_text"


class RAGResponse(BaseModel):
    answer: str = Field(description="The main answer to the user's question in markdown")
    found_answer: bool = Field(description="True if relevant information was found in the documentation")
    confidence: float = Field(description="Confidence score from 0.0 to 1.0")
    confidence_explanation: str = Field(description="Explanation about the confidence level")
    answer_type: Literal["how-to", "explanation", "troubleshooting", "comparison", "reference"] = Field(description="The category of the answer")
    followup_questions: list[str] = Field(description="Suggested follow-up questions")

def load_documents(text_dir: Path = TEXT_DIR) -> list[dict]:
    # Read every markdown book and return one dictionary per file.
    # source is the filename. content is the non-empty lines, still a list.
    documents = []
    # glob("*.md") lists every markdown file in books_text. The * matches
    # any filename, so Think Python 2e.md is included and a .pdf is not.
    # sorted keeps the books in the same order each run.
    for path in sorted(text_dir.glob("*.md")):
        lines = path.read_text(encoding="utf-8").splitlines()
        # strip() removes leading and trailing whitespace. A blank line and
        # a line of only spaces both become "", which is false, so they are
        # dropped. A line with any real text is kept.
        content = [line for line in lines if line.strip()]
        documents.append({
            "source": path.name,
            "content": content,
        })
    return documents


def getDocumentChunkLength(documents, bookName):
    # Find one book by filename, chunk only that book, and print how many
    # lines and chunks it produced, plus where the first and last chunks sit.
    # Read the inside from the for, then the if, then the value at the front.
    # This is the same as:
    #   docs = []
    #   for d in documents:
    #       if d['source'].startswith(bookName):
    #           docs.append(d)
    # documents is the full list of book dictionaries. Each d is one book,
    # so d['source'] is the filename, such as "Think Python 2e.md".
    # startswith(bookName) is true when that filename begins with the text
    # passed in. The d at the front is what gets stored, so docs contains
    # the matching dictionaries, not just the filenames.
    #
    # Pattern: result = [what_to_keep for item in collection if condition]
    docs = [d for d in documents if d['source'].startswith(bookName)]
    chunks = chunk_documents(docs, size=100, step=50)
    print(docs[0]['source'], 'lines', len(docs[0]['content']), 'chunks', len(chunks))
    print('first start', chunks[0]['start'], 'last start', chunks[-1]['start'], 'last lines', len(chunks[-1]['content']))


def createIndex(chunks) -> Index:
    documents = []
    for chunk in chunks:
        doc = chunk.copy()
        doc["content"] = "\n".join(chunk["content"])
        documents.append(doc)

    # Empty index. text_fields says content is the searchable text:
    # minsearch splits it into words and ranks chunks by the query.
    # source and start stay on each chunk, but they are not searched.
    # fit on the next line loads the chunks into this index.
    index = Index(text_fields=["content"])
    index.fit(documents)
    #print total chunks we indexed
    print(f"indexed {len(documents)} chunks")
    return index

def searchIndex(index, query, max_results=10):
    results = index.search(query, num_results=max_results)
    return results

def printSearchResults(results):
    print(f"search results: {results}")


def build_prompt(question, search_results):
    context = json.dumps(search_results, indent=2)
    prompt = prompt_template.format(
        question=question,
        context=context
    ).strip()
    return prompt

def search(index, question):
    return index.search(question, num_results=5)

def llm(openai_client, user_prompt, instructions, output_type=RAGResponse, model='gpt-4o-mini'):
    messages = []

    if instructions is not None:
        messages.append({
            "role": "system",
            "content": instructions
        })

    messages.append({
        "role": "user",
        "content": user_prompt
    })

    """response = openai_client.responses.create(
        model=model,
        input=messages,
        text_format=output_type
    )

    #print Usage response
    print("Usage response: ", response.usage)
    return response.output_text"""

    response = openai_client.responses.parse(
        model=model,
        input=messages,
        text_format=output_type
    )
    
    print("output_parsed: ", response.output_parsed)
    #print usage metrics
    print("Usage metrics: ", response.usage)
    return response.output_text


def rag(index, query, output_type=RAGResponse) -> str:

    deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]

    client = AzureOpenAI(
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
        azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
        api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    )

    search_results = search(index, query)
    prompt = build_prompt(query, search_results)
    answer = llm(client, prompt, instructions, model=deployment_name, output_type=output_type)
    return answer

def main() -> None:
    # Load every book, split all of them into overlapping chunks, print
    # sizes, then print the chunk count for Think Python 2e.
    documents = load_documents()
    chunks = chunk_documents(documents, size=100, step=50)

    char_lengths = []
    word_lengths = []
    for chunk in chunks:
        text = "\n".join(chunk["content"])
        char_lengths.append(len(text))
        word_lengths.append(len(text.split()))

    print(f"documents: {len(documents)}")
    for doc in documents:
        print(f"  {doc['source']}: {len(doc['content'])} lines")
    print(f"chunks: {len(chunks)}")
    if chunks:
        print(f"avg characters: {sum(char_lengths) / len(char_lengths):.0f}")
        print(f"avg words: {sum(word_lengths) / len(word_lengths):.0f}")

    print("checking chunks for Think Python 2e")
    # Read the inside from the for, then the if, then the value at the front.
    getDocumentChunkLength(documents, 'Think Python 2e')

    #Creating Index For Semantic Search and Embeddings
    index = createIndex(chunks)
    print("index created")

    #Search the index for a query
    query = "python function definition"
    print("\n\nsearching index for query: ", query)
    results = searchIndex(index, query, max_results=5)
    printSearchResults(results)

    answer = rag(index, query, output_type=RAGResponse)
    print("\n\nRAG Answer: ", answer)

if __name__ == "__main__":
    main()
