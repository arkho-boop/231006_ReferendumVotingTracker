from ftplib import FTP

def aec_ftp_pull(remote_filedir, filename, local_directory):
    ftp_host = 'mediafeed.aec.gov.au'
    ftp_port = 21
    ftp_user = 'anonymous'
    ftp_password = 's'

    # Create an FTP object and connect to the server
    ftp = FTP()
    ftp.connect(ftp_host, ftp_port)

    # Log in with your credentials
    ftp.login(ftp_user, ftp_password)

    print('logged in')

    # Specify the remote file path (path on the FTP server)
    remote_file_path = remote_filedir + '/' + filename  

    print('remote_file_path: ' + remote_file_path)

    # Specify the local file path (including the directory where you want to save the file)
    local_file_path = local_directory + '/' + filename

    print('local_file_path: ' + local_file_path)

    # Change working directory
    ftp.cwd(remote_filedir)

    print('changed working directory to ' + remote_filedir)

    # Download the file from the FTP server to the specified local directory
    with open(local_file_path, 'wb') as local_file:
        ftp.retrbinary('RETR ' + filename, local_file.write)

    # Close the FTP connection
    ftp.quit()

def list_directory(remote_filepath):
    # FTP server details
    ftp_host = 'mediafeed.aec.gov.au'
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

    