import os
from random import randint
from datetime import datetime, timedelta

# Get the current date
current_date = datetime.now()

# Iterate over each day of the current year
for day in range(1, current_date.timetuple().tm_yday + 1):
    
    # Calculate the date for this day
    commit_date = current_date - timedelta(days=day)
    
    # Iterate over a random number of commits for this day
    for commit in range(0, randint(1, 10)):
        # Format the date for Git commit
        d = commit_date.strftime('%a %b %d %X %Y %z')
        
        # Write to file
        with open('file.txt', 'a') as file:
            file.write(d + '\n')
        
        # Stage changes
        os.system('git add .')
        
        # Commit changes with the specified date
        os.system(f'GIT_AUTHOR_DATE="{d}" GIT_COMMITTER_DATE="{d}" git commit -m "commit {day}-{commit}"')

# Push changes to the remote repository
os.system('git push -u origin main')
