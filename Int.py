{\rtf1\ansi\ansicpg936\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 .AppleSystemUIFontMonospaced-Regular;\f1\fnil\fcharset0 HelveticaNeue;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab560
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # inventory management prototype
\fs34 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f1\fs26 \cf0 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f0\fs24 \cf0 inventory = \{
\fs34 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f1\fs26 \cf0 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f0\fs24 \cf0     "A": 20,
\fs34 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f1\fs26 \cf0 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f0\fs24 \cf0     "B": 15,
\fs34 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f1\fs26 \cf0 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f0\fs24 \cf0     "C": 30,
\fs34 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f1\fs26 \cf0 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f0\fs24 \cf0     "D": 25,
\fs34 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f1\fs26 \cf0 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f0\fs24 \cf0     "E": 10
\fs34 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f1\fs26 \cf0 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f0\fs24 \cf0 \}
\fs34 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f1\fs26 \cf0 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f0\fs24 \cf0 def show_inventory():
\fs34 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f1\fs26 \cf0 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f0\fs24 \cf0     print("\\nCurrent Inventory")
\fs34 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f1\fs26 \cf0 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f0\fs24 \cf0     print("-----------------")
\fs34 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f1\fs26 \cf0 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f0\fs24 \cf0     for product, quantity in inventory.items():
\fs34 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f1\fs26 \cf0 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f0\fs24 \cf0         print(product + ":", quantity)
\fs34 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f1\fs26 \cf0 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f0\fs24 \cf0 def process_order():
\fs34 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f1\fs26 \cf0 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f0\fs24 \cf0     product = input("\\nEnter product (A-E): ").upper()
\fs34 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f1\fs26 \cf0 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f0\fs24 \cf0     if product not in inventory:
\fs34 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f1\fs26 \cf0 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f0\fs24 \cf0         print("Product does not exist.")
\fs34 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f1\fs26 \cf0 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f0\fs24 \cf0         return
\fs34 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f1\fs26 \cf0 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f0\fs24 \cf0     try:
\fs34 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f1\fs26 \cf0 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f0\fs24 \cf0         quantity = int(input("Enter quantity: "))
\fs34 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f1\fs26 \cf0 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f0\fs24 \cf0     except ValueError:
\fs34 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f1\fs26 \cf0 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f0\fs24 \cf0         print("Please enter a number.")
\fs34 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f1\fs26 \cf0 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f0\fs24 \cf0         return
\fs34 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f1\fs26 \cf0 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f0\fs24 \cf0     if quantity <= 0:
\fs34 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f1\fs26 \cf0 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f0\fs24 \cf0         print("Quantity must be greater than 0.")
\fs34 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f1\fs26 \cf0 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f0\fs24 \cf0         return
\fs34 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f1\fs26 \cf0 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f0\fs24 \cf0     if quantity > inventory[product]:
\fs34 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f1\fs26 \cf0 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f0\fs24 \cf0         print("Insufficient stock.")
\fs34 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f1\fs26 \cf0 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f0\fs24 \cf0         print("Available:", inventory[product])
\fs34 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f1\fs26 \cf0 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f0\fs24 \cf0         return
\fs34 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f1\fs26 \cf0 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f0\fs24 \cf0     inventory[product] = inventory[product] - quantity
\fs34 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f1\fs26 \cf0 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f0\fs24 \cf0     print("\\nOrder accepted.")
\fs34 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f1\fs26 \cf0 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f0\fs24 \cf0     print("Product:", product)
\fs34 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f1\fs26 \cf0 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f0\fs24 \cf0     print("Quantity:", quantity)
\fs34 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f1\fs26 \cf0 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f0\fs24 \cf0     print("Remaining stock:", inventory[product])
\fs34 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f1\fs26 \cf0 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f0\fs24 \cf0 print("Inventory Management System")
\fs34 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f1\fs26 \cf0 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f0\fs24 \cf0 show_inventory()
\fs34 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f1\fs26 \cf0 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f0\fs24 \cf0 while True:
\fs34 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f1\fs26 \cf0 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f0\fs24 \cf0     process_order()
\fs34 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f1\fs26 \cf0 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f0\fs24 \cf0     show_inventory()
\fs34 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f1\fs26 \cf0 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f0\fs24 \cf0     again = input("\\nProcess another order? (Y/N): ").upper()
\fs34 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f1\fs26 \cf0 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f0\fs24 \cf0     if again != "Y":
\fs34 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f1\fs26 \cf0 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f0\fs24 \cf0         break
\fs34 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f1\fs26 \cf0 \
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f0\fs24 \cf0 print("\\nProgram finished.")\
}