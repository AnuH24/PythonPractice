def make_album(name,title,songs=None):
    album={"artist_name":name,"album_title":title}
    if songs:
        album["songs"]=songs
    return album
new_album=make_album("DSP","Karige Loga")
print(new_album)
new_album=make_album("SPB","Nuvvu natho",3)
print(new_album)
new_album=make_album("Thaman","Kajal Chelliva",5)
print(new_album)