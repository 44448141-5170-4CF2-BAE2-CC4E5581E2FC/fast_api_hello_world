from sqlalchemy.schema import CreateSchema
from hello_world import database, models, crud


def main():
    schemas = set()
    for table in models.Base.metadata.tables.values():
        if table.schema is not None:
            schemas.add(table.schema)

    db = database.SessionLocal()
    for schema in schemas:
        db.execute(CreateSchema(schema, if_not_exists=True))
    db.commit()

    models.Base.metadata.create_all(bind=database.engine)
    crud.create_hello_world_values(["Hello world!"], db)
    db.commit()


if __name__ == '__main__':
    main()
