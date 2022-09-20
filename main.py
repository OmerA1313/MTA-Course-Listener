import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import playsound
from selenium.webdriver.common.keys import Keys

import MailSender
import PushNotifier
import SMSSender
message = ""
course_code_2name = {'145006': "Project Management",
                     '141161': "System Analysis",
                     '142209': "Value Creation",
                     '141163': "Astrophysics",
                     '11126' : "Test: course available"}

try:
    course_code = sys.argv[1]
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://mtamn.mta.ac.il")
    driver.maximize_window()
    #user_name_input = driver.find_element(By.TAG_NAME, "input-signin-username")
    time.sleep(3)
    user_name_input = driver.find_element(By.ID, "Ecom_User_ID")
    password_input = driver.find_element(By.ID, "Ecom_Password")
    logon_button = driver.find_element(By.ID, "loginButton2")
    user_name_input.send_keys("omerat")
    password_input.send_keys("Oter!995")
    logon_button.click()
    time.sleep(5)
    courses_submission_menuItem = driver.find_element(By.XPATH, "//*[@id=\"#kt_header_menu\"]/div/div[1]/a/span")
    courses_submission_menuItem.click()
    time.sleep(1)
    courses_submission_menuItem_inner = driver.find_element(By.XPATH, "//*[@id=\"#kt_header_menu\"]/div/div[1]/div/div[1]/a")
    courses_submission_menuItem_inner.click()
    time.sleep(3)
    course_code_input = driver.find_element(By.ID, "SubjectCode")
    course_code_input.send_keys(course_code)
    time.sleep(2)
    driver.find_element(By.ID, "searchButton").click()
    class_full_msg_XPATH = "//*[@id=\"MyFather1\"]/div/div[2]/div[1]/span"
    course_sub_btn_arr = driver.find_elements(By.XPATH, "//*[@id=\"REG1\"]")
    # class_full_msg = driver.find_element(By.XPATH,class_full_msg_XPATH)
    # while class_full_msg.text == 'הקורס מלא':
    #     print("in loop")
    #     driver.refresh()
    #     class_full_msg = driver.find_element(By.XPATH, class_full_msg_XPATH)
    #     time.sleep(180)
    i = 0
    while len(course_sub_btn_arr) == 0:
        print("in loop, running for " + str(i) +" minutes")
        i += 3
        driver.refresh()
        course_sub_btn_arr = driver.find_elements(By.XPATH, "//*[@id=\"REG1\"]")
        time.sleep(180)

    if len(course_sub_btn_arr) >0:
        message = f"course number {course_code}  ( {course_code_2name.get(course_code)} ) became available!!!!!!!!!!!" #todo insert course code here


except Exception as err:
    message = f"Error with course {course_code_2name.get(course_code)} : " + str(err)
    print(err)

finally:
    #while(True):
            #playsound.playsound("alarm.mp3")
    #SMSSender.send_SMS(sms_message)
    if message == "":
        message = f"process {course_code_2name.get(course_code)} terminated"
    PushNotifier.send_push(message)

#subject_code_input = driver.find_element(By.XPATH, "//*[@id=\"#kt_header_menu\"]/div/div[1]/div/div[1]/a/span")

#user_name_input = driver.find_element(By.ID,"loginButton2")
