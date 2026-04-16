from openai import OpenAI


class AIClient:

    def __init__(self, api_key):
        if not api_key:
            raise ValueError(
                "OPENAI_API_KEY is missing. Add it to your .env file before generating drafts."
            )

        self.client = OpenAI(api_key=api_key)

        # 🔒 Hard-set model and token limit
        self.model = "gpt-4o-mini"
        self.max_tokens = 10000

    def chat(self, messages, temperature=0.2):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            max_tokens=self.max_tokens,
            temperature=temperature,
        )
        return (response.choices[0].message.content or "").strip()
