# 🚀 NeuroServe -- GPU-Ready FastAPI AI Server

[![Python](https://img.shields.io/badge/Python-3.12%2B-blue.svg)](https://www.python.org/)\
[![FastAPI](https://img.shields.io/badge/FastAPI-0.116.1-009688.svg)](https://fastapi.tiangolo.com/)\
[![PyTorch](https://img.shields.io/badge/PyTorch-2.6.0%2B-ee4c2c.svg)](https://pytorch.org/)\
[![Tests](https://github.com/USERNAME/REPO/actions/workflows/tests.yml/badge.svg)](https://github.com/USERNAME/REPO/actions)\
[![License:
MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)

------------------------------------------------------------------------

## 📖 Overview

**NeuroServe** is an **AI Inference Server** built on
[FastAPI](https://fastapi.tiangolo.com/) designed to run seamlessly on
**GPU / CPU / ROCm / macOS MPS**.\
It provides:

-   🌐 **Ready-to-use REST API** with Swagger UI & ReDoc\
-   ⚡ **PyTorch integration** (CUDA / ROCm / CPU / MPS)\
-   🧠 **Prefetch scripts** for Hugging Face models (BART, DistilBERT,
    mT5, Whisper, TinyLlama, ResNet18...)\
-   🔧 **install_torch.py** script for automatic PyTorch installation\
-   📊 Runtime utilities to inspect GPU & benchmark performance (CUDA
    info + warmup)\
-   🧩 Example TinyNet model & **MLP memory size calculator**\
-   📚 Unified `unify_response` utility for consistent model/API outputs

------------------------------------------------------------------------

## 📂 Project Structure

    gpu-server/
    ├── app/                # Core server (FastAPI + Runtime + Models)
    │   ├── main.py         # FastAPI entrypoint
    │   ├── runtime.py      # Device & CUDA management
    │   ├── toy_model.py    # Simple PyTorch model
    │   └── utils/          # Utilities (unified responses)
    ├── scripts/            # Helper scripts
    │   ├── install_torch.py  # Auto PyTorch installer
    │   ├── prefetch_models.py # Download Hugging Face models
    │   └── conftest.py       # PyTest fixtures
    ├── docs/               # Docs & licenses
    ├── requirements.txt    # Core dependencies
    ├── requirements-dev.txt# Dev/test dependencies
    ├── pyproject.toml      # Ruff + PyTest + Coverage configs
    └── LICENSE             # MIT License

------------------------------------------------------------------------

## ⚙️ Installation

### 1. Clone the repo

``` bash
git clone https://github.com/USERNAME/gpu-server.git
cd gpu-server
```

### 2. Create virtual environment

``` bash
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate    # Windows
```

### 3. Install dependencies

``` bash
pip install -r requirements.txt
```

### 4. (Optional) Auto-install PyTorch

``` bash
python -m scripts.install_torch --gpu   # or --cpu / --rocm
```

### 5. Run the server

``` bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

------------------------------------------------------------------------

## 🖥️ Usage

Once running, open your browser:

-   <http://localhost:8000/> → Home\
-   <http://localhost:8000/docs> → Swagger UI\
-   <http://localhost:8000/redoc> → ReDoc\
-   <http://localhost:8000/health> → Health check
- http://localhost:8000/env

Example request:

``` bash
curl http://localhost:8000/health
# {"status": "ok"}
```

------------------------------------------------------------------------

## 🧪 Development & Testing

Install dev requirements:

``` bash
pip install -r requirements-dev.txt
pre-commit install
```

Run tests:

``` bash
pytest
```

------------------------------------------------------------------------

## 📊 Prefetch Models

To download supported models into `models_cache/`:

``` bash
python -m scripts.prefetch_models
```

Included models: - 📄 NLP: BART, DistilBERT, mT5, TinyLlama\
- 🎙️ Speech: Whisper\
- 🖼️ Vision: ResNet18

------------------------------------------------------------------------

## 🤝 Contributing

Contributions are welcome!\
- Open **Issues** for ideas or bugs.\
- Use **Pull Requests** for changes.\
- Follow code style (Ruff + pre-commit).

------------------------------------------------------------------------

## 📜 License

This project is licensed under the **MIT License** -- see
[LICENSE](./LICENSE).\
\> Some models have their own licenses -- see
[docs/LICENSES.md](docs/LICENSES.md).
