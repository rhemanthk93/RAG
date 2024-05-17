import os
from openai import OpenAI

# Define your OpenAI API key
OPENAI_API_KEY = ""  # Replace with your actual API key


def test_openai_api():
    try:
        client = OpenAI(api_key=OPENAI_API_KEY)
        response = client.chat.completions.create(
            model="gpt-4",  # Use the GPT-4 model
            messages=[
                {"role": "user", "content": "How to say hi in tamil"}
            ],
            max_tokens=50
        )

        # Extract and print specific details
        answer = response.choices[0].message.content.strip()
        completion_tokens = response.usage.completion_tokens
        prompt_tokens = response.usage.prompt_tokens
        total_tokens = response.usage.total_tokens

        print("API Response:", answer)
        print("Completion Tokens:", completion_tokens)
        print("Prompt Tokens:", prompt_tokens)
        print("Total Tokens:", total_tokens)

    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    test_openai_api()
