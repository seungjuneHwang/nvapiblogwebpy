
# A very simple Flask Hello World app for you to get started with...

# 우리가 만든 네이버 API
import nvblogapi

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route('/kbaseball')
def kbaseball():
    return render_template('kbaseball.html')
    # return '한국 야구 페이지'

@app.route('/')
def blog():
    return render_template('blog.html')

@app.route('/action_page')
def action_page():
    keyword = request.args["keyword"]
    # 우리가 만든 API코드에 keyword를 넣어서 결과값을 리스트로 받음
    blog_list = nvblogapi.get_blog_api(keyword)

    # return f"당신이 입력한 검색어: {keyword}"
    return render_template('bloglist.html', items=blog_list)
    # return render_template('blog.html')

