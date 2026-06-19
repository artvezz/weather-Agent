from playwright.sync_api import sync_playwright
import os

def capture_dashboard():
    os.makedirs("exports", exist_ok=True)
    
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1400, "height": 800})
        
        # Aguarda o Streamlit carregar completamente
        page.goto("http://localhost:8501")
        page.wait_for_timeout(3000)  # 3 segundos para carregar
        
        page.screenshot(path="exports/dashboard.png", full_page=True)
        browser.close()
    
    print("Screenshot salvo em exports/dashboard.png")

if __name__ == "__main__":
    capture_dashboard()

