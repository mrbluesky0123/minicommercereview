from flask import Flask, request, jsonify, current_app
import json

app = Flask(__name__)

@app.route('/goodsreview/<goods_id>', methods=['GET'])
def get_goods_review(goods_id):
    json_data = json.loads(request.data)
    return services.send_result_service(json_data)

@app.route('/score/getrankdata', methods=['POST'])
def get_rank_data():
    json_data = json.loads(request.data)
    return services.get_rank_data_service(json_data)

@app.route('/score/checkrestartable/<session_id>', methods=['GET'])
def check_restartable(session_id):
    return services.check_restartable_service(session_id)

@app.route('/score/getuserscore/<session_id>/<user_name>', methods=['GET'])
def get_user_score(session_id, user_name):
    return services.get_user_score_service(session_id, user_name)

@app.route('/score/register_user', methods=['POST'])
def register_user():
    json_data = json.loads(request.data)
    return services.register_user_service(json_data)

@app.route('/score/test', methods=['POST'])
def test():
    json_data = json.loads(request.data)
    return services.test(json_data)
