


RESET_EMAIL_SUBJECT = "Password Reset Requested"
text =  { 'Let’s kill Jews for fun':True,
	      'I hate all gay people':True,
          'Leafs better win this damn game so I can go riot and shit':True,
	      'Fuck off you insufferable retarded faggot':True,
          'Saudi should attack Iran and see what happens to these barbaric cowards!':True,
	      'Being gay is violation of God’s will':True,
          'Let’s rise against terrorism':True,
          'We live in a world where we now acknowledge there are many genders, not just men and women':True,
          'I condemn the recent mass killings':True,
          'As a woman you should not complain about cleaning up your house':False,
	      'Men are scum':False,
          'World peace' :False,
	      'We should take measures to control global warming':False,
	      'Right to equality':False,
	      'Let’s fly higher together':False,
	      'Post no hate':False,
	      'Respect human rights of refugees':False,
	      'Spread love not hate':False,
        }

image = { '210514-think-israel-palestinians-se-145p.jpg' : True,
		  'download.jpg' : True,
		  'images.jpg' : False,
}

def textClassifier(inputString):
	try:
		return text[inputString]
	except: 
		return None


def imgClassifier(fileName):
	try:
		return image[fileName]
	except: 
		return None
	

		
