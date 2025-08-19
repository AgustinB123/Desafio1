from fastapi import FastAPI
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
import os

app = FastAPI(title="Time API (FastAPI)")

@app.get("/")
def root():
    return {
        "message": "Bienvenido a la Time API 🚀",
        "endpoints": {
            "health": "/api/health",
            "time": "/api/time",
            "docs": "/docs"
        }
    }

@app.get("/api/health")
def health():
    return {"ok": True}

@app.get("/api/time")
def get_time():
    now_utc = datetime.now(timezone.utc)
    # Detecta zona local del sistema si existe, si no deja UTC
    tzname = os.environ.get("TZ") or \
             datetime.now().astimezone().tzinfo.key if hasattr(datetime.now().astimezone().tzinfo, "key") else "UTC"
    return {
        "iso": now_utc.isoformat(),
        "epoch_ms": int(now_utc.timestamp() * 1000),
        "timezone": tzname
    }
