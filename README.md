# Predicting Vacancy in Cleveland using NST Data

### What’s been done before?
As part of the IBM Smarter Cities Challenge, IBM worked with the city of Syracuse to:
identify indicators for factors contributing to the causes of property vacancy, 
integrate and analyze relevant data from disparate sources across a broad ecosystem of stakeholders, and 
develop a predictive, flexible model to show the impact various events or actions could have on a neighborhood's stability.

IBM drew from machine learning and data mining techniques in order to help identify “bubble” neighborhoods and individual vacant properties. Syracuse estimated that about 1,500 of their 35,000 residential parcels were vacant.

The data used in the Syracuse model can be separated into three main categories:
* physical parcel characteristics (length, depth, acreage) 
* building characteristics (# of bedrooms, bathrooms, fireplaces, code violations, taxable value)
* owner/renter characteristics (owner occupied, etc.)

### What’s different between Syracuse and Cleveland?
The biggest challenge in Syracuse was the collection of the data, which is largely already done in Cleveland, thanks to NST. Although filtering the data and building the model take time, those elements are not dependent on acquiring data from outside partners, which is often the most time consuming.

NST has traditionally been used on a case-by-case basis (looking at parcel histories), or getting a snapshot or trend of neighborhoods, as well as streamlining the data collection process. Using the data from NST to predict would be a novel use of NST and potentially unlock additional value in the data.

### Information about the algorithm
The algorithm used in the Syracuse study is referred to as a “random forest” model. Important to know is that this approach trades accuracy for interpretability, meaning that it bests traditional econometric approaches but does not lend itself as well in interpreting the effects that variables have on the outcome (vacancy). The model can be used to predict a binary outcome (vacant, not vacant), as well as the probability from 0 to 1 that a property is vacant. 

The model would be built off of Thriving Communities Institute surveys, so the model would effectively predict if a parcel is likely to be called vacant by a TCI survey, which we are assuming to be “true” vacant.

Lastly, this model can built with historical data in an attempt to predict whether a parcel is likely to become vacant in the future (e.g. 6 months from now.)

## Data processing

### Property data
Data from `main_prop.csv`. This file is **large** and was filtered to data from the year 2013 (most recent available in the dataset as far as I know).

* zip code
* property size
* pclass
* total usable area
* total market value
* condition
* housing style
* owner occupancy
* total number of buildings
* year built
* exterior wall type

### Demographic data
Data acquired through NEO CANDO 2010+ via Census. Using a file provided by Nina, matched parcel numbers to census tracts, and imputed missing data with median values.

* Vacant housing units, percent, 2012 5-yr est (ACS 2012 5-year)
* Median gross rent, number, 2012 5-yr est (ACS 2012 5-year)
* Property crimes, rate per 100,000 population, 2014 (Crime)
* Burglaries, rate per 100,000 population, 2014 (Crime)
* Other illicit drug violations, rate per 100,000 population, 2014 (Crime)
* Part I crimes, rate per 100,000 population, 2014 (Crime)
* Part II crimes, rate per 100,000 population, 2014 (Crime)
* Persons with bachelors degree or more, percent, 2012 5-yr est (ACS 2012 5-year)
* Poverty rate, 2012 5-yr est (ACS 2012 5-year)
* Median household income, 2012 5-yr est (ACS 2012 5-year)
* White, percent, 2012 5-yr est (ACS 2012 5-year)
* Black, percent, 2012 5-yr est (ACS 2012 5-year)
* Asian/Pac Islander, percent, 2012 5-yr est (ACS 2012 5-year)
* Other race, percent, 2012 5-yr est (ACS 2012 5-year)
* Hispanic, percent, 2012 5-yr est (ACS 2012 5-year)
* Population aged 0-17, percent, 2012 5-yr est (ACS 2012 5-year)
* Population aged 18-64, percent, 2012 5-yr est (ACS 2012 5-year)
* Population aged 65+, percent, 2012 5-yr est (ACS 2012 5-year)

### Armslength sales
Original filename: `armslengthsales2006_2014.csv`

* number of records for each parcel number
* flags for deed type (restricted to Quit Claim Deed, Warranty Deed, Limited Warranty, Survivorshi Deed, Fiduciary Deed)
* amount paid in last sale, or else 0 (?)
* sale valid code in last sale (1 if code, 0 if no code)

### Transfers

Original filename: `transfers2000_2014.csv`

* number of transfers
	* could include number of transfers in time period 
* deed type of most recent entry (or else listed as 'Other'), for 10 most common deed types

### County land bank

* flag variable for existence in dataset (1 if in, else 0)

### Postal vacancy 	

Most recent entries to the dataset occur in 2/2014.

* flag variable for existence of Y and P in 'vindall', (1 if yes, 0 if no)

### Violations

* violations count of each task (application acceptance, closure, condemnation, etc.)
* violations count (total)
* violations count (since 3/1/2014)
* count of violations by type (for each type with at least 500 counts), such as fire damance, 30 day condemnations, etc.

### Complaints

* counts by type of complaint (at least ~6,000 counts), including OVV, fire damange, electrical, etc. 
* complaint count total
* complaint count since 9/1/2013
* complaint count since 12/1/2013

### Foreclosure data

* active foreclosure (1 if true, else 0)
* most recent pamount (since 3/1/2011)
* flags for 'dis w/o prej', 'newly filed', 'default','disp. other'

### Sheriff's auction

* count of sheriff's auctions since 1/1/2013
* count of sheriff's auctions, total

### Tax bill information
From December 2014.

* grand total balance
* lender process type


