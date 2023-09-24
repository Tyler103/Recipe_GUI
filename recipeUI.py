from ezgraphics import GraphicsImage, GraphicsWindow


class RecipeUI:

    def __init__(self, w=950, h=1200):
        self._width = w
        self._height = h
        self._gap = 20
        self._num_pictures = 20
        self._max_width = 950
        self._win = None
        self._canvas = None

        self.set_up_window()

    def set_up_window(self):
        self._win = GraphicsWindow(self._width, self._height)
        self._canvas = self._win.canvas()
        self._win.setTitle("Tyler Ton's Recipe Viewer")

    def layout_ui(self, recipes):

        x = self._gap
        y = self._gap

        max_y = 0

        image = recipes[0].get_image()
        first_image = recipes[0]
        pic = GraphicsImage(image)
        self._canvas.drawImage(x, y, pic)
        self.show_recipe_desc(first_image, x, y + pic.height())

        for recipe in recipes[1:16]:
            max_y = max(max_y, pic.height())
            previous = pic
            filename = recipe.get_image()
            pic = GraphicsImage(filename)
            x = x + previous.width() + self._gap

            if x + pic.width() < self._max_width:
                self._canvas.drawImage(x, y, pic)
                self.show_recipe_desc(recipe, x, y + pic.height())

            else:
                x = self._gap
                y = y + max_y + self._gap + 35
                self._canvas.drawImage(x, y, pic)
                self.show_recipe_desc(recipe, x, y + pic.height())

        self._win.wait()

    def show_recipe_desc(self, recipe, x, y):
        desc = ""
        desc += "Name: " + recipe.get_name()[:25] + "\n"
        desc += "Prep Time: " + recipe.get_prep_time() + "\n"
        desc += "Cook Time: " + recipe.get_cook_time() + "\n"
        self._canvas.drawText(x, y, desc)

