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

    # connect and query the the db
    connection = steven.model.get_db()
    cur = connection.execute(
        "SELECT username, fullname "
        "FROM users"
    )
    users = cur.fetchall()

    context = {"users": users}
    return flask.render_template('index.html', **context)