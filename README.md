# Flask MongoDB CRUD Application

This is a simple Flask application that performs CRUD (Create, Read, Update, Delete) operations on a MongoDB database for a User resource using a REST API. The application is containerized using Docker.

## Features

- REST API endpoints for CRUD operations on a User resource
- User resource fields: `id`, `name`, `email`, `password`
- Dockerized for easy setup and deployment

## Prerequisites

- Docker
- Docker Compose

## Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd flask_mongo_app

```

### 2. Build and Run the Docker Containers

docker-compose up --build

### 3. Access the Application
 
http://localhost:5000/

### 4. Test the Endpoints

You can use a tool like Postman or curl to test the API endpoints.

- GET /users: Returns a list of all users.
- GET /users/<id>: Returns the user with the specified ID.
- POST /users: Creates a new user with the specified data.
- PUT /users/<id>: Updates the user with the specified ID with the new data.
- DELETE /users/<id>: Deletes the user with the specified ID.

## Project Structure

flask_mongo_app/
│
├── app/
│   ├── __init__.py        # Initialize the Flask app and register Blueprints
│   ├── config.py          # Configuration settings for the Flask app
│   ├── models.py          # MongoDB models and schema definitions
│   └── routes.py          # API route definitions
│
├── Dockerfile             # Dockerfile for building the Flask app image
├── requirements.txt       # Python dependencies
└── run.py                 # Entry point for running the Flask app

