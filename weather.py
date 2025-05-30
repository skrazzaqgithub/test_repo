import re
import urllib.request
#http://www.weather-forecast.com/locations/Paris/forecasts/latest
city = input("Enter your city: ")
url = "http://www.weather-forecast.com/locations/" + city + "/forecasts/latest"
data = urllib.request.urlopen(url).read()
data1 = data.decode("utf-8")
print(data1)

m=re.search('span class="phrase"')
start=m.start
end=start+100
newString=data1[start:end]
