import wave
import numpy as np
import matplotlib.pyplot as plt


goodmorning = wave.open('good-morningMan.wav', 'r')
Afternoon = wave.open('good-afternoon.wav', 'r')

frames = goodmorning.readframes(-1)
framesAfter = Afternoon.readframes(-1)

#print(frames[:10])
#print(framesAfter[:10])


ondaConvertida = np.frombuffer (frames, dtype='int16')
ondaConvertidaAfter = np.frombuffer (framesAfter, dtype='int16')

#print (ondaConvertida [:10])
#print (ondaConvertidaAfter [:10])

framerate_gm = goodmorning.getframerate()
framerate_af = Afternoon.getframerate()

print(framerate_gm)
print(framerate_af)

time_gm = np.linspace(start=0, stop=len(ondaConvertida)/framerate_gm, num=len(ondaConvertida))
print(time_gm[:10])

time_af = np.linspace(start=0, stop=len(ondaConvertidaAfter)/framerate_af, num=len(ondaConvertidaAfter))
print(time_af[:10])


#GENERACION DE GRAFICA

plt.title('Good morning VS Good afternoon')

#etiquetas de los ejes
plt.xlabel('Tiempo (Segundos)')
plt.ylabel('Amplitud')

#agregar informacion de las ondas
plt.plot(time_af, ondaConvertidaAfter, label="Good Afternoon")
plt.plot(time_gm, ondaConvertida, label="Good Morning", alpha= 0.5)

plt.legend()
plt.show()












