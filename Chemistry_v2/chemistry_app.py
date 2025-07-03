import random

class ChemApp:
    def __init__(self):
        from elements import elements
        self.elements = elements
        self.current_element = ""

        self.set_random_element()


    def set_random_element(self):
        """Gets a random key from classes own chemistry element dictionary
        and returns it"""
        keys = list(self.elements.keys())
        self.current_element = random.choice(keys)

    def delete_current_element(self):
        """Deletes entry from dictionary using the key set to
        current element"""
        self.elements.pop(self.current_element)




test_app = ChemApp()

