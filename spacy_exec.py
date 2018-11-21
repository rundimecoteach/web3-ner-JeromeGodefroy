import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm
from bs4 import BeautifulSoup
import requests
import re


def url_to_string(url):
    res = requests.get(url)
    html = res.text
    soup = BeautifulSoup(html, 'html5lib')
    for script in soup(["script", "style", 'aside']):
        script.extract()
    return " ".join(re.split(r'[\n\t]+', soup.get_text()))


def getUrl(filename):
	fichier = open(filename, "r")
	urls = fichier.read().split("\n")
	return urls



if __name__ == '__main__':

	urls = getUrl("url.txt")
	
	entities = [[]]

	for url in urls:
		if url != "":
			print(url, "------------------------------------")
			nlp = en_core_web_sm.load()

			txtHtml = url_to_string(url)

			#print(txtHtml)

			doc = nlp(txtHtml)

			#print([(X.text, X.label_) for X in doc.ents])


			entity=[(X, X.ent_iob_, X.ent_type_) for X in doc if X.ent_iob_!='O' and (X.ent_type_=="LOC" or X.ent_type_=="ORG")]

			#print(entity)

			entities.append(entity)

	print(entities)

