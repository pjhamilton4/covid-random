import datetime
import requests
from bs4 import BeautifulSoup

from prettytable import PrettyTable


def run():
    website_url = requests.get("https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data").text

    soup = BeautifulSoup(website_url, features="html.parser")
    covid_table = soup.find(id='thetable')
    table_out = parse_table(covid_table)

    print(table_out)

    t = PrettyTable()

    print(t)


def parse_table(table):
    head_body = {'head':[], 'body':[]}
    for tr in table.select('tr'):
        if all(t.name == 'th' for t in tr.find_all(recursive=False)):
            head_body['head'] += [tr]
        else:
            head_body['body'] += [tr]
    return head_body

if __name__ == '__main__':
    run()
