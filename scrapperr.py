from selenium import webdriver
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import time

url  = input("Enter Url")

names = []
add = []
phone_num = []
dic_numbers = {
        'dc': '+',
        'fe': '(',
        'hg': ')',
        'ba': '-',
        'acb': '0',
        'yz': '1',
        'wx': '2',
        'vu': '3',
        'ts': '4',
        'rq': '5',
        'po': '6',
        'nm': '7',
        'lk': '8',
        'ji': '9'
}

driver = webdriver.Chrome(ChromeDriverManager().install())        
#url = 'https://www.justdial.com/Bangalore/Fashion-Designer-Stores/nct-10200832/page-1'  #sample url
driver.get(url)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")                   # Just dial website does not load fully if we stay at the top and it will load dynamically as we scroll down.
                                                                                         # So, to avoid this the web page is scrolled to bottom and the program is freezed for 7 seconds to load the web page fully
time.sleep(7)
vendor_info = driver.find_elements_by_class_name('store-details')

for i in range(len(vendor_info)):

    a = vendor_info[i].find_element_by_class_name('jcn')
    t = a.find_element_by_tag_name('a')

    try:
        name = t.get_attribute('title')

    except NoSuchElementException:
        name = ''

    try:
        address = vendor_info[i].find_element_by_class_name('cont_fl_addr').get_attribute('innerHTML')

    except NoSuchElementException:
        address = ''

    try:
        phone = vendor_info[i].find_elements_by_class_name('mobilesv')
    except NoSuchElementException:
        phone = ''

    phone_numbers = []

    if phone != '':
        for j in range(len(phone)):
            temp = phone[j].get_attribute('class').split("-")[1]
            phone_numbers.append(dic_numbers[temp])
    else:
        phone_numbers = 'N O T  P R O V I D E D'.split()

    names.append(name)
    add.append(address)
    phone_num.append(str(''.join(phone_numbers)))

dic = {
    'Name of Vendor': names,
    'Address of the vendor': add,
    'Phone Number': phone_num
}

df = pd.DataFrame(dic)

print(df.head())
df.to_excel('banglore_fashion.xlsx', index = False)
