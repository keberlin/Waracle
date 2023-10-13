"""List of exposed URL api routes."""

from api.cake import CakeApi, CakesApi

URL_PREFIX = f"/api/v1"

URLS = [
    (CakesApi, "/cakes"),
    (CakeApi, "/cakes/<int:cake_id>"),
]
