import requests
from bs4 import BeautifulSoup

# --- Option 1: Fetch HTML from the live website ---
# Note: This will likely fail in an environment that respects robots.txt
# To use this, uncomment the following lines and comment out Option 2.
#
# url = "https://news.hada.io/"
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# try:
#     response = requests.get(url, headers=headers)
#     response.raise_for_status() # Raise an exception for bad status codes
#     html_content = response.text
# except requests.exceptions.RequestException as e:
#     print(f"Error fetching URL: {e}")
#     # As a fallback, read from the local file if the request fails
#     print("Falling back to reading from local file.")
#     with open('hada_news.html', 'r', encoding='utf-8') as f:
#         html_content = f.read()


# --- Option 2: Read HTML from a local file (for testing) ---
# This is the default option to ensure the script runs.
with open('hada_news.html', 'r', encoding='utf-8') as f:
    html_content = f.read()


# Parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Find all topic rows
topic_rows = soup.find_all('div', class_='topic_row')

print("--- Hada News Headlines ---")
# Extract and print the title from each row
for row in topic_rows:
    # The title is within an <h1> tag inside a <a> tag
    title_tag = row.find('h1')
    if title_tag:
        print(title_tag.get_text().strip())

print("--------------------------")
