# Weather Query Web Application

A Django web application that fetches weather data from OpenWeatherMap and stores query history in PostgreSQL.

## Features
- Fetch current weather for any city
- Store query history in PostgreSQL
- View recent queries on the main page
- Full query history page
- REST API endpoints for queries

## Setup

1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies:
```bash
3. pip install -r requirements.txt
```
4. Create a `.env` file with your settings:DB_NAME=weather_db
```
DB_USER=postgres
DB_PASSWORD=
DB_HOST=
DB_PORT=
WEATHER_API_KEY=
```
<details><summary>Local launch: Django/PostgreSQL</summary><br>

***!!! It is assumed that the user has installed [PostgreSQL](https://www.postgresql.org/)!!!***


1.* Create a new PostgreSQL database and pass the credentials to the [.env] file.

2.Run the migrations and launch the application:
```bash
python manage.py makemigrations && \
python manage.py migrate && \
python manage.py runserver
```
The project will run locally at `http://127.0.0.1:8000/`

</details>

<details><summary>Lounch via Docker: Docker Compose</summary>

2. From the root directory of the project, execute the command:
```bash
docker-compose docker-compose up -d --build
```
The project will be hosted in two docker containers (db, app) at `http://localhost:8000/`.

3. You can stop docker and delete containers with the command from the root directory of the project:
```bash
docker-compose docker-compose down
```
add flag -v to delete volumes 
```bash
 docker-compose docker-compose down -v
 ```
</details><h1></h1>