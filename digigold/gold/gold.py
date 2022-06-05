import requests
from bs4 import BeautifulSoup

def extractNumFromString(val):
	return float(''.join([x for x in val if x.isdigit() or x == '.']))

def goldPrice():
	try:
		patroData = requests.get("https://www.hamropatro.com/gold")
		if "upstream connect error" in patroData.text:
			return "Error Fectching Data",-1
	except:
		return "Error Fectching Data",-1
	soup = BeautifulSoup(patroData.text, 'html.parser')
	data = soup.find("ul", class_="gold-silver").find_all("li",onclick="$('.goldchart').hide();$('#goldchart').show();")
	withoutNRS = data[1].text.replace("Nrs.","")
	price = extractNumFromString(withoutNRS)
	return data[0].text,price;

def changeRate(weight):
	gType,gPrice = goldPrice()
	rate = float(weight)*gPrice
	return rate
