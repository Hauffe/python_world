with open("input.txt") as f:
    lines = f.readlines()


class Submarine:
    horizontal: int = 0
    vertical: int = 0
    aim: int = 0


submarine = Submarine()
for line in lines:
    command, places = line.split()
    if command == "up":
        # submarine.vertical -= int(places)
        submarine.aim -= int(places)
    if command == "down":
        # submarine.vertical += int(places)
        submarine.aim += int(places)
    if command == "forward":
        submarine.horizontal += int(places)
        submarine.vertical += int(places) * submarine.aim
    print(f"aim {submarine.aim} - H {submarine.horizontal} - D {submarine.vertical}")

print(submarine.horizontal * submarine.vertical)
