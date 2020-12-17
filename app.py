import os
import signal

from flask import Flask, request, render_template

from project import generator, parser_vk

app = Flask(__name__, template_folder='resources', static_folder='resources')

signal.signal(signal.SIGINT, lambda s, f: os.exit(0))


@app.route('/')
def generate_news():
    page = '<html><head><meta content="text/html; charset=windows-1251"><title>RatVK</title><style>'
    page += 'table {font-family: "Lucida Sans Unicode", "Lucida Grande", Sans-Serif;font-size: 14px; ' \
            'border-collapse: collapse; text-align: center; margin: auto;}\n' \
            'th, td:first-child { background: #a1b4e5; color: white; padding: 10px 20px; }\n th, td { border-style: ' \
            'solid;' \
            'border-width: 0 2px 2px 0; border-color: white; }\n' \
            'td { background: #D8E6F3; }\n' \
            'th:first-child, td:first-child { text-align: left; }\n'
    page += '.txt {font-family: "Lucida Sans Unicode", "Lucida Grande", Sans-Serif; font-size:50px; ' \
            'letter-spacing:2px; width:100%; ' \
            'position: relative; display: block; top: 7%; margin: 0 auto; margin-left: auto;' \
            'margin-right: auto; text-align: center;}\n'
    page += '.profile {font-family: "Lucida Sans Unicode", "Lucida Grande", Sans-Serif; font-size:25px; ' \
            'text-align: center;}\n'
    page += '.form {position: fixed; bottom: 10px; left: 50%; margin-left: -104.5px;}\n'
    page += '.ex5 .txt:before {content: ""; position: absolute; height: 3px; width: 400px;' \
            'background:rgb(81, 227, 213); top: -7%;margin: 0 auto; left: 0;right: 0;}\n'
    page += '\n</style></head>' \
            '<body><div class="ex5"><p class="txt" ">RatVK - чекаем страницу Сани</p></div>'
    url = "https://vk.com/id185394982/"
    page += '<h3 class="profile"><img src="' + parser_vk.get_profile_pic(url) + '"">'
    page += parser_vk.get_profile_name(url) + '</h3>'
    page += '<h3 class="profile">Статус: ' + parser_vk.get_profile_online_status(url) + '</h3>'
    page += '<h3 class="profile">Слушает: ' + parser_vk.get_profile_music(url) + '</h3>'
    page += '<h3 class="profile" align="center">' \
            '<form action="/generator" target="_blank" style="position: absolute; bottom: 0"><button>Генератор ' \
            'слоганов</button></form> '
    page += '</body></html>'
    return page


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/generator')
def generate_buzz():
    page = '<html><head><meta content="text/html; charset=windows-1251"><title>Мой CI/CD проект</title><style>'
    page += "table {font-family: \"Lucida Sans Unicode\", \"Lucida Grande\", Sans-Serif;font-size: 14px; " \
            "border-collapse: collapse; text-align: center; margin: auto;}" \
            "th, td:first-child { background: #a1b4e5; color: white; padding: 10px 20px; } th, td { border-style: " \
            "solid;" \
            "border-width: 0 2px 2px 0; border-color: white; }" \
            "td { background: #D8E6F3; }" \
            "th:first-child, td:first-child { text-align: left; }"
    page += '.txt {font-family: "Lucida Sans Unicodes"; font-size:50px; letter-spacing:2px; width:100%; ' \
            'position: relative; display: block; top: 7%; margin: 0 auto; margin-left: auto;' \
            'margin-right: auto; text-align: center;}'
    page += '.ex5 .txt:before {content: ""; position: absolute; height: 3px; width: 400px;' \
            'background:rgb(81, 227, 213); top: -7%;margin: 0 auto; left: 0;right: 0;}'
    page += '</style></head>' \
            '<body><div class="ex5"><p class="txt">Генератор слоганов</p></div>'
    page += '<h2 align="center">' + generator.generate_buzz() + '</h2>'
    page += '</body></html>'
    return page


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.getenv('PORT'))  # port 5000 is the default
