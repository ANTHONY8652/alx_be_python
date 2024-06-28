#ask for the user to input their current weather conditions
weather = input("What's the weather like today? (sunny/rainy/cold): ").strip().lower()
#print what happens if a certain weather condition is selected
#if weather is sunny print the user to wear a tshirt and sunglasses
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
#elif weather is rainy tell the user to wear an umbrella and raincoat
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
#else if it is cold tell the user to wear awarm coat and a scarf
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
#else print sorry i dont have recommendations for this weather
else:
    print("Sorry, I don't have recommendations for this weather.")
