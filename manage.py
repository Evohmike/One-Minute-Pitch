from app import create_app,db
from flask_script import Manager,Server

#connect to models
from app.models import User




# Creating app instance
app = create_app('development')

#create manger instance
manager = Manager(app)

manager.add_command('server',Server)


@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User )
    
if __name__ == '__main__':
    manager.run()



