from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello Web!'


# -------------------------------------------------------------------------------------
f = open('requirements.txt', 'r')
g = f.read()


@app.route('/requirements/')
def requir():
    return render_template('requir.html', text=g)


f.close()
# -------------------------------------------------------------------------------------


if __name__ == '__main__':
    app.run(debug=True)
