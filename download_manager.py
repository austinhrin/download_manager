import urllib
import urllib.request
import os
from time import sleep
import random

download_folder = 'downloads'
# if true it will add a delay between downloads
delay_downloads = True

current_directory = os.getcwd()
downloads_folder = current_directory + f'/{download_folder}'
file_with_urls = current_directory + f'/downloads.txt'

# create folder if it doesn't exist
if os.path.isdir(downloads_folder) != True:
    os.makedirs(download_folder)

# setup user agent
opener = urllib.request.build_opener()
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36'
opener.addheaders = [('User-Agent', user_agent)]
urllib.request.install_opener(opener)

# download files
with open(file_with_urls, 'r') as urls:
    for url in urls:
        # remove line break
        url = url.replace('\n', '')
        url_split = url.split('/')
        filename = url_split[len(url_split)-1]
        save_file_path = downloads_folder + f'/{filename}'
        # check if file exists
        if os.path.isfile(save_file_path):
            print(f'File exists skipping.. {filename}')
        else:
            #print("File not exist")
            try:
                urllib.request.urlretrieve(url, save_file_path)
                if delay_downloads == True:
                    sleep(0.5*random.uniform(1, 3))
            except:
                print(f'Failed to download {filename}')
