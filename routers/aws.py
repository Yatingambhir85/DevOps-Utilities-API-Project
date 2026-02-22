from fastapi import APIRouter, HTTPException
from routers import metrics
from services.aws_service import get_buckets_info
from services.aws_service import get_aws_user_info
from services.aws_service import get_ec2_info

router=APIRouter()

@router.get("/s3", status_code=200, summary="Get S3 Metrics", description="Fetches S3 metrics such as bucket names and creation dates.")
def get_aws_metrics_router():
    try:
        metrics = get_buckets_info()
        return metrics
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/sts", status_code=200, summary="Get AWS User Info", description="Fetches AWS user information such as user ID, account number, and ARN which is configured in the system.")
def get_aws_user_info_router():
    try:
        metrics = get_aws_user_info()
        return metrics
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    
@router.get("/ec2", status_code=200, summary="Get AWS EC2 Info", description="Fetches AWS EC2 information such as instance IDs and states.")
def get_aws_ec2_info_router():
    try:
        metrics = get_ec2_info()
        return metrics
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))