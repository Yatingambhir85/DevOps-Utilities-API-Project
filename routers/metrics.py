from fastapi import APIRouter, HTTPException
from services.metrics_service import get_system_metrics

router=APIRouter()

@router.get("/metrics", status_code=200, summary="Get System Metrics", description="Fetches system metrics such as CPU and memory usage.")
def get_metrics_router():
    try:
        metrics = get_system_metrics()
        return metrics
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))