import os
import vlc
from flask import Flask, render_template, request

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
    if __name__ == __main__:
        app.run(debug=True)

        def play_video(): data = request.get_json()
    video_link = data['audioLink']

    try:
       
        Instance = vlc.Instance()
        player = Instance.media_player_new()
        media = Instance.media_new(video_link)
        player.set_media(media)

    
        player.video_set_spu(False)

        player.play()
        return 'Audio started'
    except Exception as e:
        return f'Errore durante la riproduzione: {str(e)}'