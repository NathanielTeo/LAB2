def main():
    display_main_menu()
    n=get_user_inputs()
    avg=calc_average_temperature(n)
    print(avg)


def display_main_menu():
    print ("Enter some numbers seperated by commas ")

def get_user_inputs():
    x = input()
    y=(x.split(','))
    y2=[]
    for x in range(len(y)):
        floatnum=float(y2[x])
        y2.append(floatnum)
    return y2

def calc_average_temperature(n):
    for num in range(len(n)):
        sum=sum+n[num]

    avg=sum/(len(n))
    return avg







if __name__ == "__main__" :
    main()
