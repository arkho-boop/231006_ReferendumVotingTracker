import time
import FtpPullFunctions

while True:
    try:
        new_log = FtpPullFunctions.list_directory(r'29581/Detailed/Verbose')

        # Compare new_log and prior_log to find the difference
        added_files = [file for file in new_log if file not in prior_log]
        removed_files = [file for file in prior_log if file not in new_log]

        # Update prior_log with the current new_log
        prior_log = new_log

        # Save prior_log to "file_log.txt" every time it's updated
        with open('file_log.txt', 'w') as f:
            f.write('\n'.join(prior_log))

        # Do something with the added_files and removed_files lists
        # For example, print them
        if added_files:
            print("Added files:", added_files)
            for filename in added_files:
                FtpPullFunctions.aec_ftp_pull(r'29581/Detailed/Verbose', filename, 'cache')
        if removed_files:
            print("Removed files:", removed_files)
    except Exception as e:
        # Handle exceptions, e.g., print an error message
        print("Error:", e)

    # Add a delay (e.g., sleep for a certain time) to control how often you check the directory
    # This is important to avoid continuous polling and reduce resource consumption
    time.sleep(60)  # Sleep for 60 seconds (adjust as needed)
