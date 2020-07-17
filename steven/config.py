"""
Steven website development configuration
"""

import pathlib

APPLICATION_ROOT = '/'

# Secret key for encrypting cookies
SECRET_KEY = b'\x03,\xae\x92\x108\xean\xef\xb4\x1a\xb2\x195K\xd9\xc8\xb3w\\\x1c\xe4\x86\xdc'
SESSION_COOKIE_NAME = 'login'

# File uploads to var/uploads/
steven_ROOT = pathlib.Path(__file__).resolve().parent.parent # the folder where the package lives in
UPLOAD_FOLDER = steven_ROOT/'var'/'uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
MAX_CONTENT_LENGTH = 16 * 1024 * 1024

# Database file is var/stevendb.sqlite3
DATABASE_FILENAME = steven_ROOT/'var'/'stevendb.sqlite3'