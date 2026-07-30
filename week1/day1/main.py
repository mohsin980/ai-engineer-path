response_times = [101, 12, 113, 214, 315, 416, 517, 618, 719, 820]
label_times = {
    "low": 100,
    "medium": 150,
    "high": 200,
}

for response_time in response_times:
    if response_time < label_times["low"]:
        print("low response time", label_times["low"])
    elif response_time < label_times["medium"]:
        print("medium response time", label_times["medium"])
    else:
        print("high response time", label_times["high"])