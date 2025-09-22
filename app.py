from flask import Flask, render_template

application = Flask(__name__)

@application.route('/')
def home():
    return render_template('base.html')

@application.route('/donation')
def page2():
    return render_template('donation.html')

if __name__ == '__main__':
    application.run(debug=False)