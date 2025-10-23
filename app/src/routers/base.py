from fastapi import APIRouter

from ..schemas.base import Version

router = APIRouter(prefix="")

@router.get(
    "/version",
    response_model=Version,
    responses={
        200: {"description": "Success"},
        500: {"description": "Internal server error"}
    }
)
def get_version():
    """Get number of version"""
    
    return Version(version="0.01")