# 🚀 NeuroServe — GPU-Ready FastAPI AI Server

## 📊 Project Status

| Category      | Badges |
|---------------|--------|
| **Languages** | ![Python](https://img.shields.io/badge/Python-3.12%2B-blue) ![HTML](https://img.shields.io/badge/HTML-5-orange) ![CSS](https://img.shields.io/badge/CSS-3-blueviolet) |
| **Framework** | ![FastAPI](https://img.shields.io/badge/FastAPI-0.116.x-009688) |
| **ML / GPU**  | ![PyTorch](https://img.shields.io/badge/PyTorch-2.6.x-ee4c2c) ![CUDA Ready](https://img.shields.io/badge/CUDA-Ready-76B900?logo=nvidia&logoColor=white) |
| **CI**        | [![Ubuntu CI](https://github.com/TamerOnLine/repo-fastapi/actions/workflows/ci-ubuntu.yml/badge.svg)](https://github.com/TamerOnLine/repo-fastapi/actions/workflows/ci-ubuntu.yml) [![Windows CI](https://github.com/TamerOnLine/repo-fastapi/actions/workflows/ci-windows.yml/badge.svg)](https://github.com/TamerOnLine/repo-fastapi/actions/workflows/ci-windows.yml) [![Windows GPU CI](https://github.com/TamerOnLine/repo-fastapi/actions/workflows/ci-gpu.yml/badge.svg)](https://github.com/TamerOnLine/repo-fastapi/actions/workflows/ci-gpu.yml) [![macOS CI](https://github.com/TamerOnLine/repo-fastapi/actions/workflows/ci-macos.yml/badge.svg)](https://github.com/TamerOnLine/repo-fastapi/actions/workflows/ci-macos.yml) |
| **License**   | ![License](https://img.shields.io/badge/License-MIT-green) |
| **Support**   | [![Sponsor](https://img.shields.io/badge/Sponsor-💖-pink)](https://paypal.me/tameronline) |


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

---

## 📂 Project Structure

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
```

---

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

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

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
```

---

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
```python
from app.plugins.base import AIPlugin

class Plugin(AIPlugin):
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

---

## 📜 License

Licensed under the **MIT License** — see [LICENSE](./LICENSE).  
⚠️ AI models may have their own licenses (see `docs/LICENSES.md`).
