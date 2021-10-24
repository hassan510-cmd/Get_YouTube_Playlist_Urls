import csv
import youtube_dl
import sys

playlist_url = sys.argv[1]
#
# ydl_opts = {
#     'quiet': True
# }

youtube_dl_manager = youtube_dl.YoutubeDL(ydl_opts)

def get_urls(playlist_url):
    data = []
    x = youtube_dl_manager.extract_info(f"{playlist_url}", download=False)
    playlist_title=x['title']
    urls_numbers=len(x['entries'])
    for count, i in enumerate(x['entries']):
        data.append(
            {
                'ID':f"{count + 1}",
                'Title':f"{i['title']}",
                'Url':f"{i['webpage_url']}",
                'Duration in minutes':f"{round(int(i['duration'])/60,3)}",
                'state':'waiting'
            }
        )
    return (playlist_title,data)

data = get_urls(playlist_url)
playlist_title=data[0].replace("/","-")
content=data[1]
with open(f'{playlist_title}.csv', 'w', newline='') as current:
    headers = ['ID', 'Title','Url','Duration in minutes','state']
    writer = csv.DictWriter(current, fieldnames=headers)
    writer.writeheader()
    list(map(lambda row: writer.writerow(row), content))


