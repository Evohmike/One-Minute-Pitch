from app import create_app,db
from flask_script import Manager,Server
from  flask_migrate import Migrate, MigrateCommand
from app.models import User, Role, Category,Pitch

#connect to models
from app.models import User

# Creating app instance
app = create_app('production')

#create manager instance
manager = Manager(app)

manager.add_command('server',Server)

# Create migrate instance
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)


@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User,Category=Category, Pitch=Pitch )
    
if __name__ == '__main__':
    manager.run()






# # Import db from app factory
# from app import create_app,db
# from flask_script import Manager,Server
# # Connect to models
# from app.models import User,Post,Comment,Upvote,Downvote
# # Set up migrations
# from flask_migrate import Migrate,MigrateCommand

# # Creating app instance
# app = create_app('development')


# # Create manager instance
# manager = Manager(app)

# # Create migrate instance
# migrate = Migrate(app,db)

# manager.add_command('server',Server)
# manager.add_command('db',MigrateCommand)

# if __name__ == '__main__':
#     manager.run()
