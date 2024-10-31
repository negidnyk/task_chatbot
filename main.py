from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from src.chatbot.router import router as task_router

app = FastAPI()

# Create templates object for HTML files
templates = Jinja2Templates(directory="templates")

app.include_router(task_router)


# Route for getting chat to interact with
@app.get("/", response_class=HTMLResponse)
async def get_chat_page(request: Request):
    # Serve the index.html template
    return templates.TemplateResponse("index.html", {"request": request})
