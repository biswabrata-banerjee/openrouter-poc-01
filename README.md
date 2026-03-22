# openrouter-poc-01

Experiments with the [OpenRouter Python SDK](https://openrouter.ai/docs/sdks/python) (package `openrouter` on PyPI).

## Requirements

- Python 3.9 or newer
- An [OpenRouter API key](https://openrouter.ai/settings/keys)

## Setup

1. Create and activate a virtual environment:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   On macOS or Linux:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. Install this project in editable mode (installs `openrouter` and `python-dotenv` from `pyproject.toml`):

   ```bash
   pip install -e .
   ```

   Alternatively, with [uv](https://docs.astral.sh/uv/): `uv sync` (if you add a `uv.lock` later) or `uv pip install -e .`.

3. Configure the API key. Copy `.env.example` to `.env` and set your key:

   ```
   OPENROUTER_API_KEY=sk-or-v1-...
   ```

   Or export `OPENROUTER_API_KEY` in the shell instead of using a `.env` file.

## Run

```bash
python main.py
```

The sample uses the free model `minimax/minimax-m2.5:free`. Change the `MODEL` constant in `main.py` to try others.

## Troubleshooting

- **`ModuleNotFoundError: No module named 'openrouter'`** — Run with the project virtual environment’s Python (activate `.venv`, or use `.venv\Scripts\python.exe main.py` on Windows). In Cursor/VS Code, pick **Python: Select Interpreter** and choose `.venv`, or rely on [`.vscode/settings.json`](.vscode/settings.json) which pins the workspace interpreter.
- If the API returns an error about **guardrails or data policy**, adjust [privacy settings](https://openrouter.ai/settings/privacy) on your OpenRouter account so the chosen model is allowed.
- Free models and rate limits are described in the [OpenRouter FAQ](https://openrouter.ai/docs/faq#how-are-rate-limits-calculated).

Important step to perform in your Openrouter Account:
https://openrouter.ai/workspaces/default/guardrails
Setup guardrail.
API Key & Member Guardrails > Click Create, assing which API key (if more than one) > save
Only then it will allow you to use the free model.