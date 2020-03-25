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


@bp.route('/tavern', methods=('GET', 'POST'))
def tavern():

    current_scene = {
    "title": "The Blue Moon Tavern",
    "intro": """You're in the tavern. Straight ahead there is the bar.
    To your right there is a strange man, staring at you. Do you:\n
    1) Go to the bar. 2) Go talk to the strange man."""
    }

    if request.method == 'POST':
        choice = request.form['action']

        if choice == "1":
            return redirect(url_for('scenes.bar'))
        if choice == "2":
            return redirect(url_for('scenes.stranger'))
        else:
            return redirect(url_for('scenes.death'))

    return render_template('scenes/index.html', scene=current_scene)


@bp.route('/bar', methods=('GET', 'POST'))
def bar():

    current_scene = {
    "title": "The bar in the tavern",
    "intro": "You approach the bar in the tavern"
    }

    return render_template('scenes/index.html', scene=current_scene)


@bp.route('/stranger', methods=('GET', 'POST'))
def stranger():

    current_scene = {
    "title": "Approaching the stranger",
    "intro": "You approach the stranger who was eyeing you up."
    }

    return render_template('scenes/index.html', scene=current_scene)


@bp.route('/town-center')
def town_center():

    current_scene = {
    "title": "The town center",
    "intro": "As you wander into the town center..."
    }

    return render_template('scenes/index.html', scene=current_scene)


@bp.route('/trader-wagon')
def trader_wagon():

    current_scene = {
    "title": "The trader's wagon on the edge of town",
    "intro": "You approach the trader's wagon"
    }

    return render_template('scenes/index.html', scene=current_scene)
