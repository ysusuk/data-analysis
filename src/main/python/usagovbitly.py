import json
import collections
import pandas as pd
import numpy as np

from collections import Counter
from pandas import DataFrame, Series

path = '/Users/ysusuk/scout24/helloworld-pybuilder/src/main/resources/usagov_bitly_data2013-05-17-1368832207.txt'

lines = []
shortrenedLine = open(path).readline()
shortened = json.loads(shortrenedLine)
lines.append(shortrenedLine)
lines.append(shortened['cy'])
lines.append(shortened['ll'])

records = [json.loads(line) for line in open(path).readlines()]
lines.append("Size: ")
lines.append(len(records))
lines.append("First record: ")
lines.append(records[1])
lines.append(records[1].get('g', 'blah'))
print(lines)

time_zones = [record['tz'] for record in records if 'tz' in record]
print('---')
# print(time_zones)
print("number of records: {}".format(len(time_zones)))
print("number of different time zones: {}".format(len(set(time_zones))))


# python standard
def get_time_zones_count(time_zones):
    time_zones_count = {}

    for time_zone in time_zones:
        if time_zone in time_zones_count:
            time_zones_count[time_zone] += 1
        else:
            time_zones_count[time_zone] = 1

    return  time_zones_count

print(get_time_zones_count(time_zones)['America/New_York'])

def get_top_time_zones(time_zones_count, n = 10):
    items = [(count, time_zone) for time_zone, count in time_zones_count.items()]
    print("not sorted: {}\n".format(items))
    items.sort()
    print
    print("\nsorted: {}\n".format(items))
    return items[-n:]

print("top 10: {}\n".format(get_top_time_zones(get_time_zones_count(time_zones))))
print("top 15: {}\n".format(Counter(time_zones).most_common(15)))

# python pandas - powerfull data structures
frame = DataFrame(records)
print("{}\n".format(frame['tz'].value_counts()))

tz = frame['tz'].fillna('Missing')
print("{}\n".format(tz.value_counts()[:10]))
tz[tz == ''] = 'Missing'
print("{}\n".format(tz.value_counts()[:10]))

# plot and save
tz_plot = tz.value_counts()[:10].plot(kind = 'barh', rot=0)
tz_plot.figure.savefig('tz_plot')

print("{}\n".format(frame.a[:5]))

browsers = Series([a.split()[0] for a in frame.a.dropna()]).value_counts()[:5]

print("{}\n".format(browsers))

clean_frame = frame[frame.a.notnull()]

os = Series(np.where(clean_frame['a'].str.contains('Windows'), 'Windows', 'Not Windows'))

print("{}\n".format(os[:5]))

by_tz_os = clean_frame.groupby(['tz', os])

agg_counts = by_tz_os.size().unstack().fillna(0)

print("{}\n".format(agg_counts))

indexer = agg_counts.sum(1).argsort()
# print(indexer)

subset = agg_counts.take(indexer)[-10:]
subset_plot = subset.plot(kind = 'barh', stacked = True)
subset_plot.figure.savefig('susbet_plot')


