# Quality Time API

A FastAPI backend project built for learning and improving API design, routing, models, and backend structure.Learn while making is my goal for this project while making this project fun.

## Features
- Quiz API (add, update, delete, list, random)
- Structured with:
  - `models/`
  - `routes/`
  - `database/`
- Clean router-based architecture
- Pydantic data validation
- REST principles
- Fully tested with Swagger UI (`/docs`)

## Project Structure

quality_time_api/
│── app/
│ ├── database/
│ │ ├── memory_db.py
│ ├── models/
│ │ ├── quiz_model.py
│ ├── routes/
│ │ ├── quiz_routes.py
│── main.py
│── venv
│── README.md
│── .gitignore



## API Endpoints

### Quiz Routes
- `POST /quiz/add`
- `GET /quiz/all`
- `GET /quiz/random`
- `PUT /quiz/update/{index}`
- `DELETE /quiz/delete/{index}`

## Installation

```bash
git clone https://github.com/sam5683/quality_time_api
cd quality_time_api
python -m venv venv
venv\Scripts\activate
pip install fastapi uvicorn pydantic or pip install -r requirements.txt
uvicorn main:app --reload

