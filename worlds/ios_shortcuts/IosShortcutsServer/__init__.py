from ..flask import Flask

class IosShortcutsServer:
    app = Flask(__name__)

    @app.route("/")
    def hello_world():
        return "<p>Hello, World!</p>"

    async def main(self):
        app.run()