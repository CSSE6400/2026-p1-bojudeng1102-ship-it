from flask import Blueprint, jsonify, request

api = Blueprint("api", __name__, url_prefix="/api/v1")

# ---- Health ----
@api.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


# ---- Todos (hardcoded for Week 1) ----
# A single hard-coded todo used for all endpoints this week
HARDCODED_TODO = {
    "id": 1,
    "title": "Watch CSSE6400 Lecture",
    "description": "Watch the CSSE6400 lecture on ECHO360 for week 1",
    "completed": True,
    "deadline_at": "2026-02-27T18:00:00",
    "created_at": "2026-02-20T14:00:00",
    "updated_at": "2026-02-20T14:00:00",
}

@api.route("/todos", methods=["GET"])
def get_todos():
    # Week 1: return hard-coded data
    return jsonify([HARDCODED_TODO]), 200

@api.route("/todos/<int:id>", methods=["GET"])
def get_todo(id: int):
    # Week 1: always return the hard-coded todo, but with requested id
    todo = dict(HARDCODED_TODO)
    todo["id"] = id
    return jsonify(todo), 200

@api.route("/todos", methods=["POST"])
def create_todo():
    # Week 1: accept JSON but return hard-coded todo + 201
    _ = request.get_json(silent=True)  # not used this week
    return jsonify(HARDCODED_TODO), 201

@api.route("/todos/<int:id>", methods=["PUT"])
def update_todo(id: int):
    _ = request.get_json(silent=True)  # not used this week
    todo = dict(HARDCODED_TODO)
    todo["id"] = id
    return jsonify(todo), 200

@api.route("/todos/<int:id>", methods=["DELETE"])
def delete_todo(id: int):
    todo = dict(HARDCODED_TODO)
    todo["id"] = id
    return jsonify(todo), 200