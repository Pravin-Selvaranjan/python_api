# Python API

![Blankdiagram](https://user-images.githubusercontent.com/110179866/183619804-af74bf6b-ab0d-4ef4-828f-8b4bc9b7b70c.jpeg)



## What is an API
### Benefits of API
#### Install requests

- Pip install package_name "pip install requests"
pip install requests
```
import requests

r = requests.get("https://www.bbc.co.uk/")
print(r.status_code)
```



import requests

r = requests.get("https://www.bbc.co.uk/iplayer/live/bbws")
print(r.status_code)


- if the web page is live welcome the user with the status code

- r print a message OOPs something went wrong


- if r.status_code == 200:   # if true execute the next line - if false execute the next block
```
print(f"The status code is {r.status_code} the website is live")
#     print(type(r.content)) # get the content from the web-app/endpoint
#     # find a way to change this type to json or dict or list or any type which we could
#     # iterate through with loops
#
# elif r.status_code == 404:
#     print(f"The site is unavailable until further notice the status code is {r.status_code}")
#
# else:
#     print(f"OOPs something went wrong the status code is {r} please try later")
#
#
# # should give us the status code only - numbers 200 -404 - 501 etc
```

## Second iteration

```
if r:
    print("success")  # what is it checking
elif r.status_code == 404:         # what is it checking
    print("unsuccessful")
else:                             # what is it checking
    print (f"OOPS something went wrong please try later the status code is {r.status_code}")
```

## Third iteration

```
# Third iteration
# Create a function that returns the status code with appropriate message
# use control flow to make the right decision
# USE RETURN not print inside your function

def api_function():
    if r:
        return "success"
    elif r.status_code == 404:
        return "unsuccessful"
    else:
        return f"OOPS something went wrong please try later the status code is {r.status_code}"



bbc_test = api_function()


print (bbc_test)
```


# Postcode API 
```
# import the required package
import requests
# valid postcode or invalid - url of the API address
url = "http://api.postcodes.io/postcodes/"
# store the data


postcode = input("Insert your postcode here: ")

# display the outcome
url_Arg = url + postcode # ("http://api.postcodes.io/postcodes/kt13rs"
r = requests.get(url_Arg)
# print(r.status_code)
r_dict = r.json()
result_dict = r_dict["result"]

print(r_dict)
for key in result_dict.keys():
    if key == "postcode":
        print(f"Please confirm this is your postcode {result_dict[key]}")# enter values/key that would print the postcode


print(r_dict)
for key in result_dict.keys():
    if key == "longitude":
        print(f"This is your longitude {result_dict[key]}")

    elif key == "latitude":
        print(f"This is you latitude {result_dict[key]}")
        
        
```     
- display url together with given postcode


- check the type of data scraped from the web - responses

- convert data type if needed to iterate through the data and print required information


- display longitude and latitude - postcode etc.
- once completed - create a function to do return the required value - 1 function ust only return 1 value
- create a function that checks if the post code is valid - prompt the user to input the postcode
- create a class with all of these functions
- create a file called postcode_checker.py
- import this file and class
- call these functions in postcode_checker.py
- def postcode_validity():