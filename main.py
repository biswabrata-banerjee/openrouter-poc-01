"""Minimal OpenRouter chat completion using the official Python SDK."""

import os
import sys

from dotenv import load_dotenv
from openrouter import OpenRouter

# MODEL = "nvidia/nemotron-3-super-120b-a12b:free"
MODEL = "stepfun/step-3.5-flash:free"


def main() -> None:
    load_dotenv()
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        print(
            "Missing OPENROUTER_API_KEY. Copy .env.example to .env and set your key, "
            "or export the variable in your shell.",
            file=sys.stderr,
        )
        sys.exit(1)

    with OpenRouter(api_key=api_key) as client:
        response = client.chat.send(
            model=MODEL,
            messages=[
                {"role": "user", "content": "Explain what is linked list"},
            ],
            stream=False,
        )

    content = response.choices[0].message.content
    print(content)


if __name__ == "__main__":
    main()
