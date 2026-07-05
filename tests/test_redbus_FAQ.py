from playwright.sync_api import sync_playwright
import json

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    page = browser.new_page()
    page.goto("https://www.redbus.in/info/faq")

    faq_data = {}

    categories = page.locator("[role='tab']")

    count = categories.count()

    for i in range(count):
        category = categories.nth(i)
        category_name = category.inner_text()

        category.click()

        questions = page.locator("h4")

        category_data = []

        for q in range(questions.count()):
            question = questions.nth(q)

            question_text = question.inner_text()

            question.click()

            answer = question.locator("xpath=./following-sibling::*[1]").inner_text()

            category_data.append({
                "question": question_text,
                "answer": answer
            })

        faq_data[category_name] = category_data

    print(json.dumps(faq_data, indent=2))

    browser.close()