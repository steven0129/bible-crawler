from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from tqdm import tqdm

options = Options()
options.add_argument('--headless')

driver = webdriver.Firefox(options=options, executable_path='./geckodriver')
driver.get('https://bible.fhl.net/new/read.php')

with open('bible.txt', 'w') as BIBLE:
    try:
        while(1):
            book = driver.find_element_by_xpath('/html/body/font[1]').text
            popup = driver.find_element_by_id('popup')
            content = popup.text
            lines = content.split('\n')
            for line in lines:
                if(line == ''): break
                arr = line.split(' ')
                num = arr[0]
                arr.pop(0)
                content = ''.join(arr)
                print(f'處理{book}{num}中...')
                BIBLE.write(f'{book}\t{num}\t{content}\n')

            driver.find_element_by_xpath('//*[@id="pnext"]').click()
    except:
        pass

driver.quit()