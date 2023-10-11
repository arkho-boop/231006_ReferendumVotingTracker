from ftplib import FTP

def aec_ftp_pull(remote_filepath, filename, local_directory):
    # FTP server details
    ftp_host = 'mediafeedarchive.aec.gov.au'
    ftp_port = 21
    ftp_user = 'anonymous'
    ftp_password = 's'

    # Create an FTP object and connect to the server
    ftp = FTP()
    ftp.connect(ftp_host, ftp_port)

    # Log in with your credentials
    ftp.login(ftp_user, ftp_password)

    # Specify the remote file path (path on the FTP server)
    remote_file_path = remote_filepath + '/' + filename  

    # Specify the local file path (including the directory where you want to save the file)
    local_file_path = local_directory + '/' + filename

    # Download the file from the FTP server to the specified local directory
    with open(local_file_path, 'wb') as local_file:
        ftp.retrbinary('RETR ' + remote_filepath, local_file.write)

    # Close the FTP connection
    ftp.quit()

def list_directory(remote_filepath):
    # FTP server details
    ftp_host = 'mediafeedarchive.aec.gov.au'
    ftp_port = 21
    ftp_user = 'anonymous'
    ftp_password = 's'

    # Create an FTP object and connect to the server
    ftp = FTP()
    ftp.connect(ftp_host, ftp_port)

    # Log in with your credentials
    ftp.login(ftp_user, ftp_password)

    # Change directory
    ftp.cwd(remote_filepath)

    # List
    file_list = ftp.nlst()
    ftp.quit()
    
    return(file_list)

    