import os 

basedir = os.path.abspath(os.path.dirname(__file__))
# give access to the project in any OS(operating System) we find ourselves in
#allow outside files/folders to be added to the project from the base directory 

class Config():
    """
      set config variables for the flask app.
      using environment variables where available otherwise
      create the config variable if not done already.
    """  
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'You will never guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False # turn off update msg from the sqlalchemy 