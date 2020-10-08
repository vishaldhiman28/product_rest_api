from flask import Response, request, json
from flask_restful import Resource
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError

from database.models import Product
from resources.errors import SchemaValidationError, ProductAlreadyExistsError, InternalServerError, \
    ProductNotExistsError


class ProductsAPI(Resource):
    """
    class to define handlers for products route
    """
    def get(self):
        """
        Function, to handle GET request to extract all available products
        """
        try:
            products_json = Product.objects().to_json()
            return Response(products_json, mimetype="application/json", status=200)
        except Exception:
            raise InternalServerError

    def post(self):
        """
        Function, to handle POST request to insert/create a product in the db
        """
        try:
            json_input = request.get_json()
            product_obj = Product(**json_input)
            product_obj.save()
            return Response(product_obj.to_json(), mimetype="application/json", status=201)
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except NotUniqueError:
            raise ProductAlreadyExistsError
        except Exception as e:
            raise InternalServerError


class SingleProductAPI(Resource):
    """
     class to define handlers for routes in which product are accessed  based on id
    """

    def get(self, id):
        """
         Function, to handle GET request to extract a product from the db based on given id
        """
        try:
            product = Product.objects.get(id=id).to_json()
            return Response(product, mimetype="application/json", status=200)
        except DoesNotExist:
            raise ProductNotExistsError
        except Exception:
            raise InternalServerError

    def put(self, id):
        """
          Function, to handle PUT request to update a product in the db based on given id
        """
        try:
            json_data = request.get_json()
            product_obj = Product.objects.get(id=id)
            Product.objects.get(id=id).update(**json_data)
            product_obj = Product.objects.get(id=id)
            return Response(product_obj.to_json(), mimetype="application/json", status=200)
        except InvalidQueryError:
            raise SchemaValidationError
        except DoesNotExist:
            raise ProductNotExistsError
        except Exception:
            raise InternalServerError

    def delete(self, id):
        """
           Function, to handle DELETE request to delete a product from the db based on given id
        """
        try:
            product = Product.objects.get(id=id)
            product.delete()
            return Response(json.dumps({"id": id}), mimetype="application/json", status=200)
        except DoesNotExist:
            raise ProductNotExistsError
        except Exception:
            raise InternalServerError
