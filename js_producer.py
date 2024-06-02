from books_list import books

def sanitize_title(title):
    """Sanitize the book title to create a valid filename."""
    return title.replace(' ', '_').replace("'", "").replace("-", "_").replace("?", "").replace("!", "") + '.jpg'

def read_description(title):
    """Read the description from a file in the descriptions folder."""
    description_path = f"descriptions/{title}.txt"
    try:
        with open(description_path, 'r') as file:
            description = file.read().strip()
            return description.replace('"', '\\"')
    except FileNotFoundError:
        return "Description not found."

# Create the JavaScript content
js_content = "const books = [\n"
for title, link in books:
    path = "downloaded_covers/" + sanitize_title(title)
    description = read_description(title)
    js_content += f"    {{ title: \"{title}\", link: \"{link}\", path: \"{path}\", description: \"{description}\", tags: []}},\n"
js_content += "];\n\nexport default books;"

# Write the content to books.js
with open("books.js", "w") as js_file:
    js_file.write(js_content)

print("JavaScript file 'books.js' has been created.")