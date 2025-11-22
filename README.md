# 🚀 FastAPI Backend README

개선된 MVC 구조 · 예외 처리 · 로깅 시스템 · 통합 응답 포맷(return_http)

------------------------------------------------------------------------

## 📌 프로젝트 개요 (Overview)

이 프로젝트는 **FastAPI 기반 백엔드 서버**로, Django 구조적 개발 스타일(MVC 구조, 설정 기반 개발, 통합 예외 처리)을 반영하여 개발되었습니다.

-   FastAPI Core + 개선된 MVC 구조
-   Custom Exception Handler
-   Logging 설정
-   통합 Response Wrapper (`return_http`)
-   GET/POST 메서드 오류 처리
------------------------------------------------------------------------

## 📂 디렉토리 구조

    app/
     ├─ routers/
     │   └─ items.py
     ├─ core/
     │   ├─ config.py
     │   ├─ logger_config.py
     │   ├─ middleware.py
     ├─ utils.py
     ├─ main.py

------------------------------------------------------------------------

## ⚙️ 설치 & 실행 방법

### 1️⃣ 환경 세팅

``` bash
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2️⃣ 실행

``` bash
python operate.py
```

------------------------------------------------------------------------

## 🔒 통합 예외 처리 (Exception Handling)

FastAPI 기본 예외를 Django 스타일처럼 통합 처리합니다.

### 예시

``` python
@app.exception_handler(Exception)
async def custom_all_exception_handler(request: Request, exc: Exception):
    return http_return(500, "C003", "Internal Server Error", action="internal_error")
```

------------------------------------------------------------------------

## 📦 return_http 응답 포맷

``` python
def http_return(status: int, code: str, message: str, data=None, action: str = "-"):
    req_logger = get_request_logger(
        action = action,
        code = code,
        log_msg = message
    )
    if 200 <= status < 300:
        req_logger.info(f"{code} '{message}'")
    else:
        req_logger.error(f"{code} '{message}'")

    return responses.JSONResponse(
        status_code = status,
        content = {
            "code": code,
            "message": message,
            "data": data if data is not None else {}
        }
    )
```

------------------------------------------------------------------------

## 🧪 테스트

``` bash
pytest
```

------------------------------------------------------------------------

## 📝 로깅 구조

`core/logger.py`\
- 콘솔/파일 로깅 지원\
- 요청/응답 로깅 적용 가능

------------------------------------------------------------------------