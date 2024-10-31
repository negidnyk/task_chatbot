from textblob import TextBlob
from sqlalchemy import select, insert
from sqlalchemy.sql.expression import func
from src.chatbot.models import ChatHistory, Feedback


# Define fallback message for unexpected inputs
something_went_wrong_msg = "I’m not sure I understand that. Could you clarify?"


# Given function gets message text from "handle message" function and analyzes it using TextBlob lib
async def analyze_sentiment(message):
    # Giving a message to analyze
    analysis = TextBlob(message)

    # The polarity score is a float within the range [-1.0, 1.0]. 1.0 is positive, -1.0 is negative
    # Case positive
    if analysis.sentiment.polarity > 0:
        return "positive"
    # Case negative
    elif analysis.sentiment.polarity < 0:
        return "negative"
    # Case neutral
    elif analysis.sentiment.polarity == 0:
        return "neutral"
    # Handling a case where there is something went wrong
    else:
        return "fallback"


# Generate response based on sentiment and interaction count
async def generate_response(sentiment, interaction_count: int):
    # Checking interaction_count value to ask feedback each 3 messages
    if interaction_count > 0 and interaction_count % 3 == 0:
        return "By the way, I'd love to hear your feedback on our chat so far! 😊"

    # Case positive sentiment
    if sentiment == "positive":
        return "I'm glad to hear that! 😊"
    # Case negative sentiment
    elif sentiment == "negative":
        return "I'm sorry you're facing issues. 😔 Can I help you?"
    # Case neutral sentiment
    elif sentiment == "neutral":
        return "Alright! How can I assist you further?"
    # Case if something went wrong
    else:
        return something_went_wrong_msg


# Get the number of previous interactions from the database
async def get_interaction_count(session) -> int:
    # Getting count of messages rows from DB to determine when to ask feedback
    query = select(func.count()).select_from(ChatHistory)
    result = await session.execute(query)
    count = result.scalar()
    return count


# Send message with sentiment analyzing
async def handle_message(message, session):
    # Analyze sentiment
    sentiment = await analyze_sentiment(message)

    # Get interaction count
    interaction_count = await get_interaction_count(session) + 1

    # Generate bot response
    bot_response = await generate_response(sentiment, interaction_count)

    # Save conversation to the database
    stmt = insert(ChatHistory).values(user_message=message, bot_response=bot_response, sentiment=sentiment)
    await session.execute(stmt)
    await session.commit()

    # Return the bot response
    return {"response": bot_response, "sentiment": sentiment}


# Save feedback message in DB function
async def save_feedback_in_db(feedback, session):
    stmt = insert(Feedback).values(feedback=feedback.feedback)
    await session.execute(stmt)
    await session.commit()
    return {"status": "Feedback received"}
