from pydantic import BaseModel


# Schema for inputting message of User
class UserInput(BaseModel):
    message: str


# Schema of bot`s responses
class BotResponse(BaseModel):
    response: str
    sentiment: str


# Schema of receiving feedback
class UserFeedback(BaseModel):
    feedback: str
