# name: str = input("Enter your name: ")
# print(f"WITAJ {name}")

data_of_users: list = [
    {'name': 'Julia', 'surname': 'Szklarzewska', 'posts': 5, 'Location': 'Hajnówka'},
    {'name': 'Norbert', 'surname': 'Szeliga', 'posts': 15, 'Location': 'Rzeszów'},
    {'name': 'Kacper', 'surname': 'Wójcik', 'posts': 8, 'Location': 'Legnica'},
    {'name': 'Sebastian', 'surname': 'Wątroba', 'posts': 12, 'Location': 'Siedlce'},
]
print(f'Witaj {data_of_users[0]['name']}')


def read(users: list) -> None:
    ''''
    show users from an list
    :param users: a list of users
    :return: None
    '''
    for user in users[1:]:
        print(f"Twój znajomy:  {user['name']},opublikował: {user['posts']}")


read(data_of_users)


def add_user(users: list) -> None:
    """
    add user to a list
    :param users: user list
    :return: None
    """""
    name: str=input("Enter your name: ")
    surname:str=input("Enter your surname: ")
    posts:int=int(input("Enter your number of posts: "))
    location:str=input("Enter your location: ")
    new_user: dict={'name': name, 'surname': surname, 'posts': posts, 'Location': location}
    users.append(new_user)

    # add_user(data_of_users)
    # read(data_of_users)
    def delete_user(users: list) -> None:
    name: str=input("Enter name of user to remowe: ")
    for user in users:
        if user['name']==name:
        users.remove(user)
        read(data_of_users)
        read(users)

delete_user(data_of_users)
read(data_of_users)


