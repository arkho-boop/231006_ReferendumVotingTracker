from ftplib import FTP

# FTP server details
ftp_host = 'mediafeedarchive.aec.gov.au'
ftp_port = 21
ftp_user = 'anonymous'
ftp_password = 's'

# File details
remote_file_path = '/29581/Detailed/Verbose/aec-mediafeed-Detailed-Verbose-29581-20230920135814.zip'
local_file_path = 'aec-mediafeed-Detailed-Verbose-29581-20230920135814.zip'

# Create an FTP object and connect to the server
ftp = FTP()
ftp.connect(ftp_host, ftp_port)

# Log in with your credentials
ftp.login(ftp_user, ftp_password)

# Change the working directory (optional)
# ftp.cwd('/path/to/directory')

# Retrieve the file from the server and save it locally
with open(local_file_path, 'wb') as local_file:
    ftp.retrbinary('RETR ' + remote_file_path, local_file.write)

# Close the FTP connection
ftp.quit()
