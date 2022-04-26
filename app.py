from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

# client = MongoClient('localhost', 27017, username="test", password="test")
client = MongoClient('mongodb://test:test@localhost', 27017)
# client = MongoClient('localhost', 27017)
db = client.dbonepage

## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')

# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    name_receive = request.form['name_give']
    model_receive = request.form['model_give']
    color_receive = request.form['color_give']
    count_receive = request.form['count_give']
    addr_receive = request.form['addr_give']
    phone_receive = request.form['phone_give']

    doc = {
        'name': name_receive,
        'model': model_receive,
        'color': color_receive,
        'count': count_receive,
        'addr': addr_receive,
        'phone': phone_receive
    }
    db.iphone13.insert_one(doc)
    return jsonify({'result':'success','msg': '주문 완료!'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    order_list = list(db.iphone13.find({}, {'_id':False}))
    return jsonify({'result': 'success', 'orders': order_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)