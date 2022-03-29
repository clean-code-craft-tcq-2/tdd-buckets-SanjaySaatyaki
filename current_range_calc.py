import more_itertools as mit
import csv
import random

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
            writer.writerow({'Range': str(key)[1:-1].replace(",","-"), 'Readings': range_dict[key]})
        return "Ranges_and_Readings.csv"

def remove_invalid_data(samples,range_value):
    valid_samples = [sample for sample in samples if sample <= range_value]
    return valid_samples
    

def A2D_12BtoAmps_convertor(samples):
    valid_samples_amps = [round(sample*10/4094) for sample in samples]
    return valid_samples_amps

def A2D_10BtoAmps_convertor(samples):
    valid_samples_amps = [abs(round(sample*30/1022) - 15) for sample in samples]
    return valid_samples_amps

def calc_ranges_from_sensor(samples,sensor):
    if sensor == "A2D_12B":
        valid_samples = remove_invalid_data(samples,4094)
        amps_sample = A2D_12BtoAmps_convertor(valid_samples)
    elif sensor == "A2D_10B":
        valid_samples = remove_invalid_data(samples,1022)
        amps_sample = A2D_10BtoAmps_convertor(valid_samples)
    return calc_ranges(amps_sample)