import asyncio
from inventory import Inventory
import copy


def display_catalogue(catalogue):
    burgers = catalogue["Burgers"]
    sides = catalogue["Sides"]
    drinks = catalogue["Drinks"]

    print("--------- Burgers -----------\n")
    for burger in burgers:
        item_id = burger["id"]
        name = burger["name"]
        price = burger["price"]
        print(f"{item_id}. {name} ${price}")

    print("\n---------- Sides ------------")
    for side in sides:
        sizes = sides[side]

        print(f"\n{side}")
        for size in sizes:
            item_id = size["id"]
            size_name = size["size"]
            price = size["price"]
            print(f"{item_id}. {size_name} ${price}")

    print("\n---------- Drinks ------------")
    for beverage in drinks:
        sizes = drinks[beverage]

        print(f"\n{beverage}")
        for size in sizes:
            item_id = size["id"]
            size_name = size["size"]
            price = size["price"]
            print(f"{item_id}. {size_name} ${price}")

    print("\n------------------------------\n")

async def user_order(): #function asks for IDs of items, and return the list of IDs
    print("Please enter the number of items that you would like to add to your order. Enter q to complete your order.")
    
    user_input = None
    user_order_dict = {} # id : quantity

    while user_input != "q":
        user_input = input("Enter an item number: ")
        if user_input == "q":
            break
        elif user_input.isdigit() == False:
            print("Please enter a valid ID Number.")
            continue
        if int(user_input) not in range(1, 21):
            print("Please enter a valid ID Number.")
            continue
        
        if int(user_input) in user_order_dict.keys():
            user_order_dict[int(user_input)] += 1
        else:
            user_order_dict[int(user_input)] = 1
    
    print("Placing order...")
    print()
    return user_order_dict

async def check_stock(order): #validates if if there is sufficient stock of the items in order

    # final_order = {}

    # for item in order:
    #     order_quantity = order[item]
    #     stock = await inventory.get_stock(item)

    #     if order_quantity > stock:
    #         if stock == 0:
    #             print(f"Unfortunately item number {item}, is out of stock and has been removed from your order. Sorry!")
    #             print()
    #             continue
    #         print(f"Unfortunately item number {item}, is out of stock. Sorry!")
    #         final_order[item] = stock
    #         print(f"Quantity of items has been changed to {stock}")
    #         print()
    #     else:
    #         final_order[item] = order_quantity

    # return final_order

    final_order = {}
    stock_check_dict = {}

    for item in order:
        stock_check_dict[item] = inventory.get_stock(item)
    
    result_list = list(stock_check_dict.values())

    await asyncio.gather(*result_list)

    for item in stock_check_dict:
        if stock_check_dict[item] == 0:
            if order[item] > stock_check_dict[item]:
                    print(f"Unfortunately item number {item}, is out of stock and has been removed from your order. Sorry!")
                    print()
                    continue
            print(f"Unfortunately item number {item}, is out of stock. Sorry!")
            final_order[item] = stock_check_dict[item]
            print(f"Quantity of items has been changed to {stock_check_dict[item]}")
            print()
        else:
            final_order[item] = order[item]

    return final_order

async def convert_order(order): #convert dicts {id:quantity} to list of full item dicts {id, size, price, quantity}

    result_list = []
    for id in order:
        if order[id] > 1:
            for j in range(order[id]):
                result_list.append(inventory.get_item(id))
        else:
            result_list.append(inventory.get_item(id))
    
    return await asyncio.gather(*result_list)

