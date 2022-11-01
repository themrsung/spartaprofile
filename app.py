from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

import pymongo

client = pymongo.MongoClient("mongodb+srv://spartauser:spartapassword@cluster0.0ipuykl.mongodb.net/?retryWrites=true&w=majority")
db = client.dbsparta

#
#
# db.<aaa>
# 쓰실 때 aaa 다른 사람 코드와 중복 없는지 확인해주세요
#
#

@app.route('/')
def home():
    return render_template('index.html')

#
# MJ SUNG
#

@app.route("/mjsung/postcomment", methods=["POST"])
def mjsung_comment_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    id = len(list(db.mjcomments.find({}, {'_id': False}))) + 1
    doc = {
        "id": id,
        "name": name_receive,
        "comment": comment_receive
    }

    db.fancomments.insert_one(doc)

    return jsonify({'msg':'업로드 완료.'})

@app.route("/mjsung/getcomment", methods=["GET"])
def mjsung_comment_get():

    comments = list(db.mjcomments.find({}, {'_id': False}))

    return jsonify({'comments': comments})

# @app.route("/homeworkdel", methods=["POST"])
# def homework_delete():
#     id = request.form['cid_give']
#     print(id)

#     db.fancomments.delete_one({'id':id})
#     deleted_comments += 1

#     return jsonify({'msg':'삭제되었습니다.'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)