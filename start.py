﻿from app import create_app, db
from app.models import *
#, Follow, Role, Permission, Post, Comment
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand

#app = create_app(os.getenv('FLASK_CONFIG') or 'default')
app= create_app()
manager = Manager(app)
migrate = Migrate(app, db)
#User.generate_fake()

def make_shell_context():
    return dict(app=app, db=db, Korisnik=Korisnik)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@manager.command
def deploy():
    from flask.ext.migrate import upgrade

    upgrade()



    #prije je runnao manager-a, sljivis njega zasad
if __name__ == '__main__':
    app.run(threaded=True) #podrška za mulithreading (ubrzava kad su 2 browsera fkt.)

   