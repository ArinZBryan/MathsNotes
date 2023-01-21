To use the python version:
- Place the pyton file in the source directory of your project
- Place ALL the .csv files in some other folder in your project
- When instantiating the 'Large_Dataset' class, 'rel_path_to_csvs' should be set to the relative path from the source directory to the folder full of .csv files you created earlier.

To access data in the 'Large_Dataset' Class:
dataset = large_dataset.Large_Dataset("./../CSV") #This is the relative path as the files are dowloaded
dataset.{insert place name here}[{insert year here}][{insert day number here}].{insert statistic you want here}
ie. to get the rainfall on the 31st day of the data from perth in 2015:
dataset.perth[15][31].rainfall

NOTE 1: When accessing wind speed, add .knots for the value in knots and .beaufort for the value in the beaufort scale.
NOTE 2: when accessing wind direction, add .bearing for the number on a compass, and .heading for the value in compass directions (eg. NW).