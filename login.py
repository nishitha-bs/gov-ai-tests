import random
import smtplib
from playwright.sync_api import sync_playwright

def send_otp(email, otp):
    # Use your App Password here
    sender = "nishithabs2002@gmail.com"
    password = "fbfl apcr fses vlss"
    
    msg = f"Subject: Govpreneur OTP\n\nYour code is: {otp}"
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.sendmail(sender, email, msg)

def run_login_automation():
    with sync_playwright() as p:
        # Launch browser (headless=False means you can SEE it)
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # 1. Open the page
        print("Opening browser...")
        page.goto("https://app.govpreneurs.com/?url=%252Fagency_dashboard") # Replace with your Govpreneur URL
        
        # 2. Get User Input from Terminal
        email = input("Enter email for login: ")
        otp = str(random.randint(100000, 999999))
        
        # 3. Send the OTP
        print(f"Sending OTP to {email}...")
        send_otp(email, otp)
        
        # 4. Verification
        user_code = input("Check your email and enter OTP here: ")
        if user_code == otp:
            print("Successfully verified in browser!")
            # Here you could tell playwright to click 'Submit' or 'Next'
        else:
            print("Invalid OTP.")

        # Keep browser open for a few seconds to see result
        page.wait_for_timeout(5000)
        browser.close()

if __name__ == "__main__":
    run_login_automation()
