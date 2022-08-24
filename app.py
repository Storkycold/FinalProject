from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

# HTML을 주는 부분


@app.route('/')
def mainpage():
    return render_template('mainpage.html')


@app.route('/imagetoimage')
def imagetoimage():
    return render_template('imagetoimage.html')


@app.route('/texttoimage')
def texttoimage():
    return render_template('texttoimage.html')


@app.route('/lightbox')
def lightbox():
    return render_template('lightbox.html')


@app.route('/proving')
def proving():
    return render_template('Export-feb6f0ef-f36c-43df-8566-e19c56561f69/[과제4] 검증 참고 자료 제출 aae59ae712434444a66269ed5471fb09.html')


# 서버 연결
if __name__ == '__main__':
    app.run()
