import statistics

def main():
    display_main_menu()
    num_list = get_user_input()
    avg = calc_average(num_list)
    print(avg)
    max,miniumum = find_min_max(num_list)
    print(max)
    print(miniumum)
    sort = sort_temperature(num_list)
    print(sort)
    med = calc_median_temperature(sort)
    print(med)

def display_main_menu():
    print("display main menu")
    print("69,13,313")

def get_user_input():
    print("get_user_input")
    x = input("please enter out temperatures with a , between them: ")
    temps = x.split(',')
    temps2=[]
    for x in range(len(temps)):
        floatnum=float(temps[x])
        temps2.append(floatnum)
    return temps2


def calc_average(x):
    print("calculate average")
    sum = 0
    for i in range(len(x)):
        sum = sum+x[i]

    avg = sum/(len(x))
    return avg


def find_min_max(x):
    print("find_min_max")
    max = x[0]
    for i in range(len(x)):
        if x[i]>max:
            max = x[i]
    minimum = x[0]
    for h in range(len(x)):
        if x[i]<minimum:
            minimum = x[i]
    return max,minimum


def sort_temperature(x):
    print("sort_temperature")
    x.sort()
    return x

def calc_median_temperature(x):
    print("calc_median_temperature")
    med = statistics.median(x)
    return med

if __name__ == '__main__':
    main()