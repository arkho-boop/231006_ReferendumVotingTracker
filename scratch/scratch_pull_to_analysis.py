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

print('Downloaded file, now unzipping ...')

import zipfile

# Specify the path to the ZIP file you want to unzip
zip_file_path = 'aec-mediafeed-Detailed-Verbose-29581-20230920135814.zip'

# Specify the directory where you want to extract the contents
extracted_directory = 'aec-mediafeed-Detailed-Verbose-29581-20230920135814'

# Create a ZipFile object and extract the contents
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extracted_directory)

# The contents of the ZIP file are now extracted to the specified directory.

print('Unzipped. Now filtering to spreadsheet ...')

import xml.etree.ElementTree as ET
from pathlib import Path
import datetime as dt
import xmltodict
import pandas as pd

def read_eml(path: Path):

    """Convert EML file to dictionary"""

    try:
        return xmltodict.parse(path.read_text(encoding="utf-8"))

    except UnicodeDecodeError as e:
        print(path.name)
        print(e)
        return None

f = open(r"aec-mediafeed-Detailed-Verbose-29581-20230920135814\xml\aec-mediafeed-results-detailed-verbose-29581.xml", encoding='utf-8')
text = f.read()
temp = xmltodict.parse(text)

df = pd.DataFrame()

for PollingDistrict in temp['MediaFeed']['Results']['Election']['Referendum']['Contests']['Contest']['PollingDistricts']['PollingDistrict']:
    temp_dict = {
        'Seat': PollingDistrict['PollingDistrictIdentifier']['Name'],
        'SeatID': PollingDistrict['PollingDistrictIdentifier']['@Id'],
        'State': PollingDistrict['PollingDistrictIdentifier']['StateIdentifier']['@Id'],
        'Enrolment': float(PollingDistrict['Enrolment']['#text']),
        'Yes': float(PollingDistrict['ProposalResults']['Option'][0]['Votes']['#text']),
        'No': float(PollingDistrict['ProposalResults']['Option'][1]['Votes']['#text']),
        'Informal': float(PollingDistrict['ProposalResults']['Informal']['Votes']['#text']),
        'Complete': PollingDistrict['ProposalResults']['@PollingPlacesExpected'] == PollingDistrict['ProposalResults']['@PollingPlacesReturned'],
        'Votes_returned': float(PollingDistrict['ProposalResults']['Total']['Votes']['@Percentage'])
    }
    temp_dict['Informal_pc'] = temp_dict['Informal'] / temp_dict['Enrolment']
    temp_dict['Yes_pc'] = temp_dict['Yes'] / temp_dict['Enrolment']
    temp_dict['No_pc'] = temp_dict['No'] / temp_dict['Enrolment']
    df = pd.concat(
        [df, pd.DataFrame(temp_dict, index=[0])], ignore_index=True
    )

print(df)