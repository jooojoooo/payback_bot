import datetime
import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os


base_path = os.path.dirname(os.path.abspath(__file__))
user = os.environ.get("USERPROFILE")

def payback():

    # Edge WebDriver Path
    # Check edge://version/ and download matching driver from
    # https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/?form=MA13LH#installation
    edge_driver_path = "C:\\edgedriver\\msedgedriver.exe"
    # Edge options (keep WhatsApp logged in)

    edge_options = Options()
    edge_options.add_argument(f"user-data-dir={user}\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default_payback")
    #edge_options.add_argument("--headless")  # No UI
    edge_options.add_argument("--disable-gpu")

    # Start Edge WebDriver
    service = Service(edge_driver_path)
    driver = webdriver.Edge(service=service, options=edge_options)
    driver.get("https://www.payback.de/coupons")

    wait = WebDriverWait(driver, 15)

    # Wait for the pb-coupon-center element to be present
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'pb-coupon-center')))

    # JavaScript to find and click all "not-activated" coupon buttons
    js = """
    const host = document.querySelector('pb-coupon-center');
    if (!host || !host.shadowRoot) return;

    const root1 = host.shadowRoot;
    const coupons = root1.querySelectorAll('pbc-coupon');
    let count = 0;

    coupons.forEach(coupon => {
        const couponRoot = coupon.shadowRoot;
        if (!couponRoot) return;

        const action = couponRoot.querySelector('pbc-coupon-call-to-action');
        if (!action || !action.shadowRoot) return;

        const button = action.shadowRoot.querySelector(
            'button.coupon-call-to-action__button.coupon__activate-button.not-activated,' +
            'button.coupon-call-to-action__button.coupon__activate-button.not-activated.special'
        );

        if (button) {
            button.scrollIntoView({ behavior: 'smooth', block: 'center' });
            button.click();
            count++;
        }
    });

    return count;
    """
    time.sleep(3)
    activated_count = driver.execute_script(js)
    time.sleep(activated_count//10)
    if activated_count:
        with open(base_path + "\\run_log.txt", "a") as log:
            log.write(f"{datetime.datetime.now()} - Activated {activated_count} Payback coupons.\n")
        print(f"Activated {activated_count} Payback coupons.")
    else: print("No coupons available")

    driver.quit()

payback()
