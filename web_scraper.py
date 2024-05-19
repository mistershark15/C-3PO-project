import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    # Načtení obsahu webové stránky
    response = requests.get(url)
    html_content = response.text
    
    # Analýza HTML obsahu
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Extrahování potřebných dat
    # Toto je jen příklad, měj na paměti, že můžeš přizpůsobit extrakci podle potřeby
    extracted_data = []
    for paragraph in soup.find_all('p'):
        extracted_data.append(paragraph.text)
    
    return extracted_data
