from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session
from src.chatbot.services import handle_message, save_feedback_in_db
from src.chatbot.schemas import UserInput, BotResponse, UserFeedback

# Making custom router for chatbot logic
router = APIRouter(
    prefix="/task",
    tags=["Task"]
)


# Sending message to the chat route which calls handle_message function for analyzing sentiment and store conversation
# history
@router.post("/chat/", response_model=BotResponse)
async def chat_with_bot(user_input: UserInput, session: AsyncSession = Depends(get_async_session)):
    return await handle_message(user_input.message, session)


# Sending feedback message route which calls "save_feedback_in_db" function for saving feedback msg in DB and return
# successful message after saving
@router.post("/feedback/")
async def save_feedback(feedback: UserFeedback, session: AsyncSession = Depends(get_async_session)):
    return await save_feedback_in_db(feedback, session)
