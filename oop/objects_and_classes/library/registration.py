from library import Library
from user import User


class Registration:

    def add_user(self, user: User, library: Library):
        if user.user_id not in [x.user_id for x in library.user_records]:
            library.user_records.append(user)
        else:
            return f"User with id = {user.user_id} already registered in the library!"

    def remove_user(self, user: User, library: Library):
        if user.user_id not in [x.user_id for x in library.user_records]:
            return "We could not find such user to remove!"
        else:
            library.user_records.remove(user)

    def change_username(self, user_id: int, new_username: str, library: Library):
        for obj in library.user_records:
            if obj.user_id == user_id and obj.username != new_username:
                obj.username = new_username
                return f"Username successfully changed to: {new_username} for user id: {user_id}"
            elif obj.user_id == user_id and obj.username == new_username:
                return f"Please check again the provided username - it should be different than the username used so far!"
        else:
            return f"There is no user with id = {user_id}!"


if __name__ == "__main__":
    pass
