import requests


def get_terminal_weather(location):
    url_template = 'https://wttr.in{}'
    payload = {'lang': 'ru',
               'M': '',
               'n': '',
               'q': '',
               'T': ''}

    url = url_template.format('/' + location)

    response = requests.get(url, params=payload)
    response.raise_for_status()

    return response.text


def main():
    places = ['Лондон', 'svo', 'Череповец']

    for place in places:
        print(get_terminal_weather(place))


if __name__ == '__main__':
    main()
