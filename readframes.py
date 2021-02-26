import wave


goodmorning = wave.open('good-morningMan.wav', 'r')

frames = goodmorning.readframes(-1)

print(frames[:10])