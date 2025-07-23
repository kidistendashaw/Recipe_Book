from recipe_manager import Recipe, RecipeBook


def print_menu():
    """A simple function to show the user their options."""
    print("\n--- Recipe Book Menu ---")
    print("1. Add a new recipe")
    print("2. Find a recipe")
    print("3. Delete a recipe")
    print("4.Exit")


def main():

    filename = "recipes.json"
    my_book = RecipeBook()
    my_book.load_from_file(filename)  # Load any saved recipes at the start

    while True:
        print_menu()
        choice = input("Enter your choice (1-4):")

        if choice == "1":
            name = input("Enter recipe name: ")
            ingredients_str = input("Enter ingredients (separated by a comma): ")
            ingredients = [item.strip() for item in ingredients_str.split(",")]
            instructions = input("Enter instructions: ")
            new_recipe = Recipe(name, ingredients, instructions)
            my_book.add_recipe(new_recipe)

        elif choice == "2":
            name = input("Enter the recipe name to find: ")
            recipe = my_book.find_recipe(name)
            if recipe:
                print(recipe)
            else:
                print("Recipe not found.")

        elif choice == "3":
            name = input("Enter the name of the recipe to delete:")
            my_book.delete_recipe(name)
        elif choice == "4":
            my_book.save_to_file(filename)
            print("Recipe saved.Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
