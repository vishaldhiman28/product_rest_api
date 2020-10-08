"""
Here, All the custom Exception and error response  are defined for the api use
"""


class InternalServerError(Exception):
    pass


class SchemaValidationError(Exception):
    pass


class ProductAlreadyExistsError(Exception):
    pass


class UpdatingProductError(Exception):
    pass


class DeletingProductError(Exception):
    pass


class ProductNotExistsError(Exception):
    pass


errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
    "SchemaValidationError": {
        "message": "Request is missing required fields",
        "status": 400
    },
    "ProductAlreadyExistsError": {
        "message": "Product with given name already exists",
        "status": 400
    },
    "UpdatingProductError": {
        "message": "Updating error",
        "status": 403
    },
    "DeletingProductError": {
        "message": "Deleting error",
        "status": 403
    },
    "ProductNotExistsError": {
        "message": "Product with given id doesn't exists",
        "status": 400
    },
}
