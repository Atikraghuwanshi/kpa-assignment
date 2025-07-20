#KPA Assignment AP



This is a FastAPI backend built for the KPA assignment. It contains two APIs:
-  Pizza API: To create and retrieve pizza records.
-  Wheel Specification API: To submit and fetch wheel spec data.


### Setup Instructions (Local)

1. Clone or download this project folder
2. Open the folder in VS Code or any terminal
3. Create and activate a virtual environment:

```bash

python -m venv venv #Creating a Virtual Environment 

.\venv\Scripts\activate    # For Windows

pip install -r requirements.txt #Install Dependencies

DATABASE_URL=postgresql://username:password@localhost/dbname    #create.env file(replace password with your PostgreSQL Password)

uvicorn main:app --reload # Running the Server

http://127.0.0.1:8000/docs # Open in Browser


### Tech Used
- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- Uvicorn
- Postman

### Pizza API
- `GET /v1/pizzas/` — Get all pizzas
- `POST /v1/pizzas/` — Create a pizza

### Wheel Specification API
- `GET /api/forms/wheel-specifications/` — Get wheel specs
- `POST /api/forms/wheel-specifications/` — Submit wheel spec

### Notes
- Ensure PostgreSQL is running
- The Postman collection file is included: `KPA-ATIK-Assignment.postman_collection.json`
- Swagger UI is available at: `/docs`
