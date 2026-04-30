import random

comprehensions = [
    'Alice', 'bob', 'Charlie', 'dylan',
    'Emma', 'Gregory', 'john', 'kenin', 'Liam'
]

comprehensions_capitalized = [name.capitalize() for name in comprehensions]
compr_only_capit = [name for name in comprehensions if name[0].isupper()]

dict_comprehensions = {
    name: random.randint(0, 800) for name in comprehensions_capitalized
    }

average = sum(dict_comprehensions.values()) / len(dict_comprehensions)

high_scores = {
    name: score for name, score in dict_comprehensions.items()
    if score > average
    }

if __name__ == "__main__":
    print("=== Game Data Alchemist ===")
    print()
    print(f"Initial list of players: {comprehensions}")
    print(f"New list with all names capitalized: {comprehensions_capitalized}")
    print(f"New list of capitalized names only: {compr_only_capit}\n")
    print(f"Score dict: {dict_comprehensions}")
    print(f"Score average: {average:.2f}")
    print(f"High scores: {high_scores}")
