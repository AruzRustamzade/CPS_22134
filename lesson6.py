import requests
a = input("Enter a link: ")
try:
    response = requests.get(a)
except:
    print("Error, your mistake or the server. I don't really care.\n-programmer ")
else:
    print(response)