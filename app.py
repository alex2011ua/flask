from flask import Flask,  render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/departures/<departure>/')
def departure(departure):
    return render_template('departure.html', departure=departure)


@app.route('/tours/<id>/')
def tour(id):
    return render_template('tour.html', id=id)


if __name__ == '__main__':
    app.run()
