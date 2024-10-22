from flask import Blueprint
from controllers.CategoryController import (
    index as category_index,
    store as category_store,
    show as category_show,
    update as category_update,
    delete as category_delete,
)

# Blueprint untuk Category
category_bp = Blueprint("category_bp", __name__)

# Mendefinisikan route untuk Category
category_bp.route("", methods=["GET"])(category_index)
category_bp.route("", methods=["POST"])(category_store)
category_bp.route("/<int:category_id>", methods=["GET"])(category_show)
category_bp.route("/<int:category_id>/edit", methods=["POST"])(category_update)
category_bp.route("/<int:category_id>", methods=["DELETE"])(category_delete)
