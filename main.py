from api import create_app
import os

from api.config import Config


def main():
    HOST = os.environ.get("FLASK_RUN_HOST", "127.0.0.1")
    PORT = os.environ.get("FLASK_RUN_PORT", "5000")
    app = create_app(Config)
    app.run(host=HOST, port=int(PORT))


if __name__ == '__main__':
    main()
