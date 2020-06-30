import random
import antigravity #it takes u to a website of comic on python
def coin_flip():
    	return random.choice(['heads', 'tails'])

if coin_flip() == 'heads':
	print('Heads - You win!')
else:
	print('Tails - You lose!')