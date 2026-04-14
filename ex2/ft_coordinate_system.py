import math


def get_player_pos():
    while True:
        args = input("Enter new coordinates as floats in format 'x,y,z':")
        possible_coordinates = args.split(",")
        if len(possible_coordinates) != 3:
            print("Invalid syntax")
            continue
        coords = []
        error = False
        for x in possible_coordinates:
            try:
                coords.append(float(x.strip()))
            except ValueError as e:
                print(f"Error on parameter '{x}': {e}")
                error = True
                break
        if not error:
            return tuple(coords)
        

if __name__=="__main__":
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    tuple_coordinates1 = get_player_pos()
    print(f"Got a first tumple: {tuple_coordinates1}")
    x1 = tuple_coordinates1[0]
    y1 = tuple_coordinates1[1]
    z1 = tuple_coordinates1[2]
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    distance_center1 = math.sqrt((x1)**2 + (y1)**2 + (z1)**2)
    print(f"Distance to center: {distance_center1:.4f}")

    print("\nGet a second set of coordinates")
    tuple_coordinates2 = get_player_pos()
    x2 = tuple_coordinates2[0]
    y2 = tuple_coordinates2[1]
    z2 = tuple_coordinates2[2]
    distance_center2 =  math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    print(f"Distance between the 2 sets of coordinates: {distance_center2:.4f}")
    