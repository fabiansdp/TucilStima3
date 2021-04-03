import requests

key = 'AIzaSyAcw74coYeNlfh7qqfy851C7zPuLa92dgQ'

#test
src = input("Input source location: ")
dest = input("Input destination location: ")

url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&"

r = requests.get(url+"origins="+src+"&destinations="+dest+"&key="+key)

print(r.text) #JSON output