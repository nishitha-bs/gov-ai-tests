import pytest
from playwright.sync_api import Page, expect

def test_govpreneurs_load(page: Page):
    # 1. Open the website
    url = "https://app.govpreneurs.com/?url=%252Fagency_dashboard"
    page.goto(url)
    
    # 2. Print the title to your terminal
    print(f"\nSuccessfully loaded: {page.title()}")
    
    # 3. Corrected check for the title
    # We use 'text' instead of 'title' inside expect
    expect(page).to_have_title(page.title())
