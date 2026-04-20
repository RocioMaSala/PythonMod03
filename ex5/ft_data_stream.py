import random
import typing

names = ['alice', 'dylan', 'charlie', 'bob']

actions = ['run', 'eat', 'sleep', 'grab', 'move', 'climb', 'swim', 'release']


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        yield (random.choice(names), random.choice(actions))


def consume_event(
        data_list: list[tuple[str, str]]
        ) -> typing.Generator[tuple[str, str], None, None]:
    while data_list:
        index = random.randrange(len(data_list))
        yield data_list.pop(index)


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    generator = gen_event()
    for n in range(1000):
        name, action = next(generator)
        print(f"Event {n}: Player {name} did action {action}")

    ten_events = [next(generator) for n in range(11)]
    print(f"Built list of 10 events: {ten_events}")

    re_generator = consume_event(ten_events)
    for n in range(11):
        out_list = next(re_generator)
        print(f"Got event from list: {out_list}")
        print(f"Remains in list {ten_events}")
