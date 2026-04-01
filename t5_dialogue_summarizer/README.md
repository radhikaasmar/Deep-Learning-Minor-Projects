# Dialogue Summarizer

This repository contains a FastAPI-based dialogue summarization app using a T5 model from `transformers` and `torch`.

## Setup

1. Run `t5_dialogue_summarizer.ipynb` file

   Make sure the `saved_summary_model` folder is placed in the root directory of this project.

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



