import sys


def command_quest():
    print(f"Program name: {sys.argv[0]}")
    if len(sys.argv) > 1:
        print(f"Arguments received: {len(sys.argv) - 1}")
        num = len(sys.argv)
        for pos in range(1, num):
            print(f"Argument {pos}: {sys.argv[pos]}")
    else:
        print("No arguments provided!")
    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    print("=== Command Quest ===")
    command_quest()
