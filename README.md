Instructions for the Cakes server app
=====================================

How to install:
---------------

``docker-build.sh``

How to run:
-----------

``docker-run.sh``

How to use:
-----------

The server is running on port 5000 of the localhost.

Getting swagger info:

``curl localhost:5000/swagger/``

Seeing the swagger interface via a web browser use:

``http://localhost:5000/swagger-ui/``

Getting all cakes:

``curl localhost:5000/api/v1/cakes``

Adding a new cake:

``curl -X POST localhost:5000/api/v1/cakes -H "Content-Type: application/json" -d '{"name":"Chocolate","comment":"a type of Sponge cake made with chocolate","imageUrl":"https://en.wikipedia.org/wiki/Chocolate_cake#/media/File:Chocolate_fudge_cake.jpg","yumFactor":"5"}'``

Updating a cake:

``curl -X PUT localhost:5000/api/v1/cakes/4 -H "Content-Type: application/json" -d '{"name":"Black Forest Gateau","imageUrl":"https://en.wikipedia.org/wiki/Black_Forest_gateau#/media/File:Black_Forest_gateau.jpg","yumFactor":"5"}'``

Deleting a cake:

``curl -X DELETE localhost:5000/api/v1/cakes/4``
