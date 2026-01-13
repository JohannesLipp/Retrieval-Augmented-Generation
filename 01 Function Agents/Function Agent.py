# Based on https://developers.llamaindex.ai/python/framework/getting_started/starter_example_local/

import asyncio

from llama_index.core.agent.workflow import FunctionAgent
from llama_index.llms.ollama import Ollama


# Define a simple calculator tool
def multiply(a: float, b: float) -> float:
    """Useful for multiplying two numbers."""
    return a * b


def is_prime(n: int) -> bool:
    """Useful to determine if a number is prime."""
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


is_prime_agent = FunctionAgent(
    tools=[is_prime],
    llm=Ollama(
        model="llama3.1",
        request_timeout=360.0,
        # Manually set the context window to limit memory usage
        context_window=8000,
    ),
    system_prompt="You are a helpful assistant that can determine if a number is prime. Use a markdown table as output.",
)

multiply_agent = FunctionAgent(
    tools=[multiply],
    llm=Ollama(
        model="llama3.1",
        request_timeout=360.0,
        # Manually set the context window to limit memory usage
        context_window=8000,
    ),
    system_prompt="You are a helpful assistant that can multiply two numbers.",
)


async def main():
    response = await is_prime_agent.run(
        "For each of the following numbers, tell me if they are prime or not: 24, 37,29,5017, 5713, 9999")
    # response = await multiply_agent.run("What is 12345679 * 9?")
    print(str(response))


# Run the agent
if __name__ == "__main__":
    asyncio.run(main())
