# Module_Nine_Challenge_Surfs_Up

## Project Overview
Analyze weather information from weather stations in Oahu, Hawaii to determine the sustainability of a surf and ice cream business. In order to determine if the business is sustainable year-round, use termperature data for the months of June and December to identify termperature trends.

## Resources
 - Data: hawaii.sqlite
 - Software: Visual Studio Code, Python, Jupiter Notebook, Pandas, Json, Numpy, Datetime, Sqlalchemy, Matplotlib

## Results
### Summary Statistics
![June_Summary_Statistics](https://github.com/LLeyva-bot/Surfs_Up/blob/main/June_Summary_Statistics.PNG)![December_Summary_Statistics](https://github.com/LLeyva-bot/Surfs_Up/blob/main/December_Summary_Statistics.PNG)
 - The average temperature in June is 3.9 degrees fahrenheit higher than the average temperature in December.
 - The standard deviation of temperature in June is 0.5 degrees fahrenheit lower the standard deviation of temperature in December.
 - The lowest temperature in June is 8 degrees fahrenheit higher than the lowest temperature in Decemeber.
 - The highest temperature in June is 2 degrees fahrenheit higher than the highest temperature in December.

## Summary
The month of June in Oahu, on average, is consistenlty warmer than the month of December.  Though the temperatures only slightly varies, both months hold high average temepratures year-round and make it an ideal location for a surf and ice cream business to thrive. To further our analysis, it's recommeneded to review the precipitation trends. This can be done by running four additional queries. 

 1. Queries to identify the total precipitation levels in Oahu for June and December.
session.query(Measurement.date, Measurement.prcp).filter(extract('month', Measurement.date) == 6).all()
session.query(Measurement.date, Measurement.prcp).filter(extract('month', Measurement.date) == 12).all()

 2. Queries to identfiy the amount of precipitation in the most active weather station in Oahu for June and December.
session.query(Measurement.prcp).filter(Measurement.station == 'USC00519281').filter(extract('month', Measurement.date) == 6).all()
session.query(Measurement.prcp).filter(Measurement.station == 'USC00519281').filter(extract('month', Measurement.date) == 12).all()