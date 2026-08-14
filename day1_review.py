requests = [
    {"user": "Amy",   "status": "success", "tokens": 150},
    {"user": "Bob",   "status": "failed",  "tokens": 0},
    {"user": "Cindy", "status": "success", "tokens": 300},
    {"user": "David", "status": "failed",  "tokens": 0},
    {"user": "Eva",   "status": "success", "tokens": 200},
    {"user": "Frank", "status": "success", "tokens": 100}
]
# Q1
def get_success_users(requests):
    result = []

    for request in requests:
        if request["status"] == "success":
            result.append(request["user"]) #每次都忘記 .append => 在 list 的最後面新增一個元素

    return result

success_users = get_success_users(requests)
print(success_users)

# Q2
def get_average_tokens(requests):
   
    total = 0
    success_count = 0


    for request in requests:
        if request["status"] == "success":
            total += request["tokens"]
            success_count += 1
    token_average = total / success_count
    return token_average

average = get_average_tokens(requests)
print(average)

        
