import random

achievements = [
    'Crafting Genius', 'Strategist', 'World Savior',
    'Speed Runner', 'Survivor',
    'Master Explorer', 'Treasure Hunter', 'Unstoppable',
    'First Steps', 'Collector Supreme',
    'Untouchable', 'Sharp Mind', 'Boss Slayer'
]


def gen_player_achievements() -> set[str]:
    return set(
          random.sample(achievements, random.randint(1, len(achievements)))
          )


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    all_sets = {}
    for player in ['Alice', 'Bob', 'Charlie', 'Dylan']:
        player_achievements = gen_player_achievements()
        all_sets[player] = player_achievements
        print(f"Player {player}: {player_achievements}")
    print()

    distinct_achievements = set.union(*all_sets.values())
    print(f"All distinct achievements: {distinct_achievements}\n")

    common_achievements = set.intersection(*all_sets.values())
    print(f"Common achievements: {common_achievements}\n")

    unique_achievements = {}
    for player in all_sets:
        others = set().union(*(v for p, v in all_sets.items() if p != player))
        unique_achievements[player] = all_sets[player].difference(others)
        print(f"Only {player} has: {unique_achievements[player]}")

    print()
    missing_achievements = {}
    for player in all_sets:
        others = set().union(*(v for p, v in all_sets.items() if p != player))
        missing_achievements[player] = others.difference(all_sets[player])
        print(f"{player} is missing: {missing_achievements[player]}")
