from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.pipeline import run_all, forecast_future, run_sql, retrain
from app.services.reports import summary, future_forecast, recs

router = APIRouter()

class RunReq(BaseModel):
    zip_path: str
    max_series: int = 3000

@router.get("/health")
def health(): return {"status":"ok"}

@router.get("/summary")
def get_summary(): return summary()

@router.post("/pipeline/run_all")
def p_run_all(req: RunReq): return run_all(req.zip_path, req.max_series)

@router.post("/pipeline/forecast_future")
def p_future(req: RunReq): return forecast_future(req.zip_path, req.max_series)

@router.post("/pipeline/run_sql")
def p_sql(req: RunReq): return run_sql(req.zip_path, req.max_series)

@router.post("/pipeline/retrain")
def p_retrain(req: RunReq): return retrain(req.zip_path, max(1000, req.max_series))

@router.get("/forecast/future")
def get_future(store_id: str|None=None, item_id: str|None=None, limit: int=1000):
    return future_forecast(store_id, item_id, limit)

@router.get("/recs/{kind}")
def get_recs(kind: str, store_id: str|None=None, limit: int=200):
    if kind not in {"inventory","pricing","assortment","sql_top_items"}:
        raise HTTPException(400, "Invalid kind")
    return recs(kind, store_id, limit)
