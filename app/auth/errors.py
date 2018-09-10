from flask import render_template
from . import auth


# Error handler decorator
@auth.app_errorhandler(404)
def four_Ow_four(error):
    '''
    Function to render the 404 error page
    '''
    title = 'Not Found'
    return render_template('fourOwfour.html', title=title,404
