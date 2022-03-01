import csv
import os
import speedtest

# initialize speedtest and set the best server
speedtest = speedtest.Speedtest()
speedtest.get_best_server()

# get and set the download and upload internet speed
speedtest.download()
speedtest.upload(pre_allocate = False)

# get results
speedtest.results.share()
data = speedtest.results.dict()

# creating csv
headers = ['Server ID', 'Sponsor', 'Server Name', 'Timestamp', 'Distance',
           'Ping', 'Download', 'Upload', 'Share', 'IP Address']

ping = int(round(data['ping'], 0))
download = int(round(data['download'] / 1000.0, 0))
upload = int(round(data['upload'] / 1000.0, 0))

row = [data['server']['id'], data['server']['sponsor'],
       data['server']['name'], data['timestamp'],
       data['server']['d'], ping, 
       (download / 1000.0), (upload / 1000.0), 
       speedtest.results._share or '', speedtest.results.client['ip']]

# checking if the csv already exists, if true, does not write the headers
file_name = '/speedtest/speedtest_results.csv'
writeHeaders = True
if os.path.exists(file_name):
    writeHeaders = False

with open(file_name, 'a', encoding='UTF8', newline='') as file:
    writer = csv.writer(file)
    if writeHeaders:
        writer.writerow(headers)
    writer.writerow(row)