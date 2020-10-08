# product_rest_api
This is a REST API which allows the user to interact with a database of products which are available on localhost via Docker.

Features:

- It allows to view all of the available products.
- It allows to add new product.
- It allows to update a product.
- It allows to delete a product.
- It allows to view a single product.

Tech Stack
==========

- Python, Flask, Flask-RESTful, Flask-mongoengine
- Database: MongoDB

Directory Structure and Description
===================================
```bash
.
├── app.py : This contains main login to initialize flask app, rest_app and  database configuration.
├── database
│   ├── db.py: This defines initializer for database using mongoengine.
│   ├── models.py: This defines schema for Product model.
├── Dockerfile: This files defines the configuration for docker container.
├── requirements.txt: This lists the requirement to run project.
└── resources
    ├── errors.py:  This defines all custom error possible in project.
    ├── product.py: This defines all the handler for available enpoints.
    └── routes.py: This defines all the endpoints available for the API.

```

Get started
===========

Installation
------------


### Install from source

```bash
git clone https://github.com/vishaldhiman28/product_rest_api
cd product_rest_api

pip install -r requirements.txt

python app.py

```

### Deploying With Docker

First Install docker on your device and then 
```bash
git clone https://github.com/vishaldhiman28/product_rest_api
cd product_rest_api

docker build --tag product_rest_api .
docker run --name  product_rest_api -d -p 5001:5001 product_rest_api
```

### Accessing API
After deploying docker container on localhost access api using POSTMAN.

So install postman and visit the api endpoints. Following are the endpoint that will be avialabe on localchost.
http://127.0.0.1:5001/api/
      

### API Documentation
Please see [API DOCUMENTATION](https://documenter.getpostman.com/view/10207322/TVRj5oGL)


### Possible Features Upates

Here are some of update that can be done:

- Adding Authentication feature
- When viewing all products pagination can be done to limit number of prodcuts.
