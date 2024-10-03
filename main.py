'''
flow logs column names:
version, account-id, interface-id, srcaddr, dstaddr, srcport, dstport, protocol, packets, bytes, start, end, action, log-status
'''

'''
lookup column names:
dstport,protocol,tag
'''

from collections import defaultdict

flow_log_column = ["version", "account-id", "interface-id", "srcaddr", "dstaddr", "srcport", "dstport", "protocol", "packets", "bytes", "start", "end", "action", "log-status"]

with open('data/flow_logs.txt', 'r') as file:
    table = [line.strip().split(' ') for line in file.readlines()]

# create a dictionary to hold the data
flow_logs_table = {}

# iterate over each row in the table
for row in table:
    # iterate over each value in the row and extract its column name from flow_log_column
    for index, value in enumerate(row):
        column_name = flow_log_column[index]
        # check if the column name is already in the hashmap
        if column_name in flow_logs_table:
            flow_logs_table[column_name].append(value)
        else:
            flow_logs_table[column_name] = [value]

# read the 'lookup_table.csv' file, reading the header of the file of as a string and converting it into a list of column names
with open("data/lookup_table.csv", 'r') as file:
    header_line = file.readline().strip()
    lookup_column_names = header_line.split(',')

# read the lookup_table.csv file, reading this file as a csv file with a header, and outputing a hashmap with the key being the column name, and the value being the list of values in that column
lookup_table = defaultdict(list)

with open("data/lookup_table.csv", 'r') as file:
    for line in file:
        values = line.strip().split(',')
        for i, column_name in enumerate(lookup_column_names):
            lookup_table[column_name].append(values[i])

# we have two tables, represented as hashmaps with the keys being the column name, and the value being the list of values in the column
# this is a table that reprecents the results of the groupby
# where the key is the tag (the groupby column) and
# the values are the other rows (count)
group_by_tag = defaultdict(int)

# Create a mapping of (dstport, protocol) tuples to tags
# this is going to be our search
tag_mapping = {}
for i in range(len(lookup_table['dstport'])):
    key = (lookup_table['dstport'][i], lookup_table['protocol'][i])
    tag_mapping[key] = lookup_table['tag'][i]

# then for each row in flow logs table
for i in range(len(flow_logs_table['dstport'])):
    key = (flow_logs_table['dstport'][i], flow_logs_table['protocol'][i])
    # search for the combination in the tag mapping
    tag = tag_mapping.get(key, 'Untagged')
    group_by_tag[tag.lower()] += 1

# for each protocol port combination, count them
# this does not require the lookup table as all the data is in the flow table
group_by_dstport_protocol = defaultdict(int)

# for each index in the flow logs table
for i in range(len(flow_logs_table['dstport'])):
    # create the composite key
    key = (flow_logs_table['dstport'][i], flow_logs_table['protocol'][i])

    # increment the count by one or set to one if it does not exist
    # this is standard as we are using defaultdict
    group_by_dstport_protocol[key] += 1

# write the output to the files
with open('output.txt', 'w') as file:
    file.write("Tag Counts:\n")
    file.write("Tag,Count\n")

    for tag, count in group_by_tag.items():
        file.write(f"{tag},{count}\n")

    file.write("\nPort/Protocol Combination Counts:\n")
    file.write("Port,Protocol,Count\n")

    for key, count in group_by_dstport_protocol.items():
        dstport, protocol = key
        file.write(f"{dstport},{protocol},{count}\n")
