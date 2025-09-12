<<<<<<< HEAD
# 🚀 NeuroServe — GPU-Ready FastAPI AI Server

## 📊 Project Status

| Category      | Badges |
|---------------|--------|
| **Languages** | ![Python](https://img.shields.io/badge/Python-3.12%2B-blue) ![HTML](https://img.shields.io/badge/HTML-5-orange) ![CSS](https://img.shields.io/badge/CSS-3-blueviolet) |
| **Framework** | ![FastAPI](https://img.shields.io/badge/FastAPI-0.116.x-009688) |
| **ML / GPU**  | ![PyTorch](https://img.shields.io/badge/PyTorch-2.6.x-ee4c2c) ![CUDA Ready](https://img.shields.io/badge/CUDA-Ready-76B900?logo=nvidia&logoColor=white) |
| **CI**        | [![Ubuntu CI](https://github.com/TamerOnLine/repo-fastapi/actions/workflows/ci-ubuntu.yml/badge.svg)](https://github.com/TamerOnLine/repo-fastapi/actions/workflows/ci-ubuntu.yml) [![Windows CI](https://github.com/TamerOnLine/repo-fastapi/actions/workflows/ci-windows.yml/badge.svg)](https://github.com/TamerOnLine/repo-fastapi/actions/workflows/ci-windows.yml) [![Windows GPU CI](https://github.com/TamerOnLine/repo-fastapi/actions/workflows/ci-gpu.yml/badge.svg)](https://github.com/TamerOnLine/repo-fastapi/actions/workflows/ci-gpu.yml) [![macOS CI](https://github.com/TamerOnLine/repo-fastapi/actions/workflows/ci-macos.yml/badge.svg)](https://github.com/TamerOnLine/repo-fastapi/actions/workflows/ci-macos.yml) |
| **License**   | ![License](https://img.shields.io/badge/License-MIT-green) |

---
---

## 📖 Overview

**NeuroServe** is an **AI Inference Server** built on **FastAPI**, designed to run seamlessly on **GPU (CUDA/ROCm)**, **CPU**, and **macOS MPS**.  
It provides ready-to-use REST APIs, a modular **plugin system**, runtime utilities, and a consistent unified response format — making it the perfect foundation for AI-powered services.

---

## ✨ Key Features

- 🌐 **REST APIs out-of-the-box** with Swagger UI (`/docs`) & ReDoc (`/redoc`).
- ⚡ **PyTorch integration** with automatic device selection (`cuda`, `cpu`, `mps`, `rocm`).
- 🔌 **Plugin system** to extend functionality with custom AI models or services.
- 📊 **Runtime tools** for GPU info, warm-up routines, and environment inspection.
- 🧠 **Built-in utilities** like a toy model and model size calculator.
- 🧱 **Unified JSON responses** for predictable API behavior.
- 🧪 **Cross-platform CI/CD** (Ubuntu, Windows, macOS, Self-hosted GPU).
=======
# 🧠 NeuroServe – GPU/CPU FastAPI AI Server

[![Python](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-Framework-green)](https://fastapi.tiangolo.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![CI (Linux)](https://github.com/TamerOnLine/NeuroServe/actions/workflows/ci-linux.yml/badge.svg)](https://github.com/TamerOnLine/NeuroServe/actions/workflows/ci-linux.yml)
[![CI (macOS)](https://github.com/TamerOnLine/NeuroServe/actions/workflows/ci-macos.yml/badge.svg)](https://github.com/TamerOnLine/NeuroServe/actions/workflows/ci-macos.yml)
[![CI (Windows)](https://github.com/TamerOnLine/NeuroServe/actions/workflows/ci-windows.yml/badge.svg)](https://github.com/TamerOnLine/NeuroServe/actions/workflows/ci-windows.yml)
[![GPU CI (Windows self-hosted)](https://github.com/TamerOnLine/NeuroServe/actions/workflows/gpu-ci.yml/badge.svg)](https://github.com/TamerOnLine/NeuroServe/actions/workflows/gpu-ci.yml)


A lightweight **REST API server** powered by **FastAPI** & **PyTorch**.  
It runs seamlessly on **GPU (CUDA)** if available, and safely falls back to **CPU**.  

🚀 Includes a demo model, performance probes, a **web control panel**, and an extendable **Plugin System** for real AI models.

---

## ✨ Features
- ✅ Auto-selects **GPU or CPU** at runtime (`DEVICE` in `.env`).
- ✅ Clean **FastAPI** endpoints with Swagger UI (`/docs`) and ReDoc (`/redoc`).
- ✅ Interactive **Control Panel** (`/ui`) & **Model Size Calculator** (`/tools/model-size`).
- ✅ Example **TinyNet** model + benchmarks (`/matmul`, `/infer`).
- ✅ Extensible **Plugin System** with ready-to-use AI models.
- ✅ Works on **Windows/Linux/macOS** (CPU) & **CUDA** (NVIDIA GPUs).
>>>>>>> de61936 (start)

---

## 📂 Project Structure
<<<<<<< HEAD

```text
gpu-server/
├── app/                 # Main application code
│   ├── core/            # Config, logging, error handling
│   ├── routes/          # API routes (auth, inference, plugins, uploads)
│   ├── plugins/         # Plugin system (dummy, neu_server, base, loader)
│   ├── utils/           # Unified responses
│   ├── static/          # Static assets (CSS, favicon)
│   ├── templates/       # HTML templates
│   ├── main.py          # FastAPI entrypoint
│   ├── runtime.py       # Device/GPU management
│   └── toy_model.py     # Example PyTorch model
├── scripts/             # Install torch, prefetch models, test API
├── tests/               # Unit & integration tests
├── models_cache/        # Model cache (HuggingFace / Torch)
├── docs/                # Documentation & model licenses
├── logs/                # Errors & plugin logs
└── ...
=======
```
app/
  main.py           # FastAPI app & endpoints
  runtime.py        # device selection, CUDA info, warmup
  toy_model.py      # TinyNet demo model
  plugins/          # Modular plugins (bart, clip, resnet18, ner, etc.)
  templates/        # HTML templates for UI
scripts/
  install_torch.py  # Auto-installs correct PyTorch (CPU/GPU)
  test_api.py       # Quick client to test endpoints
requirements.txt
README.md
>>>>>>> de61936 (start)
```

---

<<<<<<< HEAD
## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/USERNAME/gpu-server.git
cd gpu-server
```

### 2. Create a virtual environment
```bash
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows
.venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. (Optional) Auto-install PyTorch
```bash
python -m scripts.install_torch --gpu    # or --cpu / --rocm
```

---

## 🚀 Running the Server

=======
## ⚡ Quickstart

### 1. Setup Environment
**Windows (PowerShell)**:
```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Linux/macOS**:
```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
python -m scripts.install_torch
```

### 3. Run the Server
>>>>>>> de61936 (start)
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

<<<<<<< HEAD
Available endpoints:
- 🏠 **Home** → [http://localhost:8000/](http://localhost:8000/)  
- ❤️ **Health** → [http://localhost:8000/health](http://localhost:8000/health)  
- 📚 **Swagger UI** → [http://localhost:8000/docs](http://localhost:8000/docs)  
- 📘 **ReDoc** → [http://localhost:8000/redoc](http://localhost:8000/redoc)  
- 🧭 **Env Summary** → [http://localhost:8000/env](http://localhost:8000/env)  
- 🔌 **Plugins** → [http://localhost:8000/plugins](http://localhost:8000/plugins)  

Quick test:
```bash
curl http://localhost:8000/health
# {"status": "ok"}
=======
Open in browser:
- **Swagger UI** → http://localhost:8000/docs  
- **Control Panel** → http://localhost:8000/ui  
- **Plugin Console** → http://localhost:8000/plugins/ui  
- **Infer Client** → http://localhost:8000/infer-client  

---

## ⚙️ Configuration (`.env`)
```ini
# Prefer the first CUDA GPU if available
DEVICE=cuda:0

# Force CPU mode (override)
# DEVICE=cpu

# Warmup matrix size (for benchmarks)
WARMUP_MATMUL_SIZE=1024
>>>>>>> de61936 (start)
```

---

<<<<<<< HEAD
## 🔌 Plugin System

Each plugin lives in `app/plugins/<name>/` and typically includes:

```
manifest.json
plugin.py        # Defines Plugin class inheriting AIPlugin
README.md        # Documentation
```

API Endpoints:
- `GET /plugins` — list all plugins with metadata.  
- `POST /plugins/{name}/{task}` — execute a task inside a plugin.  

Example:
=======
## 🔌 API Endpoints

| Method | Path                | Description                      |
|--------|---------------------|----------------------------------|
| GET    | `/health`           | Health check                     |
| GET    | `/cuda`             | CUDA / device info               |
| GET    | `/env`              | Environment summary              |
| GET    | `/env/full`         | Full environment + GPU list      |
| GET    | `/env/system`       | OS/CPU/RAM system info           |
| POST   | `/matmul`           | Matrix multiply benchmark        |
| POST   | `/infer`            | TinyNet inference                |
| POST   | `/inference`        | Generic plugin inference         |
| GET    | `/plugins`          | List available plugins           |
| GET    | `/ui`               | Interactive control panel        |
| GET    | `/tools/model-size` | Model size calculator (UI)       |

---

## 🧩 Plugins
NeuroServe uses a **modular plugin system** under `app/plugins/`.

Available plugins:
- **bart** → Text summarization (`facebook/bart-large-cnn`)
- **clip** → Text ↔ Image embeddings & similarity
- **distilbert** → Sentiment classification
- **resnet18** → Image classification (ImageNet)
- **ner** → Named Entity Recognition
- **tinyllama** → Lightweight text generation
- **translator / translator_m2m** → Translation
- **pdf_reader** → Extract text from PDFs
- **dummy** → Ping test
- **dichfoto_proxy** → Forwarding proxy

🔧 **Build your own Plugin (5 min)**
>>>>>>> de61936 (start)
```python
from app.plugins.base import AIPlugin

class Plugin(AIPlugin):
<<<<<<< HEAD
    name = "my_plugin"
    tasks = ["infer"]

    def load(self):
        # Load models/resources once
        ...

    def infer(self, payload: dict) -> dict:
        return {"message": "ok", "payload": payload}
```

---

## 🧪 Development

Install dev dependencies:
```bash
pip install -r requirements-dev.txt
pre-commit install
```

Run tests:
```bash
pytest
```

Ruff (lint + format check) runs automatically via pre-commit hooks.

---

## 📦 Model Management

Download models in advance:
```bash
python -m scripts.prefetch_models
```

Models are cached in `models_cache/` (see `docs/LICENSES.md` for licenses).

---

## 🏭 Deployment Notes

- Use `uvicorn`/`hypercorn` behind a reverse proxy (e.g., Nginx).  
- Configure environment with `APP_*` variables instead of hardcoding.  
- Enable HTTPS and configure CORS carefully in production.  

---

## 🗺️ Roadmap

- [ ] Add `/cuda` endpoint → return detailed CUDA info.  
- [ ] Add `/warmup` endpoint for GPU readiness.  
- [ ] Provide a **plugin generator CLI**.  
- [ ] Implement API Key / JWT authentication.  
- [ ] Example plugins: translation, summarization, image classification.  
- [ ] Docker support for one-click deployment.  
- [ ] Benchmark suite for model inference speed.  

---

## 🤝 Contributing

Contributions are welcome!  
- Open **Issues** for bugs or ideas.  
- Submit **Pull Requests** for improvements.  
- Follow style guidelines (Ruff + pre-commit).  
=======
    tasks = ["hello"]

    def load(self):
        print("[plugin] hello ready")

    def infer(self, payload):
        name = payload.get("name", "world")
        return {"task": "hello", "message": f"Hello, {name}!"}
```
Add it in `app/plugins/hello/` with `manifest.json`.

---

## 🖥️ Example Requests

**Matrix Multiply**
```bash
curl -X POST http://localhost:8000/matmul   -H "Content-Type: application/json"   -d '{"n": 2048}'
```

**BART Summarization**
```bash
curl -X POST http://localhost:8000/inference   -H "Content-Type: application/json"   -d '{"provider":"bart","task":"summarize","text":"Deep learning is a subfield..."}'
```

**NER Entity Extraction**
```bash
curl -X POST http://localhost:8000/inference   -H "Content-Type: application/json"   -d '{"provider":"ner","task":"extract-entities","text":"Barack Obama was born in Hawaii."}'
```

---

## 🛠️ Troubleshooting
- **Torch import error** → Ensure Python 3.12 + rerun `python -m scripts.install_torch`.
- **No GPU detected** → Falls back to CPU. Force with `DEVICE=cpu`.
- **CUDA mismatch** → Reinstall torch with matching CUDA runtime.
- **Out of Memory (OOM)** → Reduce `max_length` or use CPU mode.
- **Windows Execution Policy** →  
  ```powershell
  Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
  ```

---

## 📍 Roadmap
- [ ] File upload endpoints (images/text).
- [ ] Docker images (CPU & GPU).
- [ ] Extended plugin demo UI.
- [ ] CI/CD with pre-commit hooks & GitHub Actions.
- [x] Real AI plugins (BART, CLIP, ResNet, DistilBERT, NER, etc.).
>>>>>>> de61936 (start)

---

## 📜 License
<<<<<<< HEAD

Licensed under the **MIT License** — see [LICENSE](./LICENSE).  
⚠️ AI models may have their own licenses (see `docs/LICENSES.md`).
=======
MIT © 2025 [TamerOnLine](https://github.com/TamerOnLine)
>>>>>>> de61936 (start)