async def combo_combiner(order): #function to combine Combo from order items

    comboed_order = []
    burgers = []
    sides = []
    drinks = []
    
    for item in order:
        if item["category"] == "Burgers":
            burgers.append(item)
        if item["category"] == "Sides":
            sides.append(item)
        if item["category"] == "Drinks":
            drinks.append(item)

    #sorting Categories by price High to Low
    burgers = sorted(burgers, key=lambda d: d['price'], reverse = True)
    sides = sorted(sides, key=lambda d: d['price'], reverse = True)
    drinks = sorted(drinks, key=lambda d: d['price'], reverse = True)

    combo_count = min(len(burgers), len(sides), len(drinks))

    if len(burgers) and len(sides) and len(drinks) > 0:
        #Combo creating

        for combo_id in range(combo_count):

            burger = copy.copy(burgers.pop(0))
            burger["combo_id"] = combo_id + 1

            side = copy.copy(sides.pop(0))
            side["combo_id"] = combo_id + 1

            drink = copy.copy(drinks.pop(0))
            drink["combo_id"] = combo_id + 1

            comboed_order.append(burger)
            comboed_order.append(side)
            comboed_order.append(drink)

    not_in_combo = burgers + sides + drinks

    comboed_order += not_in_combo
    comboed_order = sorted(comboed_order, key=lambda d: ("combo_id" not in d, d.get("combo_id")))
    print()

    return comboed_order, combo_count

def summary(order, combo_count):   #printing out summary of the order

    if len(order) == 0:
        return

    print("Here is a summary of your order:\n")

    subtotal_price = 0

    for i in range(combo_count):  #printing combos
        combo = list(filter(lambda x: "combo_id" in x, order))
        combo = list(filter(lambda y: y["combo_id"] == i+1, combo))

        combo_price = 0

        for item in combo:
            combo_price += item["price"]*0.85

        print(f"&{round(combo_price, 2)} Burger Combo - regular price: {round(combo_price/0.85, 2)}")

        for j in combo:
            if j["category"] == "Burgers":
                print("   " + j["name"])
            else:
                print(f"   {j['size']} {j['subcategory']}")

        subtotal_price += combo_price

    not_combo_items = list(filter(lambda y: ("combo_id" not in y), order))

    for item in not_combo_items:
        if item["category"] == "Burgers":
            print(f"${item['price']} {item['name']}")
        else:
            print(f"${item['price']} {item['size']} {item['subcategory']}")
        subtotal_price += item['price']

    tax = subtotal_price*0.05
    total_price = subtotal_price + tax

    print(f"\nSubtotal: ${round(subtotal_price, 2)}")
    print(f"Tax: ${round(tax, 2)}")
    print(f"Total: ${round(total_price, 2)}")

    return order, round(total_price, 2)

async def order_loop():

    order = await user_order()

    order_1 = await check_stock(order)

    order_2 =  await convert_order(order_1)

    order_3, combo_count = await combo_combiner(order_2)

    summary_order, total_price = summary(order_3, combo_count)
    
    while True:

        user_purchase = input(f"Would you like to purchase this order for ${total_price} (yes/no)? ")

        if user_purchase == "yes":
            async_queue = []
            for item in summary_order:
                async_queue.append(inventory.decrement_stock(item["id"]))

            await asyncio.gather(*async_queue)
            print("Thank you for your order!")
            break

        elif user_purchase == "no":
            print("No problem, please come again!")
            break
        else:
            print("This is not a valid option.\n")
            continue



    while True:
        another_order = input("Would you like to make another order (yes/no)? ")

        if another_order == "yes":
            await order_loop()
            break
        elif another_order == "no":
            return
        else:
            print("This is not a valid option.\n")
            continue           

async def main():
    print("Welcome to the ProgrammingExpert Burger Bar!")
    print("Loading catalogue...")
    catalogue_task = asyncio.create_task(inventory.get_catalogue())
    await catalogue_task

    display_catalogue(catalogue_task.result())

    # order = await user_order()

    # order_1 = await check_stock(order)

    # order_2 =  await convert_order(order_1)

    # order_3, combo_count = await combo_combiner(order_2)

    # summary_1 = summary(order_3, combo_count)

    order_l = await order_loop()

    print("Goodbye!")

if __name__ == "__main__":
    global inventory
    inventory = Inventory()

    asyncio.run(main())
