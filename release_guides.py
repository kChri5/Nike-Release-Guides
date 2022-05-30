import requests
from bs4 import BeautifulSoup
import json, time, sys, ctypes, os
from art import *
from dateutil import parser
from datetime import datetime, timezone
from forex_python.converter import CurrencyRates

ctypes.windll.kernel32.SetConsoleTitleW("Release Guides by kChris#6478")
clear = lambda: os.system('cls')
c = CurrencyRates()

def utc_to_local(utc_dt):
    return utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=None)

discord_webhook_url = ""

def discord_webhook():
	embed = {
    "description": f"**Release Date:** {release_date}\n**Launch Type:** {launch_type}\n**SKU:** {sku}\n** **\n** **",
    "title": f"**{name}**",
    "url": f"{user_input_url}",
    "color": 000000,
    "thumbnail": {
    	"url": image,
    },
	"fields": [
		{
			"name": "**Retail:**",
			"value": f"{price_formatted}\n** **\n** **",
		},
		{
			"name": f"**Available Sizes (US{sizes_available}):**",
			"value": f"{sizes_stock_formatted_1}\n** **",
			"inline": True,
		},
		{
			"name": "** **",
			"value": f"{sizes_stock_formatted_2}\n** **",
			"inline": True,
		},
		{
			"name": "** **",
			"value": "** **",
			"inline": True,
		},
		{
			"name": "**Links:**",
			"value": f"[StockX](http://stockx.com/search?s={sku})  |  [GOAT](https://www.goat.com/search?query={sku})  |  [Novelship](https://novelship.com/search?q={sku})  |  [Oxstreet](https://oxstreet.com/search?query={sku})  |  [Early Link]({user_input_url}?productId={product_id}&size=)",
		},
	],
	}
	data = {
	    # "content": "",
	    "username": "kChris",
	    "embeds": [
	        embed
	        ],
	}

	result = requests.post(discord_webhook_url, json=data)
	if 200 <= result.status_code < 300:
	    print(f"Webhook sent {result.status_code}")
	else:
	    print(f"Not sent with {result.status_code}, response:\n{result.json()}")

