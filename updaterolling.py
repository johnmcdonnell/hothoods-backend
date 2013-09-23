
import subprocess as sp

boros = ["manhattan", "bronx", "brooklyn", "queens", "statenisland"]
url_template = "http://www.nyc.gov/html/dof/downloads/pdf/rolling_sales/rollingsales_{boro}.xls"
name_template = "housingsheets/rollingsales_{boro}.xls"

for boro in boros:
    url = url_template.format(boro=boro)
    name = name_template.format(boro=boro)
    sp.call(['curl', '-o', name, url])
