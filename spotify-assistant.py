import spotipy
from spotipy.oauth2 import SpotifyOAuth
import speech_recognition as sr
import random

recognizer = sr.Recognizer()
song_queue = []

#Spotify Apı bilgileri
SPOTIPY_CLIENT_ID = 'ILGILI_BILGILERI_DOLDURUNUZ'
SPOTIPY_CLIENT_SECRET = 'ILGILI_BILGILERI_DOLDURUNUZ'
SPOTIPY_REDIRECT_URI = 'http://localhost:8888/callback'

scope = "user-modify-playback-state user-read-playback-state user-library-read user-library-modify"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope=scope))

def kayit():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        ses = recognizer.listen(source)
        return ses

def recognize_speech(ses):
    try:
        yazi = recognizer.recognize_google(ses, language="tr-TR")
        yazi = yazi.lower().strip()

        if "oynat" in yazi:
            query = yazi.replace("oynat", "").replace("çal", "").strip()
            play_song(query)
        elif "durdur" in yazi:
            pause_song()
        elif "sonraki" in yazi:
            next_song()
        elif "önceki" in yazi:
            previous_song()
        elif "devam et" in yazi:
            resume_song()
        elif "sıraya ekle" in yazi:
            query = yazi.replace("sıraya ekle", "").strip()
            add_to_queue(query)
        elif "favorilere ekle" in yazi:
            query = yazi.replace("favorilere ekle", "").strip()
            add_to_favorites(query)
        elif "favorilerden çıkar" in yazi:
            query = yazi.replace("favorilerden çıkar", "").strip()
            remove_from_favorites(query)
        elif "karışık çal" in yazi:
            play_favorites_randomly()
        elif "sıralı çal" in yazi:
            play_favorites_sequentially()
        elif "programdan çık" in yazi:
            print("Programdan çıkılıyor...")
            exit()    
    except sr.UnknownValueError:
        pass
    except sr.RequestError:
        print("Bağlantı hatası, internet bağlantınızı kontrol edin.")

def play_song(query):
    results = sp.search(q=f'track:{query}', limit=1, type='track')
    if results['tracks']['items']:
        track_uri = results['tracks']['items'][0]['uri']
        sp.start_playback(uris=[track_uri])
        print(f"Şarkı oynatılıyor: {query}")
        check_queue()
    else:
        print("Şarkı bulunamadı.")

def pause_song():
    sp.pause_playback()
    print("Şarkı durduruldu")

def resume_song():
    sp.start_playback()
    print("Şarkı devam ettiriliyor")

def next_song():
    if song_queue:
        next_track = song_queue.pop(0)
        sp.start_playback(uris=[next_track])
        print("Sonraki şarkıya geçildi ve sıradaki şarkı çalınıyor.")
    else:
        sp.next_track()
        print("Sonraki şarkıya geçildi.")
    check_queue()

def previous_song():
    sp.previous_track()
    print("Önceki şarkıya döndüm.")
    check_queue()

def add_to_queue(query):
    results = sp.search(q=f'track:{query}', limit=1, type='track')
    if results['tracks']['items']:
        track_uri = results['tracks']['items'][0]['uri']
        song_queue.append(track_uri)
        print(f"Şarkı sıraya eklendi: {query}")
    else:
        print("Şarkı bulunamadı.")

def add_to_favorites(query=None):
    if query:
        results = sp.search(q=f'track:{query}', limit=1, type='track')
        if results['tracks']['items']:
            track_uri = results['tracks']['items'][0]['uri']
            sp.current_user_saved_tracks_add([track_uri])
            print(f"Şarkı favorilere eklendi: {query}")
        else:
            print("Şarkı bulunamadı.")
    else:
        current_track = sp.current_playback()
        if current_track and current_track['is_playing']:
            track_uri = current_track['item']['uri']
            sp.current_user_saved_tracks_add([track_uri])
            print(f"Mevcut şarkı favorilere eklendi: {current_track['item']['name']}")
        else:
            print("Şu anda çalan bir şarkı yok.")

def remove_from_favorites(query):
    results = sp.search(q=f'track:{query}', limit=1, type='track')
    if results['tracks']['items']:
        track_uri = results['tracks']['items'][0]['uri']
        sp.current_user_saved_tracks_delete([track_uri])
        print(f"Şarkı favorilerden çıkarıldı: {query}")
    else:
        print("Şarkı bulunamadı.")

def play_favorites_randomly():
    results = sp.current_user_saved_tracks()
    tracks = results['items']
    if not tracks:
        print("Favoriler listesi boş.")
        return
    random.shuffle(tracks)
    first_track = tracks.pop(0)['track']['uri']
    sp.start_playback(uris=[first_track])
    for track in tracks:
        sp.add_to_queue(track['track']['uri'])
    print("Favoriler karışık olarak çalınıyor.")
    check_queue()

def play_favorites_sequentially():
    results = sp.current_user_saved_tracks()
    tracks = results['items']
    if not tracks:
        print("Favoriler listesi boş.")
        return
    first_track = tracks.pop(0)['track']['uri']
    sp.start_playback(uris=[first_track])
    for track in tracks:
        sp.add_to_queue(track['track']['uri'])
    print("Favoriler sıralı olarak çalınıyor.")
    check_queue()

def check_queue():
    if song_queue:
        next_track = song_queue.pop(0)
        sp.add_to_queue(next_track)
        print("Sıradaki şarkı sıraya eklendi.")

def show_menu():
    print("Hoş geldiniz!")
    print("Bu program, zweNNNN tarafından yapılmıştır.")
    print("Aşağıdaki komutları verebilirsiniz:")
    print("- Oynat [şarkı adı] [şarkı sahibi]: Şarkıyı oynatır.")
    print("- Durdur: Çalan şarkıyı durdurur.")
    print("- Devam et: Duran şarkıyı devam ettirir.")
    print("- Sonraki: Sonraki şarkıya geçer.")
    print("- Önceki: Önceki şarkıya döner.")
    print("- Sıraya ekle [şarkı adı]: Şarkıyı sıraya ekler.")
    print("- Favorilere ekle: Çalan şarkıyı favorilere ekler.")
    print("- Favorilere ekle [şarkı adı]: Söylediğiniz şarkıyı favorilere ekler.")
    print("- Favorilerden çıkar [şarkı adı]: Şarkıyı favorilerden çıkarır.")
    print("- Karışık çal: Favorileri karışık olarak çalar.")
    print("- Sıralı çal: Favorileri sıralı olarak çalar.")
    print("- Programdan Çık : Programdan çıkar.")
    print("Komutları dinliyorum...")

if __name__ == "__main__":
    show_menu()
    while True:
        ses = kayit()
        recognize_speech(ses)
