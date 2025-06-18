## Overview

This repository contains two backend projects demonstrating different approaches to interacting with a PostgreSQL database:

1. **MVT (Model-View-Template) Project**: Traditional Django web application
2. **API Project**: Pure REST API implementation using Django REST Framework

Both projects provide the same core functionality for adding and deleting data from a PostgreSQL database.

## Project 1: MVT Implementation

### Description
A traditional Django web application using the Model-View-Template pattern to:
- Add data to PostgreSQL database
- Delete data from PostgreSQL database
- View existing data

### Features
- Django admin interface for data management
- Form-based CRUD operations
- Template-rendered views
- PostgreSQL database integration

### Setup
```bash
# Install requirements
pip install -r requirements.txt

# Configure database settings in settings.py

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver

```

## Project 2: Pure API Implementation

### Description
Implements the same functionality as the MVT project but as a pure REST API using Django REST Framework:
- RESTful endpoints for adding/deleting data
- JSON responses

### Features
- REST API endpoints
- JSON request/response format
- Swagger documentation
- PostgreSQL database integration

### Setup
```bash
# Install requirements
pip install -r requirements.txt

# Configure database (same as MVT project)

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver
```
