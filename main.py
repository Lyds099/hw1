# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '106000198.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)
#=======================================

# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))
import pandas as pd

df = pd.DataFrame(data=data, columns=header)
df = df.drop(df[(df['HUMD'] == '-99.000') | (df['HUMD'] == '-999.000')].index)
#df.to_csv('output.csv', index=False)

df['HUMD'] = df['HUMD'].astype(float)
id_list = ['C0A880', 'C0F9A0', 'C0G640', 'C0R190', 'C0X260']
target_data = []
for id in id_list:
   id_output = [id]
   filtered = df[df['station_id'] == id]
   if filtered.empty:
      id_output.append('None')
   else:
      sum = filtered['HUMD'].sum()
      id_output.append(sum)
   target_data.append(id_output)

# Retrive ten data points from the beginning.
#target_data = data[:10]

#=======================================

# Part. 4
#=======================================
# Print result
print(target_data)
#========================================