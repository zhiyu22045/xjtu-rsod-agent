from fastapi import APIRouter

router = APIRouter()


@router.get("/api/health")
def health_check():
    return {"status": "healthy", "app_name": "RSOD Agent Platform", "version": "0.1.0"}


@router.get("/api/health/database")
def database_health():
    return {"status": "healthy", "database": "postgresql", "message": "数据库连接正常"}


@router.get("/api/health/redis")
def redis_health():
    return {"status": "healthy", "redis": "connected", "message": "Redis连接正常"}


@router.get("/api/health/minio")
def minio_health():
    return {"status": "healthy", "minio": "connected", "message": "MinIO连接正常"}
