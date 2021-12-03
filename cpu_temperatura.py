# Importing the library
import psutil
  
# Calling psutil.cpu_precent() for 4 seconds
print('The CPU usage is: ', psutil.cpu_percent(4))
print('-------------------')
print('', psutil.sensors_temperatures())
print('-------------------')
print('', psutil.sensors_temperatures('acpitz["\'Core 1"\']'))
print('batery:', psutil.sensors_battery())
print('-------------------')
print('', psutil.disk_usage('/'))


