from api import create_app
import os


def main():
    HOST = os.environ.get("FLASK_RUN_HOST", "127.0.0.1")
    PORT = os.environ.get("FLASK_RUN_PORT", "5000")
    app = create_app()
    app.run(host=HOST, port=PORT)


if __name__ == '__main__':
    main()
