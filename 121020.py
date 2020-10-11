#!/usr/bin/env python
# coding: utf-8

# In[52]:


import matplotlib.pyplot as plt
import librosa.display
import numpy as np
import librosa
from PIL import _imaging

audio_data = r'C:\Users\arina\Documents\Проект\WAV\Mozart Piano Sonata No. 16 in C Major.wav'
x , sr = librosa.load(audio_data,sr=44100)
print(type(x), type(sr))
#<class 'numpy.ndarray'> <class 'int'>
print(x.shape, sr)


#in E-Major  Etude No. 1 , Op. 65 
#Mozart - Divertimento No. 11 for oboe, 2 horns & strings in D major
#Mozart - Симфония № 5        #G major
#Mozart Piano Sonata No. 16 in C Major
#Моцарт В. А. - Соната для скрипки и фортепиано до мажор 
#Моцарт Вольфганг Амадей - Соната 16 в до мажоре

#1do
#В траве сидел кузнечик минус       (Ля-минор(А))
#В траве сидел
#Мажорное трезвучие - Б35
#подбор по слуху трезвучие - I-III-V-I до мажор
#Распевка - мажорное трезвучие


y, sr = librosa.load(audio_data,sr=44100)
S = np.abs(librosa.stft(y, n_fft=4096))**2
chroma = librosa.feature.chroma_stft(S=S, sr=sr)
chroma
fig, ax = plt.subplots()
img = librosa.display.specshow(chroma, y_axis='chroma', x_axis='time', ax=ax)
fig.colorbar(img, ax=ax)
ax.set(title='Chromagram')


# In[53]:


b=['C','C♯ / D♭','D','D♯ / E♭','E','F','F♯ / G♭','G','G♯ / A♭','A','A♯ / B♭','H?B']
a=[]
for i in chroma:
    l=len(i)
    m=i
    sum=0
    for j in range(l):
        if m[j]>=0.8 :
            sum+=m[j]
    a.append(sum)
    
max = a[0]
pos = 0
for i in range(0,len(a)):
    if a[i]>max: max=a[i];pos=i
print ("max=", max,", cord=", b[pos])


# In[54]:



max_1, max_2, max_3 = sorted(a)[-1], sorted(a)[-2], sorted(a)[-3]
print (b[a.index(max_1)])
print (b[a.index(max_2)])
print (b[a.index(max_3)])


# In[29]:


import IPython.display as ipd
ipd.Audio(audio_data)


# In[35]:


a=['C','C♯ / D♭','D','D♯ / E♭','E','F','F♯ / G♭','G','G♯ / A♭','A','A♯ / B♭','B']

for i in chroma:
    l=len(i)
    m=i
    sum=0
    for j in range(l):
        if m[j]>=0.8 :
            sum+=m[j]
    a.append(sum)
    
max = a[12]
pos = 12
for i in range(12,len(a)):
    if a[i]>max: max=a[i];pos=i
print ("max=", max,", cord=", a[pos-12])


# In[36]:


for i in range (12):
    print(a[i], '==', round(a[i+12]))
    print()


# In[ ]:





# In[ ]:


from os import path
from pydub import AudioSegment
directory = r'C:\Users\arina\Documents\Проект\Mozart - Complete Piano Sonatas (Voskresenskiy) [5 CD] [V0]\1 01-03 Piano Sonata 1 in С major, KV 279 (189d)'
files = os.listdir(directory)
for k in range(0,3):
  files[k] = (files[k].replace(".mp3", ""))
  print(files[k])
for k in range(0,3):
  src = "{}{}{}".format('C:/Users/arina/Documents/Проект/Mozart - Complete Piano Sonatas (Voskresenskiy) [5 CD] [V0]/1 01-03 Piano Sonata 1 in С major, KV 279 (189d)/',files[k] ,".mp3")
  dst = "{}{}{}".format('C:/Users/arina/Documents/Проект/wav_mp3/',files[k],".wav")
# convert wav to mp3
  sound = AudioSegment.from_mp3(src)
  sound.export(dst, format="wav")


# In[ ]:




