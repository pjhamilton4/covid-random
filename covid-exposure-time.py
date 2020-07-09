import datetime

from prettytable import PrettyTable

date_of_exposure = datetime.datetime(2020, 7, 2)


def run():
    txt = input("Enter date of first exposure (MM/DD/YYYY):")
    month, day, year = map(int, txt.split('/'))
    date1 = datetime.date(year, month, day)
    end_days_out = 0
    txt = input("Do you have a known last exposure date? (Y/N)")
    if txt == "Y" or txt == "y":
        txt = input("Enter date of last exposure (MM/DD/YYYY)")
        month, day, year = map(int, txt.split('/'))
        date2 = datetime.date(year, month, day)
        end_days_out = (date2 - date1).days + 1
    else:
        print("Using +3 days as end exposure date")
        end_days_out = 4

    dates = []
    for x in range(0, end_days_out):
        temp_date = (date_of_exposure + datetime.timedelta(days=x))
        dates.append(temp_date)

    dates_header = list(map(lambda x: x.strftime("%m/%d/%Y"), dates))
    dates_header.insert(0, "Days Since")

    t = PrettyTable(dates_header)

    rows = []
    for x in range(3, 16):
        row = [str(x)]
        for date in dates:
            temp_date = date + datetime.timedelta(days=x)
            row.append(temp_date.strftime("%m/%d/%Y"))
        t.add_row(row)

    print(t)


if __name__ == '__main__':
    run()

