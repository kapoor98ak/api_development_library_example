from flask import Flask, jsonify, request

app = Flask(__name__)

# Placeholder data for demonstration purposes
books = [
    {"id": 1, "title": "The Catcher in the Rye", "author": "J.D. Salinger"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
]

# Step 3: Define Endpoints (in the same script)
@app.route('/books', methods=['GET'])
def get_all_books():
    return jsonify(books)

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((b for b in books if b['id'] == book_id), None)
    if book:
        return jsonify(book)
    else:
        return jsonify({"error": "Book not found"}), 404  # 404 status code for not found

@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.get_json()
    new_book['id'] = max(b['id'] for b in books) + 1
    books.append(new_book)
    return jsonify(new_book), 201  # 201 status code indicates resource creation

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((b for b in books if b['id'] == book_id), None)
    if book:
        updated_data = request.get_json()
        book.update(updated_data)
        return jsonify(book)
    else:
        return jsonify({"error": "Book not found"}), 404

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [b for b in books if b['id'] != book_id]
    return 'Deleted!', 204  # 204 status code indicates successful deletion with no content

# Step 4: Run the App
if __name__ == '__main__':
    app.run(debug=True)
