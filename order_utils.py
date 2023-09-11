import datetime
import os

# Welcome and End Messages
WELCOME_MSG = "Hello! Welcome to Vietnamese Breakfast To-go.\nBelow is our menu today:"
END_LINE = "-------END--------"
SEE_YOU_MSG = "Thank you! See you soon!"

# Order Completion Messages
THANK_YOU_MSG = "Thank you for your order! Your order ID is {}.\nPlease wait while we prepare your breakfast."
CANCEL_ORDER_MSG = "Your order has been cancelled."
LARGE_ORDER_MSG = "For the large order over 100 items, please contact our shop owner directly!\nThank you!"

# Item Added Messages
COFFEE_ADDED_MSG = "Coffee added to your order!"
SANDWICH_ADDED_MSG = "Sandwich added to your order!"

# Prompts for User Input
COFFEE_PROMPT = "How many coffees would you like to order? "
SANDWICH_PROMPT = "How many sandwiches would you like to order? "
TAILOR_PROMPT = "Would you like them to the same as your previous order?\n Answer: Yes = Y | No = N: "
OTHER_ITEMS_PROMPT = "Would you like to add other items?"
NO_ITEMS_LEFT_PROMPT = "No items left. Would you like to order other items? Yes/No: "
ORDER_AGAIN_PROMPT = "Would you like to order again?/n Answer: Yes = Y | No = N: "
CANCEL_PROMPT = "Are you sure to cancel your order? /n Answer: Yes = Y | No = N: "

# Error Messages
INPUT_ERROR_MSG = "Invalid input. Try again!"
INPUT_YESNO_ERROR_MSG = "Please enter 'Y' for yes or 'N' for no."

# Menu options
# Define the various menu options available to the user.
INITIAL_MENU_OPTIONS = [
    "1. Vietnamese Coffee", "2. Vietnamese Sandwich",
    "3. No, thanks! I will order later."
]
AFTER_SELECTION_MENU_OPTIONS = [
    "1. Vietnamese Coffee", "2. Vietnamese Sandwich", "3. Proceed to checkout"
]
EDIT_OPTIONS = ["1. Edit my order", "2. Delete All", "3. Pay my order"]
COFFEE_TYPE_OPTIONS = ["1. HOT", "2. ICED"]
SANDWICH_TYPE_OPTIONS = [
    "1. Grilled Pork Sandwich", "2. Shredded Chicken Sandwich"
]
MILK_OPTIONS = ["0. No milk", "1. One teaspoon", "2. Two teaspoons"]
SUGAR_OPTIONS = ["0. No sugar", "1. One teaspoon", "2. Two teaspoons"]

# Prices
COFFEE_PRICE = 1
SANDWICH_PRICE = 2


# Custom Exception
# Use when the user tries to order more than 100 items.
class LargeOrderException(Exception):
  pass


# Function to display the menu to the user and get their choice.
# Print out the options
# and validate inputs.
def display_menu(options):
  for option in options:
    print(option)
  valid_choices = [
      int(option.split('.')[0]) for option in options
      if option.split('.')[0].isdigit()
  ]
  return get_valid_input("Enter your choice: ", valid_choices)


# Function to get the quantity of an order from the user.
# check if the input is a valid integer and checks for large orders.
def get_order_quantity(prompt):
  while True:
    try:
      user_input = int(input(prompt))
      if user_input == 0:
        raise ValueError
      elif user_input > 100:
        print(LARGE_ORDER_MSG)
        print(END_LINE)
        raise LargeOrderException()
        return None
      return user_input
    except ValueError:
      print(INPUT_ERROR_MSG)


# Function to get valid input from the user.
# check if the input matches the expected format or options.
def get_valid_input(prompt, valid_options=None, is_yes_no=False):
  while True:
    user_input = input(prompt)
    if is_yes_no:
      if user_input.lower() == 'y':
        return 'y'
      elif user_input.lower() == 'n':
        return 'n'
      else:
        print(INPUT_YESNO_ERROR_MSG)
    else:
      try:
        user_input = int(user_input)
        if valid_options and user_input not in valid_options:
          raise ValueError
        return user_input
      except ValueError:
        print(INPUT_ERROR_MSG)


