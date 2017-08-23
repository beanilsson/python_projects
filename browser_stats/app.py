import csv
import pdb

supported_browsers = ['Android', 'Blackberry', 'Chrome', 'Facebook', 'Firefox' 'Safari', 'Mobile', 'mobile']

mobile_browsers = []
with open('browser_data.csv', 'r') as f:
     rows = f.readlines()
     for row in rows:
         for browser in supported_browsers:
             if row not in mobile_browsers:
                 if row.find(browser) == 0:
                     mobile_browsers.append(row)


with open('mobile_browsers.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)
    for mb in mobile_browsers:
        writer.writerow(mb)
