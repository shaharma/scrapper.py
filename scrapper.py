#################################
##########WEB SCRAPPER##########
################################
from selenium import webdriver
import time
import csv

url = 'https://cool-proxy.net/'
# error catch-ignore.
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(
    options=options, executable_path=r'C:\Python27\Scripts\chromedriver.exe')  # Might need to change based on your chromedriver directory.
driver.get(url)
# Sleep is necessary because it's an interactive scrapper (interactive js data).
# If not for sleep, the program would not return any value, since the website takes some seconds to load.
time.sleep(6)

# Preparing the CSV
file = open('cool-proxy.csv', 'wb')
writer = csv.writer(file)

# Headers
writer.writerow(['IP Addresses', 'Ports'])

# Iterating on each element in the table.
# Starting at 2 since this is the base index, could reach 40 (not included), but on average there are 20~ IP addresses
# The code will either run until it reaches the 40th IP address (less likely) or just stop by itself once it reaches the end.
for i in range(2, 40):
    # For some reason the loop stops at the 9th iteration, probably because of ads placed in the website.
    # Using continue we will skip the 9th interation since tr[9] simply does not exist as found in tests.
    if(i == 9):
        continue
    # ASCII encoding in order to remove any unicode (and there's plenty).
    ip = driver.find_element_by_xpath(
        '//*[@id= "main"]/table/tbody/tr[' + str(i) + ']' + '/td[1]').text.encode('ascii', 'ignore')
    port = driver.find_element_by_xpath(
        '//*[@id= "main"]/table/tbody/tr[' + str(i) + ']' + '/td[2]').text.encode('ascii', 'ignore')
    print(ip, port)
    writer.writerow([ip, port])

file.close()
