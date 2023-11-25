from flask import Flask
import random

app = Flask(__name__)

facts_list = ["Большинство людей, страдающих технологической зависимостью, испытывают сильный стресс, когда они находятся вне зоны покрытия сети или не могут использовать свои устройства.","Согласно исследованию, проведенному в 2018 году, более 50% людей в возрасте от 18 до 34 лет считают себя зависимыми от своих смартфонов.", "Илон Маск утверждает, что социальные сети созданы для того, чтобы удерживать нас внутри платформы, чтобы мы тратили как можно больше времени на просмотр контента." ]
monetka = ["Подбрасывание монетки: тебе выпала решка!","Подбрасывание монетки: тебе выпал орёл!"]

@app.route("/")
def index():
    return f'<h1> Здесь можно узать случайный факт </h1> <a href="/fact>" Посмотреть факт! </a>'

@app.route("/fact")
def facts():
    return f'<p>{random.choice(facts_list)}</p>'

@app.route("/two")
def bye():
    return "<p> Bye! </p>"

@app.route("/secret")
def secrett():
    return f'<p>{random.choice(monetka)}</p>'

if __name__=='__main__':
    app.run()
    
