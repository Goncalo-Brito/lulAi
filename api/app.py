from flask import Flask, request, jsonify
from pymongo import MongoClient
from datetime import datetime
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS 
from bson.objectid import ObjectId

app = Flask(__name__)
CORS(app) 

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={'app_name': "Chatbot API"})
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

client = MongoClient('mongodb://localhost:27017/')
db = client['chatbot_db']

@app.route('/websites', methods=['POST'])
def create_website():
    data = request.json
    website = {
        'website_url': data['website_url'],
        'website_name': data['website_name'],
        'integration_date': datetime.now()
    }
    website_id = db.websites.insert_one(website).inserted_id
    return jsonify({'message': 'Website created', 'website_id': str(website_id)}), 201

@app.route('/websites/<website_id>', methods=['GET'])
def get_website(website_id):
    website = db.websites.find_one({'_id': ObjectId(website_id)})
    if website:
        website['_id'] = str(website['_id'])
        return jsonify(website), 200
    else:
        return jsonify({'error': 'Website not found'}), 404

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user = {
        'username': data['username'],
        'user_type': data['user_type'],
        'email': data['email'],
        'password': data['password'], 
        'registered_date': datetime.now()
    }
    user_id = db.users.insert_one(user).inserted_id
    return jsonify({'message': 'User created', 'user_id': str(user_id)}), 201

@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = db.users.find_one({'_id': ObjectId(user_id)})
    if user:
        user['_id'] = str(user['_id'])
        return jsonify(user), 200
    else:
        return jsonify({'error': 'User not found'}), 404

@app.route('/scraped_data', methods=['POST'])
def create_scraped_data():
    data = request.json
    scraped_data = {
        'sourceType': data['sourceType'],
        'source_id': data['source_id'],
        'scraped_content': data['scraped_content'],
        'scrape_date': datetime.now()
    }
    scraped_id = db.scraped_data.insert_one(scraped_data).inserted_id
    return jsonify({'message': 'Scraped data created', 'scraped_id': str(scraped_id)}), 201

@app.route('/scraped_data/<scraped_id>', methods=['GET'])
def get_scraped_data(scraped_id):
    scraped_data = db.scraped_data.find_one({'_id': ObjectId(scraped_id)})
    if scraped_data:
        scraped_data['_id'] = str(scraped_data['_id'])
        return jsonify(scraped_data), 200
    else:
        return jsonify({'error': 'Scraped data not found'}), 404

@app.route('/documents', methods=['POST'])
def create_document():
    data = request.json
    document = {
        'document_name': data['document_name'],
        'document_path': data['document_path'],
        'document_type': data['document_type'],
        'upload_date': datetime.now()
    }
    document_id = db.documents.insert_one(document).inserted_id
    return jsonify({'message': 'Document created', 'document_id': str(document_id)}), 201

@app.route('/documents/<document_id>', methods=['GET'])
def get_document(document_id):
    document = db.documents.find_one({'_id': ObjectId(document_id)})
    if document:
        document['_id'] = str(document['_id'])
        return jsonify(document), 200
    else:
        return jsonify({'error': 'Document not found'}), 404

