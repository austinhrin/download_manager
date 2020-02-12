Download Manager in python

Needed a way to download a list of files so I decided to put this script together really quick.

This will download files relative to the folder you have the script in and put them in `/downloads`. It is setup by default to sleep between download but this can be changed by setting `delay_downloads` to False.

Just put a file in the directory with the script called downloads.txt with all the urls in it you want to download on a new line. Then run `python download_manager.py`.
