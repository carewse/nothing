from pydub import AudioSegment
from pydub.silence import detect_silence
song = AudioSegment.from_mp3('Where-IS-Bear.mp3')
start_end = detect_silence(song,300,-35,1)
start = start_end[0][1]
n=0;
for i in start_end[1:]:
    end = i[0]
    song[start:end].export('sli_mp3/'+str(n)+'.mp3',format='mp3')
    start = i[1]
    n=n+1
