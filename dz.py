def read_recipes(filename):
    cook_book = {}
    with open(filename, 'r') as file:
        recipe_name = ""
        ingredients_list = []
        for line in file:
            line = line.strip()
            if line:
                if not recipe_name:
                    recipe_name = line
                elif not ingredients_list:
                    ingredients_count = int(line)
                else:
                    ingredient_name, quantity, measure = line.split(" | ")
                    ingredients_list.append({
                        "ingredient_name": ingredient_name,
                        "quantity": int(quantity),
                        "measure": measure
                    })
                    if len(ingredients_list) == ingredients_count:
                        cook_book[recipe_name] = ingredients_list
                        recipe_name = ""
                        ingredients_list = []
    return cook_book

filename = "recipes.txt"
recipes = read_recipes(filename)
print(recipes)
