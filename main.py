import requests
import json
import sys

print("To exit don't type anything, but press 'Enter'.")
try:
    value_from = str(input("Enter your currency: "))
    value_to = str(input("Enter currency you want: "))
    money = float(input("Enter your money: "))
except ValueError:
    sys.exit()
dictionary = {}
url = "http://www.floatrates.com/daily/" + value_from + ".json"
req = requests.get(url).text
try:
    dictionary.update({value_from: {'eur': json.loads(req)['eur']['rate'], 'usd': json.loads(req)['usd']['rate']}})
except KeyError:
    try:
        dictionary.update({value_from: {'eur': json.loads(req)['eur']['rate']}})
    except KeyError:
        dictionary.update({value_from: {'usd': json.loads(req)['usd']['rate']}})
while True:
    print("Checking the cache...")
    if dictionary.get(value_from) and dictionary.get(value_from).get(value_to):
        print("It is in the cache!")
        money = dictionary[value_from][value_to] * money
    else:
        print("Sorry, but it is not in the cache!")
        dictionary[value_from].update({value_to: json.loads(req)[value_to]['rate']})
        money = dictionary[value_from][value_to] * money

    print("You received",  round(money, 2), value_to + ".")
    value_to = str(input("Enter currency you want: "))
    if value_to == '':
        break
    money = float(input("Enter your money: "))
