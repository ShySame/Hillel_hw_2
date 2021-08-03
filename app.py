from flask import Flask, render_template, request,url_for
from faker import Faker
import csv, requests

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello Web!'
# -------------------------------------------------------------------------------------
@app.route('/requirements/')
def requir():
    f = open('requirements.txt', 'r')
    g = f.read()
    f.close()
    return render_template('requir.html', text=g)
# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
@app.route('/generate-users/')
def users():
    kol=int(request.args.get("numbers"))
    fake = Faker()
    user = []
    for i in range(kol):
        name = fake.name()
        email = "".join(name.split()) + "@mail.com"
        user_ = name + " : " + email.lower()
        user.append(user_)
    return render_template("user_gen.html", us=user, kol=kol)
# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
@app.route('/mean/')
def heiwei():
    with open("hw.csv", newline='') as csvfile:
        reader_object = csv.DictReader(csvfile, delimiter=",")
        height, weight=0,0
        for row in reader_object:
            height+=float(row['Height(Inches)'])
            weight += float(row['Weight(Pounds)'])
        kol=int(row['Index'])
    return render_template('average.html', avg_hei=height/kol, avg_wei=weight/kol)
# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
@app.route('/space/')
def space():
    r = requests.get('http://api.open-notify.org/astros.json')
    return render_template('space.html', kol=r.json()['number'])
# -------------------------------------------------------------------------------------


if __name__ == '__main__':
    app.run(debug=True)
