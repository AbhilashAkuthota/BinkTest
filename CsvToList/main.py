from datetime import datetime
import sys
import csv


def print_list(list):
    for i in range(len(list)):
        print(list[i])


def read_csv_to_list(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        data = list(reader)
        del data[0]
        return data


def sort_by_current_rent(ori_list):
    sorted_list = sorted(ori_list, key=lambda x: float(x[10]), reverse=False)
    print("\n========== A list sorted by “Current Rent” in ascending order ===========")
    print_list(sorted_list)
    return sorted_list


def get_first_5items(ori_list):
    sorted_list = sorted(ori_list, key=lambda x: float(x[10]), reverse=False)
    items = sorted_list[0:5]
    print("\n========== The lowest 5 items ===========")
    print_list(items)
    return items


def filter_by_lease_year(ori_list, lease_year):
    filtered_list = [line for line in ori_list if int(line[9]) == lease_year]
    print("\n========== Items of {} Lease Year  ===========".format(lease_year))
    print_list(filtered_list)
    return filtered_list


def get_rent_sum(ori_list):
    result = sum(float(x[10]) for x in ori_list)
    print("\nTotal Rent for items of 25 Lease Years is ", result)
    return result


def gen_dict_of_tenant(ori_list):
    tenant_dict = {}
    for item in ori_list:
        if item[6] not in tenant_dict:
            tenant_dict[item[6]]=1
        else:
            tenant_dict[item[6]]+=1
    print("\n=========== dictionary containing tenant name and a count of masts for each tenant ============")
    for keys,values in tenant_dict.items():
        print("{} : {}".format(keys, values))

    return tenant_dict


def get_list_in_range(ori_list, start_date, end_date):
    start_date=datetime.strptime(start_date, '%Y-%m-%d')
    end_date=datetime.strptime(end_date, '%Y-%m-%d')
    filtered_list=[]
    for item in ori_list:
        lease_start_date=datetime.strptime(item[7], '%d-%b-%y')
        if (lease_start_date>=start_date) & (lease_start_date<=end_date):
            item[7]=datetime.strptime(item[7], '%d-%b-%y').strftime('%d/%m/%Y')
            item[8] = datetime.strptime(item[8], '%d-%b-%y').strftime('%d/%m/%Y')
            filtered_list.append(item)
    print("\n========== List the data for rentals with “Lease Start Date” between {} and {}  ===========".format(
        start_date, end_date))
    print_list(filtered_list)
    return filtered_list


if __name__ == '__main__':
    raw_data = read_csv_to_list("./Python Developer Dataset.csv")
    if len(sys.argv) == 1:
        print("Run All Scripts...")
        sorted_by_cur_rent = sort_by_current_rent(raw_data)
        get_first_5items(raw_data)
        lease25_list = filter_by_lease_year(raw_data, 25)
        get_rent_sum(lease25_list)
        gen_dict_of_tenant(raw_data)
        get_list_in_range(raw_data, "1991-06-01", "2007-08-31")
    elif len(sys.argv) == 2:
        if sys.argv[1] == "sort":
            sorted_by_cur_rent = sort_by_current_rent(raw_data)
        elif sys.argv[1] == "top_5":
            get_first_5items(raw_data)
        elif sys.argv[1] == "lease_25":
            lease25_list = filter_by_lease_year(raw_data, 25)
            get_rent_sum(lease25_list)
        elif sys.argv[1] == "tenants":
            gen_dict_of_tenant(raw_data)
        elif sys.argv[1] == "filter_in_range":
            get_list_in_range(raw_data, "1991-06-01", "2007-08-31")
        else:
            pass
