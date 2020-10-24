from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

#Loads chrome with default settings
opt=Options()
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
"profile.default_content_setting_values.media_stream_mic": 1,
"profile.default_content_setting_values.media_stream_camera": 1,
"profile.default_content_setting_values.geolocation": 1,
"profile.default_content_setting_values.notifications": 1
})

#Gives path to chrome webdriver and loads classroom webpage
driver=webdriver.Chrome(chrome_options=opt, executable_path='C:\Program Files (x86)\chromedriver.exe')
driver.get('https://accounts.google.com/ServiceLogin/identifier?service=classroom&passive=1209600&continue=https%3A%2F%2Fclassroom.google.com%2F&followup=https%3A%2F%2Fclassroom.google.com%2F&emr=1&flowName=GlifWebSignIn&flowEntry=AddSession')

#Logs in the classroom
username=driver.find_element_by_id('identifierId')
username.click()
username.send_keys('Your--Email--Address')

next=driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]')
next.click()
time.sleep(2)
password=driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
password.click()
password.send_keys('Your--Password')


next=driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]')
next.click()

time.sleep(15)

#Finds the classroom
classroom=driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/div[1]/div[2]/div/ol/li[1]/div[1]/div[3]/h2/a[1]/div[1]')
classroom.click()

time.sleep(5)

link=driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/div[2]/div[1]/div/div[2]/div[3]/div/span/a/div')
link.click()

time.sleep(2)


#Switches the tab
#driver.switch_to.window(driver.window_handles[1])
current_tab=driver.window_handles[1]
driver.switch_to_window(current_tab)

#print(driver.title)

time.sleep(5)

#Turns off mic and camera and joins the meet
camera=driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[5]/div[3]/div/div/div[2]/div/div/div[1]/div/div[4]/div[2]/div/div')
camera.click()

mic=driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[5]/div[3]/div/div/div[2]/div/div/div[1]/div/div[4]/div[1]/div/div/div')
mic.click()

join=driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[5]/div[3]/div/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span/span')
join.click()
