products = ["Sankofa Foods", "Jamestown Coffee", "Bioko Chocolate", "Blue Skies Ice Cream", "Fair Afric Chocolate", "Kawa Moka Coffee", "Aphro Spirit", "Mensado Bissap", "Voltic"]

prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]

#print(prices)

#print(prices[0] + prices[1] + prices[2])

total_price = 0 
#print(total_price)
for price in prices:
    total_price = total_price + price
#    print(total_price, price)
average_total_price = round(total_price / len(prices), 2)
print(average_total_price)
print()



reduce_price = 5
new_price_list = []
for index in range(len(prices)):
    new_price = prices[index] - reduce_price
    new_price_list.append(new_price)
print(new_price_list)


total_revenue = 0
for index, price in enumerate(prices):
     product_revenue = prices[index] * last_week[index]
     total_revenue = total_revenue + product_revenue
print(total_revenue)


average_total_revenue = round(total_revenue / len(last_week), 2)
print(average_total_revenue)


cheap_products = [products for products, price in zip(products, new_price_list) if price < 30]
print(cheap_products)









