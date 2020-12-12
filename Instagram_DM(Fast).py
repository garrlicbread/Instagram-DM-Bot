# Instagram bot that DMs your friends effortlessly (Faster version)

# Importing libraries
import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Defining a class that does the job for us
class DMBot:
    def __init__(self, user, pw, name, text):
        
        self.driver = webdriver.Firefox(executable_path = "C:\Program Files (x86)\geckodriver.exe") # Enter webdriver path 
        self.driver.get("https://www.instagram.com/?hl=en")
    
        WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys(user)
        WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.NAME, "password"))).send_keys(pw)
        WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.XPATH,
                                                                              "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button")))\
            .click()
        
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                                              "/html/body/div[1]/section/main/div/div/div/div/button")))\
            .click()
            
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                                              "button.aOOlW:nth-child(2)")))\
            .click()
                
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((By.XPATH,
                                                                              "/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")))\
            .send_keys(name)
            
        sleep(1.5)
        
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")\
            .send_keys(Keys.ENTER, Keys.ENTER)
        
        WebDriverWait(self.driver, 4).until(EC.element_to_be_clickable((By.XPATH,
                                                                              "/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/div/button")))\
            .click()
        
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,
        #                                                                       ".sqdOP")))\
        #     .click()
       
        WebDriverWait(self.driver, 4).until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                                              ".ItkAi > textarea:nth-child(1)")))\
            .send_keys("**Hi, the following DM was sent using a python bot made by Sukant Sindhwani.**")
    
        test = self.driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")    
        test.send_keys(Keys.SHIFT, Keys.ENTER)
        test.send_keys(Keys.SHIFT, Keys.ENTER)
        test.send_keys(Keys.SHIFT, Keys.ENTER)
        test.send_keys(text)
        test.send_keys(Keys.ENTER)
        time.sleep(6)
        self.driver.close()
        
# time.sleep(1)

# Entering credentials
IG_username = "" # Enter username
Password = "" # Enter password
Person_to_Dm = str(input("Enter name of recipient: ")) # Enter follower who you want to text 
text = str(input("Enter message: ")) # Enter the message 

# Initializing start time
start = time.time()
        
# Calling the class 
DMBot(IG_username, Password, Person_to_Dm, text) 

# Printing execution time
end = time.time()
print(f"\nThis program completes it's task in {round(((end - start) - 5), 2)} seconds.")
