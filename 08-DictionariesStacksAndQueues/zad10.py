countries = [
    {"country": "Poland", 
    "population": 38000000},
    {"country": "Argentina", 
    "population": 45000000},
    {"country": "Croatia",
    "population": 4000000},
    {"country": "Germany", 
    "population": 83000000},
    {"country": "Oman", 
    "population": 5000000}
]

lenght = len(countries)
while lenght>0:
    for k,v in countries[lenght-1].items():
        print(k,":",v)
    print("")

    lenght= lenght-1