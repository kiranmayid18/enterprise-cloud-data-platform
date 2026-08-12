import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
CONFIG_FILE = BASE_DIR / "config" / "pipeline_config.json"

def load_config():
    with CONFIG_FILE.open("r", encoding="utf-8") as f:
        return json.load(f)
