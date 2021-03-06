DROP TABLE sales;
CREATE TABLE sales (
    Borough ENUM('Manhattan', 'Bronx', 'Brooklyn', 'Queens', 'Staten Island'), 
    Neighborhood VARCHAR(80),
    BuildingClassCategory VARCHAR(80),
    TaxClassAtPresent VARCHAR(80),
    Block INT,
    Lot INT,
    Easment VARCHAR(80),
    BuildingClassAtPresent VARCHAR(80),
    Address VARCHAR(360),
    ApartmentNumber VARCHAR(80),
    ZipCode INT,
    ResidentialUnits INT,
    CommercialUnits INT,
    TotalUnits INT,
    LandSquareFeet INT,
    GrossSquareFeet INT,
    YearBuilt INT,
    TaxClassAtTimeOfSale VARCHAR(80),
    BuildingClassAtTimeOfSale VARCHAR(80),
    SalePrice Int,
    SaleDate DATE,
    PRIMARY KEY (Borough, address, ApartmentNumber, SalePrice, SaleDate));

