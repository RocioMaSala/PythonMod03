import sys


def command_quest():
    if len(sys.argv) < 2:
        print("No scores provided. Usage: python3 ft_score_analytics. py <score1> <score2> ...")
        num = len(sys.argv)
        for pos in range(1, num):
            print(f"Argument {pos}: {sys.argv[pos]}")
    else:
        print(f"Scores Processed: [{sys.argv}]")
        print(f"Total players: {len(sys.argv) - 1}")
        print(f"Total players: {len(sys.argv) - 1}")
    


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    command_quest()
