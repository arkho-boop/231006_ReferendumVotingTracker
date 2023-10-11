import zipfile

# Specify the path to the ZIP file you want to unzip
zip_file_path = 'aec-mediafeed-Detailed-Verbose-29581-20230920135814.zip'

# Specify the directory where you want to extract the contents
extracted_directory = 'aec-mediafeed-Detailed-Verbose-29581-20230920135814'

# Create a ZipFile object and extract the contents
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extracted_directory)

# The contents of the ZIP file are now extracted to the specified directory.