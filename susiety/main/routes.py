from flask import render_template, Blueprint
# from susiety.main.utils import r_quotes

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    return render_template('home.html', title='Home')


@main.route("/about")
def about():
    return render_template('about.html', title='About')


@main.route("/howto")
def howto():
    return render_template('howto.html', title='Howto')


# @main.route("/banner")
# def banner():
#     banner_img = random_banner()
#     return render_template('banner.html', title='Banner', banner_img=banner_img)
