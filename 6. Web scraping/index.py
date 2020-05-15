import requests
import urllib
from bs4 import BeautifulSoup

def run():
    for i in range(1, 6):
        response = requests.get('https://xkcd.com/{}'.format(i))
        soup = BeautifulSoup(response.content, 'html.parser')
        image_container = soup.find(id='comic')

        image_url = image_container.find('img')['src']
        image_name = image_url.split('/')[-1]
        print('\n\nDescargando imagen: \t{}'.format(image_name))
        urllib.request.urlretrieve('https:{}'.format(image_url), image_name)
        input('\tPresiona una tecla para descargar la siguiente imagen ...')
        
if __name__ == '__main__':
    run()