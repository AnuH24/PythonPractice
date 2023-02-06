def make_album(name,title,songs=None):
    album={"artist_name":name,"album_title":title}
    if songs:
        album["songs"]=songs
    return album
while True:
    print(f"\nPlease give details")
    print("Enter q to quit")
    artist_name=input("Artist_Name: ")
    if artist_name == "q":
        break
    album_title=input("Album_Title: ")
    if album_title == "q":
        break
    songs=input("Songs: ")
    if songs == "q":
        break
    new_album=make_album(artist_name,album_title,songs)
    print(f"\n{new_album}")
# new_album=make_album("SPB","Nuvvu natho",3)
# print(new_album)
# new_album=make_album("Thaman","Kajal Chelliva",5)
# print(new_album)