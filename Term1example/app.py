from flask import Flask, render_template, request
import requests

profile_selected=""
playlist = " " 


app = Flask(__name__)


@app.route('/')
def index():
    return render_template ('index.html')

@app.route('/profile_selection', methods=['POST'])
def post_message():
    
    api_key = "AIzaSyA_K_vgbbsFRtH5WvP3Jx47_TvztoAD4fs"
    
    
    
    
    me = {
        'name': 'Coach Julian',
        'pic': 'https://upload.wikimedia.org/wikipedia/commons/0/0b/Netflix-avatar.png',
        'here_before': True,
        'movie' : 'https://www.youtube.com/watch?v=vxvP9zSOL7s',
        #'photos': ['https://static.bunnycdn.ru/i/cache/images/4/42/422670a855efae8d8d8fafb59d43c197.jpg', 'https://static.bunnycdn.ru/i/cache/images/2018/04/ef7eece108cfbe794eb505dc983f7fe4.jpg', 'https://static.bunnycdn.ru/i/cache/images/2018/05/4c127405d9fa8f78a9d86052721cbefe.jpg','https://static.bunnycdn.ru/i/cache/images/2019/04/961fbb823be55a3f4310c7cc944ec585.jpg']
        'playlist': 'PLFl907chpCa6nKger8cXrlUjoHsLJwl1V'
    }

    leech = {
        'name': 'Leech',
        'pic': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSAEy-Hi3lntqni03_IgMHV_6nbWR5sG5EuE11oKCej1YqlHvxzo6lfyF7L_JXrJaoZIkY&usqp=CAU',
        'here_before': True,
        'photos': ['https://m.media-amazon.com/images/M/MV5BMjE2NDkxNTY2M15BMl5BanBnXkFtZTgwMDc2NzE0MTI@._V1_QL75_UX100_CR0,3,100,148_.jpg','https://m.media-amazon.com/images/M/MV5BMTc5MDE2ODcwNV5BMl5BanBnXkFtZTgwMzI2NzQ2NzM@._V1_QL75_UX100_CR0,0,100,148_.jpg','https://m.media-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_QL75_UX100_CR0,0,100,148_.jpg', 'https://m.media-amazon.com/images/M/MV5BNDg1NTU2OWEtM2UzYi00ZWRmLWEwMTktZWNjYWQ1NWM1OThjXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_QL75_UX100_CR0,0,100,148_.jpg'],
        'playlist': 'PLZHQObOWTQDOjmo3Y6ADm0ScWAlEXf-fp'
    }

    friends = {
        'name': 'Friends',
        'pic': 'https://i.pinimg.com/736x/db/70/dc/db70dc468af8c93749d1f587d74dcb08.jpg',
        'here_before': False,
        'photos': []
    }

    kids = {
        'name': 'Kids',
        'pic': 'https://mir-s3-cdn-cf.behance.net/project_modules/disp/84c20033850498.56ba69ac290ea.png',
        'photos': []
    }

    if "Me" in request.form:
        profile_selected = me
        
    elif "Leech" in request.form:
        profile_selected = leech
        #print("2")
    elif "Friends" in request.form:
        profile_selected = friends
    elif "Kids" in request.form:
        profile_selected = kids

    playlist = profile_selected['playlist']

    response = requests.get(f"https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId={playlist}&key={api_key}")
    parsed_playlist= response.json()

    
    print(parsed_playlist)
    print("1")

    #pulls specific info?
    video_ids = []
    for item in parsed_playlist['items']:
        print(item["id"])
        video_ids.append(item)

    #video_ids= [item['videoId'] for item in playlist['items']]
    #print(videoId)
    return render_template('gallery.html', user=profile_selected, video_ids=video_ids)

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')