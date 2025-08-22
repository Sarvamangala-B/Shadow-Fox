#HERE WE ARE EXTRACTING 5 QUESTION FROM THE 4 TOPIC FROM THE INDIA BIX WEBSITE.

import requests
from bs4 import BeautifulSoup

# List of topics and their URLs
topics = {
    "Time and Work": "https://www.indiabix.com/aptitude/time-and-work/",
    "Problems on Trains": "https://www.indiabix.com/aptitude/problems-on-trains/",
    "Height and Distance ": "https://www.indiabix.com/aptitude/height-and-distance/",
    "Problems on Age": "https://www.indiabix.com/aptitude/problems-on-ages/"
}

for topic_name, url in topics.items():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    questions = soup.find_all('div', class_='bix-td-qtxt')

    print(f"\n=== {topic_name} ===\n")
    for idx, question in enumerate(questions, start=1):
        question_text = question.get_text(strip=True)
        print(f"{idx}. {question_text}\n")
