To set up the project:
1. Pull the project
2. Run command: "pip install -r requirements.txt"
3. Wait until packages are installed
4. Set up .env file with DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASS variables (just fill the variables with credentials of any PostgreSQL DB)
5. Run command "alembic revision --autogenerate" for generating DB migration
6. Run command "alembic upgrade head" for applying DB migration
7. Go to the any PostgresSQL management tool (PGAdmin, for example)
8. Connect to the DB with your own creds which you used for DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASS
9. Make sure that "alembic_version", "chat_history" and "feedback" tables are created
10. Run command: "uvicorn main:app --reload"
11. Go to the path: "http://127.0.0.1:8000" in a browser
12. Interact with a chat and check if chat messages are stored in DB
13. Make sure that feedback messages are stored too
14. Also, there is a possibility to go to the path "http://127.0.0.1:8000/docs#/" to check Swagger page to interact with

