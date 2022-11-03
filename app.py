import json
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

# @app.route('/mjsungcommentdeletetest', methods=["GET"])
# def mjsung_comment_delete_test():

#     comments = list(db.mjcomments.find())

#     return jsonify({'comments': comments})

# @app.route("/homeworkdel", methods=["POST"])
# def homework_delete():
#     id = request.form['cid_give']
#     print(id)

#     db.fancomments.delete_one({'id':id})
#     deleted_comments += 1

#     return jsonify({'msg':'삭제되었습니다.'})


# seongkh


@app.route("/homework", methods=["POST"])
def homework_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    doc = {
        'name': name_receive,
        'comment': comment_receive
    }

    db.homework.insert_one(doc)
    return jsonify({'msg':'작성완료!'})

@app.route("/homework", methods=["GET"])
def homework_get():
    comment_list = list(db.homework.find({},{'_id':False}))
    return jsonify({'comments':comment_list})





@app.route('/mjsung', methods=['GET', 'POST'])
def mjsung():
    return render_template('mjsung.html')

@app.route('/mjcode', methods=['GET', 'POST'])
def mjcode():
    return render_template('mjsung/mjcode.html')

@app.route('/mjsungpostrep', methods=['POST'])
def mjsungpostrep():
    rep_receive = request.form['rep_give']

    doc = {
        "rep": rep_receive
    }

    db.mjrep.insert_one(doc)

    return jsonify({'msg':'업로드 완료.'})

@app.route("/mjsunggetrep", methods=["GET"])
def mjsunggetrep():

    reps = list(db.mjrep.find({}, {'_id': False}))

    total = 0

    for r in reps:
        total += int(r['rep'])
    
    if len(reps) > 0:
        avg = total / len(reps)
    else:
        avg = 0

    avg100 = avg * 100


    return jsonify({'reps': reps, 'avg': avg, 'avg100': avg100})

# leo -----------------------------------------------

@app.route("/comment", methods=["POST"])
def comment_post():
    uuid_receive = request.form['uuid_give']
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    doc = {
        "uuid": uuid_receive,
        "name": name_receive,
        "comment": comment_receive,
    }

    db.comment.insert_one(doc)
    return jsonify({'msg': '작성 완료!'})

@app.route("/comment", methods=["DELETE"])
def comment_delete():
    uuid_receive = request.form["uuid_give"]

    db.comment.delete_one({"uuid": uuid_receive})
    return jsonify({"msg": "삭제 완료!"})

@app.route("/comment", methods=["GET"])
def comment_get():
    post_list = list(db.comment.find({}, {'_id':False}))
    print(post_list)
    return jsonify({"post": post_list})

# Lth
@app.route("/homework_lth", methods=["POST"])
def lth_post():
    name_receive = request.form["name_give"]
    comment_receive = request.form["comment_give"]

    doc = {
        'name': name_receive,
        'comment': comment_receive
    }

    db.homeworklth.insert_one(doc)
    return jsonify({'msg':'댓글 감사합니다!'})

@app.route("/homework_lth", methods=["GET"])
def lth_get():
    comment_list = list(db.homeworklth.find({},{'_id':False}))
    return jsonify({'comments':comment_list})
# Lth

@app.route('/dain', methods=['GET', 'POST'])
def dain():
    return render_template('pro.html')

@app.route('/leetaehyun', methods=['GET', 'POST'])
def leetaehyun():
    return render_template('LeeTaeHyun.html')

@app.route('/seongchange', methods=['GET', 'POST'])
def seongchange():
    return render_template('seong-change.html')

@app.route('/leo', methods=['GET', 'POST'])
def leo():
    return render_template('leo.html')

@app.route('/main', methods=['GET', 'POST'])
def main():
    return render_template('main.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

