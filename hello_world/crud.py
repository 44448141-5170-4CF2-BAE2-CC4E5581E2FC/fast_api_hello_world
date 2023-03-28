from fastapi import Depends
from sqlalchemy.orm import Session

from hello_world import deps, models, schemas


def get_all_hello_world_values(db: Session = Depends(deps.get_db)):
    return [
        models.map_model_to_schema(row, schemas.HelloWorldValues)
        for row in db.query(models.HelloWorldValues).all()
    ]


def create_hello_world_values(values: list[str], db: Session = Depends(deps.get_db)) -> None:
    for value in values:
        db.add(models.HelloWorldValues(value=value))
