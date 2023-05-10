from fastapi import APIRouter

from ..service import package_files

router = APIRouter()


@router.get("/package_files")
async def get_package_files():
    return package_files.get_package_files()
