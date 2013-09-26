import os
from ReadExcel import ReadExcel
import MySQLdb

boroughcodes =  {
    1: 'Manhattan', 
    2: 'Bronx', 
    3: 'Brooklyn', 
    4: 'Queens', 
    5: 'Staten Island'}


with open("dbpassword") as passwdfile:
    dbpassword = passwdfile.read().strip()

db = MySQLdb.connect(user="mcdon", passwd=dbpassword, host="nycsales.ciiztqxgtuvl.us-west-2.rds.amazonaws.com", port=3306, db="prices")

insertion_query = """INSERT INTO sales
    (Borough, Neighborhood, BuildingClassCategory,
    TaxClassAtPresent, Block, Lot, Easment, BuildingClassAtPresent,
    Address, ApartmentNumber, ZipCode, ResidentialUnits, CommercialUnits,
    TotalUnits, LandSquareFeet, GrossSquareFeet,
    YearBuilt, TaxClassAtTimeOfSale,
    BuildingClassAtTimeOfSale, SalePrice, SaleDate)
    VALUES
        (%s,%s,%s,
        %s,%s,%s,%s,%s,
        %s,%s,%s,%s,%s,
        %s,%s,%s,
        %s,%s,
        %s,%s,%s)
    ON DUPLICATE KEY UPDATE Borough = Borough;
    """

sheetsdir = "housingsheets"
# Possibly missed file 5 (I think Queens 2012)
files = [os.path.join(sheetsdir, filename) for filename in os.listdir(sheetsdir)]

c = db.cursor()
for file in files:
    print "Reading in ", file
    try:
        workbook = ReadExcel(file)
        sheet = workbook.worksheets()[0]
        for row in workbook.getiter(sheet, returnlist=True):
            #print row
            try:
                row[0] = boroughcodes[row[0]]
                c.execute(insertion_query, row)
            except MySQLdb.IntegrityError as e:
                print e
                print "Integrity error inserting:", row
        db.commit()
    except e:
        print "Failed to read %s;" % file, e

#nrows = sheet.nrows-1
#ncols = sheet.ncols-1

#i = 0
#while 1:
#    if sheet.cell_value(i, ncols) :
#        break
#    else:
#        i+=1

