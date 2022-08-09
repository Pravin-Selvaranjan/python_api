import requests

r = requests.get("https://www.bbc.co.uk/")
# print(r.status_code)



print(f"The status code is {r.status_code} the website is live")
# should give us the status code only - numbers 200 -404 - 501 etc






