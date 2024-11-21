# Transaction Management API

## Overview

The Transaction Management API is a Django application that manages financial transactions. It allows users to perform operations such as creating transactions, viewing transaction history, and updating transaction statuses. This project leverages Django REST Framework (DRF) to provide a RESTful interface for managing transactions.

## Features

- _Create Transactions_
  Users can create financial transactions with details like amount, type (DEPOSIT/WITHDRAWAL), and associated user.

- _View Transaction History_
  Retrieve all transactions associated with a specific user.

- _Update Transaction Status_
  Update the status of an existing transaction to either COMPLETED or FAILED.

- _Retrieve Transaction Details_
  Fetch details of a specific transaction by its ID.

## Prerequisites

- _Python 3.8+_
- _Django 4.0+_
- _Django REST Framework (DRF)_
- _SQLite (or any other database configured in settings.py)_

## Installation

Follow these steps to set up the Transaction Management API project locally:

- _Clone the Repository_

`git clone <repository_url>`
`cd transaction-management-api`

- _Create a Virtual Environment_
  Create a virtual environment to isolate dependencies:

`python -m venv env`

- _Activate the Virtual Environment_

On Windows:
`.\env\Scripts\activate`
On Linux/MacOS:
`source env/bin/activate`

- _Install Dependencies_
  Install all required dependencies from the requirements.txt file:

`pip install -r requirements.txt`
Apply Database Migrations
Generate and apply the migrations to set up the database:

`python manage.py makemigrations`
`python manage.py migrate`

- _Create a Superuser_
  Create a superuser account to access the Django admin interface:

`python manage.py createsuperuser`

- _Start the Development Server_
  Launch the Django development server to test the application:

`python manage.py runserver`

## API Endpoints

1. Create a Transaction
   POST `/api/transactions/`

Request Body:

`{
  "amount": 100.00,
  "transaction_type": "DEPOSIT",
  "user": 1
}`

Response:

json
Copy code
{
"transaction_id": 1,
"amount": 100.00,
"transaction_type": "DEPOSIT",
"status": "PENDING",
"user": 1,
"timestamp": "2024-11-16T10:30:00Z"
} 2. Retrieve Transactions by User
GET /api/transactions/?user_id=<user_id>

Response:

json
Copy code
{
"transactions": [
{
"transaction_id": 1,
"amount": 100.00,
"transaction_type": "DEPOSIT",
"status": "PENDING",
"timestamp": "2024-11-16T10:30:00Z"
},
{
"transaction_id": 2,
"amount": 50.00,
"transaction_type": "WITHDRAWAL",
"status": "COMPLETED",
"timestamp": "2024-11-15T15:00:00Z"
}
]
} 3. Update Transaction Status
PUT /api/transactions/<transaction_id>/

Request Body:

json
Copy code
{
"status": "COMPLETED"
}
Response:

json
Copy code
{
"transaction_id": 1,
"amount": 100.00,
"transaction_type": "DEPOSIT",
"status": "COMPLETED",
"timestamp": "2024-11-16T10:30:00Z"
} 4. Retrieve Transaction Details
GET /api/transactions/<transaction_id>/

Response:

json
Copy code
{
"transaction_id": 1,
"amount": 100.00,
"transaction_type": "DEPOSIT",
"status": "COMPLETED",
"timestamp": "2024-11-16T10:30:00Z"
}
