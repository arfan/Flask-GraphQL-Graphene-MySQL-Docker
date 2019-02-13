from flask_script import Server, Manager
from app import create_app

app = create_app()
server = Server(host="0.0.0.0", port=5000)
manager = Manager(app)
manager.add_command("runserver", server)


if __name__ == "__main__":
    manager.run()