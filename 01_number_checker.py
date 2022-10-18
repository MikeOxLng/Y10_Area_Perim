def numcheck(question):

    error = "Please enter a number that is more than zero"

    while True:

        try:
            response = float(input(question))

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

# Main routine starts here

keep_going = ""
while keep_going == "":
    width = numcheck("Please enter the width: ")
    height = numcheck("Please enter the height")

    area = width * height
    perimeter = 2 * (width + height)

    print("Area: {} square units".format(area))
    print("Perimeter: {} units".format(perimeter))

    print()
    keep_going = input("Press <enter> to keep going or any key to quit")
    print()