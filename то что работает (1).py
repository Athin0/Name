

import matplotlib.pyplot as plt
import librosa.display


import librosa
audio_data = r'C:\Users\arina\Downloads\Моцарт Вольфганг Амадей - Соната 16 в до мажоре.wav'
x , sr = librosa.load(audio_data)
print(type(x), type(sr))
#<class 'numpy.ndarray'> <class 'int'>
print(x.shape, sr)
#(94316,) 22050
#незнайка 2т — В траве сидел кузнечик минус
#Моцарт В. А. - Соната для скрипки и фортепиано до мажор 
#Моцарт Вольфганг Амадей - Соната 16 в до мажоре
#Wolfgang Amadeus Mozart - Симфония № 5 (Allegro con brio).wav
#in E-Major Etude No. 1 , Op. 65 (Live) (192 kbps) (4).wav
#Lang Lang - Mozart Piano Sonata No. 16 in C Major, K. 545 Sonata facile - 3. Rondo. Allegretto_(Inkompmusic.ru)



import IPython.display as ipd
ipd.Audio(audio_data)



librosa.load(audio_data, sr=44100)



X = librosa.stft(x)
Xdb = librosa.amplitude_to_db(abs(X))
plt.figure(figsize=(14, 5))
librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='log')
plt.colorbar()



chromagram = librosa.feature.chroma_stft(x, sr=sr)
plt.figure(figsize=(15, 5))
librosa.display.specshow(chromagram, x_axis='time', y_axis='chroma', cmap='coolwarm')



import numpy as np
audio_data = r'C:\Users\arina\Downloads\Моцарт В. А. - Соната для скрипки и фортепиано до мажор .wav'
y, sr = librosa.load(audio_data,sr=44100)
S = np.abs(librosa.stft(y, n_fft=4096))**2
chroma = librosa.feature.chroma_stft(S=S, sr=sr)
chroma
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
img = librosa.display.specshow(chroma, y_axis='chroma', x_axis='time', ax=ax)
fig.colorbar(img, ax=ax)
ax.set(title='Chromagram')


#


import numpy as np
audio_data = r'C:\Users\arina\Downloads\Wolfgang Amadeus Mozart Классическая музыка для медитации - Divertimento No. 11 for oboe, 2 horns & strings in D major, K. 251 Andantino_(Inkompmusic.ru).wav'
y, sr = librosa.load(audio_data,sr=sr)
S = np.abs(librosa.stft(y, n_fft=4096))**2
chroma = librosa.feature.chroma_stft(S=S, sr=sr)
chroma
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
img = librosa.display.specshow(chroma, y_axis='chroma', x_axis='time', ax=ax)
fig.colorbar(img, ax=ax)
ax.set(title='Chromagram')






