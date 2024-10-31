from sqlalchemy import Column, Integer, String, Text, DateTime, MetaData
from datetime import datetime
from database import Base


metadata = MetaData()


# Creating DB model of chat history to save it
class ChatHistory(Base):
    __tablename__ = "chat_history"

    id = Column(Integer, primary_key=True, index=True)
    user_message = Column(Text)
    bot_response = Column(Text)
    sentiment = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)


# Creating DB model for soring feedback
class Feedback(Base):
    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    feedback = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)