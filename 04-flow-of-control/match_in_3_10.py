# Example of the new 3.10 syntax for match

command = input("What are you doing next? ")

match command:
    case "quit":
        print("Goodbye!")
    case "look":
        print("Looking out")
    case "up" | "down":
        print("up or down")
    case _:
        print("The default")

match command.split():
    case ["go", "left"]:
        print("go left")
    case ["go", ("fast" | "slow")]:
        print("go fast or slow")

point = (3, 3)
match point:
    case (x, y) if x == y:
        print(f"The point is located on the diagonal Y=X at {x}.")
    case (x, y):
        print(f"Point is not on the diagonal.")
