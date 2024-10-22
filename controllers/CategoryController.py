import sys
from flask import render_template, redirect, url_for, request, abort, jsonify
from models.Category import Category
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def index():
    categories = Category.query.all()
    return jsonify([category.to_dict() for category in categories])


def store():
    new_category_data = request.get_json()
    new_category = Category(name=new_category_data["name"])
    db.session.add(new_category)
    db.session.commit()
    return (
        jsonify(
            {
                "message": "Category added successfully!",
                "category": new_category.to_dict(),
            }
        ),
        201,
    )


def show(category_id):
    category = Category.query.get(category_id)
    if not category:
        return jsonify({"error": "Category not found"}), 404
    return jsonify(category.to_dict())


def update(category_id):
    category = Category.query.get(category_id)
    if not category:
        return jsonify({"error": "Category not found"}), 404
    updated_category_data = request.get_json()
    if "name" in updated_category_data:
        category.name = updated_category_data["name"]
    db.session.commit()
    return jsonify(
        {
            "message": "Category partially updated successfully!",
            "category": category.to_dict(),
        }
    )


def delete(category_id):
    category = Category.query.get(category_id)
    if not category:
        return jsonify({"error": "Category not found"}), 404
    db.session.delete(category)
    db.session.commit()
    return jsonify({"message": "Category deleted successfully!"})
