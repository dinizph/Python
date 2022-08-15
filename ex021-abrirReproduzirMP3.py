#fazer programa que abre e reproduz arquivo mp3

import vlc

p = vlc.MediaPlayer('.mp3')

p.play()
time.sleep(10)
p.stop()


#resposta usa biblioteca do pygame e tocar um mp3 da msm pasta
