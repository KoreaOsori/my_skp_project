# 간단한 홈페이지 제공
# 1. 모듈 가져오기 

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

# 2. FastAPI 객체 생성, 전역변수 생성

app = FastAPI()
templates = Jinja2Templates(directory="templates")


# 3. 라우팅 구성/정의

@app.get("/")
def home(req:Request): 
    # 홈페이지("/")를 요청(get방식) → 매칭되는 함수 home() 호출됨 
    # → index html을 읽어서 req데이터를 전달하여 동적으로 html을 구성 
    # → 응답(return) → 클라이언트 브라우저에게 전달 → 랜더링 → dom tree
    # → 브라우저 해석, 화면에 그리기 → 클라이언트는 응답 결과를 화면에서 볼 수 있다.
    return templates.TemplateResponse("index.html", {"request":req})

# 4. 