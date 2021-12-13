from selenium import webdriver
import time
import random
a = "abcdefghijklmnopqrstuvwxyz"
listostrings = random.sample(a, 8)
name = ''.join(listostrings)

file = open('namelist.txt', 'a')
file.write(name + '\n')
file.close()
print('Supply correct data types..')
print('Location of edgedriver:') #loc of driver, upto .exe
driverr = input()

print(f'Using name:{name}') #randomly generated name
print('How many rooms to create?')
last = int(input())
print('How many error messages per room?')
n = int(input())
browser = webdriver.Edge(driverr) #opens edgedriver
browser.get("https://hermes-prototype.herokuapp.com/")
fillintheblanks = browser.switch_to.alert
fillintheblanks.send_keys(name)
fillintheblanks.accept()
time.sleep(1)
for i in range(0, last):
    print(f'Working with room{i+1}::', end='')
    linkelem = browser.find_element_by_id('createroom')
    browser.execute_script("arguments[0].click();", linkelem)
    # linkelem.click()
    rnameprmpt = browser.switch_to.alert
    derr = f"DatabaseErr:{random.randint(1256,7899)}{i}"
    rnameprmpt.send_keys(derr)
    rnameprmpt.accept()
    browser.find_element_by_id(derr).click()
    for i in range(0, n):
        fieldx = browser.find_element_by_id('input')
        fieldx.send_keys(
            'Err: A Fatal Error in Database has disabled further data entries: X88990Cvdj'*5)
        fieldx.submit()
    print('Done')

print('==========')
print('FINISHED')
browser.close()