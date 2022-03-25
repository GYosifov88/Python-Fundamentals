num = float(input())

if num == 0:
    print ('zero')
elif abs(num) < 1 and num != 0 and num > 0:
    print ('small positive')
elif abs(num) < 1 and num != 0 and num < 0:
    print ('small negative')
elif 1 < num < 1000000:
    print ('positive')
elif -1 > num > -1000000:
    print('negative')
elif num > 1000000:
    print ('large positive')
elif num < -1000000:
    print ('large negative')