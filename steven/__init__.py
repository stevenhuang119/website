"""
Steven Personal Website Package Initializer
"""
import flask

# the app object will be used by all the code modules in this package
app = flask.Flask(__name__) # pylint: disable=invalid-name

# read the settings from the config module (insta485/config.py)
app.config.from_object('steven.config')

app.config.from_envvar('steven_SETTINGS', silent=True)

import steven.views # noqa: E402  pylint: disable=wrong-import-position
import steven.model # noqa: E402  pylint: disable=wrong-import-position
import steven.api # noqa: E402 pylint: disable=wrong-import-position
