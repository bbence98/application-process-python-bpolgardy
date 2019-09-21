import data_manager
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/mentor-names')
def mentor_names():
    # We get back dictionaries here (for details check 'database_common.py')
    mentor_names = data_manager.get_mentor_names()

    return render_template('mentor_names.html', mentor_names=mentor_names)


@app.route('/mentor-nicknames')
def mentor_nicknames():
    mentor_nicknames = data_manager.get_mentor_nicknames('Miskolc')

    return render_template('mentor_names.html', mentor_names=mentor_nicknames, mentor_nicknames=True)


@app.route('/applicant-info')
def applicant_info():
    applicant_info = data_manager.get_applicant_info('Carol')

    return render_template('applicant_info.html', applicant_info=applicant_info)


if __name__ == '__main__':
    app.run(debug=True)
