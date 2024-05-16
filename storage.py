import json

class JSONStorage:
    def __init__(self, filename):
        """
        Initializes a JSONStorage object with the specified filename.

        Args:
            filename (str): The name of the JSON file to read from or write to.

        Returns:
            None
        """
        self.filename = filename

    def save_data(self, data):
        """
        Saves data to the JSON file.

        Args:
            data (list or dict): The data to be saved.

        Returns:
            None
        """
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)

    def load_data(self):
        """
        Loads data from the JSON file.

        Returns:
            list or dict: The loaded data, or None if the file is not found.
        """
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return None
