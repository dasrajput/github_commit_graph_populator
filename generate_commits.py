import os
import random
import argparse
from datetime import datetime, timedelta

def run_command(command):
    os.system(command)

def generate_commits(start_date, end_date):
    current_date = start_date
    while current_date <= end_date:
        if random.random() < 0.7:  # 70% chance of committing on any given day
            num_commits = random.randint(1, 5)  # 1 to 5 commits on a given day
            for _ in range(num_commits):
                commit_time = datetime(
                    current_date.year,
                    current_date.month,
                    current_date.day,
                    random.randint(9, 17),  # Commits between 9 AM and 5 PM
                    random.randint(0, 59),
                    random.randint(0, 59)
                ).strftime('%Y-%m-%dT%H:%M:%S')
                
                commit_message = f"Update on {current_date.strftime('%Y-%m-%d')}"
                
                run_command(f'git commit --allow-empty -m "{commit_message}" --date="{commit_time}"')
        
        current_date += timedelta(days=1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate fake Git commits.")
    parser.add_argument('--start-date', help="Start date in YYYY-MM-DD format.")
    parser.add_argument('--end-date', help="End date in YYYY-MM-DD format. Defaults to today.")

    args = parser.parse_args()

    if args.start_date:
        start_date = datetime.strptime(args.start_date, '%Y-%m-%d')
    else:
        # Default to the beginning of the current year
        today = datetime.now()
        start_date = datetime(today.year, 1, 1)

    if args.end_date:
        end_date = datetime.strptime(args.end_date, '%Y-%m-%d')
    else:
        end_date = datetime.now()

    generate_commits(start_date, end_date)
    
    print(f"Fake commits generated successfully from {start_date.date()} to {end_date.date()}!")