# Time API (FastAPI)

## Endpoints

- `GET /api/health` → `{ ok: true }`
- `GET /api/time` → `{ iso, epoch_ms, timezone }`

## Correr local

```bash
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
# http://localhost:8000/api/time
```
