from flask import render_template
from . import main
from flask_login import login_required
from ..models import Pitch,Comment,Types

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    
    types = Types.get_categories()
    
    title = 'Pitch up your Pitch'
    return render_template('index.html',types=types, title=title)
    
@main.route('/type/<int:id>')
def single_type(id):
    '''
    A view function that will return the pitches on a specific kind of view
    '''

    types = Types.query.get(id)
    title = f'{types.name} pitches'
    pitches = Pitch.get_pitches(types.id)

    return render_template('type.html', title=title,types=types,pitches=pitches)

@main.route('/type/pitch/new/<int : id>', methods=["GET","POST"])
@login_required
def pitch_new(id):
    '''
    view function that helps renders theform to create a new pitch
    '''