import requests as requests

url = 'http://localhost:5000/v1/region/add'
data = {
    'region_code': 48,
    'name': 'Москва'
}

response = requests.post(url, json=data)
parsed_response = response.json()

print(response)
print(parsed_response)


url = 'http://localhost:5000/v1/region/update'
data = {
    'region_code': 48,
    'name': 'Томск'
}

response = requests.post(url, json=data)
parsed_response = response.json()

print(response)
print(parsed_response)



# url = 'http://localhost:5000/v1/region/delete'
# data = {
#     'region_code': 48
# }
#
# response = requests.post(url, json=data)
# parsed_response = response.json()
#
# print(response)
# print(parsed_response)


url = 'http://localhost:5000/v1/region/get'
data = {
    'region_code': 48
}

response = requests.get(url, json=data)
parsed_response = response.json()

print(response)
print(parsed_response)


url = 'http://localhost:5000/v1/region/get/all'

response = requests.get(url)
parsed_response = response.json()

print(response)
print(parsed_response)


url = 'http://localhost:5000/v1/car/tax-param/add'
data = {
    'code_rate': 1,
    'region_code': 48,
    'from_hp_car': 400,
    'to_hp_car': 500,
    'from_production_year_car': 2000,
    'to_production_year_car': 2016,
    'rate': 0.6
}

response = requests.post(url, json=data)
parsed_response = response.json()

print(response)
print(parsed_response)


url = 'http://localhost:5000/v1/car/tax-param/update'
data = {
    'code_rate': 12,
    'region_code': 54,
    'from_hp_car': 300,
    'to_hp_car': 400,
    'from_production_year_car': 2002,
    'to_production_year_car': 2013,
    'rate': 0.8
}

response = requests.post(url, json=data)
parsed_response = response.json()

print(response)
print(parsed_response)



url = 'http://localhost:5000/v1/car/tax-param/delete'
data = {
    'code_rate': 12
}

response = requests.post(url, json=data)
parsed_response = response.json()

print(response)
print(parsed_response)


url = 'http://localhost:5000/v1/car/tax-param/get'
data = {
    'code_rate': 20
}

response = requests.get(url, json=data)
parsed_response = response.json()

print(response)
print(parsed_response)


url = 'http://localhost:5000/v1/car/tax-param/get/all'

response = requests.get(url)
parsed_response = response.json()

print(response)
print(parsed_response)


url = 'http://localhost:5000/v1/car/tax-param/tax/calc'
data = {
    'code_rate': 20,
    'year': 2005,
    'horsepower': 350
}

response = requests.get(url, json=data)
parsed_response = response.json()

print(response)
print(parsed_response)


url = 'http://localhost:5000/v1/area/tax-param/add'
data = {
    'area_code': 2,
    'region_code': 54,
    'rate': 0.45
}

response = requests.post(url, json=data)
parsed_response = response.json()

print(response)
print(parsed_response)


url = 'http://localhost:5000/v1/area/tax-param/update'
data = {
    'region_code': 54,
    'rate': 0.1
}

response = requests.post(url, json=data)
parsed_response = response.json()

print(response)
print(parsed_response)


url = 'http://localhost:5000/v1/area/tax-param/delete'
data = {
    'region_code': 12
}

response = requests.post(url, json=data)
parsed_response = response.json()

print(response)
print(parsed_response)



url = 'http://localhost:5000/v1/area/tax-param/get'
data = {
    'area_code': 2
}

response = requests.get(url, json=data)
parsed_response = response.json()

print(response)
print(parsed_response)


url = 'http://localhost:5000/v1/area/tax-param/get/all'

response = requests.get(url)
parsed_response = response.json()

print(response)
print(parsed_response)


url = 'http://localhost:5000/v1/area/tax/calc'
data = {
    'region_code': 54,
    'cadastre_value': 700
}

response = requests.get(url, json=data)
parsed_response = response.json()

print(response)
print(parsed_response)