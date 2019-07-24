#import modules needed to pull in data and output result
import os
import csv
import sys

#point to location of cvs file
csvpath = os.path.join('Happy_Coord2.csv')
outpath = os.path.join("Happy_Coord_Dist.csv")


#open data file using defined path
with open(csvpath, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    with open(outpath, 'w', newline='') as outfile:

        # Initialize csv.writer
        csvwriter = csv.writer(outfile, delimiter=',')

        # Write the first row (column headers)
        csvwriter.writerow(['Country1','Happiness Rank1','Happiness Score1','Latitude1','Longitude1',
            'Country2','Happiness Rank2','Happiness Score2','Latitude2','Longitude2','Latitude Distance',
            'Longitude Distance','Distance','Rank Difference','Score Difference'])
            #loop through each row in Coord data to calculate results
        for i, a in enumerate(csvreader) :
            for j, b in enumerate(csvreader):
                if j>i:
                    if a[3]>b[3]:
                        lat_dist = float(a[3])-float(b[3])
                    else :
                        lat_dist = float(b[3])-float(a[3])
                    if a[4]>b[4]:
                        lng_dist = float(a[4])-float(b[4])
                    else :
                        lng_dist = float(b[4])-float(a[4])
                    dist = (lat_dist**2+lng_dist**2)**(1/2)
                    rank_diff = abs(int(a[1])-int(b[1]))
                    score_diff = abs(float(a[2])-float(b[2]))
                    csvwriter.writerow([a[0],a[1],a[2],a[3],a[4],b[0],b[1],b[2],b[3],b[4],
                        lat_dist,lng_dist,dist,rank_diff,score_diff])