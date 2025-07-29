# rows = [
# {'address': '5412 N CLARK', 'date': '07/01/2012'},
# {'address': '5148 N CLARK', 'date': '07/04/2012'},
# {'address': '5800 E 58TH', 'date': '07/02/2012'},
# {'address': '2122 N CLARK', 'date': '07/03/2012'},
# {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
# {'address': '1060 W ADDISON', 'date': '07/02/2012'},
# {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
# {'address': '1039 W GRANVILLE', 'date': '07/04/2012'}
# ]
# Sort and group values by using date in ascending order
# output should be like as below:
#
# 07/01/2012
#   {'address': '5412 N CLARK', 'date': '07/01/2012'}
#   {'address': '4801 N BROADWAY', 'date': '07/01/2012'}
# 07/02/2012
#   {'address': '5800 E 58TH', 'date': '07/02/2012'}
#   {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'}
#   {'address': '1060 W ADDISON', 'date': '07/02/2012'}
# 07/03/2012
#   {'address': '2122 N CLARK', 'date': '07/03/2012'}
# 07/04/2012
#   {'address': '5148 N CLARK', 'date': '07/04/2012'}
#   {'address': '1039 W GRANVILLE', 'date': '07/04/2012'}

# Sample data
rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'}
]

# Sort the rows by date using string comparison
rows.sort(key=lambda x: x['date'])

# Group by date
grouped = {}
for row in rows:
    date = row['date']
    if date not in grouped:
        grouped[date] = []
    grouped[date].append(row)

# Output the grouped results in the desired format
for date, addresses in grouped.items():
    print(date)
    for address in addresses:
        print(f"  {address}")