while True:
	clear()
	tprint("\nRelease Guides")
	print("Select Region:")
	print("[1] JP")
	print("[2] SG/MY")
	print("[3] GB")
	print("[4] AU")
	print("[5] US")
	print("[6] MX")
	user_input = input(">>>")
	if user_input in ["1","2","3","4","5","6"]:
		if user_input == "1":
			clear()
			print("Coming Soon...")
			time.sleep(2)
			clear()
		elif user_input == "2":
			clear()
			user_input_url = input("URL: ")
			# format url
			url_sg = user_input_url
			url_split = url_sg.split("/")
			url_split[3] = "my"
			url_my = "/".join(url_split)
			# sg
			r_sg = requests.get(url_sg)
			soup_sg = BeautifulSoup(r_sg.content, "html.parser")
			result_nike_details_sg = soup_sg.find(type='application/ld+json')
			result_nike_details_sg = result_nike_details_sg.prettify()
			# my
			r_my = requests.get(url_my)
			soup_my = BeautifulSoup(r_my.content, "html.parser")
			result_nike_details_my = soup_my.find(type='application/ld+json')
			result_nike_details_my = result_nike_details_my.prettify()
			# product_id
			result_product_id = soup_sg.find("meta", attrs={"name": "branch:deeplink:productId"})
			# sg
			soup_sg = BeautifulSoup(result_nike_details_sg, 'html.parser')
			res_sg = soup_sg.find('script')
			json_object_sg = json.loads(res_sg.contents[0])
			# my
			soup_my = BeautifulSoup(result_nike_details_my, 'html.parser')
			res_my = soup_my.find('script')
			json_object_my = json.loads(res_my.contents[0])
			name = json_object_sg['description']
			name = name.replace("Explore and buy the ", "")
			name = name.replace(". Stay a step ahead of the latest sneaker launches and drops.","")
			print(name)
			# price sg/my
			price_sg = json_object_sg['offers']['price']
			price_my = json_object_my['offers']['price']
			price_my_sg = str(round(c.convert('MYR', 'SGD', price_my),2))
			# formatted currency and price
			price_formatted = f"SG: S${price_sg}\nMY: MYR {price_my} (S${price_my_sg})"
			print(price_formatted)
			# sku
			sku = json_object_sg['sku']
			print(sku)
			# product_id
			product_id = result_product_id['content']
			print(product_id)
			# release_date +0800
			release_date = json_object_sg['releaseDate']
			release_date = utc_to_local(parser.parse(release_date))
			print(release_date)
			# image
			image = json_object_sg['image']
			# color
			color = json_object_sg['color']
			print(color)
		elif user_input == "3":
			clear()
			print("Coming Soon...")
			time.sleep(2)
			clear()
		elif user_input == "4":
			clear()
			user_input_url = input("URL: ")
			url_au = user_input_url
			# sg
			r_au = requests.get(url_au)
			soup_au = BeautifulSoup(r_au.content, "html.parser")
			result_nike_details_au = soup_au.find(type='application/ld+json')
			result_nike_details_au = result_nike_details_au.prettify()
			# product_id
			result_product_id = soup_au.find("meta", attrs={"name": "branch:deeplink:productId"})
			soup_au = BeautifulSoup(result_nike_details_au, 'html.parser')
			res_au = soup_au.find('script')
			json_object_au = json.loads(res_au.contents[0])
			name = json_object_au['description']
			name = name.replace("Explore and buy the ", "")
			name = name.replace(". Stay a step ahead of the latest sneaker launches and drops.","")
			print(name)
			# price sg/my
			price_au = json_object_au['offers']['price']
			price_au_sg = str(round(c.convert('AUD', 'SGD', price_au),2))
			# formatted currency and price
			price_formatted = f"A${price_au} (S${price_au_sg})"
			print(price_formatted)
			# sku
			sku = json_object_au['sku']
			print(sku)
			# product_id
			product_id = result_product_id['content']
			print(product_id)
			# release_date +0800
			release_date = json_object_au['releaseDate']
			release_date = utc_to_local(parser.parse(release_date))
			print(release_date)
			# image
			image = json_object_au['image']
			# color
			color = json_object_au['color']
			print(color)
		elif user_input == "5":
			clear()
			print("Coming Soon...")
			time.sleep(2)
			clear()
		elif user_input == "6":
			clear()
			user_input_url = input("URL: ")
			url_mx = user_input_url
			# mx
			r_mx = requests.get(url_mx)
			soup_mx = BeautifulSoup(r_mx.content, "html.parser")
			result_nike_details_mx = soup_mx.find(type='application/ld+json')
			result_nike_details_mx = result_nike_details_mx.prettify()
			# product_id
			result_product_id = soup_mx.find("meta", attrs={"name": "branch:deeplink:productId"})
			soup_mx = BeautifulSoup(result_nike_details_mx, 'html.parser')
			res_mx = soup_mx.find('script')
			json_object_mx = json.loads(res_mx.contents[0])
			name = json_object_mx['description']
			name = name.replace("Explora y compra el ", "")
			name = name.replace(". Mantente un paso adelante de los últimos lanzamientos de calzado deportivo.","")
			name = name.replace(". Mantente un paso adelante de los últimos lanzamientos de calzado.","")
			print(name)
			# price sg/my
			price_mx = json_object_mx['offers']['price']
			price_mx_sg = str(round(c.convert('MXN', 'SGD', price_mx),2))
			# formatted currency and price
			price_formatted = f"M${price_mx} (S${price_mx_sg})"
			print(price_formatted)
			# sku
			sku = json_object_mx['sku']
			print(sku)
			# product_id
			product_id = result_product_id['content']
			print(product_id)
			# release_date +0800
			release_date = json_object_mx['releaseDate']
			release_date = utc_to_local(parser.parse(release_date))
			print(release_date)
			# image
			image = json_object_mx['image']
			# color
			color = json_object_mx['color']
			print(color)
		else:
			clear()
		filter_nike = None
		if user_input == "1":
			filter_nike = "merchGroup(XD)"
		elif user_input == "2":
			filter_nike = "merchGroup(XA)"
			input_region = "SG"
		elif user_input == "4":
			filter_nike = "merchGroup(XP)"
			input_region = "AU"
		elif user_input == "6":
			filter_nike = "shipNode(MX_FAST)"
			input_region = "MX"
		response = requests.get(f"https://api.nike.com/merch/skus/v2/?filter=productId%28{product_id}%29&filter=country%28{input_region}%29")
		data = response.json()
		data = data['objects']
		sizes = []
		gtin = []
		for num in range(len(data)):
			sizes.append(data[num]['nikeSize'])
			gtin.append(data[num]['gtin'])
		# scrape stock level "OOS,LOW,MEDIUM,HIGH"
		response = requests.get(f"https://api.nike.com/deliver/available_gtins/v3/?filter=styleColor({sku})&filter={filter_nike}")
		data = response.json()
		data = data['objects']
		stock_level = []
		gtin_2 = []
		for num in range(len(data)):
			stock_level.append(data[num]['level'])
			gtin_2.append(data[num]['gtin'])
		gtin_sizes = dict(list(zip(sizes,gtin)))
		dictionary = dict(list(zip(gtin_2,stock_level)))
		all_sizes_and_stock = {k:dictionary.get(gtin_sizes[k], "OOS") for k in gtin_sizes}
		all_sizes_and_stock = [[key, all_sizes_and_stock[key]] for key in all_sizes_and_stock.keys()]
		print(all_sizes_and_stock)
		# splitting sizes/stock 1
		sizes_and_stock_1 = all_sizes_and_stock[0::2]
		dict_sizes_and_stock_1 = dict(sizes_and_stock_1)
		# splitting sizes/stock 2
		sizes_and_stock_2 = all_sizes_and_stock[1::2]
		dict_sizes_and_stock_2 = dict(sizes_and_stock_2)
		# sizes/stock formatted 1
		sizes_stock_formatted_1 = ""
		for key,value in dict_sizes_and_stock_1.items():
			sizes_stock_formatted_1 += f"{key} - {value}\n"
		# sizes/stock formatted 2
		sizes_stock_formatted_2 = ""
		for key,value in dict_sizes_and_stock_2.items():
			sizes_stock_formatted_2 += f"{key} - {value}\n"
		# sizes available
		sizes_available = f"{sizes[0]} - {sizes[-1]}"
		print(sizes_available)
		launch_type = input("Launch Type (PHIL/LEO/DAN): ")
		launch_type = launch_type.upper()
		input("Press ENTER to continue")
		discord_webhook()
		print("Generating Discord Webhook")
		print("Webhook Sent")
		print("Exiting in 3 seconds")
		time.sleep(3)
		quit()
	else:
		clear()