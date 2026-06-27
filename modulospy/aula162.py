from datetime import datetime
from pytz import timezone


data = datetime.now()
data = data.astimezone(timezone('Europe/Lisbon'))

print(data.timestamp())
print(datetime.fromtimestamp(1780182092))