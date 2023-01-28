from flask import Flask, render_template, request


profile_selected=""  


app = Flask(__name__)


@app.route('/')
def index():
    return render_template ('index.html')

@app.route('/profile_selection', methods=['POST'])
def post_message():
    me = {
        'name': 'Coach Julian',
        'pic': 'https://upload.wikimedia.org/wikipedia/commons/0/0b/Netflix-avatar.png',
        'here_before': True,
        'movie' : 'https://www.youtube.com/watch?v=vxvP9zSOL7s',
        'photos': ['https://static.bunnycdn.ru/i/cache/images/4/42/422670a855efae8d8d8fafb59d43c197.jpg', 'https://static.bunnycdn.ru/i/cache/images/2018/04/ef7eece108cfbe794eb505dc983f7fe4.jpg', 'https://static.bunnycdn.ru/i/cache/images/2018/05/4c127405d9fa8f78a9d86052721cbefe.jpg','https://static.bunnycdn.ru/i/cache/images/2019/04/961fbb823be55a3f4310c7cc944ec585.jpg']
    }

    leech = {
        'name': 'Leech',
        'pic': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSAEy-Hi3lntqni03_IgMHV_6nbWR5sG5EuE11oKCej1YqlHvxzo6lfyF7L_JXrJaoZIkY&usqp=CAU',
        'here_before': True,
        'photos': ['https://m.media-amazon.com/images/M/MV5BMjE2NDkxNTY2M15BMl5BanBnXkFtZTgwMDc2NzE0MTI@._V1_QL75_UX100_CR0,3,100,148_.jpg','https://m.media-amazon.com/images/M/MV5BMTc5MDE2ODcwNV5BMl5BanBnXkFtZTgwMzI2NzQ2NzM@._V1_QL75_UX100_CR0,0,100,148_.jpg','https://m.media-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_QL75_UX100_CR0,0,100,148_.jpg', 'https://m.media-amazon.com/images/M/MV5BNDg1NTU2OWEtM2UzYi00ZWRmLWEwMTktZWNjYWQ1NWM1OThjXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_QL75_UX100_CR0,0,100,148_.jpg']
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
        #print(profile_selected)
    elif "Leech" in request.form:
        profile_selected = leech
        #print("2")
    elif "Friends" in request.form:
        profile_selected = friends
    elif "Kids" in request.form:
        profile_selected = kids
     
    return render_template('gallery.html', user=profile_selected)

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')