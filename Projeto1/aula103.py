from datetime import datetime
from pytz import timezone

data_str_data = '2022/04/20 07:49:23'
data_str_data = '20/04/2022'
data_str_fmt = '%d/%m/%Y'

# data = datetime(2022, 4, 20, 7, 49, 23)
data = datetime.strptime(data_str_data, data_str_fmt)
# print(data)

i = 0
while i <= 100000:
    data = datetime.now()
    print(data.timestamp())  # Isso está na base de dados
    print(datetime.fromtimestamp(data.timestamp()))
    # data_str_data = '2022/04/20 07:49:23'
    # data_str_data = '20/04/2022'
    # data_str_fmt = '%d/%m/%Y'

    # data = datetime(2022, 4, 20, 7, 49, 23, tzinfo=timezone('Asia/Tokyo'))
    # data = datetime.strptime(data_str_data, data_str_fmt)
    i += 1