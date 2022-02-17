from time import sleep
import os
import logging


MINUTES_SLEEP = 5 * 60 # 15 minutes


if __name__ == "__main__":
    while True:
        try:
            output = os.popen('termux-wifi-connectioninfo').read()
            
            if output.find('null') > -1:
                os.system('termux-wifi-enable false')
                sleep(10)
                os.system('termux-wifi-enable true')
                sleep(20)
            else:
                sleep(MINUTES_SLEEP) 
        except Exception as e:
            logging.error(e)
            sleep(10)
            continue