# Function to add coffee to the order.
# prompt the user for coffee details
# and add them to the order list
def add_coffee(orderList):
  try:
    numCoffees = get_order_quantity(COFFEE_PROMPT)
  except LargeOrderException:
    return orderList, False
  for i in range(numCoffees):
    coffeeType = display_menu(COFFEE_TYPE_OPTIONS)
    milkAmount = int(display_menu(MILK_OPTIONS))
    sugarAmount = int(display_menu(SUGAR_OPTIONS))
    coffeeOrder = {
        'type': 'HOT' if coffeeType == 1 else 'ICED',
        'milk': milkAmount,
        'sugar': sugarAmount
    }
    orderList.append(coffeeOrder)
    remaining_coffees = numCoffees - (i + 1)

    coffee_added_msg = f"Your coffee has been added.\n You still have {remaining_coffees} more coffee(s) to order."
    all_coffees_added_msg = f"All {numCoffees} coffees have been added to your order!"

    if remaining_coffees > 0:
      print(coffee_added_msg)
      choice = get_valid_input(TAILOR_PROMPT, is_yes_no=True)
      if choice == "y":
        for _ in range(remaining_coffees):
          orderList.append(coffeeOrder)
        print(all_coffees_added_msg)
        print(OTHER_ITEMS_PROMPT)
        choice = get_valid_input("(Y/N): ", is_yes_no=True)
        return orderList, choice == "y"
    else:
      print(COFFEE_ADDED_MSG)
  print(OTHER_ITEMS_PROMPT)
  choice = get_valid_input("(Y/N): ", is_yes_no=True)
  return orderList, choice == "y"


# Function to add sandwiches to the order.
# prompt the user for sandwich details a
# and add them to the order list.
def add_sandwich(orderList):
  try:
    numSandwiches = get_order_quantity(SANDWICH_PROMPT)
  except LargeOrderException:
    return orderList, False
  for i in range(numSandwiches):
    sandwichType = display_menu(SANDWICH_TYPE_OPTIONS)
    sandwichOrder = {
        'type':
        'Grilled Pork Sandwich'
        if sandwichType == 1 else 'Shredded Chicken Sandwich'
    }
    orderList.append(sandwichOrder)
    remaining_sandwiches = numSandwiches - (i + 1)

    sandwich_added_msg = f"Your sandwich has been added.\n You still have {remaining_sandwiches} more sandwich(es) to order."
    all_sandwiches_added_msg = f"All {numSandwiches} sandwiches have been added to your order!"

    if remaining_sandwiches > 0:
      print(sandwich_added_msg)
      choice = get_valid_input(TAILOR_PROMPT, is_yes_no=True)
      if choice == "y":
        for _ in range(remaining_sandwiches):
          orderList.append(sandwichOrder)
        print(all_sandwiches_added_msg)
        print(OTHER_ITEMS_PROMPT)
        choice = get_valid_input("(Y/N): ", is_yes_no=True)
        return orderList, choice == "y"
    else:
      print(SANDWICH_ADDED_MSG)
  print(OTHER_ITEMS_PROMPT)
  choice = get_valid_input("(Y/N): ", is_yes_no=True)
  return orderList, choice == "y"


