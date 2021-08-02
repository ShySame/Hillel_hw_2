from flask import Flask, render_template, request
from faker import Faker


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


# -------------------------------------------------------------------------------------
@app.route('/generate-users/')
def users():
    kol=int(request.args.get("numbers"))
    print(kol)
    fake = Faker()
    user = []
    for i in range(kol):
        name = fake.name()
        email = "".join(name.split()) + "@mail.com"
        user_ = name + " : " + email.lower()
        user.append(user_)
    print(user)

    return render_template("user_gen.html", us=user, kol=kol)
# -------------------------------------------------------------------------------------


if __name__ == '__main__':
    app.run(debug=True)
