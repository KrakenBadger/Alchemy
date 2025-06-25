from datetime import datetime, date
from enum import Enum
from flask import Flask
import jinja_partials
import helpers
import json
import os


__all__ = [
    "DateType",
    "get_current",
    "load_config",
    "create_app"
]


class DateType(Enum):
    DAY = 1
    MONTH = 2
    YEAR = 3
    FULL = 4


def get_current(date_type: DateType) -> date:
    if date_type == DateType.DAY:
        return datetime.now().day
    elif date_type == DateType.MONTH:
        return datetime.now().month
    elif date_type == DateType.YEAR:
        return datetime.now().year
    elif date_type == DateType.FULL:
        return datetime.now().date()


def load_config(path: str, app: Flask) -> None:
    with open(helpers.ROOT_DIR / path, "r") as f:
        app.config.update(json.load(f))



def create_app(config_file: str, FLASK_SECRET_KEY: str) -> Flask:
    app = Flask(
        __name__,
        template_folder=helpers.ROOT_DIR / "templates",
        static_folder=helpers.ROOT_DIR / "static"
    )
    app.secret_key = FLASK_SECRET_KEY
    load_config(config_file, app)
    jinja_partials.register_extensions(app)
    return app
