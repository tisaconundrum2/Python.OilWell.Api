# Oil Well App API

A simple 

https://wwwapps.emnrd.nm.gov/OCD/OCDPermitting/Data/WellDetails.aspx?api=30-045-35432
## Setup

1. Setup Virtual Enviornment
```
pythom -m 
```

1. Install dependencies:
```
pip install -r requirements.txt
```

2. Run the application:
```
python run.py
```

The API will be available at http://127.0.0.1:5000

## Swagger Documentation

The API includes interactive Swagger documentation. Visit http://127.0.0.1:5000/swagger/ to explore and test the endpoints.

## API Endpoints

### GET /todos
Retrieve all todos

**Response:**
```json
[
  {
    "id": 1,
    "title": "Sample Todo",
    "description": "Description",
    "completed": false
  }
]
```

### GET /todos/<id>
Retrieve a specific todo by ID.

### POST /todos
Create a new todo.

**Request Body:**
```json
{
  "title": "New Todo",
  "description": "Description",
  "completed": false
}
```

### PUT /todos/<id>
Update an existing todo.

**Request Body:**
```json
{
  "title": "Updated Todo",
  "description": "Updated Description",
  "completed": true
}
```

### DELETE /todos/<id>
Delete a todo by ID.

## Project Structure

- `app/models/todo.py`: Todo model
- `app/repositories/todo_repository.py`: Data access layer
- `app/controllers/todo_controller.py`: API routes
- `run.py`: Application entry point
