#!/usr/bin/python3
"""
Create an endpoint that retrieves the number of each objects by type:
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route("/status")
def status():
    """
    Create JSON status
    """
    return jsonify({'status': 'OK'})


@app_views.route("/stats")
def storage_counts():
    '''
        return counts of all classes in storage
    '''
    cls_counts = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User")
    }
    return jsonify(cls_counts) 
