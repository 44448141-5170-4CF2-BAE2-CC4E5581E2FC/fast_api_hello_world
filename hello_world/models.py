from typing import TypeVar, Type

from pydantic import BaseModel
from sqlalchemy import Column, String, Integer, DateTime, func
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class HelloWorldValues(Base):
    __tablename__ = 'hello_world_values'
    __table_args__ = {
        "schema": "hello_world",
    }

    id = Column(Integer, primary_key=True)
    value = Column(String(128), nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)


_BaseModelT = TypeVar('_BaseModelT', bound=BaseModel)
_BaseT = TypeVar('_BaseT', bound=Base)


def map_model_to_schema(model: Type[_BaseT], schema: Type[_BaseModelT]) -> _BaseModelT:
    if schema.__config__.orm_mode:
        return schema.from_orm(model)
    return schema(**model.__dict__)


def map_schema_to_model(schema: _BaseModelT, model: Type[_BaseT]) -> _BaseT:
    try:
        new = model(**{
            key: schema.__dict__[key]
            for key in model.__table__.columns
        })
    except KeyError as e:
        fq_name = f"{schema.__class__.__module__}.{schema.__class__.__name__}"
        raise KeyError(f"Field for {e} not found in schema {fq_name}") from e
    return new
