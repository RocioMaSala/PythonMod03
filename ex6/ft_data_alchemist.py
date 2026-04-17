import random

comprehensions = [
    'Alice', 'bob', 'Charlie', 'dylan', 
    'Emma', 'Gregory', 'john', 'kenin', 'Liam'
]

comprehensions_capitalized = [name.capitalize() for name in comprehensions]
comprehensions_only_capitalized = [name for name in comprehensions if name[0].isupper()]

dictionary_comprehensions = {name: random.randint(0,800) for name in comprehensions}

average = sum(dictionary_comprehensions.values()) / len(dictionary_comprehensions)

high_scores = {name: score for name, score in dictionary_comprehensions.items() if score > average}

if __name__ == "__main__":
    print ("=== Game Data Alchemist ===")
    print()
    print(f"Initial list of players: {comprehensions}")
    print(f"New list with all names capitalized: {comprehensions_capitalized}")
    print(f"New list of capitalized names only: {comprehensions_only_capitalized}\n")
    print(f"Score dict: {dictionary_comprehensions}")
    print(f"Score average: {average:.2f}")
    print(f"High scores: {high_scores}")
