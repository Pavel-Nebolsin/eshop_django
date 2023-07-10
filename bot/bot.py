import requests

from main import settings

webhook_url = settings.EXTERNAL_DOMAIN +'/bot/'



set_webhook_api = f"https://api.telegram.org/bot{settings.TELEGRAM_API_TOKEN}/setWebhook"

print(f"Setting webhook url {webhook_url}")

requests.post(set_webhook_api, data={"url": webhook_url})

