from pathlib import Path
from playwright.sync_api import sync_playwright

Path("capturas").mkdir(exist_ok=True)

with sync_playwright() as p:
    navegador = p.chromium.launch()
    pagina = navegador.new_page(viewport={"width": 1440, "height": 900})
    pagina.goto("https://xstack.com.br")
    pagina.wait_for_load_state("networkidle")
    pagina.screenshot(path="capturas/home_desktop.png", full_page=True)
    navegador.close()

print("Captura salva em capturas/home_desktop.png")