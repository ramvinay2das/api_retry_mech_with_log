# api_retry_mech_with_log
flask application of basic status code and python req_log code with retry mechanism

## Steps to follow:
* create a virtual env(optional) and activate the same

* in cmd run : pip install -r requirements.txt (make sure you are in same location where your requirements.txt file is present)
* run python run.py file
* first run run.py file
```python
python run.py
```
* in req_logging.py file change status as required as below and execute
```python
if __name__ == "__main__":
    r = get_data("http://127.0.0.1:5000/status/200")
    print(r)
```
