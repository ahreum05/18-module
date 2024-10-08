from datetime import date
from datetime import datetime

# 오늘 날짜 확인
print(date.today())
print('-' * 20)

print(datetime.today())
print('-' * 20)

# 년월일시분초 설정
d1 = datetime(2024, 6, 1, 20, 30, 30)
print(d1)
print('{}/{}/{}'.format(d1.year, d1.month, d1.day))
print('{}:{}:{}'.format(d1.hour, d1.minute, d1.second))
print('{:%Y/%m/%d %H:%M:%S}'.format(d1))
print('{:%Y/%m/%d}'.format(d1))
print('{:%H:%M:%S}'.format(d1))
print('{:%D}'.format(d1))
print('-' * 20)

# 일수 계산
day1 = datetime(2024, 1, 1)
day2 = datetime.now()
day_num = day2 - day1
print('일수 :', day_num.days + 1)
print('-' * 20)

day1 = datetime(2025, 1, 1)
day2 = datetime(2025, 12, 31)
day_num = day2 - day1
print('일수 :', day_num.days + 1)
