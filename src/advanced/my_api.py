import json
import requests as req


def get_data(url):
    try:
        return req.get(url).text
    except Exception as ex:
        print(ex)


def load_data():
    data = get_data('https://randomuser.me/api')
    if not data is None:
        j = json.loads(data)
        first_name = j['results'][0]['name']['first']
        last_name = j['results'][0]['name']['last']
        email = j['results'][0]['email']

        print('First name: {}'.format(first_name))
        print('Last name: {}'.format(last_name))
        print('Email: {}'.format(email))


def main():
    load_data()


if __name__ == '__main__':
    main()
