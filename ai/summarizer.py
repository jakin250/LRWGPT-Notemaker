from ai.client import AIClient
from ai.prompts import build_messages


class LegalDraftGenerator:

    def __init__(self, config):
        self.client = AIClient(config["api_key"])
        self.temperature = config.get("temperature", 0.2)

    def generate(
        self,
        text,
        prompt_id,
        audience_id,
        custom_instructions="",
        draft_title="",
    ):
        messages = build_messages(
            prompt_id=prompt_id,
            text=text,
            audience_id=audience_id,
            custom_instructions=custom_instructions,
            draft_title=draft_title,
        )

        return self.client.chat(
            messages=messages,
            temperature=self.temperature,
        )


class Summarizer(LegalDraftGenerator):
    pass
