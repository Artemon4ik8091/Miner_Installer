import json
from os.path import isfile
from os import system as sys

# Money
# {username: balance, ...}
class money():
    def read():
        if not isfile("money.json"):
            sys('echo "{}" > money.json')
        with open('money.json', 'r') as openfile:
            data = json.load(openfile)
        return data
    def write(data):
        js = json.dumps(data, indent=4)
        with open("money.json", "w") as outfile:
            outfile.write(js)

# Mining + Registrations
# Hash is encrypted!
# [ {"PrevHash": "00043dsafd", "nonce": 1,"date":  , "OpenKey": "762eagdfgtars5e34"}, ...]
class mine():
    def read():
        if not isfile("mine.json"):
            sys('echo "[]" > mine.json')
        with open('mine.json', 'r') as openfile:
            data = json.load(openfile)
        return data
    def write(data):
        js = json.dumps(data, indent=4)
        with open("mine.json", "w") as outfile:
            outfile.write(js)

# Pay + Registrations?
# Hash is encrypted!
# [ {"Payer": "user32532", "Receiver": "user64582", "OpenKey": "762eagdfgtars5e34", "PrevHash": "fsd2675ads"} , ...]
class pay():
    def read():
        if not isfile("pay.json"):
            sys('echo "[]" > pay.json')
        with open('pay.json', 'r') as openfile:
            data = json.load(openfile)
        return data
    def write(data):
        js = json.dumps(data, indent=4)
        with open("pay.json", "w") as outfile:
            outfile.write(js)

# Keys
# {"user32532": "762eagdfgtars5e34", ...}
class keys():
    def read():
        if not isfile("keys.json"):
            sys('echo "{}" > keys.json')
        with open('keys.json', 'r') as openfile:
            data = json.load(openfile)
        return data
    def write(data):
        js = json.dumps(data, indent=4)
        with open("keys.json", "w") as outfile:
            outfile.write(js)
