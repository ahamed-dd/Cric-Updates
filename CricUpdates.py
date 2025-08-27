from selenium import webdriver
import time
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service


class CricUpdates:

    def find_all_match_month(self):
        s = Service(executable_path=r'C:\Users\chromedriver.exe')
        driver = webdriver.Chrome(service=s)

        url = 'https://www.icc-cricket.com/fixtures-results'
        driver.get(url)

        time.sleep(5)

        page = driver.page_source
        soup = BeautifulSoup(page, 'lxml')

        driver.quit()

        allm = soup.find_all('div', class_="si-tab-card-section")

        for match in allm:
            date = match.find('span', class_= 'si-card-date').text
            print(date)
            title = match.find('span', class_="si-card-match-info").text
            print(title)

    def check_matches(self):
        inp = input("Enter the team to check if they have match in the next month: ")
        s = Service(executable_path=r'C:\Users\chromedriver.exe')
        driver = webdriver.Chrome(service=s)

        url = 'https://www.icc-cricket.com/fixtures-results'
        driver.get(url)

        time.sleep(5)

        page = driver.page_source
        soup = BeautifulSoup(page, 'lxml')

        driver.quit()

        allm = soup.find_all('div', class_="si-tab-card-section")

        for match in allm:

            date = match.find('span', class_='si-card-date').text
            title = match.find('span', class_="si-card-match-info").text
            namea = match.find('div', class_="si-team si-team-a").text
            nameb = match.find('div', class_="si-team si-team-b").text
            if inp in namea or nameb:
                print(date)
                print(title)
                print(namea + 'VS' + nameb)
                break
            else:
                print('No matches found')




if __name__ == '__main__':
    update = CricUpdates()
    update.find_all_match_month()










