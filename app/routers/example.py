from fastapi import APIRouter

router = APIRouter()

@router.get("/example")
def read_example():
    return {"message": "Ruta de ejemplos"}