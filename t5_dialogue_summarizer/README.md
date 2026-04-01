# Dialogue Summarizer

This repository contains a FastAPI-based dialogue summarization app using a T5 model from `transformers` and `torch`.

## Setup


2. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # macOS/Linux
   # .venv\Scripts\activate  # Windows
   ```

3. Upgrade pip and install packages:
   ```bash
   pip install --upgrade pip
   pip install fastapi uvicorn pydantic transformers sentencepiece torch
   ```

## Run

```bash
uvicorn app:app --reload --host 127.0.0.1 --port 8000
```

Then open: `http://127.0.0.1:8000`

## Notes

- In `app.py`, use `from fastapi import FastAPI, Request` (not `Requests`).
- If your editor says `import 'fastapi' could not be resolved`, ensure VS Code uses `.venv` interpreter and restart the window.

## Optional dependencies

- `uvicorn[standard]` (for production-ready async performance)
- `transformers[sentencepiece]` (for some tokenizers)

## Minimal lint/sanity check

```bash
python -c "from fastapi import FastAPI; print('fastapi', FastAPI)"
python -c "from transformers import T5ForConditionalGeneration, T5Tokenizer; print('transformers loaded')"
```
