from pytube import Search
from pytube import YouTube
import youtube_dl
from flask import Flask, send_file, request
import os

from flask_cors import CORS
app = Flask(__name__)
app.config.from_object(__name__)
CORS(app, resources={r"/*":{'origins':"*"}})

dic = {"users": []}

print(youtube_dl.__file__)

def result(query):
    s = Search(query)
    print(query)
    first_result = str(s.results[0])
    id = first_result.split('=')[1].split(">")[0]
    print(id)
    url = ("https://www.youtube.com/watch?v=" + id)
    print(url)
    vid = YouTube(url)
    print("task 1 complete")
    video = vid.streams.filter(only_audio=True).first()
    print("task 2 complete")
   # out_file = video.download(output_path="C:/Users/Ephre/Documents/adonias projects/VueApps/Mezmur/Mezmur_frontend/src/views/")
    # base, ext = os.path.splitext(out_file)
    # new_file = base + '.mp3'
    # os.rename(out_file, new_file)
    ydl_options = {'formate': "bestaudio"}
    with youtube_dl.YoutubeDL(ydl_options) as dl:
        info = dl.extract_info(url, download = False)
        print("task 3 complete")
        url2 = info['formats'][0]['url']
    dic2 = {"url": url2, "author": vid.author, "title": vid.title}
    return dic2

@app.route('/search/<query>', methods=['GET'])
def ReturnSearchQuery(query):
    s = Search(query)
    print(query)
    first_result = str(s.results[0])
    id = first_result.split('=')[1].split(">")[0]
    print(id)
    url = ("https://www.youtube.com/watch?v=" + id)
    print(url)
    vid = YouTube(url)
    print("task 1 complete")
    video = vid.streams.filter(only_audio=True).first()
    print("task 2 complete")
   # out_file = video.download(output_path="C:/Users/Ephre/Documents/adonias projects/VueApps/Mezmur/Mezmur_frontend/src/views/")
    # base, ext = os.path.splitext(out_file)
    # new_file = base + '.mp3'
    # os.rename(out_file, new_file)
    ydl_options = {'formate': "bestaudio"}
    with youtube_dl.YoutubeDL(ydl_options) as dl:
        info = dl.extract_info(url, download = False)
        print("task 3 complete")
        url2 = info['formats'][0]['url']
    print('Task Completed!') 
    url3 = {"url": url2}
    return url3

@app.route('/searchList/<search>', methods=['GET'])
def ReturnResults(search):
    query = Search(search)
    results = query.results
    returns = {"one":[], "two":[], "three":[], "four":[], "five": [], "six":[]}
    for x in range(6):
        info = str(results[x]).split('=')[1].split(">")[0]
        url = ("https://www.youtube.com/watch?v=" + info)
        result = YouTube(url)
        title = result.title
        author = result.author
        dic = {"title": title, "author": author}
        if x == 0:
            returns["one"].append(dic)
        if x == 1:
            returns["two"].append(dic)
        if x == 2:
            returns["three"].append(dic)
        if x == 3:
            returns["four"].append(dic)
        if x == 4:
            returns["five"].append(dic)
        if x == 5:
            returns["six"].append(dic)

    return returns

@app.route('/Create/<username>/<password>', methods=['GET'])
def CreateUser(username, password):
    user = {"name": username, "password": password, "playlists": []}
    for x in dic["users"]:
        print(x)
        if username == x["name"]:
            return ("username already taken")
    dic["users"].append(user) 
    return dic

@app.route('/SignIn/<username>/<password>', methods=['GET'])
def SignInUser(username, password):
    for x in dic["users"]:
        print(x)
        if username == x["name"]:
            if password == x["password"]:
                return("success")
            
    return("invalid")

@app.route('/createPlaylist/<Id>/<Playlist_name>', methods=['GET'])
def CreatePlaylist(Id, Playlist_name):
    playlist = {"pl_name": Playlist_name, "list": []}
    for x in dic["users"]:
        if Id == x["name"]:
            x["playlists"].append(playlist) 
        

    return dic

@app.route('/playlists/<id>/')
def returnPlaylist(id):
    for x in dic["users"]:
        print(x["name"])
        if id == x["name"]:
            print(id, x["name"])
            return x["playlists"]

    return dic
@app.route('/AddToPlaylist/<id>/<playlist>/<song>')
def AddToplaylist(id, playlist, song):
    for x in dic["users"]:
        print(x["name"])
        if id == x["name"]:
            for l in x["playlists"]:
                if playlist == l["pl_name"]:
                    total = result(song)
                    l["list"].append(total)
                    return total
    return("fail")

@app.route('/withinPlaylist/<id>/<playlist>')
def ReturnPlaylist(id, playlist):
    for x in dic["users"]:
        print(x["name"])
        if id == x["name"]:
            for l in x["playlists"]:
                if playlist == l["pl_name"]:
                    return l["list"]
    return("fail")

if __name__ == "__main__":
    app.run(debug=True)
    print("running!") 