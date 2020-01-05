cal=[['January',31],['February',28],['March',31],['April',30],['May',31],['June',30],['July',31],['August',31],['September',30],['October',31],['November',30],['December',31]];

str=input("Which month's no. of days you want:")
for i in range(0,12):
    if (str==cal[i][0]):
        print("The no. of days in ",str,"is ",cal[i][1])
