from litestar import Litestar

from app.controlers import AuthorController, BookController
from app.database import sqlalchemy_config

app = Litestar([AuthorController, BookController], debug=True, plugins=[sqlalchemy_config])
