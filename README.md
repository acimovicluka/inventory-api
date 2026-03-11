# Inventory Management API

A REST API for managing product inventory, built with FastAPI and MySQL.

## Tech Stack

- Python
- FastAPI
- MySQL
- SQLAlchemy
- JWT Authentication

## Getting Started

### Prerequisites

- Python 3.11+
- MySQL

### Installation

1. Clone the repository

git clone https://github.com/acimovicluka/inventory-api.git
cd inventory-api

2. Create and activate virtual environment

python -m venv venv
venv\Scripts\activate

3. Install dependencies

pip install -r requirements.txt

4. Create a .env file based on .env.example and fill in your database credentials

5. Run the server

uvicorn app.main:app --reload

6. Open the API documentation at http://127.0.