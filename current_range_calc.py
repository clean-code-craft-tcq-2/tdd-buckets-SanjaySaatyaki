import more_itertools as mit

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
    return range_dict