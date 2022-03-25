number_of_days = int(input())
daily_plunder = int(input())
expected_plunder = float(input())
gathered_plunder = 0
for i in range (1, number_of_days + 1):
    gathered_plunder += daily_plunder
    if i % 3 == 0:
        gathered_plunder += daily_plunder /2

plunder_left = expected_plunder - gathered_plunder
percentage_left = 100 - (plunder_left / expected_plunder * 100)

if gathered_plunder >= expected_plunder:
    print(f"Ahoy! {gathered_plunder:.2f} plunder gained.")
else:
    print(f"Collected only {percentage_left:.2f}% of the plunder.")