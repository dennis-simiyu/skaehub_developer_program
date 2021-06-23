from urllib.request import urlopen
  
# import json
import json
def jsonDictConverter(url):

  
# store the response of URL
    response = urlopen(url)
  
# storing the JSON response 
# from url in danta

    json_data = response.read()

#converting to the dictionary
    dict_data = json.loads(json_data)
  
# print the json response
    print(type(dict_data))
    print(dict_data)
     
jsonDictConverter("https://api.github.com/")

