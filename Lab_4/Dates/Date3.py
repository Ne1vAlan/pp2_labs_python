from datetime import datetime

current_time = datetime.now()

time_without_microseconds = current_time.replace(microsecond=0)

print("Time with microseconds:", current_time)
print("Time without microseconds:", time_without_microseconds)