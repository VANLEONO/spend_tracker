from entities.category.model import Category

categories = ['Groceries', 'Utilities', 'Car']

default_categories = [Category(title=category) for category in categories]