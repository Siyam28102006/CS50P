import requests

base_url = "https://pokeapi.co/api/v2/"

def get_info(name):
    url=f"{base_url}/pokemon/{name.lower()}"
    response=requests.get(url)
    if response.status_code == 200:
        #print(f"Data retrieved {response.status_code}")
        pokemon_data=response.json()
        return pokemon_data
    else :
        print(f"Failed to retrieve data {response.status_code}")

def main():
    pokemon_name = input("Who's that Pokemon??! : ")
    pokemon_info = get_info(pokemon_name) # this gets all the info about a pokemon

    if pokemon_info:
        print(f"The name of is {pokemon_info["name"].capitalize()}")
        print(f"Height:", pokemon_info["height"])
        print(f"Weight:", pokemon_info["weight"])

#print(response)  ; this gives a status code. if it is 200 -> all okay else not okay ; it is a status code
main()


