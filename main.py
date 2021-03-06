import os
from os import error
from flask import Flask, jsonify, request, make_response
import amazon_api as API

app = Flask(__name__)

@app.route('/', methods=["POST"])
def post_img():
    # input_url = request.args.getlist("input")
    img = request.files['upfile'].read()
    # img.save(img.filename)
    # 入力
    # 処理
    # post_img = '/Users/Minami-Yuta/就活用/サマーインターンシップ/Optim/img/yasai.jpg'
    Amazon_api = API.amazon_api() # インスタンス作成
    recog_result = Amazon_api.call_api(img=img) # AmazonAPIを呼び出し，画像認識した結果のラベルリスト(json形式)
    label_list = Amazon_api.output_label(response_label_list=recog_result) # 食材ラベルの出力
    
    resp = make_response(jsonify(label_list))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    resp.headers['Access-Control-Allow-Methods'] = 'GET,PUT,POST,DELETE,OPTIONS'
    return resp

@app.route("/ping", methods=["GET"])
def index():
    return "ok"
    
if __name__ == "__main__":
    port = int(os.getenv("PORT", 8889))
    app.run(host="0.0.0.0", port=port)
