/setvar key=extra []|
/ife ( (characterArchetype != 'Human') and (characterArchetype != 'Tauric') and (characterArchetype != 'Demi-Human') and (characterArchetype != 'Pokémon') and (characterArchetype != 'Digimon') and (characterArchetype != 'Android')){:
	/ife ( (characterType != 'Animalistic') and (characterType != 'None')) {:
		/addvar key=extra "{{getvar::characterArchetype}} {{getvar::characterType}}"|
	:}|
	/else {:
		/addvar key=extra "{{getvar::characterArchetype}} Animalistic"|
	:}|
:}|
/elseif (characterArchetype == 'Tauric') {:
	/addvar key=extra "Tauric"|
:}|