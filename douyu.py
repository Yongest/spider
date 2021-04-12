# coding=utf-8
# Version:python3.8.0
# Tools:PyCharm 2018.2.1 x64
__date__ = '2021/4/11 21:33'
__author__ = '张勇'

from selenium import webdriver
import time

class Douyu (object):

    def __init__(self):
        self.url = 'https://www.douyu.com/directory/all'
        self.driver = webdriver.Chrome()

    def parse_data(self):
        time.sleep(3)
        room_list = self.driver.find_elements_by_xpath('//*[@id="listAll"]/section[2]/div[2]/ul/li/div/a')
        print(len(room_list))
        self.driver.execute_script('scrollTo(0,1000000)')
        time.sleep(1)
        data_list = []
        for room in room_list:
            try:
                temp = {}

                temp['title'] = room.find_element_by_xpath('./div[2]/div[1]/h3').text
                temp['type'] = room.find_element_by_xpath('./div[2]/div[1]/span').text
                temp['owner'] = room.find_element_by_xpath('./div[2]/div[2]/h2/div').text
                temp['num'] = room.find_element_by_xpath('./div[2]/div[2]/span').text
                temp['src'] = room.find_element_by_xpath('./div[1]/div[1]/img').get_attribute('src')
                print(temp)
                data_list.append(temp)
            except:
                print('e')

        return data_list

    def save_data(self, data_list):
        for data in data_list:
            print(data)

    def run(self):
        # get
        self.driver.get(self.url)
        while True:
            # parse
            data_list = self.parse_data()
            # save
            self.save_data(data_list)
            # next
            el_next = self.driver.find_element_by_xpath('//*[contains(text(),"下一页")]')
            if el_next:
                self.driver.execute_script('scrollTo(0,1000000)')
                el_next.click()
            else:
                break

if __name__ == '__main__':

    douyu = Douyu()
    douyu.run()
