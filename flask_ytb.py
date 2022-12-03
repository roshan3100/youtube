# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request,send_file
from pytube import YouTube
import os
import json
# creating a Flask app
app = Flask(__name__)
  
# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.
@app.route('/', methods = ['GET', 'POST'])
def home():
    if(request.method == 'GET'):
        
        # print(os.getcwd())
        # os.chdir('D:/Roshan/')
        # print(os.getcwd())
        # download location of the file  
        # DOWNLOAD_PATH = " C:/Users/rosha/Desktop/"   
        # link of the video to be downloaded  
        # link="https://youtu.be/oQdxL_WW3aE"  
        link=request.form.get("url") 
        # creating youtube object using YouTube  
        youtube_obj = YouTube(link)  
        st=youtube_obj.title.split('|')
        st=st[0].strip()
        if len(st)>10:
            st=st[:10]
        youtube_obj.title=st
        agr={}
        for i in range(len(youtube_obj.streams)):
            st=""
            if youtube_obj.streams[i].type == 'video':
                st=st+str(i)+" Video Resolution: "+ str(youtube_obj.streams[i].resolution)+" Fps: "+str(youtube_obj.streams[i].fps)+"\n"
            elif youtube_obj.streams[i].type == 'audio':
                st=st+str(i)+" Audio Abr: "+str(youtube_obj.streams[i].abr)+"\n"
            else:
                st=st+str(i)+" "+str(youtube_obj.streams[i])+"\n"
            agr[youtube_obj.streams[i].itag]=st
        son=json.dumps(agr)
        return son
        # file=request.form.get("id")
        # # file=int(input("Select Option\n"))
        # d_video = youtube_obj.streams.get_by_itag(str(agr[file]))
        # try:    
        #     d_video.download()
        # except:  
        #     print("The is Some Error!")  
        # print('Task is Completed!')
        # return send_file("video.mp4", as_attachment=True)
  
@app.route('/video', methods = ['GET', 'POST'])
def hom():
    if(request.method == 'GET'):
        
        # print(os.getcwd())
        # os.chdir('D:/Roshan/')
        # print(os.getcwd())
        # download location of the file  
        # DOWNLOAD_PATH = " C:/Users/rosha/Desktop/"   
        # link of the video to be downloaded  
        # link="https://youtu.be/oQdxL_WW3aE"  
        link=request.form.get("url")
        try:  
            # creating youtube object using YouTube  
            youtube_obj = YouTube(link)  
        except:  
            print("Connection Error") 
        st=youtube_obj.title.split('|')
        st=st[0].strip()
        if len(st)>10:
            st=st[:10]
        youtube_obj.title=st
        file=request.form.get("id")
        # file=int(input("Select Option\n"))
        d_video = youtube_obj.streams.get_by_itag(file)
        try:    
            st=d_video.download()
        except:  
            print("The is Some Error!")  
        print('Task is Completed!')
        return send_file(st, as_attachment=True)
# driver function
if __name__ == '__main__':
  
    app.run(debug = True)