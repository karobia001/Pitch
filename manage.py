from app import create_app,db
from flask_script import Manager,Server
from app.models import User,Pitch


@manager.shell
def make_shell_context():
    return dict(app=app,db=db,User=User,Pitch=Pitch)

if __name__ == '__main__':
    manager.run()