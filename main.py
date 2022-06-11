from flask import Flask, session, render_template, redirect, request, url_for, flash
from database import Database
from werkzeug.utils import secure_filename

DB = Database()

app = Flask(__name__)
app.secret_key = "shinheejun"

@app.route('/',methods=["get"])
def index():
    item = DB.product_list()
    
    if "userID" in session:
        username = session.get("userID")
        follow_list = DB.list_follow(username)
        
        return render_template('index.html',username = session.get("userID"), login = True, result = item,follow_list = follow_list)
    else:
        return render_template('index.html',login = False, result = item)


@app.route('/login', methods=["post"])
def login():
    _id_ = request.form["loginId"]
    _pw_ = request.form["loginPw"]

    if _id_=="":
        flash("계정을 입력해주세요")
        return redirect(url_for("index"))

    cond = DB.login(_id_,_pw_)
    if cond :
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

@app.route('/signup_submit',methods=["post"])
def signup_submit():
    new_id = request.form["newId"]
    new_pw = request.form["newPw"]
    con_pw = request.form["confirmPw"]
    
    isexist = DB.select_id(new_id)
    
    if isexist:
        flash("이미 존재하는 계정입니다.")
        return redirect(url_for("signup"))
    

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


@app.route('/product/login/<int:p_id>',methods=["get"])
def product_login(p_id):
    
    _id_ = request.args.get("loginId")
    _pw_ = request.args.get("loginPw")
    if _id_=="":
        flash("계정을 입력해주세요")
        return redirect("/product/" + str(p_id))

    cond = DB.login(_id_,_pw_)
    if cond :
        session["userID"] = _id_
        return redirect("/product/" + str(p_id))
    else:
        flash("계정이 없거나 비밀번호가 틀립니다")
        return redirect("/product/" + str(p_id))


@app.route('/product/<int:p_id>')
def product_detail(p_id):
    
    product = DB.product_detail(p_id)
    p_username = product[0]
    p_images = DB.show_image(p_id)
    
    if "userID" in session:
        username = session.get("userID")
        isfollow = DB.search_follow(username, p_username)
        # 본인이면 안나옴
        isNotShow = (p_username == username)
        follow_list = DB.list_follow(username)
        
        return render_template('Product.html',result=product, username = session.get("userID"), login = True, images = p_images,isfollow = isfollow, isNotShow = isNotShow,follow_list=follow_list)
    else:
        return render_template('Product.html',result=product, images = p_images, login = False)

@app.route('/profile')
def profile():
    if "userID" in session:
        username = session.get("userID")
        user_item = DB.profile_item(username)
        pro_item = []

        follow_list = DB.list_follow(username)
        for i in user_item:
            pro_item.append(i[:-1])

        return render_template('profile.html', login = True, result = pro_item, username = session.get("userID"),follow_list=follow_list)
    else:
        flash("로그인을 먼저해주세요")
        return redirect(url_for("index"))
    
@app.route('/upload')
def upload():
    if "userID" in session:
        username = session.get("userID") 

        follow_list = DB.list_follow(username)
        return render_template('upload.html', login = True, username = session.get("userID"),follow_list=follow_list)
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
        
    P_soldout = request.form["isSoldOption"]
    if P_name == "":
        flash("상품 이름이 없습니다.")
        return redirect(url_for('upload'))
    elif P_price == "":
        flash("상품 가격이 없습니다.")
        return redirect(url_for('upload'))
        
    pid = DB.upload_info(username, P_name, P_price, P_keyword, P_desc, P_soldout)
        
    files = request.files.getlist('file[]')
    if files[0].filename == '':
        fileURI = '/static/img/default_image.png'
        DB.upload_url(pid,fileURI)
    else:
        for f in files:
            fileURI = './static/img/'+ secure_filename(f.filename)
            f.save(fileURI)
            DB.upload_url(pid, fileURI[1:])
    
    return redirect(url_for("profile"))

@app.route('/modifing/<int:p_id>')
def modifing(p_id):
    return redirect(url_for('modify', p_id = p_id))
            
@app.route('/modify/<int:p_id>')
def modify(p_id):
    p_five = DB.search_product(p_id)
    user = DB.user_certificate(p_id)
    if "userID" in session:
        if session.get("userID") == user:
            username = session.get("userID")
            follow_list = DB.list_follow(username)
            return render_template('modify.html',result=p_five, username = session.get("userID"), login = True,follow_list=follow_list)
        else:
            return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))
    
    
@app.route('/modifier',methods=['POST'])
def modifier():
    
    username = session.get("userID")  
    p_id = request.form['p_id']
    P_name = request.form['p_name']
    P_price = request.form['p_price']
    P_keyword = request.form['p_keyword']
    P_desc = request.form['p_descript']
    soldoption = request.form["isSoldOption"]
    files = request.files.getlist('file[]')


    user = DB.user_certificate(p_id)
    if username == user:  
        if files[0].filename == '':
            DB.modify_product(p_id,P_name,P_price,P_keyword,P_desc,soldoption)  
            return redirect(url_for('profile'))
        else:
            DB.delete_image(p_id)
            print("test1")
            for f in files:
                
                fileURI = './static/img/'+ secure_filename(f.filename)
                f.save(fileURI)
                print(fileURI)
                DB.upload_url(p_id, fileURI[1:])
                
            DB.modify_product(p_id,P_name,P_price,P_keyword,P_desc,soldoption)  
            
            return redirect(url_for('profile'))
    else:
        return redirect(url_for('profile'))    
    
    
@app.route('/following')
def following():
    follow = request.args.get('follow')
    username = session.get("userID")
    pid = request.args.get("p_id")
    if "userID" in session:
        if follow == username:
            return redirect(url_for('product_detail',p_id = pid))
        else:
            DB.insert_follow(username,follow)
            return redirect(url_for('product_detail',p_id = pid))
    else:
        flash("로그인을 먼저해주세요")
        return redirect(url_for('product_detail',p_id = pid))
    
@app.route('/unfollowing')
def unfollowing():
    follow = request.args.get('follow')
    username = session.get("userID")
    pid = request.args.get("p_id")
    DB.delete_follow(username,follow)
    return redirect(url_for('product_detail',p_id = pid))

@app.route('/followitem/<userID>', methods = ["get"])
def follow_item(userID):
    if "userID" in session:
        username = session.get("userID")
        follow_list = DB.list_follow(username)
        Search_list = DB.search_byfollow(userID)

        return render_template('index.html',username = session.get("userID"), login = True, result = Search_list,follow_list=follow_list)
    else:    
        return redirect(url_for('index'))

@app.route('/search', methods=["get"])
def search():
    _keyword_ = request.args.get("Search_input")

    if _keyword_ == "":
        flash("검색어를 입력해주세요")
        return redirect(url_for("index"))

    Search_list = DB.search_item(_keyword_)

    if "userID" in session:
        username = session.get("userID")
        follow_list = DB.list_follow(username)
        return render_template('index.html',username = session.get("userID"), login = True, result = Search_list,follow_list=follow_list)
    else:
        return render_template('index.html',login = False, result = Search_list)

if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)
    
    
    



