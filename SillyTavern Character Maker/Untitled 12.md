/let key=anatomyPrompt {{noop}}|
	/var key=find "Anatomy: {{getvar::characterArchetype}}: {{getvar::characterType}}: {{getvar::parsedAnimalType}}: {{getvar::species}}"|
	/findentry field=comment file="CMC Anatomy" "{{var::find}}"|
	/var key=wi_uid {{pipe}}|
	/getentryfield field=comment file="CMC Anatomy" {{var::wi_uid}}|
	/let key=testComment {{pipe}}|
	/ife ( find == testComment) {:
		/getentryfield field=content file="CMC Anatomy" {{var::wi_uid}}|
		/var key=anatomyPrompt {{pipe}}|
		/ife (anatomyPrompt == '') {: 
		:}|
		/else {:
			/var key=anatomyPrompt "{{getvar::characterArchetype}} Anatomy: {{getvar::characterType}}{{newline}}{{var::anatomyPrompt}}"
		:}|
		
	:}|




Anthropomorphic, Tauric, Beastkin, Animalistic, Pokémon, Digimon (Pokémon and Digimon will be done later)
Mammal, Reptile, Bird, Fish, Amphibian, Invertebrate, Fantasy


/setvar key=tagString1 {{noop}}|
/addvar key=tagString1 "{{newline}}"|
/setvar key=tagString2 {{noop}}|
/addvar key=tagString2 "{{newline}}"|
/foreach {{getvar::tags}} {:
	/len {{getvar::tags}}|
	/let key=len {{pipe}}|
	//add {{var::len}} -1|
	/addvar key=tagString1 "            \"{{var::item}}\""|
	/addvar key=tagString2 "        \"{{var::item}}\""|
	/ife (index < len-1) {:
		/addvar key=tagString1 ",{{newline}}"|
		/addvar key=tagString2 ",{{newline}}"|
	:}|
	/else {:
		/addvar key=tagString1 "{{newline}}"|
		/addvar key=tagString2 "{{newline}}"|
	:}
:}|