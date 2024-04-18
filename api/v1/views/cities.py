#!/usr/bin/python3
"""
    This is the cities page handler for Flask.
"""
from api.v1.views import app_views
from models import storage
from flask import abort, jsonify, request

from models.city import City
from models.state import State


@app_views.route('/states/<id>/cities', methods=['GET', 'POST'])
def states_id_cities(id):
    """
        Flask route at /states/<id>/cities.
    """
    state = storage.get(State, id)
    if (state):
        if request.method == 'POST':
            kwargs = request.get_json()
            if not kwargs:
                return {"error": "Not a JSON"}, 400
            if "name" not in kwargs:
                return {"error": "Missing name"}, 400
            new_city = City(state_id=id, **kwargs)
            new_city.save()
            return new_city.to_dict(), 201

        elif request.method == 'GET':
            return jsonify([c.to_dict() for c in state.cities])
    abort(404)