def vai():
    import requests
    response = requests.get("https://term.ooo/2/")
    print(response.status_code)
    print(response.text)
    
import requests
usuario = {
    "name": "Chucky",
}
response = requests.post ('https://68d00787ec1a5ff338263f44.mockapi.io/cidade/Cidadaos',
json = usuario)

print(response.status_code)
print(response.json())