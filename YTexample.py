from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")

input("Press anything after QR scan")
wait = WebDriverWait(driver, 15)

while True:
    try:
        # Replace "Your Name" with your name as it appears in WhatsApp
        person = wait.until(EC.presence_of_element_located((By.XPATH, f'//span[@title="Mum", @title="Kishor Bhaiya"]')))
        person.click()

        for i in range(1, 3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        msg_got = driver.find_elements(By.CSS_SELECTOR, "span._11JPr.selectable-text.copyable-text")
        msg = [message.text for message in msg_got]

        if msg[-1] == "Happy Birthday":
            reply_box = wait.until(EC.presence_of_element_located(
                (By.XPATH, '//div[contains(@title, "Type a message")]//*[@class="selectable-text copyable-text iq0m558w"]')))

            reply_box.send_keys("Thank you!")
            reply_box.send_keys(Keys.RETURN)



    except Exception as e:
        print(f"Error: {e}")
        continue