from flask import  Blueprint, render_template, request
lab3 = Blueprint('lab3', __name__)


@lab3.route('/lab3/')
def lab():
    return render_template('lab3.html')


@lab3.route('/lab3/form1/')
def form1():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'
    age = request.args.get('age')   
    if age == '':
        errors['age'] = 'Заполните поле!'
    sex = request.args.get('sex')

    return render_template ('form1.html', user=user, age=age, sex=sex, errors=errors)


@lab3.route('/lab3/order/')
def order():
    return render_template('order.html')


@lab3.route('/lab3/pay/')
def pay():
    price = 0
    drink = request.args.get('drink')
    if drink == 'coffee':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70
    if request.args.get('sugar') == 'on':
        price += 10
    if request.args.get('milk') == 'on':
        price += 30

    return render_template ('pay.html', price=price)


@lab3.route('/lab3/success/')
def success():
    return render_template ('success.html')


@lab3.route('/lab3/ticketform/')
def ticketform():
    usert = request.args.get('usert')
    print(f'usert={usert}')
    aget = request.args.get('age')
    kind = request.args.get('kind')
    baggage = request.args.get('baggage')
    trainshelf = request.args.get('trainshelf')
    dispatch = request.args.get('dispatch')
    arrival = request.args.get('arrival')
    date = request.args.get('date')
    return render_template('ticketform.html', usert=usert, age=age, kind=kind, baggage=baggage,
                            trainshelf=trainshelf, dispatch=dispatch, arrival=arrival, date=date)

