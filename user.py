from models import User

class UserManager:
    def __init__(self, storage):
        """
        Initializes a UserManager object with the specified storage.

        Args:
            storage (JSONStorage): The storage object used to save and load user data.

        Returns:
            None
        """
        self.storage = storage
        self.users = []

    def add_user(self, name):
        """
        Adds a new user to the user list and saves it to the storage.

        Args:
            name (str): The name of the user.

        Returns:
            None
        """
        user = User(name)
        self.users.append(user)
        self._save_users()

    def _save_users(self):
        """
        Saves the user data to the storage in JSON format.

        Returns:
            None
        """
        data = [user.to_dict() for user in self.users]
        self.storage.save_data(data)

    def load_users(self):
        """
        Loads user data from the storage and populates the user list.

        Returns:
            None
        """
        data = self.storage.load_data()
        if data:
            self.users = [User.from_dict(item) for item in data]
