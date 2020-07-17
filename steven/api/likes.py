"""
REST API for likes
"""

import flask
import steven

@steven.app.route('/api/v1/likes/', methods=['GET'])
def get_likes():
    context = {
        'name': 'steven',
        'likes_count': 3,
        'url': flask.request.path,
    }
    return flask.jsonify(**context)