import requests

r = requests.get("https://www.bbc.co.uk/")
# print(r.status_code)


# if the web page is live welcome the user with the status code

# or print a message OOPs something went wrong

#
# if r.status_code == 200:   # if true execute the next line - if false execute the next block
#     print(f"The status code is {r.status_code} the website is live")
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

if r:
     print("success")  # what is it checking
elif r.status_code == 404:         # what is it checking
     print("unsuccessful")
else:                             # what is it checking
     print (f"OOPS something went wrong please try later the status code is {r.status_code}")

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





