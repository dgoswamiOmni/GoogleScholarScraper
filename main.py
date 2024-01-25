import pandas as pd

from Classes import Scraper
from Classes import GoogleScholarScraper


def main():
    # # Replace "your_url_here" with the actual URL where your table is located
    # url = "https://computerscience.exeter.ac.uk/staff/"
    #
    # # Instantiate the parser class
    # parser = Scraper.TableParser(url)
    #
    # # Call the scrape_content function to get the data
    # data = parser.scrape_content()
    # results_list = []
    #
    # # Process or print the extracted data as needed
    # for entry in data:
    #     print((f"URL: {entry['URL']}, Content: {entry['Content']}, 'Researcher': {entry['Researcher']}"))
    #     page = url[:36]+entry["URL"]
    #     content = parser.extract_additional_info(page)
    #     name = entry['Researcher']
    #     results_list.append(({"URL": page, "Content": content,"Name":name}))
    #
    # df_results = pd.DataFrame(results_list)
    # df_results.to_csv('results.csv', index=False)
    df_results = pd.read_csv('results.csv')
    # Example usage
    professor_names = df_results["Name"]

    scholar_scraper = GoogleScholarScraper.GoogleScholarScraper()
    for professor_name in professor_names:
        citations = scholar_scraper.search_professor(professor_name)
        citations_list.append(citations)

    # Instantiate TextProcessor with the text column name
    text_processor = TextProcessor(text_column_name='text_column_name')

    # Process the DataFrame and get the most common words dictionary
    result_dict = text_processor.process_dataframe(df)

    scholar_scraper.close_browser()

        # Call the store_in_dataframe function to store the data in a DataFrame
    # parser.store_in_dataframe(data)


if __name__ == "__main__":
    main()
