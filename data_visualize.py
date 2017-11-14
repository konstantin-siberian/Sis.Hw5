import matplotlib.pyplot as plt
from filterpy.kalman import KalmanFilter
'''
with open('kostya.csv', 'wb') as csvfile:
	#Example: on each iteration write 1 data row (time, left_us,right_us,...)
	for i in range(10):
		csvfile.write('{0} {1} {2} {3} {4}\n'.format(i, i*10,i**2, i+0.2356, i-0.01))
'''
def read_data(filename):
	with open(filename, 'rb') as csvfile:
		sensors_data = csvfile.read()
		sensors_data = sensors_data.replace('\n', ' ')
		sensors_data = sensors_data.split(' ')
		del sensors_data[-1]

	right_ultrasonic = []
	left_ultrasonic = []
	time_stamps = []
	gyro_angles = []
	gyro_values = []

	for i in range(len(sensors_data)/5):
		time_stamps.append(sensors_data[i*5 + 0])
		left_ultrasonic.append(sensors_data[i*5 + 1])
		right_ultrasonic.append(sensors_data[i*5 + 2])
		gyro_angles.append(sensors_data[i*5 + 3])
		gyro_values.append(sensors_data[i*5 + 4])

	return time_stamps, left_ultrasonic, right_ultrasonic, gyro_angles, gyro_values


time_stamps, left_ultrasonic, right_ultrasonic, gyro_angles, gyro_values = read_data('kostya_final.txt')

print('You have {0} points in total. Very wonderful!'.format(len(time_stamps)) )
fig, ax = plt.subplots()

line1, = ax.plot(time_stamps, left_ultrasonic, 'o', linewidth=2,
                 label='Left ultrasonic')
 
line2, = ax.plot(time_stamps, right_ultrasonic, 'o', linewidth=2,
                 label='Right ultrasonic')


'''
line3, = ax.plot(time_stamps, gyro_angles, '-', linewidth=2,
                 label='Left ultrasonic')

line4, = ax.plot(time_stamps, gyro_values, '-', linewidth=2,
                 label='Left ultrasonic')
'''
plt.show()

