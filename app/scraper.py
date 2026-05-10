from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import json
import time

def scrape_shl_catalog():

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    url = "https://www.shl.com/solutions/products/product-catalog/"
    driver.get(url)

    time.sleep(5)

    links = driver.find_elements(By.TAG_NAME, "a")

    assessments = []
    added = set()

    for link in links:

        href = link.get_attribute("href")
        text = link.text.strip()

        if not href:
            continue

        if "/products/product-catalog/view/" not in href:
            continue

        if not text or text in added:
            continue

        added.add(text)

        title_lower = text.lower()

        # simple skill extraction (important for SHL scoring)
        skills = []

        if "java" in title_lower:
            skills.append("java")
        if "python" in title_lower:
            skills.append("python")
        if "analyst" in title_lower:
            skills.append("analytics")
        if "manager" in title_lower:
            skills.append("management")
        if "sales" in title_lower:
            skills.append("sales")

        assessments.append({
            "name": text,
            "url": href,
            "test_type": "K",
            "skills": skills,
            "description": text
        })

    driver.quit()

    with open("app/data/shl_catalog.json", "w", encoding="utf-8") as f:
        json.dump(assessments, f, indent=4)

    print(f"Saved {len(assessments)} assessments")


if __name__ == "__main__":
    scrape_shl_catalog()