from recipeProcessor import RecipeProcessor
from recipeUI import RecipeUI


def main():
    r = RecipeProcessor()
    r.load_recipes('recipes.json')
    r.tabulate_recipes()
    recipes = r.get_recipes()
    j = RecipeUI()
    j.layout_ui(recipes)


main()
