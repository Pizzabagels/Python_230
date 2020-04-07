import os
import base64

from flask import Flask, render_template, request, redirect, url_for, session

from model import Donation 

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('all'))


@app.route('/donations/')
def all():
    donations = Donation.select()
    return render_template('donations.jinja2', donations=donations)


@app.route('/new', methods=['GET', 'POST'])
def new_donation():
    if request.method == "POST":
        return redirect((url_for('donations')))
    elif request.method == "GET":
        new_donation = Donation(name=request.form['name'], donation=request.form['donation'])
        new_donation.save()
    return render_template('new_donor.jinja2', donations=Donation.select())


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)

