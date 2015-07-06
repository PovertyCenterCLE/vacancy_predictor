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

Lastly, this model can built with historical data in an attempt to predict whether a parcel is likely to become vacant in the future (e.g. 6 months from now.
