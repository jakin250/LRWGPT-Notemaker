from openai import OpenAI


class AIClient:

    def __init__(self, api_key):
        if not api_key:
            raise ValueError(
                "OPENAI_API_KEY is missing. Add it to your .env file before generating drafts."
            )

        self.client = OpenAI(api_key=api_key)

    def chat(self, model, messages, max_tokens, temperature=0.2):
        response = self.client.chat.completions.create(
            model=model,
            messages=messages,
            max_tokens=max_tokens,
            temperature=temperature,
        )
        return (response.choices[0].message.content or "").strip()
