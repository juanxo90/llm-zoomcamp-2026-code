# LLM Zoomcamp 2026 Project

This repository contains the project files and notebooks for the LLM Zoomcamp 2026 course.

## Project Overview

This project demonstrates the implementation of Retrieval-Augmented Generation (RAG) techniques using local Large Language Models and the LangChain framework.

**Key Implementation Details:**
*   **Model Interaction:** The project primarily utilizes local models via `ChatOllama` for LLM interactions, opting for local execution instead of relying on external APIs like OpenAI.
*   **Framework:** LangChain is used to orchestrate the RAG pipeline, document retrieval, and tool-calling.

## Notebook Content Note

**Please note:** The notebooks in this repository primarily contain the only code and comments with a brief explanation the implementation steps. Detailed, in-depth notes or theoretical explanations are not provided within the notebook cells themselves. This is an inspiration from the [LLM Zoomcamp 2026](https://github.com/DataTalksClub/llm-zoomcamp). 

## Files

*   `Modelfile`: Configuration for the local model.
*   `pyproject.toml`: Project dependencies and configuration.
*   `week_1/`: Contains Jupyter notebooks detailing the implementation of various RAG and function-calling concepts.
*   `week_2/`: Contains Jupyter notebooks with the vector search module.

## Setup

This project uses `uv` to install Python dependencies from `pyproject.toml` and to configure the extra PyTorch index defined in the `tool.uv.index` section.

1. Install Python 3.12 or later.
2. Install `uv` globally or in a separate bootstrap environment:

```bash
python -m pip install --upgrade pip
python -m pip install uv
```

3. Create and activate a virtual environment (recommended):

```bash
python -m venv .venv
source .venv/bin/activate
```

4. Install the repository dependencies with `uv` from the project root:

```bash
uv install
```

This will read `pyproject.toml` and install packages including `langchain-ollama`, `ollama`, `torch`, and `torchvision` using the custom `pytorch-cu126` index configured in `tool.uv.index`.

5. Verify the environment by running a simple Python import test:

```bash
python -c "import langchain_ollama, ollama, torch; print('Installed:', langchain_ollama.__name__, ollama.__name__, torch.__version__)"
```

> Note: If you are using a GPU-enabled system, `uv` will install the CUDA-aware PyTorch wheels from the configured `pytorch-cu126` index on Linux and Windows.