@app.route('/static/swagger.json')
def swagger_json():
    return jsonify({
        "swagger": "2.0",
        "info": {
            "title": "Chatbot API",
            "description": "API for managing chatbot data",
            "version": "1.0.0"
        },
        "host": "localhost:5000",
        "basePath": "/",
        "schemes": ["http"],
        "paths": {
            "/websites": {
                "post": {
                    "summary": "Create a website",
                    "consumes": ["application/json"],
                    "parameters": [{"in": "body", "name": "body", "required": True, "schema": {"$ref": "#/definitions/Website"}}],
                    "responses": {"201": {"description": "Website created"}}
                }
            },
            "/websites/{website_id}": {
                "get": {
                    "summary": "Get a website by ID",
                    "parameters": [{"name": "website_id", "in": "path", "required": True, "type": "string"}],
                    "responses": {"200": {"description": "Website found"}, "404": {"description": "Website not found"}}
                }
            },
            "/users": {
                "post": {
                    "summary": "Create a user",
                    "consumes": ["application/json"],
                    "parameters": [{"in": "body", "name": "body", "required": True, "schema": {"$ref": "#/definitions/User"}}],
                    "responses": {"201": {"description": "User created"}}
                }
            },
            "/users/{user_id}": {
                "get": {
                    "summary": "Get a user by ID",
                    "parameters": [{"name": "user_id", "in": "path", "required": True, "type": "string"}],
                    "responses": {"200": {"description": "User found"}, "404": {"description": "User not found"}}
                }
            },
            "/scraped_data": {
                "post": {
                    "summary": "Create scraped data",
                    "consumes": ["application/json"],
                    "parameters": [{"in": "body", "name": "body", "required": True, "schema": {"$ref": "#/definitions/ScrapedData"}}],
                    "responses": {"201": {"description": "Scraped data created"}}
                }
            },
            "/scraped_data/{scraped_id}": {
                "get": {
                    "summary": "Get scraped data by ID",
                    "parameters": [{"name": "scraped_id", "in": "path", "required": True, "type": "string"}],
                    "responses": {"200": {"description": "Scraped data found"}, "404": {"description": "Scraped data not found"}}
                }
            },
            "/documents": {
                "post": {
                    "summary": "Create a document",
                    "consumes": ["application/json"],
                    "parameters": [{"in": "body", "name": "body", "required": True, "schema": {"$ref": "#/definitions/Document"}}],
                    "responses": {"201": {"description": "Document created"}}
                }
            },
            "/documents/{document_id}": {
                "get": {
                    "summary": "Get a document by ID",
                    "parameters": [{"name": "document_id", "in": "path", "required": True, "type": "string"}],
                    "responses": {"200": {"description": "Document found"}, "404": {"description": "Document not found"}}
                }
            },
            "/user_queries": {
                "post": {
                    "summary": "Create a user query",
                    "consumes": ["application/json"],
                    "parameters": [{
                        "in": "body",
                        "name": "body",
                        "required": True,
                        "schema": {
                            "$ref": "#/definitions/UserQuery"
                        }
                    }],
                    "responses": {
                        "201": {
                            "description": "User query created"
                        }
                    }
                }
            },
            "/user_queries/{user_query_id}": {
                "get": {
                    "summary": "Get a user query by ID",
                    "parameters": [{
                        "name": "user_query_id",
                        "in": "path",
                        "required": True,
                        "type": "string"
                    }],
                    "responses": {
                        "200": {
                            "description": "User query found"
                        },
                        "404": {
                            "description": "User query not found"
                        }
                    }
                }
            },
            "/training_data": {
                "post": {
                    "summary": "Create training data",
                    "consumes": ["application/json"],
                    "parameters": [{
                        "in": "body",
                        "name": "body",
                        "required": True,
                        "schema": {
                            "$ref": "#/definitions/TrainingData"
                        }
                    }],
                    "responses": {
                        "201": {
                            "description": "Training data created"
                        }
                    }
                }
            },
            "/training_data/{training_data_id}": {
                "get": {
                    "summary": "Get training data by ID",
                    "parameters": [{
                        "name": "training_data_id",
                        "in": "path",
                        "required": True,
                        "type": "string"
                    }],
                    "responses": {
                        "200": {
                            "description": "Training data found"
                        },
                        "404": {
                            "description": "Training data not found"
                        }
                    }
                }
            },
            "/analytics": {
                "post": {
                    "summary": "Create analytics",
                    "consumes": ["application/json"],
                    "parameters": [{
                        "in": "body",
                        "name": "body",
                        "required": True,
                        "schema": {
                            "$ref": "#/definitions/Analytics"
                        }
                    }],
                    "responses": {
                        "201": {
                            "description": "Analytics created"
                        }
                    }
                }
            },
            "/analytics/{analytics_id}": {
                "get": {
                    "summary": "Get analytics by ID",
                    "parameters": [{
                        "name": "analytics_id",
                        "in": "path",
                        "required": True,
                        "type": "string"
                    }],
                    "responses": {
                        "200": {
                            "description": "Analytics found"
                        },
                        "404": {
                            "description": "Analytics not found"
                        }
                    }
                }
            }
        },
        "definitions": {
            "Website": {
                "type": "object",
                "properties": {
                    "website_url": {"type": "string"},
                    "website_name": {"type": "string"}
                }
            },
            "User": {
                "type": "object",
                "properties": {
                    "username": {"type": "string"},
                    "user_type": {"type": "string"},
                    "email": {"type": "string"},
                    "password": {"type": "string"}
                }
            },
            "ScrapedData": {
                "type": "object",
                "properties": {
                    "sourceType": {"type": "string"},
                    "source_id": {"type": "string"},
                    "scraped_content": {"type": "string"}
                }
            },
            "Document": {
                "type": "object",
                "properties": {
                    "document_name": {"type": "string"},
                    "document_path": {"type": "string"},
                    "document_type": {"type": "string"}
                }
            },
            "UserQuery": {
                "type": "object",
                "properties": {
                    "scraped_id": {"type": "string"},
                    "user_id": {"type": "string"},
                    "query": {"type": "string"},
                    "response": {"type": "string"},
                    "rating": {"type": "integer"},
                    "comment": {"type": "string"}
                }
            },
            "TrainingData": {
                "type": "object",
                "properties": {
                    "website_id": {"type": "string"},
                    "data_type": {"type": "string"},
                    "data": {"type": "string"}
                }
            },
            "Analytics": {
                "type": "object",
                "properties": {
                    "website_id": {"type": "string"},
                    "total_queries": {"type": "integer"},
                    "success_rate": {"type": "number"},
                    "rating": {"type": "number"},
                    "total_feedbacks": {"type": "integer"}
                }
            }
        }
    })

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
