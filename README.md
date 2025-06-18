# Payback coupon activation Automation Script

This script automates tasks in Microsoft Edge using Selenium. Follow the steps below to set up and run the script effectively.

---

## Prerequisites

1. Open `edge://version/` in your Edge browser.
2. **Note** the **Edge version** you're using (e.g., `125.0.XXXXX.X`).
3. Download the **matching version** of Edge WebDriver from:

   👉 [Edge WebDriver Download](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/?form=MA13LH#installation)

4. Extract the `msedgedriver.exe` and move it to:
C:\edgedriver\msedgedriver.exe

5. Ensure the following user data directory **exists**:
6. C:{home_directory}\AppData\Local\Microsoft\Edge\User Data\


## 🧪 First-Time Setup (UI Mode)

1. Run the script normally (in UI mode).
2. **Log in** to your account manually.
3. ✅ Make sure to check **"Remember me"** during login.
4. Once logged in, **press `Enter`** in the terminal.

This will save your session data for future headless runs.

---

## ⚙️ Switching to Headless Mode

After a successful login:

1. **Comment out** or remove the line:
input("Press Enter to continue...")
in line 34

2. Uncomment the line enabling headless mode:
options.add_argument("--headless")
in line 26

Now your script will run without opening a visible browser window

