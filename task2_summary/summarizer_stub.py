def generate_prompt(function_code, context_info):
    return f"""
You are reviewing a Python function as a senior software engineer.
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

# Example usage
if __name__ == "__main__":
    sample_function = '''
def get_user_profile(user_id):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise ValueError("User not found")
    return user.to_dict()
'''

    context = "- queries User from database\n- uses SQLAlchemy ORM\n- returns dictionary\n"
    prompt = generate_prompt(sample_function, context)
    
    print("=== Generated Prompt ===")
    print(prompt)

