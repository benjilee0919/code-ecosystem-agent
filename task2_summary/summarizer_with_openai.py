import os
import openai
from dotenv import load_dotenv

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_prompt(function_code, context_info):
    return f"""You are reviewing a Python function as a senior software engineer.
Summarize what this function does in plain English.

Function:
{function_code}

Context:
{context_info}

Your output should include:
- Summary of what it does
- Inputs and outputs
- Side effects, if any
"""

if __name__ == "__main__":
    function_code = '''
def calculate_discounted_price(price, discount_percent):
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Invalid discount percent")
    return price * (1 - discount_percent / 100)
'''

    context_info = "- calculates final price after applying discount\n- raises error if discount is out of valid range\n- pure function with no side effects"

    prompt = generate_prompt(function_code, context_info)

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a senior software engineer."},
            {"role": "user", "content": prompt}
        ]
    )

    print("\n=== LLM Summary ===")
    print(response.choices[0].message.content)
