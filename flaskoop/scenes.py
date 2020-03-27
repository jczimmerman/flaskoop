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
    To your right there is a strange man, staring at you. Do you:
    1) Go to the bar. 2) Go talk to the strange man. 3.) Leave the tavern."""
    }

    if request.method == 'POST':
        choice = request.form['action']

        if choice == "1":
            return redirect(url_for('scenes.bar'))
        elif choice == "2":
            return redirect(url_for('scenes.stranger'))
        elif choice == "3":
            return redirect(url_for('scenes.town_center'))
        else:
            return redirect(url_for('scenes.death'))

    return render_template('scenes/index.html', scene=current_scene)


@bp.route('/bar', methods=('GET', 'POST'))
def bar():

    current_scene = {
    "title": "The bar in the tavern",
    "intro": """You approach the bar in the tavern, the bartender sees you
    coming and offers you some ale... and some advice. 'Avoid that strange
    man over there!' Do you: 1) Buy an ale. 2) Go back to the tavern."""
    }

    if request.method == 'POST':
        choice = request.form['action']

        if choice == "1":
            return redirect(url_for('scenes.death'))
        elif choice == "2":
            return redirect(url_for('scenes.tavern'))
        else:
            return redirect(url_for('scenes.death'))

    return render_template('scenes/index.html', scene=current_scene)


@bp.route('/stranger', methods=('GET', 'POST'))
def stranger():

    current_scene = {
    "title": "Approaching the stranger",
    "intro": """You approach the stranger who was gazing at you with curious
    eyes. Before you have a chance to say anything, he starts speaking. 'You
    look like just the person I was looking for. If you're interested, I know
    of a spot with enough gold to buy the Kings castle and have some to spare.
    I'll tell you all about it on one condition. If you manage to make it to the
    gold, you must share it with me.' Do you: 1) Accept the strangers proposition.
    2) Go back to the tavern."""
    }

    if request.method == 'POST':
        choice = request.form['action']

        if choice == "1":
            return redirect(url_for('scenes.stranger_advice'))
        elif choice == "2":
            return redirect(url_for('scenes.tavern'))
        else:
            return redirect(url_for('scenes.death'))


    return render_template('scenes/index.html', scene=current_scene)


@bp.route('/stranger/advice', methods=('GET', 'POST'))
def stranger_advice():

    current_scene = {
    "title": "Approaching the stranger - advice",
    "intro": """You accept the stranger's offer. He replies, 'Good, I will
    give you some advice then. When you come across a lock, the way in is as easy
    as ABC.' The stranger is done talking now, and you decide to go on your way.
    Do you: 1) Go back to the tavern 2) Leave the tavern"""
    }

    return render_template('scenes/index.html', scene=current_scene)


@bp.route('/town-center')
def town_center():

    current_scene = {
    "title": "The town center",
    "intro": """You wander into the town center and look around. To the north there
    is the Gloomy Forest, which seems like just looking at it makes you feel uneasy.
    To the south there is the Somber Mountains, once home to the dwarves, now home to
    wolves and bears. Do you: """
    }

    return render_template('scenes/index.html', scene=current_scene)


@bp.route('/road')
def trader_wagon():

    current_scene = {
    "title": "The trader's wagon on the edge of town",
    "intro": "You approach the trader's wagon"
    }

    return render_template('scenes/index.html', scene=current_scene)
