# name: str = input("Enter your name: ")
# print(f"WITAJ {name}")

data_of_users: list = [
    {'name': 'Julia', 'surname': 'Szklarzewska', 'posts': 5, 'Location': 'Hajnówka'},
    {'name': 'Norbert', 'surname': 'Szeliga', 'posts': 15, 'Location': 'Rzeszów'},
    {'name': 'Kacper', 'surname': 'Wójcik', 'posts': 8, 'Location': 'Legnica'},
    {'name': 'Sebastian', 'surname': 'Wątroba', 'posts': 12, 'Location': 'Siedlce'},
]
print(f'Witaj {data_of_users[0]['name']}')
def read(users:list)->None:
    ''''
    this is a function to show users from an list
    :param users: a list of users
    :return: None
    '''
    for user in users[1:]:
        print(f"Twój znajomy:  {user['name']},opublikował: {user['posts']}")

read(data_of_users)