import requests
import m3u8
url="https://manifest.prod.boltdns.net/manifest/v1/hls/v4/clear/3588749423001/6b1db071-577d-4733-a1bc-1ee075901447/10s/master.m3u8?fastly_token=NjA2NGYwOGJfODFhMDhmMDlkNDliMTQyM2JkNDg1NjNjZmI1NDBkODI5MGVjYmYwMTk0ODE5ODY0Nzg2MjUyN2YxNzFmZjU0Yg%3D%3D"
r=requests.get(url, stream=True)
m3u8_master=m3u8.loads(r.text)
#print(m3u8_master.data)...To viewm3u8 datas in list
m3u8_link=m3u8_master.data["playlists"][0]["uri"]
r=requests.get(m3u8_link, stream=True)
m3u8_playlists=m3u8.loads(r.text)
length=len(m3u8_playlists.data["segments"])
#print(m3u8_playlists.data)...The highest quality playlist is present in [0] of list
with open("video.mp4", "wb") as f:
    for i, segments in enumerate(m3u8_playlists.data["segments"]):
        url=segments["uri"]
        chunk_final=requests.get(url,stream=True)
        f.write(chunk_final.content)
        print(str(length-i)+" segments left")
        i+=1
        
        

