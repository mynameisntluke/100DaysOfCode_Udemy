import random


class ChemApp:
    def __init__(self):
        from elements import elements
        self.elements = elements
        self.current_element_symbol = ""
        self.current_element_name = ""
        self.set_random_element()


    def set_random_element(self):
        """Gets a random key/value pair from the element dictionary and sets them to current element"""
        keys = list(self.elements.keys())
        self.current_element_symbol = random.choice(keys)
        self.current_element_name = self.elements[self.current_element_symbol]

    def delete_current_element(self):
        """Deletes entry from dictionary using the key set to
        current element"""
        self.elements.pop(self.current_element_symbol)

    def get_current_element_name(self):
        return self.current_element_name

    def get_current_element_symbol(self):
        return self.current_element_symbol

    def set_element_dict(self, n):
        """Reduces element list to the first n elements"""
        dict_reduced = {}
        keys_reduced = list(self.elements.keys())[:n]
        for key in keys_reduced:
            dict_reduced[key] = self.elements[key]
        self.elements = dict_reduced
