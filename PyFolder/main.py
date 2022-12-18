import requests
import json

token = '14064e867a8b16845e0e1db5d063167b'
response = requests.post('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token' : token}, json={
    "name": "Birdy",
    "photo": "https://w7.pngwing.com/pngs/429/182/png-transparent-pokemon-go-chansey-blissey-pokedex-kool-aid-man.png"
})

print(response.text)


response_put = requests.put('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token' : token}, json={
    "pokemon_id": 2453,
    "name": "Ченси",
    "photo": "https://w7.pngwing.com/pngs/429/182/png-transparent-pokemon-go-chansey-blissey-pokedex-kool-aid-man.png"
})

print(response_put.text)


token = '14064e867a8b16845e0e1db5d063167b'
response = requests.post('https://pokemonbattle.me:5000/trainers/add_pokeball', headers={'trainer_token' : token}, json={
   "pokemon_id": "2453"
})

print(response.text)