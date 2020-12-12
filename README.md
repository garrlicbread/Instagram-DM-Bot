# Instagram-DM-Bot

## Problem:
Anyone who has ever had to send a direct message on Instagram through their website knows how uninspiring the task is. 
This script automates the entire process and messages the person of your choice given that he/she is in your follow list and vice versa.

## Process:
The script describes the steps to follow in order to DM a person on Instagram to selenium. The steps include logging in, disabling prompts, searching for the person, opening their profile, and finally sending a message. There are two versions of this script, the first version manually pauses the program after every step before the page gets loaded while the second script uses a method called **WebDriverWait** that automatically halts the program until it detects the HTML element that it requires to perform the next step. Using **WebDriverWait** reduces the execution time from ~50 seconds to ~22 seconds, thus, increasing the speed by over 200%.

## Output:

Here's a gif of what the script does:

![Alt text](Instagram_Dm_Fast.gif) 

## Notes:
1) The script executes on Firefox so it's webdriver i.e. Geckodriver.exe is used. To use the script on any other browser, please install the relevant drivers.
2) The speed of the script depends on the speed of the Internet. If it's too slow, the program might fail.
3) Not every meeded element is of the same type, sometimes the script looks for XPATHS, sometimes it looks for CSS Selectors. These elements were decided after conducting vigorous trial and errors

## Module Used:
This project was made entirely using Selenium, a python module that helps in web automation and data scraping. 
Documentation: https://selenium-python.readthedocs.io/
