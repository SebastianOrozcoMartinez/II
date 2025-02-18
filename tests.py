import time, re
day = time.strftime("%d/%m/%Y")
isDate = '/'
print(''.join(re.findall(isDate,day)))