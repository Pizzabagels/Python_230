import os
import base64

from flask import Flask, render_template, request, redirect, url_for, session

from model import Donation, Donor

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('all'))


@app.route('/donations/')
def all():
    donations = Donation.select()
    return render_template('donations.jinja2', donations=donations)


@app.route('/new/', methods=['GET', 'POST'])
def new_donation():
    if request.method == "GET":
        return render_template('new_donor.jinja2')
    elif request.method == "POST":
        donor_name = request.form['name']
        donation_amount = request.form['donation']
        donor = Donor.select().where(Donor.name == donor_name).get()
        donation = Donation(value=donation_amount,donor=donor)
        donation.save()
        return all()


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port, debug=True)

