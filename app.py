from flask import Flask, render_template, redirect, request
from my_forms import TextForm
import get_site


app = Flask(__name__, template_folder='templates')

app.config['SECRET_KEY'] = 'you-will-never-guess'


@app.route('/', methods=['GET'])
def home():
    form = TextForm()
    return render_template('home.html', form=form)


@app.route('/', methods=['POST'])
def submit():
    form = TextForm(request.form)
    if form.validate():
        link = form.link.data
        price, price_from_advert = get_site.predict(link)
        return render_template('car.html', link=link, price=price, price_from_advert=price_from_advert)
    return redirect('/')


if __name__ == '__main__':
    app.run()
