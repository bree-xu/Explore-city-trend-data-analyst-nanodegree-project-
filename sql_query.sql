/* 
This file contains the SQL commands that is used to retrieve the tamperature data (globally and locally) from the online database in Udacity website.

The closest city near where I am right now is Helsinki, Finland.

Since the year index does not match between global data and Helsinki data, I only get the year of data that exist in both table
*/

SELECT year, avg_temp
FROM city_data
WHERE city IN ('Helsinki')
AND year BETWEEN 1750 AND 2013;


SELECT *
FROM global_data
WHERE year BETWEEN 1750 AND 2013;
