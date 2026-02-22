
"""importeren van de de nodige modules
    - re voor regex
    - sys voor error handling 
        https://docs.python.org/3/library/sys.html      
    - requests voor het maken van de http request
        https://docs.python-requests.org/en/latest/
    - yaml voor het outputten van de data in yaml formaat
 """
import re
import sys
import requests
import yaml
from python_opdracht.main import url

""" fetchen van de json data van de api url,
met een timeout van 10 seconden en error handling voor eventuele http errors """
def fetch_json(url):
  headers = {"Accept": "application/yaml"}
  r = requests.get(url, headers=headers, timeout=10)
  r.raise_for_status()
  return r.json()

""" extracten van de AS nummer uit het as veld, indien aanwezig.
Indien er geen AS nummer gevonden wordt, wordt het originele veld teruggegeven.
Indien het veld leeg is, wordt None teruggegeven. """
def extract_as(as_field):
  if not as_field:
    return None
  m = re.search(r"\bAS\d+\b", as_field)
  return m.group(0) if m else as_field

""" bouwen van de output dictionary in het gewenste formaat, met de nodige data uit de json response."""
def build_output(data):
  return {
    "infra": {
      "isp": data.get("isp"),
      "organisation": data.get("org"),
      "as": extract_as(data.get("as"))
    },
    "ip": data.get("query"),
    "land": data.get("countryCode"),
    "provider": data.get("isp")
  }


"""main functie die de url als argument neemt, de json data fetched en de output in yaml formaat print.
Indien er een error optreedt bij het fetchen van de json data, wordt deze geprint naar stderr 
en wordt het programma afgesloten met een error code."""
if __name__ == "__main__":
  try:
    data = fetch_json(url)
  except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    sys.exit(1)
  print(yaml.safe_dump(build_output(data), sort_keys=False, allow_unicode=True))