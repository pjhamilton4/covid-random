import datetime
import requests
from bs4 import BeautifulSoup

from prettytable import PrettyTable


def run():
    website_url = requests.get("https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data").text

    soup = BeautifulSoup(website_url, features="html.parser")
    covid_table = soup.find(id='thetable')
    table_out = parse_table(covid_table,limit_body=False)

    t = PrettyTable()

    t.field_names = list(table_out['head'])[0:3]
    # for some reason the "world" is in the header on wikipedia, need to find a better way to handle.
    t.add_row(list(table_out['head'])[3:6])

    for row in table_out['body'][:-1]:
        t.add_row(row)

    print(t)


def parse_table(table, limit_body=True, limit_size=15):
    head_body = {'head':[], 'body':[]}
    for index, tr in enumerate(table.select('tr')):
        [s.extract() for s in tr([ 'sup', 'div', 'abbr', 'img'])]
        if all(t.name == 'th' for t in tr.find_all(recursive=False)):
            for tag in tr.find_all('th'):
                if tag.getText().strip():
                    head_body['head'] += [tag.getText().strip()]
                    # print(tag.getText().strip())
        else:
            if limit_body is True:
                if index >= limit_size:
                    break
                else:
                    process_body(head_body, tr)
            else:
                process_body(head_body, tr)
    return head_body


def process_body(head_body, tr):
    temp_row = []
    anchor = tr.find('a')
    if anchor:
        temp_row.append(anchor.getText())
    temp_data = tr.find_all('td')
    temp_row.append(temp_data[0].getText().strip())
    try:
        temp_row.append(temp_data[1].getText().strip())
    except:
        temp_row.append("-")
    # print("TEMP DATA:", temp_row)
    head_body['body'] += [temp_row]
    # head_body['body'] += [tag.getText().strip()]


if __name__ == '__main__':
    run()
