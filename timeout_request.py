import requests
def requestTimeout():
        print("timeout = 0.001")
        try:
            r = requests.get('https://api.twitter.com/2/tweets/', timeout = 0.001)
            print(r.text)
        except requests.exceptions.RequestException as e:
            print(e)    

        print("\ntimeout = 1.0")    
        try:
            r = requests.get('https://api.twitter.com/2/tweets/', timeout = 1.0)
            print("Connected....!")
        except requests.exceptions.RequestException as e:
            print(e)
requestTimeout()