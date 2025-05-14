spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"].lower() == cuisine.lower():
            return food
    return None

def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)

def get_average_heat_level(spicy_foods):
    if not spicy_foods:
        return 0
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    return int(total_heat / len(spicy_foods))

def create_spicy_food(spicy_foods, new_food):
    return spicy_foods + [new_food]

if __name__ == "__main__":
    spicy_foods_data = [
        {"name": "Green Curry", "cuisine": "Thai", "heat_level": 9},
        {"name": "Buffalo Wings", "cuisine": "American", "heat_level": 3},
        {"name": "Mapo Tofu", "cuisine": "Sichuan", "heat_level": 6},
    ]

    print("--- Get Names ---")
    print(get_names(spicy_foods_data))

    print("\n--- Get Spiciest Foods ---")
    print(get_spiciest_foods(spicy_foods_data))

    print("\n--- Print Spicy Foods ---")
    print_spicy_foods(spicy_foods_data)

    print("\n--- Get Spicy Food by Cuisine ---")
    print(get_spicy_food_by_cuisine(spicy_foods_data, "American"))
    print(get_spicy_food_by_cuisine(spicy_foods_data, "Thai"))

    print("\n--- Print Spiciest Foods (again) ---")
    print_spiciest_foods(spicy_foods_data)

    print("\n--- Get Average Heat Level ---")
    print(get_average_heat_level(spicy_foods_data))

    print("\n--- Create Spicy Food ---")
    new_food = {
        'name': 'Griot',
        'cuisine': 'Haitian',
        'heat_level': 10,
    }
    updated_foods = create_spicy_food(spicy_foods_data, new_food)
    print(updated_foods)
