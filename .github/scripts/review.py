import os
import urllib.request
import urllib.error
import json

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
TELEGRAM_BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
TELEGRAM_CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]
PR_DIFF = os.environ["PR_DIFF"]
PR_URL = os.environ.get("PR_URL", "")
PR_AUTHOR = os.environ.get("PR_AUTHOR", "unknown")

print(f"OPENAI_API_KEY={OPENAI_API_KEY}")
print(f"TELEGRAM_BOT_TOKEN={TELEGRAM_BOT_TOKEN}")
print(f"TELEGRAM_CHAT_ID={TELEGRAM_CHAT_ID}")
print(f"PR_AUTHOR={PR_AUTHOR}")
print(f"PR_URL={PR_URL}")
print(f"PR_DIFF length={len(PR_DIFF)}")

def ask_gpt(diff):
    prompt = f"""Ты — ревьюер кода на курсе Java Core. Твоя задача — дать студенту полезную обратную связь.

Правила:
- Указывай на конкретные проблемы с объяснением почему это проблема
- Если код хороший — скажи об этом честно
- Пиши по-русски, дружелюбно но по делу
- Не переписывай код за студента, направляй вопросами или подсказками
- Если видишь типичные заблуждения новичка — объясни концепцию

Код студента (diff):
{diff}
"""

    payload = json.dumps({
        "model": "gpt-4o",
        "messages": [{"role": "user", "content": prompt}]
    }).encode()

    req = urllib.request.Request(
        "https://api.proxyapi.ru/openai/v1/chat/completions",
        data=payload,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {OPENAI_API_KEY}"
        }
    )

    with urllib.request.urlopen(req) as response:
        result = json.loads(response.read())
        return result["choices"][0]["message"]["content"]

def send_telegram(text):
    message = f"🔍 *Ревью PR от {PR_AUTHOR}*\n{PR_URL}\n\n{text}"

    payload = json.dumps({
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }).encode()

    req = urllib.request.Request(
        f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage",
        data=payload,
        headers={"Content-Type": "application/json"}
    )

    with urllib.request.urlopen(req) as response:
        return json.loads(response.read())

review = ask_gpt(PR_DIFF)
send_telegram(review)
print("Ревью отправлено в Telegram")