# 🏗️ NeuroServe — System Architecture

> Version: 1.0 · Scope: High-level and component-level architecture for the **NeuroServe** FastAPI AI server.

---

## 1) Overview

NeuroServe is a modular AI inference server built on **FastAPI** with a **plugin system** that encapsulates model logic, and a **runtime device layer** that abstracts GPU/CPU/MPS/ROCm. It includes **error & logging** pipelines, **unified response utilities**, and cross‑platform **CI** with a self‑hosted GPU workflow.

---

## 2) Layered Architecture

```
┌───────────────────────────────────────────────────────────────────────────┐
│                              Presentation Layer                           │
│  - FastAPI ASGI app (app/main.py)                                         │
│  - Routes: /health, /env, /plugins, /uploads, /inference                  │
│  - Templates & static assets (app/templates, app/static)                  │
└───────────────▲───────────────────────────────────────────────────────────┘
                │
┌───────────────┼───────────────────────────────────────────────────────────┐
│                           Service / API Layer                              │
│  - Routers (app/routes/*.py): auth, plugins, uploads, inference           │
│  - Request/response models (Pydantic)                                      │
│  - Unify responses (app/utils/unify.py)                                    │
└───────────────▲───────────────────────────────────────────────────────────┘
                │
┌───────────────┼───────────────────────────────────────────────────────────┐
│                         Core & Runtime Layer                               │
│  - Settings (app/core/config.py)                                           │
│  - Logging (app/core/logging_.py)                                          │
│  - Error handlers (app/core/errors.py)                                     │
│  - Runtime device mgmt (app/runtime.py)                                    │
└───────────────▲───────────────────────────────────────────────────────────┘
                │
┌───────────────┼───────────────────────────────────────────────────────────┐
│                           Plugin Abstraction                               │
│  - Plugin base (app/plugins/base.py)                                       │
│  - Plugin loader (app/plugins/loader.py)                                   │
│  - Plugins: dummy, neu_server, ... (app/plugins/*)                         │
└───────────────▲───────────────────────────────────────────────────────────┘
                │
┌───────────────┼───────────────────────────────────────────────────────────┐
│                        Model & Cache Subsystem                             │
│  - Torch / HF models                                                       │
│  - Cache roots (models_cache/, HF_HOME, TORCH_HOME, TRANSFORMERS_CACHE)   │
└────────────────────────────────────────────────────────────────────────────┘
```

---

## 3) Component Map

- **FastAPI App (`app/main.py`)**: App factory, router include, middlewares, CORS.
- **Core**
  - `config.py`: Pydantic Settings, cache dirs, env export, directories bootstrap.
  - `logging_.py`: Console/file loggers, levels per channel (uvicorn, plugins, errors).
  - `errors.py`: Central exception handlers with HTML/JSON rendering.
- **Runtime**
  - `runtime.py`: Device probing, CUDA/MPS availability, warmup helpers.
- **Routes**
  - `auth.py` (optional), `uploads.py`, `plugins.py`, `inference.py`.
- **Plugins**
  - `base.py`: `AIPlugin` interface (name, tasks, load(), task methods).
  - `loader.py`: Discovery, import, lifecycle (load/unload), registry.
  - `dummy/`, `neu_server/`: Reference implementations.
- **Utils**
  - `utils/unify.py`: Standard response envelope.
- **Scripts**
  - `install_torch.py`, `prefetch_models.py`, `test_api.py`, `print_caches.py`.
- **Tests**
  - CPU/GPU/MPS markers, live tests, error/logging tests.
- **CI/CD (`.github/workflows`)**
  - Ubuntu/Windows/macOS + self-hosted GPU pipeline.

---

## 4) Request Lifecycle (Happy Path)

### 4.1 `/health`

```
Client → FastAPI Router (/health)
      → Core Settings.summary() + quick probes
      → Unified JSON response
      ← 200 OK { "status": "ok", ... }
```

### 4.2 `/plugins` → list & metadata

```
Client → /plugins (GET)
      → Plugin Loader registry snapshot
      ← 200 OK [ {name, tasks, version, manifest...}, ... ]
```

### 4.3 `/plugins/{name}/{task}` (Plugin Task Execution)

```
Client → /plugins/{name}/{task} (POST JSON)
      → Router validation (Pydantic)
      → Loader.resolve(name) → AIPlugin instance
      → plugin.task(payload) on selected device (runtime picks cuda/cpu/mps)
      → Unify response + log
      ← 200 OK { "status":"ok", "data":{...}, "timings": {...} }
```

