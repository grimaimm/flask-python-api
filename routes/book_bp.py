from flask import Blueprint
from controllers.BookController import (
    index as book_index,
    store as book_store,
    show as book_show,
    update as book_update,
    delete as book_delete,
)

# Blueprint untuk Book
book_bp = Blueprint("book_bp", __name__)

# Mendefinisikan route untuk Book
book_bp.route("/", methods=["GET"])(book_index)
book_bp.route("/", methods=["POST"])(book_store)
book_bp.route("/<int:book_id>", methods=["GET"])(book_show)
book_bp.route("/<int:book_id>/edit", methods=["POST"])(book_update)
book_bp.route("/<int:book_id>", methods=["DELETE"])(book_delete)
