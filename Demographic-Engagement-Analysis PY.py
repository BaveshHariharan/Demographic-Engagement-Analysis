def main(csv_file, age_group, country):
    list1 = []
    list2 = set()
    list3 = []
    list4=[]
    list6=[]
    list7=[]
    ruraltime = []
    urbantime = []
    subtime = []

    with open(csv_file, 'r') as file:
        next(file)
        for line in file:
            data = line.strip().split(',')
            age = int(data[1])
            if age in range(age_group[0], age_group[1]+1):
                if data[6].lower() == country.lower() and data[-1].upper() == 'TRUE' and int(data[3]) > 7:
                    list1.append([data[0], float(data[-2])])
                list2.add(data[6])
                list3.append(int(data[9]))
                list4.append(int(data[3]))
                
                if data[7].lower() == 'rural':
                    ruraltime.append(int(data[3]))
                elif data[7].lower() == 'urban':
                    urbantime.append(int(data[3]))
                else:
                    subtime.append(int(data[3]))
                if data[4].lower()=='instagram'.lower():
                    list6.append(int(data[1]))
                    list7.append(int(data[-2]))
                    
                    mean_x=sum(list6)/ len(list6)
                    mean_y= sum(list7)/len(list7)
                    numerator = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(list6, list7))
                    denominator = (sum((xi - mean_x) ** 2 for xi in list6) * sum((yi - mean_y) ** 2 for yi in list7)) ** 0.5


    
    if sum(ruraltime) < sum(urbantime) and sum(ruraltime) < sum(subtime):
        place='rural'
    elif sum(urbantime) < sum(ruraltime) and sum(urbantime) < sum(subtime):
        place=('urban')
    else:
        place=('suburban')

    mean = sum(list3) / len(list3)
    std = (sum((i - mean) ** 2 for i in list3) / (len(list3) - 1)) ** 0.5
    age=sum(list4)/len(list4)
    relative_coefficient=numerator/denominator

    return list1, sorted(list2), [round(age,4),round(std, 4),place], round(relative_coefficient,4)

