import random
import sys

article = ['the', 'a']
noun = ['woman', 'boy', 'man', 'girl', 'mouse','dog', 'cat']
adv = ['badly', 'happily', 'well', 'loudly', 'speeply', 'sadly']
verb = ['cryed', 'jumped', 'swam', 'ran', 'eat', 'drank', 'laughed', 'hoped']

try:
	line = sys.argv[1]
	line = int(line)
except IndexError:
	line = 5

for i in range(line):
	r_art = article[random.randint(0, len(article)-1)]
	r_noun = noun[random.randint(0, len(noun)-1)]
	r_verb = verb[random.randint(0, len(verb)-1)]

	flag = random.randint(0, 1)

	if flag == 1:
		r_adv = adv[random.randint(0, len(adv)-1)]
		print ('%s %s %s %s' % (r_art, r_noun, r_verb, r_adv))
	else:
		print ('%s %s %s' % (r_art, r_noun, r_verb))
