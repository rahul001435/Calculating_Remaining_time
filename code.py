time = "08:00"
total_hours = 24
total_seconds=86400

entered_hours=int(time[0:2])
entered_minutes = int(time[3:5])
time_spent_seconds = (entered_hours*60*60 + entered_minutes*60)

remain_seconds=total_seconds - time_spent_seconds
#remain hours
print(f"remain hours:{remain_seconds/(60*60)}")
print(f"remain minute:{remain_seconds/60}")
print(remain_seconds)
