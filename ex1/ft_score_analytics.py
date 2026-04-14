import sys


def command_quest() -> None:
    if len(sys.argv) < 2:
        print("No scores provided.", end=" ")
        print(f"Usage: python3 {sys.argv[0]} <score1> <score2> ...")
        return

    scores = []

    for arg in sys.argv[1:]:
        try:
            scores.append(int(arg))
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
            continue

    if not scores:
        print("No scores provided.", end=" ")
        print(f"Usage: python3 {sys.argv[0]} <score1> <score2> ...")
        return

    total_players = len(scores)
    total_score = sum(scores)
    high_score = max(scores)
    low_score = min(scores)
    score_range = high_score - low_score

    print(f"Scores Processed: {scores}")
    print(f"Total players: {total_players}")
    print(f"Total score: {total_score}")
    print(f"Average score: {total_score / total_players}")
    print(f"High score: {high_score}")
    print(f"Low score: {low_score}")
    print(f"Score Range: {score_range}")
    print()


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    command_quest()
