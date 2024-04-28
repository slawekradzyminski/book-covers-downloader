from openai import OpenAI
import os
from book_descriptions import book_descriptions

client = OpenAI(api_key='')

# Function to rewrite and summarize descriptions
def rewrite_and_summarize(description):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"Create a short and concise book descriptions based on this description. Do not include any Praise from anyone, just summarize the book:\n\n{description}"}]
    )
    return response.choices[0].message.content

# Open a new file to write the processed descriptions
for title, description in book_descriptions:
    new_description = rewrite_and_summarize(description)
    file_path = os.path.join('descriptions', f'{title}.txt')
    os.makedirs(os.path.dirname(file_path), exist_ok=True)  # Ensure the directory exists
    with open(file_path, 'w') as file:
        file.write(new_description)
