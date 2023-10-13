"""Interface Schemas for the Cakes api routes."""
from marshmallow import Schema, fields, validate


class CakesSchema(Schema):
    id = fields.String(attribute="id", required=True)
    name = fields.String(attribute="name", required=True)
    comment = fields.String(attribute="comment", required=True)
    imageUrl = fields.Url(attribute="image_url", required=True)
    yumFactor = fields.Integer(attribute="yum_factor", required=True)


class CakesGetSchema(Schema):
    pass


class CakesCreateSchema(Schema):
    name = fields.String(
        attribute="name", required=True, validate=validate.Length(max=30)
    )
    comment = fields.String(
        attribute="comment", required=True, validate=validate.Length(max=200)
    )
    imageUrl = fields.Url(attribute="image_url", required=True)
    yumFactor = fields.Integer(attribute="yum_factor", required=True)


class CakesUpdateSchema(Schema):
    name = fields.String(
        attribute="name", required=False, validate=validate.Length(max=30)
    )
    comment = fields.String(
        attribute="comment", required=False, validate=validate.Length(max=200)
    )
    imageUrl = fields.Url(attribute="image_url", required=False)
    yumFactor = fields.String(attribute="yum_factor", required=False)
