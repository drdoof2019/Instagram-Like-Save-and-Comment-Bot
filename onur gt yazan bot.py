from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import sys
import time

class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
        time.sleep(4)
        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        passworword_elem = driver.find_element_by_xpath("//input[@name='password']")
        passworword_elem.clear()
        passworword_elem.send_keys(self.password)
        time.sleep(1)
        passworword_elem.send_keys(Keys.RETURN)
        time.sleep(2)


    def LikeSaveComment(self):
        driver = self.driver
        driver.get("https://www.instagram.com/p/BvcJaI2Hlk7/") #link buraya!!!!!!!!!!!!!!!! write your link to here!!!!!!!<=<=
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        wait = WebDriverWait(driver,10)
        yorumlar = ["GTGTGTGTGT","GTGTGT","GTGTG","GERİ TAKİP","Takip et","Takibe takipppp","takibe takibpppp","takipet","GT","gtgtgt","gt","gt:D","gt oto gt program"
                    "gtg","#izmir dekiler takip edin","#antalya da kiler takip edin","#istanbul dakiler takip edin","#kocaeli ndekiler takip edin",
                    "#bursa da kiler takip edin","#diyarbakır dakiler takip edin","#gaziantep dekiler takip edin","#ankara da kiler takip edin",
                    "#güzel takip edin"] #these are comments. you can keep or change them.
        #time.sleep(random.randint(1, 3))
        try:
            like_button = driver.find_element_by_xpath('//span[@aria-label="Like"]').click()
        except Exception:
            print("zaten beğenilmiş") #"EN: already liked"

        time.sleep(random.randint(1,3))
        try:
            save_button = driver.find_element_by_xpath('//span[@aria-label="Save"]').click()
        except Exception:
            print("zaten kaydedilmiş") #"EN: already saved"
        try:
            sendkey = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/div/article/div[2]/section[3]/div/form/textarea')))
            sendkey.click()
            yorumla = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[3]/div/form/textarea')
            yorumla.send_keys(random.choice(yorumlar))
            yorumla.send_keys(Keys.RETURN)
            time.sleep(2)
            yorumla.send_keys(random.choice(yorumlar))
            yorumla.send_keys(Keys.RETURN)
            time.sleep(2)
            yorumla.send_keys(random.choice(yorumlar))
            yorumla.send_keys(Keys.RETURN)
            time.sleep(1)

        except Exception:
            print("denendi ama yorum atmada sıkıntı var") # "EN: there is a problem occured in commenting"

        time.sleep(1)




if __name__ == "__main__":

    usernames = ["username1","username2..."] #enter all users you want code to enter
    passwords = ["password1","password2..."]
    sayac = 0
    while sayac < len(usernames):

        ig = InstagramBot(usernames[sayac], passwords[sayac])
        ig.login()
        sayac += 1
        ig.LikeSaveComment()
        time.sleep(1)
        ig.closeBrowser()
        time.sleep(1)
