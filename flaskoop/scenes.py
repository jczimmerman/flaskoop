from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from werkzeug.exceptions import abort

bp = Blueprint('scenes', __name__)

@bp.route('/')
def index():
    return render_template('base.html')


@bp.route('/death')
def death():
    return render_template('scenes/death.html')


@bp.route('/tavern')
def tavern():

    current_scene = {
    "title": "The tavern",
    "intro": "As you walk into the room..."
    }

    return render_template('scenes/index.html', scene=current_scene)


@bp.route('/town-center')
def town_center():

    current_scene = {
    "title": "The town center",
    "intro": "As you wander into the town center..."
    }

    return render_template('scenes/index.html', scene=current_scene)
