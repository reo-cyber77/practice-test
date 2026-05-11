import datetime

def start_timer():
    print("=== Countdown Timer ===")
    
    # 1. Get Inputs
    event_name = input('Enter event name: ')
    event_date_str = input('Enter event date (YYYY-MM-DD): ')
    event_time_str = input('Enter event time (HH:MM): ')

    try:
        # 2. Convert input strings into a single datetime object
        # Combined format: YYYY-MM-DD HH:MM
        full_event_str = f"{event_date_str} {event_time_str}"
        event_datetime = datetime.datetime.strptime(full_event_str, '%Y-%m-%d %H:%M')
        
        # 3. Get current time
        now = datetime.datetime.now()
        print(f"\nCurrent Date and Time: {now.strftime('%Y-%m-%d %I:%M %p')}")

        # 4. Event Expiration Checker
        if event_datetime < now:
            print(f"\nThe event '{event_name}' has already passed.")
        else:
            # 5. Time Calculations (Subtraction creates a 'timedelta' object)
            time_left = event_datetime - now
            
            days = time_left.days
            # Using integer division (//) and modulo (%) to get remaining hours/minutes
            hours = time_left.seconds // 3600
            minutes = (time_left.seconds // 60) % 60

            # 6. Display Results
            print(f"\nTime Remaining Before {event_name}:")
            print(f"{days} days")
            print(f"{hours} hours")
            print(f"{minutes} minutes")

    except ValueError:
        print("Invalid format! Please use YYYY-MM-DD for date and HH:MM for time.")

if __name__ == "__main__":
    while True:
        start_timer()
        print("\n" + "="*20 + "\n")