# Function to review and finalize the order.
def checkout(orderList):
  total_price = 0

  # display the items in the order, calculates the total price,
  print("\nReview:".upper())
  for idx, item in enumerate(orderList, 1):
    if item['type'] in ['HOT', 'ICED']:
      milk = f"Milk: {item.get('milk', 'No')} tsp"
      sugar = f"Sugar: {item.get('sugar', 'No')} tsp"
      print(
          f"{idx}. Coffee - {item['type']}, {milk}, {sugar} - ${COFFEE_PRICE}")
      total_price += COFFEE_PRICE
    else:
      print(f"{idx}. Sandwich: {item['type']} - ${SANDWICH_PRICE}")
      total_price += SANDWICH_PRICE
  print(f"Total amount: {len(orderList)}")
  print(f"Total price: ${total_price}")
  print("-------------------")
  print("Are you ready to order?")

  # provide options to edit or pay.
  choice = display_menu(EDIT_OPTIONS)
  if choice == 1:
    edit_item(orderList)
  elif choice == 2:
    confirmation = get_valid_input(CANCEL_PROMPT, is_yes_no=True)
    if confirmation == "y":
      orderList.clear()
      print(CANCEL_ORDER_MSG)
      print(SEE_YOU_MSG)
      print(END_LINE)
      return 'exit'
    else:
      return False
  elif choice == 3:
    save_to_file(orderList)
    orderID = generate_order_id()
    print("\nReceipt:".upper())
    for idx, item in enumerate(orderList, 1):
      if item['type'] in ['HOT', 'ICED']:
        milk = f"Milk: {item.get('milk', 'No')} tsp"
        sugar = f"Sugar: {item.get('sugar', 'No')} tsp"
        print(
            f"{idx}. Coffee - {item['type']}, {milk}, {sugar} - ${COFFEE_PRICE}"
        )
      else:
        print(f"{idx}. Sandwich: {item['type']} - ${SANDWICH_PRICE}")
    print(f"Total amount: {len(orderList)}")
    print(f"Total price: ${total_price}")
    print("-------------------")
    print(THANK_YOU_MSG.format(orderID))
    print(END_LINE)


# Function to edit an item in the order.
def edit_item(orderList):
  valid_item_ids = list(range(1, len(orderList) + 1))
  itemId = int(input("Enter item ID to edit: "))
  if itemId not in valid_item_ids:
    print(INPUT_ERROR_MSG)
    return edit_item(orderList)
  item = orderList[itemId - 1]

  # allow the user to modify or delete an item from their order.
  choice = display_menu(["1. Edit", "2. Delete"])
  if choice == 1:
    if 'milk' in item or 'sugar' in item:
      coffeeType = display_menu(COFFEE_TYPE_OPTIONS)
      milkAmount = int(display_menu(MILK_OPTIONS))
      sugarAmount = int(display_menu(SUGAR_OPTIONS))
      item = {
          'type': 'HOT' if coffeeType == 1 else 'ICED',
          'milk': milkAmount,
          'sugar': sugarAmount
      }
    else:
      sandwichType = display_menu(SANDWICH_TYPE_OPTIONS)
      item = {
          'type':
          'Grilled Pork Sandwich'
          if sandwichType == 1 else 'Shredded Chicken Sandwich'
      }
    orderList[itemId - 1] = item
    print(f"Your changes to item {itemId} have been saved.")
    checkout(orderList)
  else:
    del orderList[itemId - 1]
    if len(orderList) == 0:
      choice = get_valid_input(NO_ITEMS_LEFT_PROMPT, is_yes_no=True)
      if choice == "y":
        main()
      else:
        print(SEE_YOU_MSG)
        print(END_LINE)
        exit()
    else:
      print(f"The item {itemId} has been deleted.")
      checkout(orderList)


# Function to save the order to a file.
# create a unique order ID
# write the order details to a text file.
def save_to_file(orderList):
  orderID = generate_order_id()
  with open(f"orders_{orderID}.txt", "w") as file:
    file.write(orderID + '\n')
    for item in orderList:
      item_type = "coffee" if "milk" in item or "sugar" in item else "sandwich"
      item_with_type = {'item': item_type, **item}
      file.write(str(item_with_type) + '\n')


# Function to generate a unique order ID.
# combine the current date with a sequence number based on existing order files.
def generate_order_id():
  currentDate = datetime.datetime.now().strftime('%Y%m%d')
  order_files = [f for f in os.listdir() if f.startswith("orders_")]
  orderNumber = len(order_files) + 1
  return currentDate + "-" + str(orderNumber)
