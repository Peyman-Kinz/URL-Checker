import requests
import re

def check_url(url):
    try:
        response = requests.get(url)
        # Überprüfe den HTTP-Statuscode
        if response.status_code == 200:
            # Überprüfe auf verdächtigen Inhalt
            if is_infected(response.text):
                return False, "Die URL ist erreichbar, enthält jedoch verdächtigen Inhalt."
            else:
                return True, "Die URL ist erreichbar und enthält keinen verdächtigen Inhalt."
        else:
            return False, f"HTTP-Statuscode: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return False, f"Fehler beim Abrufen der URL: {str(e)}"

def is_infected(html_content):
    # Hier kannst du Muster für verdächtigen Inhalt definieren
    # Zum Beispiel, um nach Schadcode oder Phishing-Versuchen zu suchen
    # In diesem Beispiel suchen wir nach dem Wort "infiziert" im HTML-Inhalt
    pattern = re.compile(r'infiziert', re.IGNORECASE)
    return pattern.search(html_content) is not None

# Benutzereingabe für die URL
url = input("Geben Sie die URL ein, die Sie überprüfen möchten: ")

reachable, message = check_url(url)
print(f"URL: {url} - {'Erreichbar' if reachable else 'Nicht erreichbar'} - {message}")
