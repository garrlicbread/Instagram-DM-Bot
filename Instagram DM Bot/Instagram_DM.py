# Instagram bot that DMs your friends effortlessly.

# Initializing start time
import time
start = time.time()

# Importing libraries
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Defining a class that does the job for us
class DMBot:
    def __init__(self, user, pw, name, text1, text2):
        
        self.driver = webdriver.Firefox(executable_path = "C:\Program Files (x86)\geckodriver.exe") # Enter webdriver path 
        self.driver.get("https://www.instagram.com/?hl=en")
        
        sleep(3)
        
        self.driver.find_element_by_name("username").send_keys(user)
        self.driver.find_element_by_name("password").send_keys(pw)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button")\
            .click()
            
        sleep(5)
        
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")\
            .click()
            
        sleep(10)
        
        # self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")\
        #     .click()
        
        self.driver.find_element_by_css_selector("html.js.logged-in.client-root.js-focus-visible.sDN5V body div.RnEpo.Yx5HN div.pbNvD.fPMEg div._1XyCr div.piCib div.mt3GC button.aOOlW.HoLwm")\
            .click()
        sleep(2)
        
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")\
            .send_keys(name)
            
        sleep(2)
        
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")\
            .send_keys(Keys.ENTER, Keys.ENTER)
        
        sleep(4)
    
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/div/button")\
            .click() # /html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/button                       
            
        sleep(3)
        
        self.driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")\
            .send_keys(text1)
        test = self.driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")    
        sleep(2)
        test.send_keys(Keys.SHIFT, Keys.ENTER)
        test.send_keys(Keys.SHIFT, Keys.ENTER)
        test.send_keys(Keys.SHIFT, Keys.ENTER)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")\
            .send_keys(text2)
        test.send_keys(Keys.ENTER)
        time.sleep(2)
        self.driver.close()

# time.sleep(1)

# Entering credentials
IG_username = "" # Enter username
Password = "" # Enter password
Person_to_Dm = str(input("Enter name of recipient: ")) # Enter follower who you want to text 
text1 = ("**Hello, the following dm was sent using a python bot made by Sukant Sindhwani. He wishes you a good day!**")
text2 = str(input("Enter message: ")) # Enter the message 

# Calling the class 
DMBot(IG_username, Password, Person_to_Dm, text1, text2) 

# Printing execution time
end = time.time()
print(f"\nThis program completes it's task in {round((end - start), 2)} seconds.")
