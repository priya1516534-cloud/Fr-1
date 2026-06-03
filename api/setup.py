import os
import requests
from http.server import BaseHTTPRequestHandler

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
VERCEL_URL = os.environ.get("VERCEL_URL")  # automatically set by Vercel

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if not TOKEN or not VERCEL_URL:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(b"Missing TELEGRAM_BOT_TOKEN or VERCEL_URL")
            return

        webhook_url = f"https://{VERCEL_URL}/api/bot"
        api_url = f"https://api.telegram.org/bot{TOKEN}/setWebhook?url={webhook_url}"
        
        try:
            resp = requests.get(api_url)
            result = resp.json()
            if result.get("ok"):
                self.send_response(200)
                self.end_headers()
                self.wfile.write(f"✅ Webhook set successfully to {webhook_url}".encode())
            else:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(f"❌ Telegram error: {result}".encode())
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(f"❌ Error: {str(e)}".encode())
