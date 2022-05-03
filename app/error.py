from flask import render_template
from app import app

@app.errorhandler(404)
def not_found(error):
    '''
    Function to render the 404 error page
    '''
    return render_template('notfound.html'),404
  
