"""
Script to pull down all publically available NYC housing data.

Naming conventions changed over the years, so this is taken into account.
"""
#import pycurl

import subprocess as sp

boros = ["manhattan", "bronx", "brooklyn", "queens", "si"]
years = ["0" + str(num) for num in range(3,7)]

boros2 = ["manhattan", "bronx", "brooklyn", "queens", "statenisland"]
years2 = ["2007"]
years3 = ["2008"]
years4 = ["2009"]
years5 = [str(num) for num in range(2009, 2013)]

name_template = "20{year}_{boro}.xls"
name_template2 = "{year}_{boro}.xls"

url_template = "http://www.nyc.gov/html/dof/downloads/sales_{boro}_{year}.xls"
url_template2 = "http://www.nyc.gov/html/dof/downloads/excel/rolling_sales/sales_{year}_{boro}.xls"
url_template3 = "http://www.nyc.gov/html/dof/downloads/pdf/09pdf/rolling_sales/sales_{year}_{boro}.xls"
url_template4 = "http://www.nyc.gov/html/dof/downloads/pdf/rolling_sales/annualized%20sales/{year}_{boro}.xls"
url_template5 = "http://www.nyc.gov/html/dof/downloads/pdf/rolling_sales/annualized%20sales/{year}/{year}_{boro}.xls"

for boro in boros:
    for year in years:
        url = url_template.format(boro=boro, year=year)
        name = name_template.format(boro=boro, year=year)
        print url
        sp.call(['curl', '-o', name, url])

for boro in boros2:
    for year in years2:
        url = url_template2.format(boro=boro, year=year)
        name = name_template2.format(boro=boro, year=year)
        print url
        sp.call(['curl', '-o', name, url])
    for year in years3:
        url = url_template3.format(boro=boro, year=year)
        name = name_template2.format(boro=boro, year=year)
        print url
        sp.call(['curl', '-o', name, url])
    for year in years4:
        url = url_template4.format(boro=boro, year=year)
        name = name_template2.format(boro=boro, year=year)
        print url
        sp.call(['curl', '-o', name, url])
    for year in years5:
        url = url_template5.format(boro=boro, year=year)
        name = name_template2.format(boro=boro, year=year)
        print url
        sp.call(['curl', '-o', name, url])

