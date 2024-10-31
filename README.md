To set up the project:
1. Pull the project
2. Run command: "pip install -r requirements.txt"
3. Wait until packages are installed
4. Set up .env file with DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASS variables (just fill the variables with credentials of any PostgreSQL DB)
5. Run command "alembic revision --autogenerate" for generating DB migration
6. Run command "alembic upgrade head" for applying DB migration
7. Run command: "uvicorn main:app --reload"
8. Go to the path: "http://127.0.0.1:8000" in a browser
9. Interact with a chat
10. Also, there is a possibility to go to the path "http://127.0.0.1:8000/docs#/" to check Swagger page to interact with

