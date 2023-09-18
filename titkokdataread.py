import json
import os
import csv

os.system('cls')
numberlist = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22']

with open('ttdata.csv', 'w', newline='', encoding="utf-8") as csvfile:
    fieldnames = ['username', 'followers', 'likecount', 'viewcount', 'videolink', 'videodesc']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    csvfile.close()

viewcount = 0
likecount = 0
totalanalyzed = 0

for a in numberlist:
    with open(f'{a}.json', encoding="utf-8") as json_file:
        ttdata = json.load(json_file)
        for i in ttdata['itemList']:
            viewcount += i['stats']['playCount']
            viewcountUNI = i['stats']['playCount']

            likecount += i['stats']['diggCount']
            likecountUNI = i['stats']['diggCount']

            totalanalyzed += 1


            viewcount2 = "{:,}".format(viewcountUNI)
            likecount2 = "{:,}".format(likecountUNI)
            vlink = f"https://www.tiktok.com/@{i['author']['uniqueId']}/video/{i['id']}?lang=en"

            with open('ttdata.csv', 'a', newline='', encoding="utf-8") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow({'username': i['author']['uniqueId'], 'followers': i['authorStats']['followerCount'], 'likecount': likecount2, 'viewcount':viewcount2, 'videolink': vlink, 'videodesc': i['desc']})
                csvfile.close()


viewcount = "{:,}".format(viewcount)
likecount = "{:,}".format(likecount)

vcavg = int(viewcount.replace(',', '')) / totalanalyzed
vcavg = "{:,}".format(vcavg)

print("Total view count: " + str(viewcount))
print("Total like count: " + str(likecount))
print("Total analyzed: " + str(totalanalyzed))
print("Average view count: " + str(vcavg))
