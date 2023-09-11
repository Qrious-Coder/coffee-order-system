# Import necessary constants, functions, and classes from the order_utils module.
from order_utils import (
    AFTER_SELECTION_MENU_OPTIONS,
    CANCEL_ORDER_MSG,
    CANCEL_PROMPT,
    COFFEE_ADDED_MSG,
    COFFEE_PRICE,
    COFFEE_PROMPT,
    COFFEE_TYPE_OPTIONS,
    EDIT_OPTIONS,
    END_LINE,
    INITIAL_MENU_OPTIONS,
    MILK_OPTIONS,
    NO_ITEMS_LEFT_PROMPT,
    ORDER_AGAIN_PROMPT,
    OTHER_ITEMS_PROMPT,
    SANDWICH_ADDED_MSG,
    SANDWICH_PRICE,
    SANDWICH_PROMPT,
    SANDWICH_TYPE_OPTIONS,
    SEE_YOU_MSG,
    SUGAR_OPTIONS,
    TAILOR_PROMPT,
    THANK_YOU_MSG,
    WELCOME_MSG,
    LargeOrderException,
    add_coffee,
    add_sandwich,
    checkout,
    display_menu,
    edit_item,
    generate_order_id,
    get_order_quantity,
    get_valid_input,
    save_to_file,
)

# Initialize an empty list to store the user's orders.
orderList = []


# Main function.
def main():
  # Access the global orderList variable.
  global orderList

  # Display the welcome message.
  print(WELCOME_MSG)

  # Start an infinite loop to continuously prompt the user for their choices.
  while True:
    # If the order list is empty, display the initial menu options.
    if len(orderList) == 0:
      choice = display_menu(INITIAL_MENU_OPTIONS)
    # If there are items in the order list, display the subsequent menu options.
    else:
      choice = display_menu(AFTER_SELECTION_MENU_OPTIONS)

    # If the user chooses to add coffee.
    if choice == 1:
      orderList, add_more = add_coffee(orderList)
      # If the user doesn't want to add more items, break out of the loop.
      if not add_more:
        break
    # If the user chooses to add a sandwich.
    elif choice == 2:
      orderList, add_more = add_sandwich(orderList)
      # If the user doesn't want to add more items, break out of the loop.
      if not add_more:
        break
    # If the user chooses not to order at this time.
    elif choice == 3:
      # If the order list is empty, display a goodbye message and exit.
      if len(orderList) == 0:
        print(SEE_YOU_MSG)
        return
      # If there are items in the order list, proceed to checkout.
      else:
        result = checkout(orderList)
        # Clear the order list after checkout.
        orderList = []
        # If the result is 'exit', user has completed order, exit the main function.
        if result == 'exit':
          return
        # If the result is True, continue to loop back to main menu for other items
        elif result:
          continue
        # If the result is False, user cancel the order, break out of the loop.
        else:
          break

  # If there are items in the order list, display the review of the items ordered.
  if len(orderList) > 0:
    checkout(orderList)


# If this script is being run as the main program, execute the main function.
if __name__ == "__main__":
  main()
