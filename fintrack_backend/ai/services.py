import os
from openai import OpenAI
from django.conf import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)


def financial_chatbot(query: str) -> str:
    """AI Chatbot to provide investment/saving advice based on income & expenses."""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a financial advisor chatbot. Give helpful advice based on user queries."},
            {"role": "user", "content": query}
        ],
        max_tokens=200
    )
    return response.choices[0].message.content.strip()
 