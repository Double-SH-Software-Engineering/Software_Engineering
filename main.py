from flask import Flask, session, render_template, redirect, request, url_for, flash
from database import Database

DB = Database()

app = Flask(__name__)
app.secret_key = "shinheejun"



@app.route('/',methods=["get"])
def index():
    if "userID" in session:
        return render_template('index.html',username = session.get("userID"), login = True)
    else:
        return render_template('index.html',login = False)


@app.route('/login', methods=["get"])
def login():
    _id_ = request.args.get("loginId")
    _pw_ = request.args.get("loginPw")

    if _id_=="":
        flash("계정을 입력해주세요")
        return redirect(url_for("index"))

    cond = DB.login(_id_,_pw_)
    if cond :
        print(_id_,_pw_)
        session["userID"] = _id_
        return redirect(url_for("index"))
    else:
        flash("계정이 없거나 비밀번호가 틀립니다")
        return redirect(url_for("index"))

@app.route('/logout')

def logout():
    session.pop("userID")
    return redirect(url_for("index"))

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signup_submit',methods=["get"])
def signup_submit():
    new_id = request.args.get("newId")
    new_pw = request.args.get("newPw")
    con_pw = request.args.get("confirmPw")

    if new_pw != con_pw:
        flash("비밀번호를 재확인 바랍니다")
        return redirect(url_for("signup"))
    if len(new_pw) < 4:
        flash("비밀번호가 너무 짧습니다")
        return redirect(url_for("signup"))

    if DB.signup(new_id,new_pw):
        flash("회원가입에 성공했습니다. 로그인 해주세요")
        return redirect(url_for("index"))
    else:
        flash("중복된 ID 입니다 다시 입력해주세요")
        return redirect(url_for("signup"))

    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
