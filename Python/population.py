import json
import requests
page = 'https://datausa.io/api/data?drilldowns=Nation&measures=Population'
resp = requests.get(page)
data = resp.json()
population = data['data']
file = open('population.txt', 'w')
for entry in population:
    year = entry['Year']
    people = entry['Population']
    file.write("Rok: " + str(year) + ", Liczba mieszkancow: " + str(people) + "\n")
file.close()
print("Dane zostaly zapisane")
