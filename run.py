from app import create_app, db
from app.auth.models import User
from sqlalchemy import exc


#This is for creating all database objects using dev confiuration
flask_app = create_app('dev')
with flask_app.app_context():
    db.create_all()
    try:
        if not User.query.filter_by(user_name='harry').first():
            User.create_user(user='harry', email='harry@potters.com', password='secret')
    except exc.IntegrityError:
            flask_app.run()
"""            
#This is for running site using dev confiuration
if (__name__ == '__main__'):
    flask_app = create_app('dev')
    flask_app.run()

"""
