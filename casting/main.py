# Do not modify these lines
__winc_id__ = "62311a1767294e058dc13c953e8690a4"
__human_name__ = "casting"

# Add your code after this line

leek_price = 2
print("Leek is " + str(leek_price) + " euro per kilo.")
order_leeks = "leek 4"
number_order_leeks = int(order_leeks[order_leeks.find("4")])
sum_total = leek_price * number_order_leeks
print(sum_total)

broccoli_price = 2.34
order_broccoli = "broccoli 1.6"
number_order_broccoli = float(order_broccoli[order_broccoli.find("1.6") :])
total_price = round(broccoli_price * number_order_broccoli, 2)
print(str(number_order_broccoli) + "kg broccoli costs " + str(total_price) + "e")
