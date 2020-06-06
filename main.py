import requests

api_version = 5.107
username = ''
age_from = ''
age_to = ''


def get_main_info():
    global username, age_from, age_to
    print("Please, write full name")
    username = input()
    print("Please, write age from")
    age_from = input()
    print("Please, write age to")
    age_to = input()


if __name__ == '__main__':
    with open("token.txt", "r") as f_token:
        token = f_token.readline()
    get_main_info()
    response = requests.get('https://api.vk.com/method/users.search',
                            params={
                                'access_token': token,
                                'v': api_version,
                                'q': username,
                                'count': 10,
                                'age_from': age_from,
                                'age_to': age_to
                            })
    # print(response.content)
    try:
        users = response.json()['response']['items']
        for user in users:
            print('First name: {0}\n'
                  'Last name: {1}\n'
                  'Screen name: {2}\n'.format(user['first_name'], user['last_name'], user['screen_name']))
    except KeyError:
        print('Error on access token')
