from .product import ProductsAPI, SingleProductAPI


def initialize_routes(api):
    """
    function to add routes to flask restful api
    """
    api.add_resource(ProductsAPI, '/api/products')
    api.add_resource(SingleProductAPI, '/api/product/<id>')
