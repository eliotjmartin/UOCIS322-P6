# A brevet time calculator for CIS 322 #

Eliot Martin | eliotm@uoregon.edu

## Overview

This is a reimplementation of the RUSA ACP controle time calculator (https://rusa.org/octime_acp.html). There are three main parts to this calculator: main api (designed in project 5) that allows the user to enter distances in fields to calculate controle times, submit these times into a MongoDB database by clicking the "submit" button, and finally displaying the values from the data base on a separate page by clicking the "display" button. There is a rest-api that can also display the calculated open and close times in csv or json format (json by default) by the following logic:

- "http://host:port/listAll/csv" should return all open and close times in CSV format

- "http://host:port/listOpenOnly/csv" should return open times only in CSV format

- "http://host:port/listCloseOnly/csv" should return close times only in CSV format

- "http://host:port/listAll/json" should return all open and close times in JSON format

- "http://host:port/listOpenOnly/json" should return open times only in JSON format

- "http://host:port/listCloseOnly/json" should return close times only in JSON format

There is also an additional optional argument "top" that will display only the top k arguments. Usage is as follows:

- "http://host:port/listOpenOnly/csv?top=3" should return top 3 open times only (in ascending order) in CSV format
- "http://host:port/listOpenOnly/json?top=5" should return top 5 open times only (in ascending order) in JSON format
- "http://host:port/listCloseOnly/csv?top=6" should return top 5 close times only (in ascending order) in CSV format
- "http://host:port/listCloseOnly/json?top=4" should return top 4 close times only (in ascending order) in JSON format

Finally, there is a consumer program with three buttons "open", "close" and "all" that simply calls the rest api's default open, close and all behavior.


## Algorithm

Controle open and close times are calculated by dividing the controle distance by the maximum and minimum speeds, respectively (maximum and minimum speeds are outlined here https://rusa.org/pages/acp-brevet-control-times-calculator). This time is rounded to the nearest minute.

Furthermore, there is a small bias for closing times with controles under 60 km that is calculated by subtracting the controle distance from 60 and dividing by 60. This value is then added to the usual closing time.

Finally, each brevet distance has predetermined closing times. Thus, controles greater than the brevet distance get no additional time as the closing time is now based on the brevet.

## USAGE
Build image and run in docker from brevets folder (where the dockerfile and yml file are located). 


## Credits

Michal Young, Ram Durairajan, Steven Walton, Joe Istas.