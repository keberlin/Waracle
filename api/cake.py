"""Class to handle the Cakes api routes."""

from flask_apispec import MethodResource, doc, marshal_with, use_kwargs
from sqlalchemy import func

from db import db
from db.models.cakes import CakesModel

from .schemas.cake import (
    CakesCreateSchema,
    CakesGetSchema,
    CakesSchema,
    CakesUpdateSchema,
)


class CakesApi(MethodResource):
    @doc(description="Cakes - Fetch", tags=["Cakes"])
    @use_kwargs(CakesGetSchema, location="query")
    @marshal_with(CakesSchema(many=True))
    def get(self, **kwargs):
        session = db.session

        query = (
            session.query(CakesModel)
            # Sorting
            .order_by(func.lower(CakesModel.name))
        )

        results = query.all()

        return results

    @doc(description="Cakes - Create", tags=["Cakes"])
    @use_kwargs(CakesCreateSchema)
    @marshal_with(CakesSchema(many=False))
    def post(self, **kwargs):
        session = db.session

        cake = CakesModel(**kwargs)
        session.add(cake)

        session.commit()

        return cake, 201


class CakeApi(MethodResource):
    @doc(description="Cake - Fetch", tags=["Cake"])
    @marshal_with(CakesSchema(many=False))
    def get(self, cake_id):
        session = db.session

        result = (
            session.query(CakesModel)
            # Filters
            .filter(CakesModel.id == cake_id).one_or_none()
        )

        return result

    @doc(description="Cake - Update", tags=["Cake"])
    @use_kwargs(CakesUpdateSchema)
    def put(self, cake_id, **kwargs):
        session = db.session

        (
            session.query(CakesModel)
            # Filters
            .filter(CakesModel.id == cake_id)
        ).update(kwargs)

        session.commit()

    @doc(description="Cake - Delete", tags=["Cake"])
    def delete(self, cake_id, **kwargs):
        session = db.session

        (
            session.query(CakesModel)
            # Filters
            .filter(CakesModel.id == cake_id)
        ).delete()

        session.commit()
