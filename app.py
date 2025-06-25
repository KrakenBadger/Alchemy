from flask import Flask, url_for
from dotenv import load_dotenv
import os
import helpers
import blueprints
from argparse import ArgumentParser as Parser


load_dotenv(helpers.ROOT_DIR / ".env")


app = helpers.create_app("config.json", os.getenv("FLASK_SECRET_KEY"))


@app.context_processor
def inject_global_template_data():
    root_navigation = [
        helpers.LinkItem("Home", url_for("root.index")),
        helpers.LinkItem("Socials", url_for("root.index")),
        helpers.LinkItem("Projects", url_for("root.index")),
        helpers.LinkItem("Blog", url_for("root.index")),
        helpers.LinkItem("Admin", url_for("root.index")),
    ]
    return {
        "current_year": helpers.get_current(helpers.DateType.YEAR),
        "landing_page": url_for("root.landing"),
        "root_navigation": root_navigation,
    }


app.register_blueprint(blueprints.root)


def main():
    parser = Parser()
    parser.add_argument("--debug", action="store_true")
    parser.add_argument("--host")
    parser.add_argument("--port")
    args = parser.parse_args()

    app.run(debug=args.debug, host=args.host, port=args.port)


if __name__ == "__main__":
    main()
