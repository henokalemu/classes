"""
    Pylab 5 Nov 2016
    "Doing Evil (statistical) work."

    We're going to be looking at the data behind this story and see if we can also make sweeping and probably wrong conclusions about nutrition-studies just like this article does.

    Story:
    http://fivethirtyeight.com/features/you-cant-trust-what-you-read-about-nutrition/

    Github data repo:
    https://github.com/fivethirtyeight/data/tree/master/nutrition-studies

    Class notes:

    Python3 required, python2 not guaranteed to work completely
    Internet connection required
    Text editor required

    Contact me:
    Nathan @nate_somewhere

    More learning resources at:
    https://github.com/ndanielsen/beginning-python
"""


import os
import csv

try:
    from urllib.request import urlretrieve
except ImportError as ex:
    from urllib import urlretrieve # python2 compability

url_csv = "https://raw.githubusercontent.com/fivethirtyeight/data/master/nutrition-studies/raw_anonymized_data.csv"
csv_filename = "raw_anonymized_data.csv"

def file_downloader(url, filename):
    """Downloads and names a file given a filename and download_url"""

    if not os.path.isfile(filename):
        urlretrieve(url, filename)
        print('File: %s downloaded' % filename)
    if os.path.isfile(filename):
        file_location = os.path.realpath(filename)
        print('File: %s is located: %s' % (filename, file_location))

if __name__ == '__main__':

    #### Hello world! #####
    # print('hello world!')

    #### after hello world, uncomment below
    # file_downloader(url_csv, csv_filename)

    total = 0
    smoke_counter = 0
    not_smoke_counter = 0

    energy_smoke = 0
    energy_not_smoke = 0

    with open(csv_filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            total += 1
            if row['currently_smoke'] == 'Yes':
                smoke_counter += 1
                energy_smoke += int(row['ENERGYDRINKSFREQ'])
            else:
                not_smoke_counter += 1
                energy_not_smoke += int(row['ENERGYDRINKSFREQ'])

    # print('*' * 25)
    # """In a recent fake health study involving %s participants
    # researchers learned found that
    #
    # """ % (total, )
    #
    # print(energy_smoke)
    # print(energy_not_smoke)
    #
    # print('*' * 25)

    from collections import Counter

    with open(csv_filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)

    c = Counter(row['heart_disease'] for row in data)

    print(c)
