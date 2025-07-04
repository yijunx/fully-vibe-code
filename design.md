# 🧪 Vibe Coding Challenge: Toy Manufacturing gRPC System

This challenge tests your ability to self-drive, make assumptions, and produce clean, working code with minimal supervision — **true vibe coding**. You’ll build a toy gRPC system with CLI tooling, testing, and simulated Argo interactions.

---

## 📦 Requirements

### 1. gRPC Server: `ToyService`
Create a gRPC server that manages a `Toy` entity with the following fields:

- `manufacture_time`: timestamp
- `manufacturor`: string
- `design_time`: timestamp
- `designer`: string
- `number_manufactured`: int32

### 2. Server Features

- `CreateToy`: Create a new toy with metadata.
- `GetToy`: Retrieve toy info by ID.
- `ListToys`: List all toys.
- `UpdateManufactureStatus`: Update toy status via Argo-like callback.
- *(Optional)* `DeleteToy`: Delete a toy by ID.

### 3. Enable gRPC Reflection

Enable [gRPC server reflection](https://github.com/grpc/grpc/blob/master/doc/server-reflection.md) so tools like `grpcurl` can discover services.

---

## 🛠 Environment

- Use **Python 3.12**
- Manage dependencies with **Poetry**
- Provide dev scripts via `pyproject.toml`

---

## ✅ Testing

- Use **pytest** or similar for unit tests
- Write at least one **integration test**: CLI → Server communication

---

## 🔧 CLI: `toyctl`

Build a CLI tool to manage toys. Use `argparse` or `click`.

Supported commands:

- `toyctl manufacture --name Car`: Create a toy
- `toyctl list`: List all toys
- `toyctl update-status --toy-id <id>`: Simulate Argo callback

---

## 🤖 Argo Callback Simulation

- Simulate an **Argo Workflow callback** using mock input
- Use a static file (JSON or YAML) to simulate the payload

---

## 🐳 Docker

- Provide a `Dockerfile` to run both the server and CLI
- *(Optional)* Include a `docker-compose.yml` to:
  - Run the server
  - Run the CLI in a separate container to simulate Argo callback

---

## 📚 Documentation

Include a `README.md` with:

- Setup instructions
- Example CLI usage
- Example Argo-style callback

---

## 🌟 Bonus (Optional)

- In-memory or SQLite toy persistence
- `HealthCheck` gRPC method
- Typing + linting (`mypy`, `ruff`, or `flake8`)
- GitHub Actions CI to run tests on push
- OpenTelemetry instrumentation for observability

---

## 📅 Timebox

- **Recommended time limit:** 2–4 hours
- Push to your own **GitHub repo**
- Write a short **postmortem (1–2 paragraphs)** on:
  - What you did
  - What you'd improve with more time

---

## 💡 What We’re Looking For

| Skill                    | Covered ✅ |
|-------------------------|------------|
| Python 3.12             | ✅         |
| gRPC + Protobuf         | ✅         |
| CLI tool design         | ✅         |
| Poetry & Environment Mgmt | ✅       |
| Testing                 | ✅         |
| Simulated DevOps (Argo) | ✅         |
| Self-direction / vibe   | ✅         |
| Docs & polish           | ✅         |

---

Good luck — and vibe strong 💻✨
