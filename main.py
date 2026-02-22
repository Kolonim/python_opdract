"""
Opdracht:

Bepalingen:
 - Je moet gebruik maken van de aangeleverde variable(n)
 - Je mag deze variable(n) niet aanpassen
 - Het is de bedoeling dat je op het einde 1 programma hebt
 - Als inlever formaat wordt een PUBLIEKE git url verwacht die gecloned kan worden
 - Je hoofd bestand dat uitgevoerd dient te worden moet `main.py` noemen
 - Jouw repository mag enkel jouw python bestanden en eventuele mappen te bevatten.
 - Jouw repository mag enkel de bestanden bevatten die nodig zijn voor jouw examen uit te voeren; dus geen onnodige/overbodige bestanden
 - Alle map en bestandsnamen mogen GEEN spaties bevatten, enkel underscores
 - Alle map en bestandsnamen mogen GEEN hoofdletters bevatten, enkel kleine letters
    
LET OP! Indien het examen dat je indient niet aan deze bepalingen voldoet wordt dit geacht niet in orde te zijn en is dit per definitie 0

/ 5 ptn 1 - Maak een public repository aan op jouw gitlab of github account voor dit project
/10 ptn 2 - Gebruik python om de gegeven api url aan te spreken
/20 ptn 3 - Gebruik regex om de volgende data te extracten:
    - De AS nummmer van de provider
/15 ptn 4 - Verzamel onderstaande data en output alles als yaml. Een voorbeeld vind je hieronder.
    - Het land van het domein
    - Het ip van het domain
    - De DNS provider van het domein
    - Aparte isp naam, organisation en AS nummer van de hoster


Totaal  /50ptn
"""

""" voorbeeld yaml output

infra:
  isp: 'Unix-Solutions BV'
  organisation: 'Unix-Solutions BV'
  as: 'AS39923'
ip: 185.58.96.99
land: BE
provider: combell

"""

import sys
import yaml

url = "http://ip-api.com/json/syntra.be"

"start van opdracht"


def main():
    try:
        try:
            from python_opdracht.js_functies import fetch_json, build_output
        except Exception:
            from js_functies import fetch_json, build_output
        data = fetch_json(url)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    print(yaml.safe_dump(build_output(data), sort_keys=False, allow_unicode=True))


if __name__ == "__main__":
    main()
