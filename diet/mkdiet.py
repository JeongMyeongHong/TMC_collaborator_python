from context.domains import *


class MakeDiet(Reader):
    def __init__(self):
        self.file = File(context='./data/')

    def read_recipe(self):
        file = self.file
        file.fname = 'recipe_2mil_test_0'
        recipe = self.json(file)
        print(recipe.head(20))


if __name__ == '__main__':
    md = MakeDiet()
    md.read_recipe()
