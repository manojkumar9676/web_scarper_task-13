# web_scarper_task-13
# Web Scraping using Python

## 📌 Project Title
Web Scraping using Python, Requests, and BeautifulSoup

---

## 📖 Description
This project demonstrates basic web scraping using Python.  
The script fetches HTML content from a legal and scrape-friendly website, parses it using BeautifulSoup, extracts useful data, and stores it in a CSV file while following ethical scraping practices.

Website used: https://quotes.toscrape.com

---

## 🛠️ Tools & Technologies
- Python 3.14
- requests
- BeautifulSoup (bs4)
- VS Code
- PowerShell

---

## 📂 Files in the Project
- `web_scraper.py` → Main Python script for scraping  
- `quotes.csv` → Extracted data stored in CSV format  
- `README.md` → Project documentation  

---

## ⚙️ Installation Steps

### 1️⃣ Install Python
Download and install Python from:
https://www.python.org

---

### 2️⃣ Install Required Libraries
Run the following command in PowerShell:

```powershell
C:\Users\manoj\AppData\Local\Python\pythoncore-3.14-64\python.exe -m pip install requests beautifulsoup4
▶️ How to Run the Program
Open PowerShell

Navigate to the project folder:

cd C:\Users\manoj\OneDrive\Desktop\TASK-13
Run the script:

C:\Users\manoj\AppData\Local\Python\pythoncore-3.14-64\python.exe web_scraper.py
📊 Output
A file named quotes.csv is created

It contains:

Quote text

Author name

Tags

Quote link

🧠 Key Concepts Used
HTTP requests using requests

HTML parsing using BeautifulSoup

Tag and class identification

Safe handling of missing HTML elements

CSV file handling

Basic exception handling

⚠️ Ethical Scraping Practices
Only public and legal websites are scraped

No login or private data is accessed

Server load is kept minimal

Website terms and robots.txt are respected

✅ Conclusion
This project provides hands-on experience with web scraping fundamentals in Python.
It is suitable for beginners and helps understand real-world data extraction in an ethical manner.
