# Illustrates use of assignment expression construct
# introduced in Python 3.8

while (command := input("> ")) != "quit":
    print('You entered:', command)

print('Done')
