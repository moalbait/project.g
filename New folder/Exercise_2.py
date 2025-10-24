try:
    hours = dict()
    with open('mbox-short.txt') as fhand:
       for line in fhand:
        words = line.split()
        count= 0
        
        for word in words:
            if word.find(':') != -1:
                time = word.split(':')
                if len (time) !=3:
                    continue
                hour =time[0]
                min = time[1]
                sec = time[2]
                if hour.isdigit()and min.isdigit() and sec.isdigit():
                    hour = int(hour)
                    min = int(min)
                    sec = int(sec)
                    if hour>0 and hour <24:
                        if hour not in hours:
                            hours[hour] =1
                        else:
                            hours[hour] +=1
                    else:
                        continue
                else:
                        continue
            else:
                continue
    lst =list()
    for key, val in hours.items():
        lst.append((val,key))
    lst.sort(reverse =True)
    for val, key in lst[:20]:
        print(key, val)
except FileNotFoundError as e:
    print("file not found error occured")