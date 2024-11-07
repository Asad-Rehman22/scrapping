import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL to scrape
url = "https://www.otago.ac.nz/study/subjects/a-z#Z"

# Send HTTP request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all <li> tags and then get <a> tags within them
    links = []
    for li in soup.find_all('li'):
        a_tag = li.find('a')
        if a_tag:
            link_text = a_tag.get_text(strip=True)  # Get the text inside <a> tag
            link_url = a_tag.get('href')            # Get the href attribute value
            links.append([link_text, link_url])

    # Convert the list of links into a DataFrame
    df = pd.DataFrame(links, columns=['Text', 'URL'])

    # Save the data into a CSV file
    df.to_csv('links.csv', index=False)

    print("CSV file 'links.csv' created successfully.")
else:
    print("Failed to retrieve the page. Status code:", response.status_code)
