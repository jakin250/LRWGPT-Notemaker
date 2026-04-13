import os

from dotenv import load_dotenv


load_dotenv()


def _as_bool(value, default=False):
    if value is None:
        return default

    return value.strip().lower() in {"1", "true", "yes", "on"}


def get_config():
    return {
        "api_key": os.getenv("OPENAI_API_KEY"),
        "model": os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        "max_tokens": int(os.getenv("OPENAI_MAX_TOKENS", "4000")),
        "temperature": float(os.getenv("OPENAI_TEMPERATURE", "0.2")),
        "max_input_chars": int(os.getenv("LRW_MAX_INPUT_CHARS", "120000")),
        "max_upload_mb": int(os.getenv("MAX_UPLOAD_MB", "20")),
        "secret_key": os.getenv("FLASK_SECRET_KEY", "lrw-gpt-local-dev"),
        "host": os.getenv("FLASK_HOST", "0.0.0.0"),
        "port": int(os.getenv("FLASK_PORT", "5000")),
        "debug": _as_bool(os.getenv("FLASK_DEBUG"), default=False),
        "input_folder": "input_pdfs",
        "output_folder": "output",
        "log_folder": "logs",
    }
