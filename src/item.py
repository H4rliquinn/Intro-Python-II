class Item():
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

    def on_take(self):
        print(f'You have picked up {self.name}')

    def on_drop(self):
        print(f'You have dropped the {self.name}')
