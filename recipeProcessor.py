import json
from recipe import Recipe


class RecipeProcessor:

    def __init__(self):
        self._recipe_list = []

        self._name_list = []
        self._prep_list = []
        self._cook_list = []
        self._yield_list = []
        self._url_list = []

        self.max_size = 50

    def load_recipes(self, file, n=16):

        with open(file) as json_file:
            file_contents = json_file.read()
        parsed_json = json.loads(file_contents)

        count = 0
        max_bar_len = 50
        progress = ''
        green = f"\33[32m"
        remaining_bar = '░'
        remaining = ''
        bar = '█'

        for current_json in parsed_json[:self.max_size]:
            current_recipe = Recipe(current_json["name"], current_json["cookTime"],
                                    current_json["prepTime"], current_json["recipeYield"])

            url = current_json["image"]
            current_recipe.set_image(url)

            if count < max_bar_len:
                count += 1
                progress = bar * count
                remaining = max_bar_len - count
                print(f"\033[0mDownloading image {count} of 50   {green}{progress}{remaining * remaining_bar}",
                      end="\r")

            self._recipe_list.append(current_recipe)

            self._name_list.append(current_recipe.get_name())
            self._prep_list.append(current_recipe.get_prep_time())
            self._cook_list.append(current_recipe.get_cook_time())
            self._yield_list.append(current_recipe.get_recipe_yield())

    def get_recipes(self):
        return self._recipe_list

    def tabulate_recipes(self):
        print("\033[0m-" * 110)
        print("\033[0m{: <30}{: ^10}{:>30}{:>25}".format("Name", "|  Prep Time", "|  Cook Time", "|  Recipe Yield"))
        print('─' * 110)

        for n, p, c, r in zip(self._name_list, self._prep_list, self._cook_list, self._yield_list):
            print("\033[0m{:<30}|  {: <27}{:<22}{:<10}".format(n, p, "|  " + c, "|  " + r))

        return
