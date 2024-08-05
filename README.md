# Spotify Voice Assistant

## Açıklama

Spotify Voice Assistant, Python kullanılarak geliştirilmiş bir sesli komut uygulamasıdır. Bu uygulama, Spotify API'sini kullanarak şarkıları sesli komutlarla oynatma, durdurma, sıraya ekleme ve favorilere ekleme işlemlerini gerçekleştirir. Arka planda Spotify'ı yönetmenizi sağlar, böylece diğer işlerinizi yaparken Spotify'ı kontrol edebilirsiniz.

## Özellikler

- **Şarkı Oynatma:** Sesli komutlarla şarkı araması yaparak şarkıyı oynatın.
- **Durdurma ve Devam Ettirme:** Çalan şarkıyı durdurabilir veya devam ettirebilirsiniz.
- **Sonraki ve Önceki Şarkı:** Sonraki veya önceki şarkıya geçiş yapabilirsiniz.
- **Sıraya Ekleme:** Şarkıları çalma listesine ekleyin.
- **Favorilere Ekleme ve Çıkarma:** Şarkıları favorilere ekleyin veya favorilerden çıkarın.
- **Karışık ve Sıralı Çalma:** Favorilerinizi karışık veya sıralı olarak çalın.

## Gereksinimler

- Python 3.x
- `spotipy` kütüphanesi
- `speech_recognition` kütüphanesi
- `pyaudio` kütüphanesi (ses girişi için)


## API Bilgileri

spotify.py dosyasını düzenleyin ve Spotify API bilgilerinizi ekleyin.

https://developer.spotify.com/ adresinden alabilirsiniz.

## Kurulum

Bu repo'yu klonlayın:
```bash
git clone https://github.com/zwennnnn/Spotify-Voice-Assistant

pip install spotipy SpeechRecognition pyaudio

python spotify.py
```

## Kullanım

Program çalıştığında, sesli komutlarınızı dinlemeye başlar. Şu komutları kullanabilirsiniz:

- `oynat [şarkı adı] [şarkı sahibi]`: Şarkıyı oynatır.
- `durdur`: Çalan şarkıyı durdurur.
- `sonraki`: Sonraki şarkıya geçer.
- `önceki`: Önceki şarkıya döner.
- `sıraya ekle [şarkı adı]`: Şarkıyı sıraya ekler.
- `favorilere ekle`: Çalan şarkıyı favorilere ekler.
- `favorilere ekle [şarkı adı]`: Şarkıyı favorilere ekler.
- `favorilerden çıkar [şarkı adı]`: Şarkıyı favorilerden çıkarır.
- `karışık çal`: Favorileri karışık olarak çalar.
- `sıralı çal`: Favorileri sıralı olarak çalar.
- `programdan çık`: Programdan çıkış yapar.



