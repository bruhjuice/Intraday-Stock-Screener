from requests_html import HTMLSession
import time
from datetime import datetime

# Set time interval to amount of seconds waited. (For ex. 300 seconds would give you top movers in the last five min.) 
time_interval = 100
# Timer to measure runtime of each cycle
start_time = time.time()
original_Data = {}
updated_Data = {}
percent_differences = {}
new_additions = {}
# URL of Barchart's live site that contains the highest stocks by volume for the day
URL = "https://www.barchart.com/stocks/most-active/daily-volume-leaders"

# Function that gets current % change from Barchart's site, and storea numbers in original_Data array
def get_Initial_Data(URL, original_Data):
  x = 1
  session = HTMLSession()
  r = session.get(URL)
  r.html.render(timeout = 30)
  for number in range (1, 101):
    ticker = r.html.xpath('//*[@id="main-content-column"]/div/div[5]/div/div[2]/div/div/ng-transclude/table/tbody/tr[{}]/td[1]/div/span[2]/a'.format(x), first = True).text
    percent_change = r.html.xpath('//*[@id="main-content-column"]/div/div[5]/div/div[2]/div/div/ng-transclude/table/tbody/tr[{}]/td[5]/div/span/span/span'.format(x), first = True).text
    x+=1
    if (percent_change == 'unch'):
      percent_change = "0%"
    original_Data[ticker] = float(percent_change[:-1])
  print ("\nOriginal data finished")
  print(original_Data)

# Function that gets current % change from Barchart's site, and stores numbers in updated_Data array
def get_updated_Data(URL, updated_Data):
  x = 1
  session = HTMLSession()
  r = session.get(URL)
  r.html.render(timeout = 30)
  for number in range (1, 101):
    ticker = r.html.xpath('//*[@id="main-content-column"]/div/div[5]/div/div[2]/div/div/ng-transclude/table/tbody/tr[{}]/td[1]/div/span[2]/a'.format(x), first = True).text
    percent_change = r.html.xpath('//*[@id="main-content-column"]/div/div[5]/div/div[2]/div/div/ng-transclude/table/tbody/tr[{}]/td[5]/div/span/span/span'.format(x), first = True).text
    x+=1
    if (percent_change == 'unch'):
      percent_change = "0%"
    updated_Data[ticker] = float(percent_change[:-1])
  print ("\nUpdated data finished")
  print(updated_Data)

# For displaying current time at after it finishes running
def get_time():
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  return current_time

# Function that writes results to output.txt
def write_to_file(largest_movers, new_additions):
  filename = "output.txt"
  with open(filename, "a") as file_object:
    file_object.write("\nTop gainers in the last 5 minutes " + "as of " + get_time() + "\n")
    for i in largest_movers:
      print(i + ":" + str(largest_movers[i]) +"%", file = file_object)
    if (bool(new_additions) == True):
      file_object.write("\nNew additions\n")
      for i in new_additions:
        print(i + ":" + str(new_additions[i]) +"%", file = file_object)

# Function that calculates the flat percentage change from the original data set and the updated data set
# If a new ticker is found in the updated data set that was not present in the original, it is added to the new_additions array
def get_difference(updated_Data, original_Data, percent_differences):
  print ("\nPercent Changes:")
  for ticker in updated_Data:
    if ticker in original_Data:
      percent_differences[ticker] = round(updated_Data[ticker] - (original_Data[ticker]), 2)
    else:
      new_additions[ticker] = updated_Data[ticker]
  print (percent_differences)

# Prints out the largest gainers by flat % in the last time interval
def print_top_movers(largest_movers, new_additions):
  print ("\nBiggest gainers in the last {} min.".format(round(time_interval/60, 2)))
  for i in largest_movers:
    print(i + ":" + str(largest_movers[i]) +"%")
  print (new_additions)

# Resets the arrays and datasets for next loop
def reset_dicts(updated_Data, largest_movers, new_additions, percent_differences):
  updated_Data.clear()
  largest_movers.clear()
  new_additions.clear()
  percent_differences.clear()

# Initialize data
get_Initial_Data(URL, original_Data)
# Wait out the time interval
time.sleep(time_interval)
# Get updated data set
get_updated_Data(URL, updated_Data)
# Calculate the flat % change
get_difference(updated_Data, original_Data, percent_differences)
# Sort to only include the top 10 gainers
largest_movers = dict(sorted(percent_differences.items(), key = lambda item: item[1], reverse = True)[:10])
print_top_movers(largest_movers, new_additions)
print("--- %s seconds ---" % (time.time() - start_time))
# Write results to output file
write_to_file(largest_movers, new_additions)

# Will continue to loop program until program is stopped
while (True):
  start_time = time.time()
  original_Data = updated_Data.copy()
  print("\nOriginal data finished:\n" + str(original_Data))
  reset_dicts(updated_Data, largest_movers, new_additions, percent_differences)
  time.sleep(time_interval)
  get_updated_Data(URL, updated_Data)
  print(original_Data)
  get_difference(updated_Data, original_Data, percent_differences)
  largest_movers = dict(sorted(percent_differences.items(), key = lambda item: item[1], reverse = True)[:10])
  print_top_movers(largest_movers, new_additions)
  print("--- %s seconds ---" % (time.time() - start_time))
  write_to_file(largest_movers, new_additions)
