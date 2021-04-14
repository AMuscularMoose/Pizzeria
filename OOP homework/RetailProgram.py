import RetailClass as r


def main():
    print(
        "\t\t" + "Description" + "\t\t" + "Units in Inventory" + "\t\t" + "Price" + "\n"
    )

    item_desc = input("What is the item description? ")
    unit_inv = int(input("What is the number of units on hand? "))
    price = float(input("What is the price of the item? "))
    retail_item = r.Retail(item_desc, unit_inv, price)
    print(retail_item)

    item_desc = input("What is the item description? ")
    unit_inv = int(input("What is the number of units on hand? "))
    price = float(input("What is the price of the item? "))
    retail_item = r.Retail(item_desc, unit_inv, price)
    print(retail_item)

    item_desc = input("What is the item description? ")
    unit_inv = int(input("What is the number of units on hand? "))
    price = float(input("What is the price of the item? "))
    retail_item = r.Retail(item_desc, unit_inv, price)
    print(retail_item)


main()