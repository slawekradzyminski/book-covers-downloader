import json
from openai_client import get_openai_client

def rewrite_and_summarize(client, description):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{
            "role": "user", 
            "content": f"Create a short and concise book description based on this description. Do not include any praise from anyone, just summarize the book:\n\n{description}"
        }]
    )
    return response.choices[0].message.content

def process_book_details():
    client = get_openai_client()
    
    with open('book_details.json', 'r') as f:
        book_details = json.load(f)
    
    for book in book_details:
        title = book['title']
        description = book.get('description')
        print(f"Title: '{title}'")
        print(f"Description before change: \n\n '{description}'")
        if description:
            new_description = rewrite_and_summarize(client, description)
            book['description'] = new_description
            print(f"Description after change: \n\n '{new_description}'")
        else:
            print(f"No description found for '{title}'. Skipping...")
        
    with open('book_details.json', 'w') as f:
        json.dump(book_details, f, indent=2)
    
    print("Updated book_details.json with AI-obtained descriptions")

if __name__ == "__main__":
    process_book_details()