### 4.4 Error Path (e.g., ValidationError)

```
Exception → app/core/errors.py
         → wants_html? → HTML template (app/templates/error.html)
           else JSON envelope with code/message/details
         → log error stack (errors.log) + request_id (if any)
```

---

## 5) Plugin Architecture

- **Manifest (`manifest.json`)**: metadata (name, version, tasks, entry).
- **Base (`AIPlugin`)**: contract: `name`, `tasks`, `load()`, and task methods.
- **Loader**:
  - Discovers packages under `app/plugins/*`.
  - Imports module, instantiates `Plugin` class, calls `load()` once.
  - Keeps a registry map `{name → instance}` for fast lookup.
- **Concurrency**:
  - Task methods should be **async-safe** or internally offload to a worker thread if CPU-bound.
- **Isolation** (future):
  - Optional process/thread pools per plugin for heavy models.
- **Example Use‑cases**:
  - Text: translate/summarize/classify.
  - Audio: ASR (Whisper-like).
  - Vision: image classification/embedding.

---

## 6) Runtime & Device Management

- Picks device automatically: `cuda:N` → `mps` → `cpu` (configurable).
- Exposes helpers for:
  - **availability** checks (`torch.cuda.is_available()` / MPS).
  - **device info** (count, names, memory) – candidate `/cuda` endpoint.
  - **warmup** kernels for reduced first‑infer latency.
- **Cache dirs** are exported to env to keep model downloads in `models_cache/`.

---

## 7) Configuration & Environments

- **Settings** via Pydantic (`APP_*` env vars, `.env` file).
- Key knobs:
  - `APP_DEVICE`, `APP_MODEL_CACHE_ROOT`, `APP_HF_HOME`, `APP_TORCH_HOME`,
    `APP_TRANSFORMERS_CACHE`, `APP_LOG_LEVEL*`, `APP_CORS_*`.
- **Directories** auto‑created on startup (logs, caches, uploads, templates, static).

---

## 8) Logging & Error Handling

- **Console**: root level (info/debug).
- **Files**:
  - `logs/errors.log` — exception stacks.
  - `logs/plugins.log` — plugin activity/metrics.
- **Uvicorn access** tuning (reduce noise in CI).

---

## 9) CI/CD & Quality Gates

- **Linux/macOS/Windows** workflows (CPU tests, lint/format).
- **Self‑hosted GPU** workflow for CUDA:
  - Python discovery on the runner.
  - `nvidia-smi` check + Torch CUDA probe.
  - Marker‑based test selection (`-m "gpu or gpu_cuda or gpu_mps"`).
- **Pre‑commit** (ruff + ruff-format auto‑fix).
- Smoke tests for `/health` on each platform.

---

## 10) Deployment Topologies

- **Single Node** (Dev): `uvicorn --reload`.
- **Prod Single GPU**: `uvicorn --workers N` behind Nginx, CUDA visible devices.
- **Multi‑GPU**:
  - Run multiple workers with `CUDA_VISIBLE_DEVICES` per instance.
  - Optional plugin‑specific device pinning.
- **Containerization (Future)**: Dockerfile, compose with volume‑mounted caches.

---

## 11) Extension Points

- **Add new plugin** under `app/plugins/<name>`.
- **New route** under `app/routes`, include in `app/main.py`.
- **New device logic** in `app/runtime.py` (ROCm, MIG policy, etc.).
- **Auth**: add JWT/API‑Key in `routes/auth.py` + dependency in routers.

---

## 12) ASCII Sequence — Plugin Task

```
Client
  │  POST /plugins/summarizer/infer {text}
  ▼
FastAPI Router
  │  validate payload
  ▼
Plugin Loader
  │  get('summarizer')
  ▼
Plugin.infer()
  │  runtime.pick_device()
  │  model.forward()
  ▼
Unify + Logging
  │
  └─→ 200 OK {status,data,timings}
```

---

## 13) Security & Hardening (Backlog)

- Auth (API Key / JWT), rate limiting, CORS allow‑list.
- Size limits for uploads, streaming IO for large files.
- Input validation per plugin and schema versioning.

---

## 14) Observability (Backlog)

- Request IDs, timing middleware, tracing hooks (OTEL), metrics endpoints.
- Per‑plugin counters (invocations, avg latency, failures).

---

## 15) Roadmap Glue

- `/cuda` + `/warmup` endpoints.
- Plugin generator CLI.
- Docker build + GPU runtime notes.
- Example production plugin (ASR + Summarize workflow).
