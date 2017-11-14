import matplotlib.pyplot as plt
import numpy as np
'''
with open('kostya.csv', 'wb') as csvfile:
	#Example: on each iteration write 1 data row (time, left_us,right_us,...)
	for i in range(10):
		csvfile.write('{0} {1} {2} {3} {4}\n'.format(i, i*10,i**2, i+0.2356, i-0.01))
'''

def read_data(filename):
	"""
	@param filename
	This function reads the data from files: kostya_final.txt and nikita_final.txt
	"""
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
		time_stamps.append(float(sensors_data[i*5 + 0]))
		left_ultrasonic.append(float(sensors_data[i*5 + 1]))
		right_ultrasonic.append(float(sensors_data[i*5 + 2]))
		gyro_angles.append(float(sensors_data[i*5 + 3]))
		gyro_values.append(float(sensors_data[i*5 + 4]))

	return time_stamps, left_ultrasonic, right_ultrasonic, gyro_angles, gyro_values


time_stamps, left_ultrasonic, right_ultrasonic, gyro_angles, gyro_values = read_data('kostya_final.txt')
time_stamps, left_ultrasonic, right_ultrasonic, gyro_angles, gyro_values = read_data('nikita_final.txt')

print('You have {0} points in total. Very wonderful!'.format(len(time_stamps)) )


plt.rcParams['figure.figsize'] = (10, 8)

# intial parameters
iterations = len(left_ultrasonic) - 20
sz = (iterations,) # size of array

proposed_value = 30 # truth value 

z = np.array(left_ultrasonic)
Q = 1e-5 # Variance


xhat=np.zeros(sz)      # a posteri estimate of values
P=np.zeros(sz)         # a posteri error estimate
xhatminus=np.zeros(sz) # a priori estimate of values
Pminus=np.zeros(sz)    # a priori error estimate
K=np.zeros(sz)         # gain or blending factor

R = 0.1**2 # estimate of measurement variance, change to see effect

# intial guesses
xhat[0] = 0.0
P[0] = 1.0

#Kalman filtering process
for k in range(1,iterations):
    # Time update
    xhatminus[k] = xhat[k-1]
    Pminus[k] = P[k-1]+Q

    # Measurement update
    K[k] = Pminus[k]/( Pminus[k] + R )
    xhat[k] = xhatminus[k]+K[k]*(z[k]-xhatminus[k])

    P[k] = (1-K[k])*Pminus[k]

plt.figure()
plt.plot(z,'k+',label='noisy measurement data')
plt.plot(xhat,'b-',label='Estimated data')
# plt.axhline(proposed_value,color='g',label='truth value')
plt.legend()
plt.title('Estimate vs. iteration step', fontweight='bold')
plt.xlabel('Iteration')
plt.ylabel('Ultrasonic distance')


plt.show()