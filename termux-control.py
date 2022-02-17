from time import sleep
import os
import logging
import sys


PATH_BATTERY = sys.argv[1]
MINUTES_SLEEP = 5 * 60 # 5 minutes


def get_battery():
    output = os.popen('termux-battery-status').read()

    string_to_find = '"percentage":'
    start = output.find(string_to_find) + len(string_to_find)
    end = output[start:].find(',')

    percentage = output[start:end].strip()
    return percentage


def is_connected():
    output = os.popen('termux-wifi-connectioninfo').read()

    if output.find('null') > -1:
        return False
    else:
        return True

def save_in_file(name, text):
    with open(name, 'w+') as file:
        file.write(text)


if __name__ == "__main__":
    while True:
        try:
            save_in_file(str(sys.argv[1]) + 'battery', get_battery())
            
            if not is_connected():
                os.system('termux-wifi-enable false')
                sleep(10)
                os.system('termux-wifi-enable true')
                sleep(20)
            else:
                sleep(MINUTES_SLEEP) 
        except Exception as e:
            logging.error(e)
            sleep(5)
            continue
