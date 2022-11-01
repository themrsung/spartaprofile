from flask import Flask, render_template, request, jsonify, url_for
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

#
# HTML 링크 방법
# 1. templates 폴더 내에 있는 경우
# href="{{ url_for('블라블라') }}"
# 
# 쓰시고 이 파일 하단에
# @app.route('/블라블라', methods=['GET', 'POST'])
# def 블라블라():
#     return render_template('파일명.html')
#
# 파일을 직접 호줄하면 에러가 발생하여 이 파일에서 호출 함수를 써준 뒤, 그 함수를 html 파일에서 호출하는 방식입니다.
# 이 코드 쓴 사람 누군지 참 궁금하네요ㅎㅎ
#
# 2. static 폴더 내에 있는 경우
# href="{{ url_for('static', filename='파일명.확장자') }}"
#

@app.route('/')
def home():
    return render_template('index.html')

#
# MJ SUNG
#

@app.route("/mjsungpostcomment", methods=["POST"])
def mjsung_comment_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    doc = {
        "name": name_receive,
        "comment": comment_receive
    }

    db.mjcomments.insert_one(doc)

    return jsonify({'msg':'업로드 완료.'})

@app.route("/mjsunggetcomment", methods=["GET"])
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

@app.route('/mjsung', methods=['GET', 'POST'])
def mjsung():
    return render_template('mjsung.html')

@app.route('/dain', methods=['GET', 'POST'])
def dain():
    return render_template('pro.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)