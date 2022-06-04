from flask import Flask, session, render_template, redirect, request, url_for, flash
from datetime import datetime
from database import Database
from werkzeug.utils import secure_filename
import os

DB = Database()

app = Flask(__name__)
app.secret_key = "shinheejun"






@app.route('/',methods=["get"])
def index():
    item = DB.product_list()
    if "userID" in session:
        return render_template('index.html',username = session.get("userID"), login = True, result = item)
    else:
        return render_template('index.html',login = False, result = item)


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



    
@app.route('/product/login/<int:p_id>',methods=["get"])
def product_login(p_id):
    
    _id_ = request.args.get("loginId")
    _pw_ = request.args.get("loginPw")
    print(_id_,_pw_)
    if _id_=="":
        flash("계정을 입력해주세요")
        return redirect("/product/" + str(p_id))

    cond = DB.login(_id_,_pw_)
    if cond :
        print(_id_,_pw_)
        session["userID"] = _id_
        return redirect("/product/" + str(p_id))
    else:
        flash("계정이 없거나 비밀번호가 틀립니다")
        return redirect("/product/" + str(p_id))


@app.route('/product/<int:p_id>')
def product_detail(p_id):
    
    product = DB.product_detail(p_id)
    if "userID" in session:
        p_images = DB.show_image(p_id)
        return render_template('Product.html',result=product, username = session.get("userID"), login = True, images = p_images)
    else:
        return render_template('Product.html',result=product, login = False)

@app.route('/profile')
def profile():
    if "userID" in session:
        username = session.get("userID")
        user_item = DB.profile_item(username)
        pro_item = []
        for i in user_item:
            pro_item.append(i[:-1])

        return render_template('profile.html', login = True, result = pro_item, username = session.get("userID"))
    
    else:
        flash("로그인을 먼저해주세요")
        return redirect(url_for("index"))
    
@app.route('/upload')
def upload():
    if "userID" in session:
        username = session.get("userID") 
        return render_template('upload.html', login = True, username = session.get("userID"))
    else:
        flash("로그인을 먼저해주세요")
        return redirect(url_for("index"))
    
@app.route('/uploader', methods = ['GET','POST'])
def uploader():
        
    username = session.get("userID")
    P_name = request.form['p_name']
    P_price = request.form['p_price']
    P_keyword = request.form['p_keyword']
    P_desc = request.form['p_descript']
        
    soldoption = request.form["isSoldOption"]
        
    if "0" in soldoption:
        P_soldout = 0
    elif "1" in soldoption:
        P_soldout = 1
            
    pid = DB.upload_info(username, P_name, P_price, P_keyword, P_desc, P_soldout)
        
    # return pid
    files = request.files.getlist('file[]')

    for f in files:
        fileURI = './static/img/'+ secure_filename(f.filename)
        f.save(fileURI)
        DB.upload_url(pid, fileURI[1:])
    
    return redirect(url_for("profile"))
            
@app.route('/modify/<int:p_id>')
def modify(p_id):
    
    product = DB.search_product(p_id) 
    # result = ["상품이름","상품설명","키워드","1234567", 0]
    
    return render_template("modify.html", result = )


if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)
    
    
    



