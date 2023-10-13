"""Database Model for the Cakes table."""

from db import db


class CakesModel(db.Model):
    __tablename__ = "cakes"

    __table_args__ = {"implicit_returning": False}

    id = db.Column(
        "id",
        db.Integer,
        db.Identity(),
        primary_key=True,
        nullable=False,
    )
    name = db.Column("name", db.String(30))
    comment = db.Column("comment", db.String(200))
    image_url = db.Column("image_url", db.String, nullable=False)
    yum_factor = db.Column("yum_factor", db.Integer, nullable=False)
