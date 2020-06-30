from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World! (test)'

@app.route('/game')
def game():
    return render_template('gamelogin.html')

@app.route('/hi/<name>')
def hi(name):
    return "hello {}".format(name)

@app.route('/naver')
def naver():
    return render_template("naver.html")

@app.route('/daum')
def daum():
    return redirect("https://www.daum.net/")

@app.errorhandler(404)
def page_not_found(error):
    return "페이지가 없습니다. URL를 확인 하세요", 404

@app.route('/nopage')
def nopage ():
    print("404로 보냅니다.")
    abort(404)
    return "404로 보냅니다."

@app.route('/garden')
def myimage():
    return render_template("myimage.html")

if __name__ == '__main__':
    app.run(debug=True)