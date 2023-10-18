import csv
with open('eggs.csv','w') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ')
    spamwriter.writerow(['Spam','Baked Beans'])
    spamwriter.writerow(['Spam','Lovely Spam','Wonderful Spam'])
    
