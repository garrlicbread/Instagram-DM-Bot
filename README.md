# Instagram-DM-Bot

## Problem:
Anyone who has ever had to send a direct message on Instagram through their website knows how uninspiring the task is. 
This script automates the entire process and messages the person of your choice given that he/she is in your follow list and vice versa.

## Tools:
This project was made using Selenium, a python module that helps in web automation and data scraping. 

## Process:
The script describes the steps to follow in order to DM a person on Instagram to selenium. The steps include logging in, disabling prompts, searching for the person, opening their profile, and finally sending a message. There are two versions of this script, the first version manually pauses the program after every step before the page gets loaded while the second script uses a method called **WebDriverWait** that automatically halts the program until it detects the HTML element that it requires to perform the next step. Using **WebDriverWait** reduces the execution time from ~45 seconds to ~20 seconds, thus, increasing the speed by over 200%

## Output:

Here's a gif of what the script does:

![Alt text](Instagram_Dm_Fast.gif) 

### Thanks:
Selenium: https://selenium-python.readthedocs.io/
