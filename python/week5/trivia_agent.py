import os

from dotenv import load_dotenv
from openai import AsyncAzureOpenAI
from pydantic import BaseModel, Field
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.azure import AzureProvider
import httpx2
import logfire

from trivia_tools import TriviaTools

load_dotenv()

class TriviaAgent:

    # Quiz behavior lives in this prompt. main.py only repeats the call and
    # keeps message_history. There is no code that picks the next question.
    instructions = """You are a trivia quizmaster. Play one question per reply, then stop and wait.

        Setup, on the first request only:
        - If the player names a category, call get_categories and use the matching id.
        - Call get_questions once with the requested amount and difficulty.
        - Remember every question, the correct answer, and the wrong answers.
        - Do not fetch questions again during the quiz.

        Each question:
        - Ask one question only.
        - Show four choices labeled A, B, C, and D. Mix the correct answer among the wrong ones.
        - Do not reveal the correct answer in this message.
        - Stop. Wait for the player's next message.

        After the player answers:
        - Say whether they are right or wrong.
        - Give the correct answer and a short explanation.
        - If questions remain, ask the next one in the same message, using the same choice rules.
        - If that was the last question, do not ask another. End with a line that starts with "Final score:" and the score, such as "Final score: 2/3".
    """    
    
    def __init__(self, name: str, logfire: logfire):
        self.tools = TriviaTools()
        self.name = name
        self.logfire = logfire
        self.agent = Agent(
            self._azure_model(),
            name=name,
            instructions=self.instructions,
            tools=[self.tools.get_questions, self.tools.get_categories],
        )

    def _azure_model(self) -> OpenAIChatModel:
        timeout = httpx2.Timeout(
            connect=float(os.environ["OPENAI_CLIENT_CONNECT_TIMEOUT"]),
            read=float(os.environ["OPENAI_CLIENT_READ_TIMEOUT"]),
            write=float(os.environ["OPENAI_CLIENT_WRITE_TIMEOUT"]),
            pool=float(os.environ["OPENAI_CLIENT_POOL_TIMEOUT"]),
        )
        client = AsyncAzureOpenAI(
            api_key=os.environ["AZURE_OPENAI_API_KEY"],
            azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
            api_version=os.environ["AZURE_OPENAI_API_VERSION"],
            timeout=timeout,
        )
        return OpenAIChatModel(
            os.environ["AZURE_OPENAI_DEPLOYMENT"],
            provider=AzureProvider(openai_client=client),
        )
    
