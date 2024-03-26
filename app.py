import json

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///goods.db'
db = SQLAlchemy(app)


class Goods(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    tags = db.Column(db.String(20), nullable=False)
    user_evaluation = db.Column(db.Integer, nullable=True)
    price = db.Column(db.Integer, nullable=False)
    stock_balance = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Goods &r' % self.id


# class GoodSchema

@app.route('/', methods=['GET'])
def index():
    goods = Goods.query.all()
    return serialized_goods(goods)


@app.route('/goods/<string:tag>', methods=['GET'])
def get_goods_by_tag(tag):
    print(tag)
    goods = Goods.query.filter_by(tags=tag).all()

    return serialized_goods(goods)


@app.route('/goods/price', methods=['GET'])
def get_goods_by_price_range():
    min_price = request.args.get('min')
    max_price = request.args.get('max')
    goods = Goods.query.filter(Goods.price.between(min_price, max_price))
    result = serialized_goods(goods)
    if not result:
        print('Нет такого диапазона цен')
        return request.args
    else:
        return result


@app.route('/goods/title', methods=['GET'])
def get_goods_by_title():
    title = request.args.get('title')
    goods = Goods.query.filter(Goods.title.like(title))
    return serialized_goods(goods)


def serialized_goods(goods: list[Goods]):
    serialized = []
    for good in goods:
        serialized.append({
            'title': good.title,
            'description': good.description,
            'tags': good.tags,
            'user_evaluation': good.user_evaluation,
            'price': good.price,
            'stock_balance': good.stock_balance
        })
    return serialized


def serialized_json(goods):
    result = []
    for good in goods:
        res = {
            'title': good.title,
            'description': good.description,
            'tags': good.tags,
            'user_evaluation': good.user_evaluation,
            'price': good.price,
            'stock_balance': good.stock_balance
        }
        result.append(json.dumps(res))
    return result


if __name__ == '__main__':
    app.run(debug=True)
