import requests


def terminal_weather(locations):
    url_template = 'https://wttr.in{}'

    for location in locations:
        url = url_template.format('/' + location + '?lang=ru&M&n&q&T')

        response = requests.get(url)
        response.raise_for_status()

        print(response.text)


def main():
    places = ['Лондон', 'svo', 'Череповец']

    terminal_weather(places)


if __name__ == '__main__':
    main()
