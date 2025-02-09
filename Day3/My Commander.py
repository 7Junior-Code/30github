# API using Python

from http.client import responses, error

import requests
import pygame
import time

base_url = "https://pokeapi.co/api/v2/"
error_s = "Game over.wav"
success_s = "cheering.wav"


def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to retrieve data {response.status_code}")
        pygame.mixer.init()
        pygame.mixer.music.load(error_s)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(1)
manual = input("Enter your pokemon: ").lower()
pokemon_name = f"{manual}"
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"Name: {pokemon_info["name"].capitalize()}")
    print(f"ID: {pokemon_info["id"]}")
    print(f"Height: {pokemon_info["height"]}")
    print(f"Weight: {pokemon_info["weight"]}")