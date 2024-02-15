from api.v1.auth.auth import Auth
from flask import abort, jsonify, request
from models.user import User
from api.v1.views import app_views

auth = Auth()

@app_views.route('/users/me', methods=['GET'], strict_slashes=False)
def view_current_user() -> str:
    """ GET /api/v1/users/me
    Return:
      - Authenticated User object JSON represented
      - 404 if no authenticated user
    """
    current_user = request.current_user
    if current_user is None:
        abort(404)
    return jsonify(current_user.to_json())

@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def view_one_user(user_id: str = None) -> str:
    """ GET /api/v1/users/:id
    Path parameter:
      - User ID
    Return:
      - User object JSON represented
      - 404 if the User ID doesn't exist
    """
    if user_id is None:
        abort(404)
    if user_id == "me":
        if request.current_user is None:
            abort(404)
        user = request.current_user
        return jsonify(user.to_json())
    user = User.get(user_id)
    if user is None:
        abort(404)
    if request.current_user is None:
        abort(404)
    return jsonify(user.to_json())

