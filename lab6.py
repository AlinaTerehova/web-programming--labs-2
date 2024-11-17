from flask import Blueprint, render_template, redirect, request, session, current_app


lab5 = Blueprint('lab6', __name__)

@lab5.route('/lab6/')
def lab():
    return render_template('lab6/lab6.html')
