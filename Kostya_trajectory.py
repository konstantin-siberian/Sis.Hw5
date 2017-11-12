import ev3dev.ev3 as ev3
import threading
# initializing the system:
#ultrasonic - 1,2
#gyroscope - 4
#large motors - A,D

motor_left=ev3.LargeMotor('outA')
motor_right=ev3.LargeMotor('outD')
gyroscope=ev3.GyroSensor('in2')
ultrasonic_left=ev3.UltrasonicSensor('in4')
ultrasonic_right=ev3.UltrasonicSensor('in3')

'''
motor_left.run_timed(time_sp=50000, speed_sp=500)
motor_right.run_timed(time_sp=50000, speed_sp=500)
print('fdsgsdfg')
motor_left.run_timed(time_sp=50000, speed_sp=500)
motor_right.run_timed(time_sp=50000, speed_sp=150)

motor_left.run_timed(time_sp=50000, speed_sp=500)
motor_right.run_timed(time_sp=50000, speed_sp=500)
'''
motor_left.run_timed(time_sp=60000, speed_sp=400)
motor_right.run_timed(time_sp=60000, speed_sp=200)

counter = 0
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

def get_data():


    global counter
    global f
    if counter ==1000:
        return
    threading.Timer(0.01, get_data).start()
    counter += 1
    f.write( bytes('{0} {1} {2} {3} {4}\n'.format(str(0.01*counter), str(ultrasonic_left.distance_centimeters), str(ultrasonic_right.distance_centimeters), str(gyroscope.angle), str(gyroscope.rate) ), 'UTF-8') )
    # print('Left ultrasonic data ' + str(ultrasonic_left.distance_centimeters))
    # print('Right ultrasonic data ' + str(ultrasonic_right.distance_centimeters))
    # print('Gyroscope data angle ' + str(gyroscope.angle))
    # print('Gyroscope data rate ' + str(gyroscope.rate))
f=open('kostya.txt','wb+')
get_data()
# f.close()
#tragectory circle


# time_stamps, left_ultrasonic, right_ultrasonic, gyro_angles, gyro_values = read_data('kostya.csv')

# print('You have {0} points in total. Very wonderful!'.format(len(time_stamps)) )