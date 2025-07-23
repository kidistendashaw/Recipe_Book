import json


class Recipe:
    def __init__(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

    def __str__(self):
        return (
            f"\n---- {self.name} ----\n"
            f"Ingredients: {', '.join(self.ingredients)}\n"
            f"Instructions: {self.instructions}"
        )


class RecipeBook:
    def __init__(self):
        self.recipes = {}

    def add_recipe(self, recipe):
        self.recipes[recipe.name] = recipe
        print(f"Added recipe: '{recipe.name}'")

    def find_recipe(self, name):
        return self.recipes.get(name)

    def delete_recipe(self, name):
        try:
            del self.recipes[name]
            print(f"Successfully deleted recipe: ' {name}")
        except KeyError:
            print(f"Error: Recipe '{name} not found and could not be deleted.")

    def save_to_file(self, filename):
        data_to_save = {}
        for name, recipe_obj in self.recipes.items():
            data_to_save[name] = {
                "ingredients": recipe_obj.ingredients,
                "instructions": recipe_obj.instructions,
            }

        with open(filename, "w") as file:
            json.dump(data_to_save, file, indent=4)
        print("Recipes saved to", filename)

    def load_from_file(self, filename):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                for name, recipe_data in data.items():
                    recipe = Recipe(
                        name, recipe_data["ingredients"], recipe_data["instructions"]
                    )
                    self.add_recipe(recipe)
        except FileNotFoundError:
            print("No save file found. Starting a new recipe book.")
        except json.JSONDecodeError:
            print("Could not read save file. Starting a new recipe book.")
