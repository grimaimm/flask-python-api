import sys
from flask import render_template, redirect, url_for, request, abort, jsonify
from models.Book import Book
from models.Category import Category
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def index():
    books = Book.query.all()
    books_with_categories = []

    for book in books:
        category = Category.query.get(book.category_id)
        books_with_categories.append(
            {
                "id": book.id,
                "title": book.title,
                "author": book.author,
                "year": book.year,
                "category_name": category.name if category else "No Category",
            }
        )

    response = {
        "status": "success",
        "data": {"books": books_with_categories},
        "message": "Books retrieved successfully",
    }

    return jsonify(response), 200


def store():
    new_book_data = request.get_json()
    new_book = Book(
        title=new_book_data["title"],
        author=new_book_data["author"],
        year=new_book_data["year"],
        category_id=new_book_data["category_id"],
    )

    db.session.add(new_book)
    db.session.commit()
    return (
        jsonify(
            {
                "message": "Book added successfully",
                "data": {"book": new_book.to_dict()},
            }
        ),
        201,
    )


def show(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({"status": "error", "message": "Book not found"}), 404

    # Fetch the related category from Book
    category = Category.query.get(book.category_id)

    book_data = {
        "id": book.id,
        "title": book.title,
        "author": book.author,
        "year": book.year,
        "category_name": category.name if category else "No Category",
    }

    response = {
        "status": "success",
        "data": {"book": book_data},
        "message": "Book retrieved successfully",
    }

    return jsonify(response), 200


def update(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({"error": "Book not found"}), 404

    updated_data = request.get_json()

    if "title" in updated_data:
        book.title = updated_data["title"]
    if "author" in updated_data:
        book.author = updated_data["author"]
    if "year" in updated_data:
        book.year = updated_data["year"]
    if "category_id" in updated_data:
        category_id = updated_data["category_id"]
        if category_id:
            book.category_id = category_id
        else:
            return jsonify({"error": "Category not found"}), 404

    db.session.commit()
    return jsonify(
        {
            "message": "Book partially updated successfully",
            "data": {"book": book.to_dict()},
        }
    )


def delete(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({"error": "Book not found"}), 404
    db.session.delete(book)
    db.session.commit()
    return jsonify({"message": "Book deleted successfully!"})
