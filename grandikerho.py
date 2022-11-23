import numpy as np
import time
from os import system
import random

def main():

	#system('clear')
	
	time.sleep(1)
	
	print('Tervetuloa Grandikerhoon!')
	
	time.sleep(2)
	print('\nmyöhässä...')
	time.sleep(2)
	
	aika = str(input('\nMikä oli saapumisaikasi RTT:lle sekunnin tarkkuudella? (esim. 9.23.41)\n'))
	aika = [int(i) for i in aika.split('.')]
	
	minuutit = (aika[0]-9)*60 + (aika[1]-17) + aika[2]/60
	
	print(f'\nOlit {int(minuutit//60)} h {int(np.floor(minuutit%60))} min {round(minuutit%1*60)} s myöhässä...')
	time.sleep(2)
	
	f = lambda t: np.log(t)/np.log(5)+0.05*t
	R = lambda t: 0.5*(np.sin(15*t)**2+1)
	g = lambda t: f(t)*R(t)
	
	max_minuutit = int(np.floor(f(minuutit)))
	max_sekunnit = np.ceil((f(minuutit) % 1) * 60)
	
	min_minuutit = int(np.floor(f(minuutit)/2))
	min_sekunnit = np.ceil(((f(minuutit)/2) % 1) * 60)
	
	
	maksimi = f'{max_minuutit} min {max_sekunnit} s'
	minimi  = f'{min_minuutit} min {min_sekunnit} s'
	
	print(f'\nTästä koituu rangaistus välillä...')
	time.sleep(3)
	print( f'\n{minimi} ... {maksimi}' )
	time.sleep(3)
	print('\nRangaistuksesi on...')
	
	rangaistus_minuutit = int(np.floor(g(minuutit)))
	rangaistus_sekunnit = int(np.ceil((g(minuutit) % 1) * 60))
	
	r = random.randint(2, 6)
	
	for i in range(r):
		time.sleep(2)
		print('...')
	time.sleep(2)
	
	print(f'{rangaistus_minuutit} min ja {rangaistus_sekunnit} s ! Tsemppiä.')
	
	kello_tunti = str(int(9+(2*minuutit+17)//60))
	kello_minuutti = str(round((2*minuutit+17)%60))
	if int(kello_minuutti) < 10:
		kello_minuutti = '0' + kello_minuutti
	
	kellonaika = f'{kello_tunti}.{kello_minuutti}'
	
	print(f'\nTämä tulee olla suoritettuna klo {kellonaika} mennessä.\n')

if __name__ == '_main_':
    main()

main()