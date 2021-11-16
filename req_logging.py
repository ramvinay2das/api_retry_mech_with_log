import functools
import time
import requests
import logging

logging.basicConfig(filename = 'request_log.txt', level = logging.DEBUG,
                    format = '%(asctime)s - %(message)s', datefmt = 
                    '%d-%b-%y %H:%M:%S')

def retry_decor(func, retry=3):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        attemp = 0
        retry_list = [ 502, 503, 504 ]
        while attemp < retry:
            try :
                r = func(*args, **kwargs)
                if r.status_code in retry_list:
                    msg = "server get status "+str(r.status_code)
                    logging.info(msg)
                    attemp += 1
                    time.sleep(2)
                else:
                    return r.text
            except Exception as e:
                logging.info(e)
                attemp += 1
                time.sleep(2)
    return wrapper

@retry_decor
def get_data(url):
    r = requests.get(url, timeout=2)
    return r

if __name__ == "__main__":
    r = get_data("http://127.0.0.1:5000/status/502")
    print(r)
