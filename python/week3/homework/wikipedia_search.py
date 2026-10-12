from GetPageTool import GetPageTool
from SearchWikipediaTool import SearchWikipediaTool


def question1_answer(query="capybara", verbose=False):
    # First page of search hits. len(hits) is the query.search count.
    # total is searchinfo.totalhits, every matching page on Wikipedia.
    results = SearchWikipediaTool(verbose=verbose)(query, limit=10, cap=10)
    print(f"query.search count: {len(results['hits'])}")
    print(f"searchinfo.totalhits: {results['total']}")
    return {
        "query_search_count": len(results["hits"]),
        "totalhits": results["total"],
    }


def question2_answer(query="capybara", verbose=False):
    # Same first page of titles as question 1.
    results = SearchWikipediaTool(verbose=verbose)(query, cap=10)
    word = query.lower()
    matches = [
        hit["title"]
        for hit in results["hits"]
        if word in hit["title"].lower()
    ]
    print(f"titles checked: {len(results['hits'])}")
    print(f"titles containing {word!r}: {len(matches)}")
    return len(matches)


def question3_answer(title="Capybara", verbose=False):
    characters = GetPageTool(verbose=verbose)(title)
    print(f"page: {title}")
    print(f"characters: {characters}")
    return characters


def main():
    query = input("Enter a search query: ")

    print("-------------Question 1-------------------")
    question1_answer(query=query)
    print("-------------Question 2-------------------")
    question2_answer(query=query)
    print("-------------Question 3-------------------")
    question3_answer(title=query, verbose=True)


if __name__ == "__main__":
    main()
