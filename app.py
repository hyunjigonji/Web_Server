import os
from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from models import db
from models import FCuser

app = Flask(__name__)

@app.route('/register', methods=['GET', 'POST'])
def register():
        if request.method == 'POST':
                userid = request.form.get('userid')
                username = request.form.get('username')
                password = request.form.get('password')
                re_password = request.form.get('re-password')

                if not (userid and username and password and re_password): #값이 모두 있는 지 확인, 아니면 페이지 초기화
                        return render_template('register.html')
                if password != re_password: #비밀번호와 확인 값이 같은 지 확인, 아니면 페이지 초기화
                        return render_template('register.html')

                fcuser = FCuser()
                fcuser.userid = userid
                fcuser.username = username
                fcuser.password = password

                db.session.add(fcuser)
                db.session.commit()
        return redirect('/')

@app.route('/')
def hello():
        return render_template('hello.html')

if __name__ == "__main__":
        basedir = os.path.abspath(os.path.dirname(__file__))
        dbfile = os.path.join(basedir, 'db.sqlite')

        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
        app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True #트랜잭션이 끝날 때마다 커밋을 함
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        db.init_app(app)
        db.app = app
        db.create_all()
        app.run(host='127.0.0.1', port=5000, debug=True)