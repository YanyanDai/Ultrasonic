import Jetson.GPIO as GPIO
import time

# Pin Definitions
trig_output_pin = 13  #Trigger PIN，J41_BOARD_PIN13---gpio14/GPIO.B06/SPI2_SCK
echo_input_pin = 18  #Echo PIN，J41_BOARD_PIN18---gpio15/GPIO.B07/SPI2_CS0

def main():
    # Pin Setup:
    # Board pin-numbering scheme
    GPIO.setmode(GPIO.BOARD)
    # set trig pin as an output pin with optional initial state of LOW
    GPIO.setup(trig_output_pin, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(echo_input_pin, GPIO.IN)

    print("Starting Measure now! Press CTRL+C to exit")
    try:
        while True:
            # Toggle the output every second
            GPIO.output(trig_output_pin, GPIO.HIGH)
            time.sleep(0.00001)
            GPIO.output(trig_output_pin, GPIO.LOW)
            
            #start recording        
            while GPIO.input(echo_input_pin)==0:
                pass
            pulse_start = time.time()
            
            #end recording
            while GPIO.input(echo_input_pin)==1:
                pass        
            pulse_end = time.time()
            
            #compute distance
            pulse_duration = pulse_end - pulse_start
            distance = round(pulse_duration * 343/2*100, 2)
            print ("Distance:{0}cm,{1}m".format(distance,distance/100))

    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    main()
    time.sleep(1)

