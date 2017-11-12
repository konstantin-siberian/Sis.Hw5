import ev3dev.ev3 as ev3
import threading
import time


motor_left=ev3.LargeMotor('outA')
motor_right=ev3.LargeMotor('outD')
gyroscope=ev3.GyroSensor('in2')
ultrasonic_left=ev3.UltrasonicSensor('in4')
ultrasonic_right=ev3.UltrasonicSensor('in3')


k=0
def straight():
    global k
    motor_left.run_timed(time_sp=2500, speed_sp=200)
    motor_right.run_timed(time_sp=2500, speed_sp=200)
    time.sleep(2.5)
    k += 1

def turn():
    global k
    motor_left.run_timed(time_sp=2500, speed_sp=320)
    motor_right.run_timed(time_sp=2500, speed_sp=0)
    time.sleep(2.5)
    k += 1

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
    if counter ==1600:
        return
    threading.Timer(0.01, get_data).start()
    counter += 1
    f.write( bytes('{0} {1} {2} {3} {4}\n'.format(str(0.01*counter), str(ultrasonic_left.distance_centimeters), str(ultrasonic_right.distance_centimeters), str(gyroscope.angle), str(gyroscope.rate) ), 'UTF-8') )

while(1):
    if k==0 or k==2 or k==4 or k==6:
        straight()
    if k==1 or k==3 or k==5:
        turn()
    if k==7:
        break

counter = 0

f=open('nikita.txt','wb+')
get_data()
