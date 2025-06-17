# Objective: Create a system to fetch content from a web URL, apply an AI-driven "spin" to chapters, allow multiple human-in-the-loop iterations, and manage content versions.

from playwright.sync_api import sync_playwright

url = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"

screenshot_path = "chapter1.png"
text_path = "chapter1.txt"

def fetch_chapter():
    with sync_playwright() as p:

        ## launching the browser

        browser = p.chromium.launch()
        page = browser.new_page()

        ## Go to the chapter page
        page.goto(url,timeout=60000)

        ## wait until the content is loaded
        page.wait_for_selector("#mw-content-text")

        ## taking the screenshot of the visible page
        page.screenshot(path=screenshot_path,full_page=True)

        ## extrating the main content
        content = page.locator("#mw-content-text").inner_text()

        with open(text_path,"w",encoding="utf-8") as f:
            f.write(content)

        ## closing the browser
        browser.close()

if __name__=="__main__":
    fetch_chapter()
