# 🚀 FastAPI Backend README

개선된 MVC 구조 · 예외 처리 · 로깅 시스템 · 통합 응답 포맷(return_http)

------------------------------------------------------------------------

## 📌 프로젝트 개요 (Overview)

이 프로젝트는 **FastAPI 기반 백엔드 서버**로, Django 구조적 개발
스타일(MVC 구조, 설정 기반 개발, 통합 예외 처리)을 반영하여
개발되었습니다.

-   FastAPI Core + 개선된 MVC 구조
-   Custom Exception Handler
-   Logging 설정
-   통합 Response Wrapper (`return_http`)
-   GET/POST 메서드 오류 처리
-   OSM/건설 관련 비즈니스 로직 모듈화

------------------------------------------------------------------------

## 📂 디렉토리 구조

    app/
     ├─ api/
     │   ├─ v1/
     │   │   ├─ building_controller.py
     │   │   └─ ...
     │   └─ routes.py
     ├─ core/
     │   ├─ config.py
     │   ├─ logger.py
     ├─ exceptions/
     │   ├─ handlers.py
     │   ├─ custom_exceptions.py
     ├─ services/
     │   ├─ building_service.py
     │   └─ ...
     ├─ utils/
     │   ├─ return_http.py
     │   └─ ...
     ├─ main.py

------------------------------------------------------------------------

## ⚙️ 설치 & 실행 방법

### 1️⃣ 환경 세팅

``` bash
python3.12 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2️⃣ 실행

``` bash
uvicorn app.main:app --reload
```

------------------------------------------------------------------------

## 🔒 통합 예외 처리 (Exception Handling)

FastAPI 기본 예외를 Django 스타일처럼 통합 처리합니다.

### 예시

``` python
@api.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return return_http(
        422, "C422", "Validation Error",
        data={"errors": exc.errors()},
        action="validation_error"
    )
```

------------------------------------------------------------------------

## 📦 return_http 응답 포맷

``` python
def return_http(status_code, code, detail, data=None, part="FASTAPI", action=None):
    response = {
        "success": str(status_code).startswith("2"),
        "code": code,
        "detail": detail,
        "part": part,
    }
    if data: response["data"] = data
    if action: response["action"] = action
    return JSONResponse(response, status_code=status_code)
```

------------------------------------------------------------------------

## 🧪 테스트

``` bash
pytest
```

------------------------------------------------------------------------

## 📚 API 문서

-   Swagger UI: http://localhost:8000/docs\
-   ReDoc: http://localhost:8000/redoc

------------------------------------------------------------------------

## 📝 로깅 구조

`core/logger.py`\
- 콘솔/파일 로깅 지원\
- 요청/응답 로깅 적용 가능

------------------------------------------------------------------------

## 🐳 Docker 실행

``` bash
docker build -t fastapi-server .
docker run -p 8000:8000 fastapi-server
```

------------------------------------------------------------------------

## 🙋 확장 또는 README 보완 필요 시

이미지 추가, ERD 추가, Swagger 캡처 추가 등\
언제든 요청하세요!
