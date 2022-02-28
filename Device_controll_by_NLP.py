import speech_recognition as sr
a = sr.Recognizer()


def user_commands():
    try:
        with sr.Microphone() as source:
            print(" Sir Please Start Speaking ")
            # voice =Listner.listen(source##)

            # listen command which we tell ,convert into text ,and also conver into
            # lower text .

            command = Listner.recognize_google(voice)
            # command = command.lower(##)
            if "walter" in command:
                command = command.replace("walter","")
                print(command)
    except:
        pass
    return command

def action_delta():
    command = user_commands()
    if 'light on' in command:
        
        import RPi.GPIO as GPIO
        import time
        
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(11,GPIO.OUT)
        
        GPIO.output(11,False)
        time.sleep(.5)
        
      

    elif 'Light off' in command:
        import RPi.GPIO as GPIO
        import time
        
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(11,GPIO.OUT)
        
        GPIO.output(11,True)
        time.sleep(.5)
        



    else:
        print("i Could not hear Properly")


action_delta()