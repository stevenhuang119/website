"""
Steven main view.

URLs include:
/
"""
import flask
import steven


@steven.app.route('/')
def show_index():
    """Display the / route."""
    context = {}
    return flask.render_template('index.html', **context)