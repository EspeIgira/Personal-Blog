from flask import Blueprint
main = Blueprint('main',__name__)
from . import views,error
from flask_mail import Mail
from flask_uploads import UploadSet,configure_uploads,IMAGES

mail = Mail()


def create_app(config_name):
    app = Flask(__name__)
    
    mail.init_app(app)

    




