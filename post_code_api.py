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

# display url together with given postcode


# check the type of data scraped from the web - responses

# convert data type if needed to iterate through the data and print required information


# display longitude and latitude - postcode etc.
# once completed - create a function to do return the required value - 1 function ust only return 1 value
# create a function that checks if the post code is valid - prompt the user to input the postcode
# create a class with all of these functions
# create a file called postcode_checker.py
# import this file and class
# call these functions in postcode_checker.py
# def postcode_validity():

