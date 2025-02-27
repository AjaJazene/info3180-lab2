from app import app
from flask import render_template, request, redirect, url_for, flash
import datetime


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Aja Ferguson")


def format_date_joined(date):
    """Return the date formatted as 'Month, Year'."""
    return date.strftime("%B, %Y")

@app.route("/profile")
def profile():
    # Set a specific date for demonstration
    date_joined = datetime.date(2025, 2, 7)  # or any date you like
    formatted_date = format_date_joined(date_joined)
    
  
    user_info = {
        "full_name": "Aja Ferguson",
        "username": "AjaJazene",
        "location": "Kingston,Jamaica",
        "bio": "Committed to excellence and growth.",
        "posts": 10,
        "followers": 100,
        "following": 50,
        "date_joined": formatted_date,
        "photo": "images/591e4aa6abf520d5f312a3ce4d3252b3.jpg"  # Path in static folder
    }
    
    # Render the profile template, passing in user_info
    return render_template("profile.html", user=user_info)


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
