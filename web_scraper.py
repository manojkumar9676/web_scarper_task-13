import requests
from bs4 import BeautifulSoup
import csv

# 2. Legal and scrape-friendly website
URL = "https://quotes.toscrape.com"

# 3. Fetch HTML content using requests
try:
    response = requests.get(URL, timeout=10)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print("❌ Error fetching the website:", e)
    exit()

# 4. Parse HTML using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# 7. Store extracted data into CSV file
with open("quotes.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Quote", "Author", "Tags", "Link"])

    # 5. Identify HTML tags and attributes
    quotes = soup.find_all("div", class_="quote")

    for quote in quotes:
        # 8. Handle missing tags safely
        text = quote.find("span", class_="text")
        author = quote.find("small", class_="author")
        tags = quote.find_all("a", class_="tag")
        link = quote.find("a")

        quote_text = text.text if text else "N/A"
        author_name = author.text if author else "N/A"
        tag_list = ", ".join(tag.text for tag in tags) if tags else "N/A"
        quote_link = URL + link["href"] if link else "N/A"

        # 6. Extract text, links, and tables
        writer.writerow([quote_text, author_name, tag_list, quote_link])

print("✅ Scraping completed. Data saved to quotes.csv")
