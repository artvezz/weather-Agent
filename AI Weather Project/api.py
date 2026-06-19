from flask import Flask, send_file, request
from playwright.sync_api import sync_playwright
import os

app = Flask(__name__)

DASHBOARD_URL = "http://localhost:8501"

@app.route("/export")
def export():
    os.makedirs("exports", exist_ok=True)
    
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(
            viewport={"width": 1400, "height": 800},
            extra_http_headers={"ngrok-skip-browser-warning": "true"}
        )
        page.goto(DASHBOARD_URL)
        page.wait_for_timeout(5000)
        page.screenshot(path="exports/dashboard.png", full_page=True)
        browser.close()
    
    return send_file("exports/dashboard.png", mimetype="image/png")

if __name__ == "__main__":
    app.run(port=5000)