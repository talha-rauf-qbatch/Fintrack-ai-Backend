import os
from openai import OpenAI
from django.conf import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

# def suggest_expense_category(description: str) -> str:
#     """Use LLM to suggest category for expense."""
#     prompt = f"""
#     You are a financial assistant.
#     Based on this expense description, suggest the most relevant category:
#     Description: "{description}"
#     Categories: Food, Travel, Bills, Shopping, Health, Entertainment, Education, Rent, Utilities,
#     Misc, Transportation, Taxes, Insurance, Debt Repayment, Childcare, Maintenance, Legal, Gifts & Donations, Pets, Miscellaneous.
#     Only return the category name.
#     """
#     response = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[{"role": "user", "content": prompt}],
#         max_tokens=20
#     )
#     return response.choices[0].message.content.strip()

# def suggest_income_category(description: str) -> str:
#     """Use LLM to suggest category for income."""
#     prompt = f"""
#     You are a financial assistant.
#     Based on this income description, suggest the most relevant category:
#     Description: "{description}"
#     Categories: Salary, Business, Investment, Freelancing, Rental Income, Dividends, Interest, Capital Gains,
#     Pension, Annuity, Social Security, Royalties, Gambling Winnings, Alimony, Child Support, Grants,
#     Scholarship, Tax Refund, Sale of Assets, Gift, Inheritance, Other.
#     Only return the category name.
#     """
#     response = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[{"role": "user", "content": prompt}],
#         max_tokens=20
#     )
#     return response.choices[0].message.content.strip()

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
 