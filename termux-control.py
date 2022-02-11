from time import sleep
import os
import logging


if __name__ == "__main__":
    while True:
        try:
            output = os.popen('termux-wifi-connectioninfo').read()
            
            if output.find('null') > -1:
                os.system('termux-wifi-enable false')
                sleep(10)
                os.system('termux-wifi-enable true')
        except Exception as e:
            logging.error(e)
            continue
        finally:
            sleep(15 * 60) # 15 minutes
