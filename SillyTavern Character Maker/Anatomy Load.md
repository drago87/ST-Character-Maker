/ife (context != '') {:
	/wi-list-books all=true|
	/setvar key=wiList {{pipe}}|
	/let key=findMale {{noop}}|
	/let key=findFemale {{noop}}|
	/ife ((useAnatomy_f != false) and ('CMC Anatomy' in wiList)) {:
		
		/ife ((parsedAnimalType == 'Fantasy') or (characterArchetype == 'Tauric') or (characterArchetype == 'Pokémon') or (characterType == 'Pokémon') or (characterArchetype == 'Digimon') or (characterType == 'Digimon')) {:
			/ife ((gender == 'Male') or (futanari == 'Yes')) {:
				/var key=findMale "Anatomy: {{getvar::seachPrivatesMale}}: {{getvar::species}}: Male"|
			:}|
			/ife ((gender == 'Female') or (futanari == 'Yes')) {:
				/var key=findFemale "Anatomy: {{getvar::seachPrivatesFemale}}: {{getvar::species}}: Female"|
			:}|
		:}|
		/else {:
			/ife ((gender == 'Male') or (futanari == 'Yes')) {:
				/var key=findMale "Anatomy: {{getvar::seachPrivatesMale}}: Male"|
			:}|
			/ife ((gender == 'Female') or (futanari == 'Yes')) {:
				/var key=findFemale "Anatomy: {{getvar::seachPrivatesFemale}}: Female"|
			:}|
		:}|
		/ife (futanari == 'Yes') {:
			/findentry field=comment file="CMC Anatomy" "{{var::findMale}}"|
			/var key=wi_uid {{pipe}}|
			/getentryfield field=comment file="CMC Anatomy" {{var::wi_uid}}|
			/let key=testComment {{pipe}}|
			/ife ( find == testComment) {:
				/getentryfield field=content file="CMC Anatomy" {{var::wi_uid}}|
				/setvar key=male_genital_structure {{pipe}}|
			:}|
			/findentry field=comment file="CMC Anatomy" "{{var::findFemale}}"|
			/var key=wi_uid {{pipe}}|
			/getentryfield field=comment file="CMC Anatomy" {{var::wi_uid}}|
			/let key=testComment {{pipe}}|
			/ife ( find == testComment) {:
				/getentryfield field=content file="CMC Anatomy" {{var::wi_uid}}|
				/setvar key=female_genital_structure {{pipe}}|
			:}|
			/ife (gender == 'Male') {:
				/var key=find {{var::findMale}}|
			:}|
			/elseif (gender == 'Female') {:
				/var key=find {{var::findFemale}}|
			:}|
		:}|
		/else {:
			/ife (findMale != '') {:
				/var key=find {{var::findMale}}|
			:}|
			/elseif (findFemale != '') {:
				/var key=find {{var::findFemale}}|
			:}|
		:}|
		/ife (futanari == 'Yes') {:
			/re-replace find="/: (Male|Female)/" replace=": Futanari" {{var::find}}|
			/var key=find {{pipe}}|
		:}|
		/findentry field=comment file="CMC Anatomy" "{{var::find}}"|
		/var key=wi_uid {{pipe}}|
		/getentryfield field=comment file="CMC Anatomy" {{var::wi_uid}}|
		/let key=testComment {{pipe}}|
		/ife ( find == testComment) {:
			/getentryfield field=content file="CMC Anatomy" {{var::wi_uid}}|
			/setvar key=genital_structure {{pipe}}|
		:}|
		
		
		/ife ((parsedAnimalType == 'Fantasy') or (characterArchetype == 'Tauric') or (characterArchetype == 'Pokémon') or (characterType == 'Pokémon') or (characterArchetype == 'Digimon') or (characterType == 'Digimon')) {:
			/var key=find "Anatomy: {{getvar::characterArchetype}}: {{getvar::characterType}}: {{getvar::species}}: {{getvar::gender}}"|
		:}|
		/else {:
			/var key=find "Anatomy: {{getvar::characterArchetype}}: {{getvar::characterType}}: {{getvar::parsedAnimalType}}: {{getvar::gender}}"|
		:}|
		/findentry field=comment file="CMC Anatomy" "{{var::find}}"|
		/var key=wi_uid {{pipe}}|
		/getentryfield field=comment file="CMC Anatomy" {{var::wi_uid}}|
		/var key=testComment {{pipe}}|
		/ife ( find == testComment) {:
			/getentryfield field=content file="CMC Anatomy" {{var::wi_uid}}|
			/var key=anatomyPrompt {{pipe}}|
			/ife (anatomyPrompt == '') {: 
			:}|
			/else {:
				/var key=anatomyPrompt "{{getvar::characterArchetype}} Anatomy: {{getvar::characterType}}{{newline}}{{var::anatomyPrompt}}"
			:}|
		:}|
	:}|
	/ife (anatomyPrompt != '') {:
		/var key=context "[{{var::contextStarter}}{{var::context}}{{newline}}{{newline}}{{var::anatomyPrompt}}{{var::contextStopper}}]{{newline}}{{newline}}"|
	:}|
	/else {:
		/var key=context "[{{var::contextStarter}}{{var::context}}{{var::contextStopper}}]{{newline}}{{newline}}"|
	:}|
:}|