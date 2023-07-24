import requests as requests


def listar_nombre_paises(url):
    paises = requests.get(url)
    paises = paises.json()

    for pais in paises:

        print(f"Nombre Oficial en Español: {pais['translations']['spa']['official']}")
        print(f"La capital: {pais['capital'][0]}")
        print(f"Codigo de telefono: {pais['idd']['root'] + pais['idd']['suffixes'][0]}")
        print(f"Su moneda actual es: {pais['currencies']}")
        print("........................................................................")


url = 'https://restcountries.com/v3.1/independent?=status=true&fields=translations,capital,idd,currencies'
listar_nombre_paises(url)