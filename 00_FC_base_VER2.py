import pandas


# Functions go here


# checks if user entered yes or no

# checks if user entered an integer to a question

def yes_no(question):
    to_check = ["yes", "no"]

    valid = False
    while not valid:

        response = input(question).lower()

        for var_item in to_check:
            if response == var_item:
                return response
            elif response == var_item[0]:
                return var_item

    print("Please enter either yes or no...\n")


# checks if user responded with a blank
def not_blank(question, error):
    valid = False
    while not valid:
        response = input(question)

        if response == "":
            print("{}. \nPlease try again.\n".format(error))
            continue

        return response


def num_check(question, error, num_type):
    valid = False
    while not valid:

        try:
            response = num_type(input(question))

            if response <= 0:
                print(error)

            else:
                return response

        except ValueError:
            print(error)


def currency(x):
    return "${:.2f}".format(x)


# Gets expenses, returns list which has
# Gets expenses, returns list which has
# the data frame and sub-total
def get_expenses(var_fixed):
    # Set up dictionaries and lists

    item_list = []
    quantity_list = []
    price_list = []

    variable_dict = {
        "Item": item_list,
        "Quantity": quantity_list,
        "Price": price_list
    }

    # loop to get component, quantity and price
    item_name = ""
    while item_name.lower() != "xxx":

        print()
        # get name, quantity and item
        item_name = not_blank("Item name: ",
                              "The component name can't be"
                              " blank.")
        if item_name.lower() == "xxx":
            break

        if var_fixed == "fixed":
            quantity = 1

        else:
            quantity = num_check("Quantity: ",
                                 "The amount must be a whole number "
                                 "more than zero",
                                 int)

        price = num_check("How much for a single item? $",
                          "The price must be a number <more"
                          "than 0>",
                          float)

        # add item, quantity and price to lists
        item_list.append(item_name)
        quantity_list.append(quantity)
        price_list.append(price)

    expense_frame = pandas.DataFrame(variable_dict)
    expense_frame = expense_frame.set_index('Item')

    # Calculate cost of each component
    expense_frame['Cost'] = expense_frame['Quantity'] \
                            * expense_frame['Price']

    # Find sub-total
    sub_total = expense_frame['Cost'].sum()

    # Currency Formatting (uses currency function)
    add_dollars = ['Price', 'Cost']
    for item in add_dollars:
        expense_frame[item] = expense_frame[item].apply(currency)

    return [expense_frame, sub_total]


def expense_print(heading, frame, subtotal):
    print()
    print("**** {} Costs ****".format(heading))
    print(frame)
    print()
    print("{} Costs: ${:.2f}".format(heading, subtotal))
    return ""


# main routine goes here
# Get product name
product_name = not_blank("Product name: ", "The product name can't be blank.")

how_many = num_check("How many products : ",
                     "The amount must be a whole number "
                     "more than zero",
                     int)

print()
print("Please enter your variable costs below...")

# Get variable costs
variable_expenses = get_expenses("variable")
variable_frame = variable_expenses[0]
variable_sub = variable_expenses[1]

print()
have_fixed = yes_no("Do you have any fixed costs (y / n)? ")

if have_fixed == "yes":
    # Get fixed costs
    fixed_expenses = get_expenses("fixed")
    fixed_frame = fixed_expenses[0]
    fixed_sub = fixed_expenses[1]

else:
    fixed_sub = 0
    fixed_frame = ""

# Find total costs

# Ask user for profit goal

# Calculate recommended price

# Write data to file

# *** Printing Area ***

print("**** Fund Raising - {} ****".format(product_name))
print()

expense_print("Variable", variable_frame, variable_sub)
if have_fixed == "yes":
    expense_print("Fixed", fixed_frame[['Cost']], fixed_sub)
