class User:
  """
  A class representing a user with a name, password, email and friends.
  """

  def __init__(self, name: str, password: str, email: str, friends: list[str]):
    """
    Initializes a new User instance.

    Args:
      name: The name of the user (string).
      password: user's password (string).
      email: user's email
      friends: A list of people associated with the user (list of strings).
    """

    self.name = name
    self.password = password
    self.email= email
    self.friends = friends
# prints user details to the console

def PrintUser(user:User):
   print(f"username: {user.name}")
   print(f"userpassword: {user.password}")
   print(f"useremail: {user.email}")
   print(f"userfriends: {user.friends}")