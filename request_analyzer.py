#import pandas as pd
#import numpy as np

requests = [
    {"user": "Amy", "status": "success", "tokens": 120},
    {"user": "Bob", "status": "failed", "tokens": 0},
    {"user": "Cindy", "status": "success", "tokens": 250},
    {"user": "David", "status": "success", "tokens": 180},
    {"user": "Eva", "status": "failed", "tokens": 0}
]

def get_failed_users(requests):
    result = []

    for request in requests:
        if request["status"] == "failed":
            result.append(request["user"])
    return result
failed = get_failed_users(requests)
print(failed)

def get_total_tokens(requests):
    total = 0

    for request in requests:
        if request["status"] == "success":
            total += request["tokens"]
    return total
tokens = get_total_tokens(requests)
print(tokens) 

def get_success_rate(requests):
    success_count = 0
    total_count = len(requests)

    for request in requests:
        if request["status"] == "success":
            success_count += 1  #request["status"] #思考成如果這筆是成功，那成功次數就加1
        
        rate = (success_count / total_count)*100
    return rate  
success_rate = get_success_rate(requests)
print(success_rate)
        