# 🚀 NeuroServe — GPU‑Ready FastAPI AI Server

## 📊 Project Status

| Category      | Badges |
|---------------|--------|
| **Languages** | ![Python](https://img.shields.io/badge/Python-3.12%2B-blue) ![HTML](https://img.shields.io/badge/HTML-5-orange) ![CSS](https://img.shields.io/badge/CSS-3-blueviolet) |
| **Framework** | ![FastAPI](https://img.shields.io/badge/FastAPI-0.116.x-009688) |
| **ML / GPU**  | ![PyTorch](https://img.shields.io/badge/PyTorch-2.6.x-ee4c2c) ![CUDA Ready](https://img.shields.io/badge/CUDA-Ready-76B900?logo=nvidia&logoColor=white) |
| **CI**        | [![Ubuntu CI](https://github.com/TamerOnLine/repo-fastapi/actions/workflows/ci-ubuntu.yml/badge.svg)](https://github.com/TamerOnLine/repo-fastapi/actions/workflows/ci-ubuntu.yml) [![Windows CI](https://github.com/TamerOnLine/repo-fastapi/actions/workflows/ci-windows.yml/badge.svg)](https://github.com/TamerOnLine/repo-fastapi/actions/workflows/ci-windows.yml) [![Windows GPU CI](https://github.com/TamerOnLine/repo-fastapi/actions/workflows/ci-gpu.yml/badge.svg)](https://github.com/TamerOnLine/repo-fastapi/actions/workflows/ci-gpu.yml) [![macOS CI](https://github.com/TamerOnLine/repo-fastapi/actions/workflows/ci-macos.yml/badge.svg)](https://github.com/TamerOnLine/repo-fastapi/actions/workflows/ci-macos.yml) |
| **License**   | ![License](https://img.shields.io/badge/License-MIT-green) |






NeuroServe is an **AI Inference Server** built on **FastAPI** and designed to run seamlessly on **GPU / CPU / ROCm / macOS MPS**.  
It provides ready-to-use REST APIs, a plugin system, prefetch utilities for models, and runtime inspection tools.

---

## ✨ Key Features
- 🌐 **Ready REST APIs** with Swagger UI (`/docs`) & ReDoc (`/redoc`).
- ⚡ **PyTorch integration** with auto device selection (CUDA/CPU/MPS/ROCm).
- 🧩 **Plugin system** for loading and running models or services as standalone plugins.
- 📊 **Runtime utilities**: CUDA info and warmup routines.
- 🧠 **Model tools**: TinyNet example model & MLP memory size calculator.
- 🧱 **Unified responses** with `unify_response` for consistent API outputs.

---

## 📂 Project Structure
```text
gpu-server/
├─ app/
│  ├─ main.py           # FastAPI entrypoint
│  ├─ runtime.py        # Device (CUDA/CPU/MPS) management & info
│  ├─ toy_model.py      # Simple PyTorch model
│  ├─ core/             # config + logging + error handling
│  ├─ routes/           # API routes (plugins, uploads, ...)
│  ├─ plugins/          # plugin system (dummy, neu_server)
│  ├─ templates/        # index.html
│  └─ static/           # style.css, favicon.ico
├─ scripts/             # helper scripts (install_torch, prefetch_models, tests)
├─ models_cache/        # HF/Torch model cache
├─ docs/                # model licenses & docs
├─ tests/               # optional tests
├─ requirements*.txt
├─ pyproject.toml       # Ruff/pytest/coverage configs
└─ README.md , LICENSE
```

---

## ⚙️ Quick Installation
### 1) Clone the repository
```bash
git clone https://github.com/USERNAME/gpu-server.git
cd gpu-server
```

### 2) Create virtual environment
```bash
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows
.venv\Scripts\activate
```

### 3) Install dependencies
```bash
pip install -r requirements.txt
```

### (Optional) Auto-install PyTorch
```bash
python -m scripts.install_torch --gpu    # or --cpu / --rocm
```

### 4) Run the server
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

> **Note:** Configuration can be set via environment variables (see "Settings").

---

## 🖥️ Usage (Direct Links)
- 🏠 **Home**: <http://localhost:8000/>
- 📚 **Swagger UI**: <http://localhost:8000/docs>
- 📘 **ReDoc**: <http://localhost:8000/redoc>
- ❤️ **Health**: <http://localhost:8000/health>
- 🧭 **Env Summary**: <http://localhost:8000/env>
- 🔌 **Plugins**: <http://localhost:8000/plugins>

### Quick Examples
```bash
curl http://localhost:8000/health
# {"status":"ok"}
```

Run a task in the **dummy** plugin:
```bash
curl -X POST http://localhost:8000/plugins/dummy/ping \
     -H "Content-Type: application/json" \
     -d '{"hello":"world"}'
```

Python:
```python
import requests
r = requests.post("http://localhost:8000/plugins/dummy/ping", json={"hello": "world"})
print(r.json())
```

---

## 🔧 Settings (Pydantic Settings)
Environment variables prefixed with `APP_` and optionally loaded from `.env`.

| Name | Default | Description |
|---|---|---|
| `APP_APP_NAME` | `NeuroServe` | Application name |
| `APP_ENV` | `development` | `development` / `staging` / `production` |
| `APP_HOST` | `0.0.0.0` | Bind address |
| `APP_PORT` | `8000` | Port |
| `APP_RELOAD` | `true` | Auto-reload in dev mode |
| `APP_LOG_LEVEL` | `info` | Log level: `debug`/`info`/`warning`/`error` |
| `APP_DEVICE` | `cuda:0` | Device (`cuda:0`, `cpu`, `mps`, etc.) |
| `APP_MODEL_CACHE_ROOT` | `models_cache` | Cache root for models |
| `APP_HF_HOME` | auto | HuggingFace cache (within root) |
| `APP_TORCH_HOME` | auto | Torch cache |
| `APP_TRANSFORMERS_CACHE` | auto | HF hub cache |
| `APP_STATIC_DIR` | `app/static` | Static files dir |
| `APP_TEMPLATES_DIR` | `app/templates` | Templates dir |
| `APP_UPLOAD_DIR` | `uploads` | Upload dir |
| `APP_CORS_ALLOW_ORIGINS` | `[*]` | CORS origins |
| `APP_CORS_ALLOW_METHODS` | `[*]` | CORS methods |
| `APP_CORS_ALLOW_HEADERS` | `[*]` | CORS headers |
| `APP_CORS_ALLOW_CREDENTIALS` | `false` | Allow cookies |
| `APP_DB_URL` | — | Database URL (optional) |
| `APP_JWT_*` | — | JWT settings (optional) |

---

## 🔌 Plugins System
Each plugin lives under `app/plugins/<name>` and usually includes:
```
manifest.json
plugin.py        # defines a Plugin class inheriting AIPlugin
README.md        # plugin docs
```

API Endpoints:
- `GET /plugins` — list all loaded plugins with metadata.
- `POST /plugins/{name}/{task}` — run a task in the specified plugin.

Example `plugin.py`:
```python
from app.plugins.base import AIPlugin

class Plugin(AIPlugin):
    name = "my_plugin"
    tasks = ["infer"]

    def load(self) -> None:
        # Load models/resources once
        ...

    def infer(self, payload: dict) -> dict:
        return {"task": payload.get("task"), "message": "ok", "payload_received": payload}
```

---

## 🧪 Development & Testing
Install dev requirements:
```bash
pip install -r requirements-dev.txt
pre-commit install
```

Run tests:
```bash
pytest
```

Ruff & formatting run automatically via pre-commit hooks.

---

## 📦 Prefetch Models
Download supported models into `models_cache/`:
```bash
python -m scripts.prefetch_models
```
(See `docs/LICENSES.md` for model licenses.)

---

## 🧰 Runtime Utilities
- **CUDA info** via `app/runtime.py` (`cuda_info()`).
- **Warmup** routines for GPU readiness.

---

## 🏭 Deployment Notes
- Use Uvicorn/Hypercorn behind a proxy (e.g., Nginx) with multiple workers.
- Configure environment via `APP_*` vars instead of code changes.
- Adjust CORS carefully for production.

---

## 🤝 Contributing
- Open **Issues** for ideas/bugs.
- Use **Pull Requests** for changes.
- Follow style (Ruff + pre-commit).

---

## 📜 License
Licensed under **MIT** — see [LICENSE](./LICENSE). Models may have their own licenses (see `docs/LICENSES.md`).

---

## 🗺️ Roadmap (Suggested)
- [ ] Add `/cuda` endpoint (return `cuda_info()`).
- [ ] Add `/warmup` endpoint.
- [ ] Provide plugin template/CLI generator.
- [ ] Support API Key/JWT authentication.
- [ ] Example plugins (translation, summarization, image classification).
