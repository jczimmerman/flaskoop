from flask import Flask

from werkzeug.exceptions import abort

bp = Blueprint('test', __name__)

@bp.route('/')
def index():
    this = ['test', 'also test', 'another test']
    return render_template('scenes/index.html', tests=this)
