# Import the books list from books_list.py
from books_list import books

def sanitize_title(title):
    """Sanitize the book title to create a valid filename."""
    return title.replace(' ', '_').replace("'", "").replace("-", "_") + '.jpg'

# Create the JavaScript content
js_content = "const books = [\n"
for title, link in books:
    path = "downloaded_covers/" + sanitize_title(title)
    js_content += f"    {{ title: \"{title}\", link: \"{link}\", path: \"{path}\" }},\n"
js_content += "];\n\nexport default books;"

# Write the content to books.js
with open("books.js", "w") as js_file:
    js_file.write(js_content)

print("JavaScript file 'books.js' has been created.")