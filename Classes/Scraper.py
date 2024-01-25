from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

class TableParser:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome()

    def scrape_content(self):
        self.driver.get(self.url)
        # Add waiting logic here if needed

        html_source = self.driver.page_source
        soup = BeautifulSoup(html_source, 'html.parser')
        table_body = soup.find('tbody')

        data = []

        for row in table_body.find_all('tr'):
            cells = row.find_all('td')

            url = cells[0].find('a')['href']
            content = cells[1].get_text(strip=True)
            researcher_name = cells[0].text.strip()

            data.append({"URL": url, "Content": content,"Researcher": researcher_name})


        return data

    def extract_additional_info(self, url: object) -> object:
        self.driver.get(url)
        html_source = self.driver.page_source
        soup = BeautifulSoup(html_source, 'html.parser')

        # Find and extract the content within the col-sm-12 class
        col_sm_12_content = soup.find('div', {'class': 'col-sm-12'})
        text_content = col_sm_12_content.get_text(separator='\n') if col_sm_12_content else ""
        # Extract professor name
        # professor_name_element = self.driver.find_element('xpath',"/html/body/div[1]/div[1]/div[2]/h2")
        # professor_name = text_content.split('Profile')[2]
        # professor_name_element.text.strip() if professor_name_element else ""

        return text_content

    def store_in_dataframe(self, data):
        df = pd.DataFrame(data)
        df.to_csv('output.csv', index=False)
        print("Data stored in DataFrame and CSV file.")
