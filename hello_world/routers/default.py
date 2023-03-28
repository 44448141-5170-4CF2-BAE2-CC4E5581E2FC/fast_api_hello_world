from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from hello_world.config import settings
from hello_world import deps, models, crud, schemas

router = APIRouter()


@router.get("/", response_model=schemas.IndexResponse)
def hello_world():
    return {
        "hello_world": True,
        "is_live": settings.IS_LIVE
    }


@router.get("/db-values")
def db_values(db: Session = Depends(deps.get_db)) -> list[schemas.HelloWorldValues]:
    return crud.get_all_hello_world_values(db)
