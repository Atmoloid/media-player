import os
import vlc
from flask import Flask, render_template, request

app = Flask(__name__)
@app.route("/",method = ["POST"])
def index():
    return render_template("index.html")
    if __name__ == __main__:
        app.run(debug=True)
        
    @app.route("/play",method = ["POST"])
    def play_audio(): data = request.get_json()
    audio_link = data['audioLink']

    try:
       
        Instance = vlc.Instance()
        player = Instance.media_player_new()
        media = Instance.media_new(audio_link)
        player.set_media(media)

    
        player.video_set_spu(False)

        player.play()
        return 'Audio started'
    except Exception as e:
    return f'Error: {str(e)}