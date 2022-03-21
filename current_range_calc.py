import more_itertools as mit
import csv

def  get_range(lst):
    return [list(group) for group in mit.consecutive_groups(lst)]

def get_reading_count(item, lst):
    count = 0
    for i  in range(item[0],item[-1]+1):
        count = count + lst.count(i)
    return count

def calc_ranges(lst):
    range_dict = {}
    lst.sort()
    ranges = get_range(lst)
    for item in ranges:
        if len(item)!=1:
            range_dict.update({(item[0],item[-1]):get_reading_count(item,lst)})
    export_dict_to_csv(range_dict)
    return range_dict

def export_dict_to_csv(range_dict):
    with open('Ranges_and_Readings.csv', 'w', newline='') as csvfile:
        fieldnames = ['Range', 'Readings']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for key in range_dict:
            writer.writerow({'Range': key, 'Readings': range_dict[key]})
        return "Ranges_and_Readings.csv"
