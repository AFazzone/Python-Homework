subtotal, gratuity_rate = eval(input("Enter the subtotal and the gratuity rate:"))
gratuity = subtotal * gratuity_rate/100
total = subtotal + gratuity
print("The gratuity is", int(gratuity * 100) / 100.0, "and the total is", int(total * 100)/100.0)