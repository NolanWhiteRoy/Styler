# imports
import json
import random
import weather
import re

#Capitalize first letter of input since they are proper pronouns
print("Enter your Country: ")
country_input = input()
print("Enter your State/Province: ")
state_input = input()
print("Enter your City: ")
city_input = input()
list_values = weather.weather_info(country_input, state_input, city_input)

#store values from the openweathermapapi
temperature = list_values[0]
wind_value = list_values[1]
weather_id = list_values[2]
report = list_values[3]
feels_like = list_values[4]

print(f"{city_input:-^30}")
print(f"Temperature: {temperature}°C")
print(f"Feels Like: {feels_like}°C")
print(f"Wind: {wind_value}")
print(f"Weather Report: {report}")

#determine if weather is good or bad
if 800 <= weather_id <= 802 and temperature >= 18:
    weather_status = "good"
else:
    weather_status = "bad"

style = ""
is_setup = False
top = ""
bottom = ""
accessory = ""
count = ""

# def print results
def print_result(obj):
    global top, bottom, accessory
    print("\n")
    if weather_status == "good":
        top = random.choice(obj.list_good_colours) + " " + random.choice(obj.list_good_tops)
        print("Your tops choice will be " + top + ".")
        bottom = random.choice(obj.list_good_colours) + " " + random.choice(obj.list_good_bottoms)
        print("Your bottom choice will be " + bottom + ".")
        accessory = random.choice(obj.list_good_colours) + " " + random.choice(obj.list_good_accessories)
        print("Accessorize with a " + accessory + "." + "\n")
    elif weather_status == "bad":
        top = random.choice(obj.list_bad_colours) + " " + random.choice(obj.list_bad_tops)
        print("Your top choice is " + top + ".")
        bottom = random.choice(obj.list_bad_colours) + " " + random.choice(obj.list_bad_bottoms)
        print("Your bottom choice is " + bottom + ".")
        accessory = random.choice(obj.list_bad_colours) + " " + random.choice(obj.list_bad_accessories)
        print("Accessorize with a " + accessory + "." + "\n")

    else:
        print("Please enter valid inputs.")


def setup_var():
    global style, is_setup
    string = input("What style you want? Choose from sporty, vintage, professional, casual, and streetwear! \n");
    styles = ["sporty", "vintage", "professional", "casual", "streetwear"]

    list_description = re.findall("[A-z]+", string)

    for each in list_description:
        each = each.lower()
        if each in styles:
            style = each
        else:
            print("Please enter valid strings")
            return 0

    is_setup = True


# data:
class sporty():
    list_good_accessories = ["ball cap", "sweatband"]
    list_bad_accessories = ["baselayer", "running jacket"]

    list_good_bottoms = ["training shorts"]
    list_bad_bottoms = ["joggers"]

    list_good_tops = ["t-shirt", "tank top/cutoff"]
    list_bad_tops = ["gym hoodie", "quarter-zip"]

    list_good_colours = ["neon pink", "lime", "aqua", "white"]
    list_bad_colours = ["forest green", "steel grey", "black", "blue grey"]


class vintage():
    list_good_accessories = ["rounded sunglasses", "hair scarf/fedora"]
    list_bad_accessories = ["jean jacket", "tweed jacket"]

    list_good_bottoms = ["skirt/5 inch inseam shorts", "jean shorts"]
    list_bad_bottoms = ["flair jeans", "pleated pants"]

    list_good_tops = ["camp shirt", "western shirt"]
    list_bad_tops = ["rugby shirt", "cotton blouse/button up"]

    list_good_colours = ["light green", "yellow", "light blue", "grey"]
    list_bad_colours = ["brown", "burnt orange", "tan", "teal", "burgundy"]


class professional():
    list_good_accessories = ["watch", "handbag/briefcase"]
    list_bad_accessories = ["overcoat", "umbrella", "blazer"]

    list_good_bottoms = ["khakis", "dress pants/skirt", "Tweed Pants"]
    list_bad_bottoms = ["khakis", "dress pants/skirt", "Tweed Pants"]

    list_good_tops = ["dress shirt/blouse"]
    list_bad_tops = ["dress shirt/blouse"]

    list_good_colours = ["tan", "white", "light blue", "light grey"]
    list_bad_colours = ["charcoal grey", "black", "white", "navy blue"]


class casual():
    list_good_accessories = ["sun glasses", "bucket hat"]
    list_bad_accessories = ["beanie"]

    list_good_bottoms = ["shorts"]
    list_bad_bottoms = ["jeans", "joggers/leggings"]

    list_good_tops = ["graphic tee"]
    list_bad_tops = ["pullover", "hoodie"]

    list_good_colours = ["white", "light blue", "peach", "tan"]
    list_bad_colours = ["grey", "black", "blue", "green", "red"]


class streetwear():
    list_good_accessories = ["flat brimmed hat", "fanny pack"]
    list_bad_accessories = ["puffy coat", "jean jacket"]

    list_good_bottoms = ["baggy/biker shorts"]
    list_bad_bottoms = ["cargo pants", "ripped jeans"]

    list_good_tops = ["oversized t-shirt"]
    list_bad_tops = ["oversized hoodie"]

    list_good_colours = ["white", "purple", "yellow", "light green", "teal"]
    list_bad_colours = ["black", "white", "red", "forest green", "blue"]



def save_outfit():
    global count
    path1 = "number_outfits.json"
    with open(path1, 'r') as f:
        data = json.load(f)
        count = data["count"]
        temp_value = int(count) + 1
    append = {"count": str(temp_value)}
    data.update(append)
    with open(path1, 'w') as f:
        json.dump(data, f, indent=4)

    path = "saved_outfits.json"
    with open(path, 'r') as f:
        data = json.load(f)
    outfit = "Outfit " + str(count)
    append = {outfit: {"Top": top, "Bottom": bottom, "Accessory": accessory}}
    data.update(append)
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)
    print("Outfit Saved!")


# insert Code
is_going = True
while is_going:

    style = ""
    is_setup = False
    while not is_setup:
        setup_var()

    if style == "sporty":

        a = sporty()
        print_result(a)

    elif style == "vintage":
        a = vintage()
        print_result(a)

    elif style == "professional":
        a = professional()
        print_result(a)

    elif style == "casual":
        a = casual()
        print_result(a)

    elif style == "streetwear":
        a = streetwear()
        print_result(a)

#choices for user when outfit generated
    choice = input("Going again? Type 2 to save your outfit and end the code, type 1 to go again, and type 0 to end the code.\n")
    if choice == "1":
        is_going = True
    elif choice == "0":
        is_going = False
        break
    elif choice == "2":
        save_outfit()
        is_going = False
        break