postcards = {
    "Maria": "London",
    "Lorenzo": "Milan",
    "Oleg": "Canberra",
    "Hans": "Calgary",
    "Mark": "Milan",
    "Alex": "Krakow",
    "Julia": "Murmansk"

}
postcards["Petra"]= "Paris"
postcards["Ivan"] = "Moscow"
postcards["Oleg"] = "Sidney"
city = set(postcards.values())
city_list = list(city)
print("На самом деле в коллекции Алисы ", len(city), " городов)", sep ='')
print("А именно: ", ', '.join(city_list), sep='', end = '.')
