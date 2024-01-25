from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GoogleScholarScraper:
    def __init__(self):
        self.base_url = "https://scholar.google.com"
        self.driver = webdriver.Chrome()  # You may need to adjust this based on your system and browser

    def search_professor(self, professor_name):
        if 'Dr' in professor_name:
            professor_name = professor_name.replace('Dr','').strip()
        first_name = professor_name.split(' ')[0]
        last_name = professor_name.split(' ')[1]
        if len(last_name) > 1:
            self.driver.get(f"{self.base_url}/scholar?hl=en&as_sdt=0%2C5&q={first_name}+{last_name}&btnG=")

        else:
            self.driver.get(f"{self.base_url}/scholar?hl=en&as_sdt=0%2C5&q={first_name}&btnG=")
        try:
            # Wait until the search results are loaded
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "gs_r"))
            )

            # Extract information from the search results
            results = self.driver.find_elements(By.CLASS_NAME, "gs_r")

            for result in results:
                name_element = result.find_element(By.XPATH, ".//h4[@class='gs_rt2']/a/b")
                affiliation_element = result.find_element(By.CLASS_NAME, "gs_nph")
                email_element = result.find_element(By.XPATH, ".//div[contains(text(), 'Verified email')]")
                citation_count_element = result.find_element(By.XPATH, ".//div[contains(text(), 'Cited by')]")

                name = name_element.text.strip()
                affiliation = affiliation_element.text.strip()
                email = email_element.text.strip().replace("Verified email at ", "")
                citation_count = citation_count_element.text.strip().split()[-1]

                # Print or store the extracted information
                print(f"Name: {name}")
                print(f"Affiliation: {affiliation}")
                print(f"Email: {email}")
                print(f"Citation Count: {citation_count}")
                print("=" * 40)
                return citation_count

        except Exception as e:
            print(f"Error while processing {professor_name}: {e}")

    def close_browser(self):
        self.driver.quit()

# # Example usage
# professor_names = ["diogo pacheco"]
#
# scholar_scraper = GoogleScholarScraper()
#
# for professor_name in professor_names:
#     scholar_scraper.search_professor(professor_name)
#
# scholar_scraper.close_browser()
