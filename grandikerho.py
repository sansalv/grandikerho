import numpy as np
import matplotlib.pyplot as plt
import time
import os
import random

"""
Grandikerhon lankutusajan laskuri, jonka myöhästyneet jäsenet joutuvat suorittamaan.
"""

def main():

	# Tyhjennä terminaali
	os.system("cls" if os.name == "nt" else "clear")
	
	# Tulostetaan aloitustekstit
	time.sleep(1)
	print('Tervetuloa Grandikerhoon!')
	time.sleep(2)
	print('\nmyöhässä...')
	time.sleep(2)
	
	# Muuttuja aika on myöhästymisaika
	aika = str(input('\nMikä oli saapumisaikasi RTT:lle sekunnin tarkkuudella? (esim. 9.23.41)\n'))
	aika = [int(i) for i in aika.split('.')]
	
	# Muutetaan myöhästymisaika minuuteiksi myöhässä
	minuutit = (aika[0]-9)*60 + (aika[1]-17) + aika[2]/60
	print(f'\nOlit {int(minuutit//60)} h {int(np.floor(minuutit%60))} min {round(minuutit%1*60)} s myöhässä...')
	time.sleep(2)
	
	# Määritellään g(t)-rangaistusfunktio
	f = lambda t: np.log(1+t)/np.log(5)+0.05*t
	R = lambda t: 0.5*(np.sin(15*t)**2+1)
	g = lambda t: f(t)*R(t)
	
	# Lasketaan minimi- ja maksimirangaistukset lattia- ja kattofunktioiden avulla
	min_minuutit = int(np.floor(f(minuutit)/2))
	min_sekunnit = int(np.ceil(((f(minuutit)/2) % 1) * 60))
	max_minuutit = int(np.floor(f(minuutit)))
	max_sekunnit = int(np.ceil((f(minuutit) % 1) * 60))
	minimi  = f'{min_minuutit} min {min_sekunnit} s'
	maksimi = f'{max_minuutit} min {max_sekunnit} s'
	
	# Tulostetaan rangaistusväli
	print('\nTästä koituu rangaistus välillä...')
	time.sleep(3)
	print( f'\n{minimi} ... {maksimi}' )
	time.sleep(3)
	print('\nRangaistuksesi on...')
	
	# Lasketaan rangaistus g(t) funktiolla
	rangaistus_minuutit = int(np.floor(g(minuutit)))
	rangaistus_sekunnit = int(np.ceil((g(minuutit) % 1) * 60))
	
	# Tulostetaan satunnainen määrä (0-8) pisteitä jännityksen kasaamiseksi
	r = random.randint(0, 8)
	for i in range(r):
		time.sleep(2)
		print('...')
	time.sleep(2)
	
	# Paljastetaan rangaistus
	print(f'{rangaistus_minuutit} min ja {rangaistus_sekunnit} s ! Tsemppiä.')
	
	# Lasketaan ja tulostetaan kellonaika, johon mennessä rangaistus tulee olla suoritettuna
	# Tämä on: 9.17 + 2 min (koodin ajamista varten) + minuutit (myöhästyminen)
	kello_tunti = str(int(9+(2*minuutit+17+2)//60))
	kello_minuutti = str(round((2*minuutit+17+2)%60))
	if int(kello_minuutti) < 10:
		kello_minuutti = '0' + kello_minuutti
	kellonaika = f'{kello_tunti}.{kello_minuutti}'
	print(f'\nTämä tulee olla suoritettuna klo {kellonaika} mennessä.')
	
	# Tulostaa kuinka huono tuuri kävi
	tau = lambda r: (2/np.pi)*np.arcsin(np.sqrt(2*r-1))
	print(f'\nTuurisi oli huonoimman {round((1-tau(R(minuutit)))*100, 2)} %:n joukossa.')

	# Plotataan g(t)-funktio rangaistuksen ympäriltä (+- 30 sek)
	t = np.arange(max(0,minuutit-0.5), minuutit+0.5, 0.001)
	y = g(t)
	plt.plot(t,y)
	plt.plot([minuutit], [g(minuutit)], 'ro')
	time.sleep(3)
	plt.show()

	print(input('\nOtatko nyt opiksi?\n'))

if __name__ == '_main_':
    main()

main()

