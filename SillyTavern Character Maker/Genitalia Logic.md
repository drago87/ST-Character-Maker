/ife (selected_btn != 'No') {:
	/buttons labels=["Yes", "No"] Do you want the character to have Privates that differs from it's species type?|
	/var selected_btn {{pipe}}|
	/ife ( selected_btn == '') {:
		/echo Aborting|
		/abort
	:}|
	/elseif ( selected_btn == 'Yes') {:
		/setvar key=privatesFemale {{noop}}|
		/setvar key=privatesMale {{noop}}|
		/setvar key=searchPrivatesFemale {{noop}}|
		/setvar key=searchPrivatesMale {{noop}}|
		/setvar key=loopGenitalia []|
		/ife (futanari == 'Yes') {:
			/addvar key=loopGenitalia Male|
			/addvar key=loopGenitalia Female|
		:}|
		/elseif (gender == 'Male') {:
			/addvar key=loopGenitalia Male|
		:}|
		/else {:
			/addvar key=loopGenitalia Female|
		:}|
		/foreach {{getvar::loopGenitalia}} {:
			/ife (privates{{var::item}} == '') {:
				/buttons labels=["Mammal", "Reptile", "Bird", "Fish", "Amphibian", "Invertebrate", "Fantasy"] <div>What type of species should the characters {{var::item}} Privates be? This will guide later generations.</div><div>Choosing Fantasy will use the selected species you chose during `Core Identity Generation`.</div>|
				/let key=t {{pipe}}|
				/ife (t == '') {:
					/echo Aborting |
					/abort
				:}|
				/elseif (t != 'Fantasy') {:
					/let key=find {{var::t}}: List|
					/findentry field=comment file="CMC Variables" {{var::find}}|
					/getentryfield field=content file="CMC Variables" {{pipe}}|
					/split find="---" {{pipe}} |
					/setvar key=temp1 {{pipe}}|
					/setvar key=temp {{getvar::temp1}}|
					/addvar key=temp Use Base Type|
					/buttons labels={{getvar::temp}} Select the Species Group you want to use for later when generating the {{var::item}} Privates.|
					/setvar key=temp {{pipe}}|
					/ife ( temp == '') {:
						/echo Aborting|
						/abort
					:}|
					/re-replace find="/\(.*$/g" replace="" {{getvar::temp}}|
					/setvar key=temp {{pipe}}|
					/ife ( temp == 'Use Base Type') {:
						/setvar key=temp {{getvar::animalBase}}|
					:}|
					/ife (futanari == 'Yes') {:
						/buttons labels=["Yes", "No"] Do you want to use the same type of Privates for the Male and Female parts?|
						/var selected_btn {{pipe}}|
						/ife ( selected_btn == '') {:
							/echo Aborting|
							/abort
						:}|
						/elseif ( selected_btn == 'Yes') {:
							/buttons labels=["Yes", "No"] <div>Do you want to use the same base for the female genitalia as the base character?</div><div>{{getvar::characterArchetype}}: {{getvar::characterType}}</div>|
							/let key=tempPrivateFemale {{pipe}}|
							/ife (tempPrivateFemale == 'Yes') {:
								/setvar key=privatesFemale {{getvar::temp}}|
								/setvar key=searchPrivatesFemale {{getvar::characterArchetype}}: {{getvar::characterType}}: {{getvar::temp}}|
							:}|
							/elseif (tempPrivateFemale == 'No') {:
								/buttons labels=["Help me Decide", "Human", "Anthropomorphic\n(Anthropomorphic is a character that combines both human and animal traits, often featuring an animal body with human-like posture, facial expressions, speech, and behavior.)", "Mythfolk\n(Mythfolk is races that mostly looks like humans like Dwarfs, Elves etc...)", "Tauric\n(Tauric are hybrid species with a humanoid upper body and an animal-like lower body, such as centaurs, lamias, and mermaids.)", "Beastkin\n(Beastkin is a character with animal features like ears and tail but otherwise human appearance.)", "Animalistic\n(Animalistic refers to standard animals, fantasy creatures, or monsters that behave and appear primarily as non-human beings, typically walking on all fours and lacking human speech or reasoning.)", "Pokémon", "Digimon", "Android\n(Android is a robot that looks and acts like a Human.)"] What type of character are you making? |
								/re-replace find="/(\n\()[\s\S]*$/g" replace="" {{pipe}}|
								/setvar key=tempFemaleGenitaliaCharacterArchetype {{pipe}}|
								/re-replace find="/\(.*$/g" replace="" {{getvar::tempFemaleGenitaliaCharacterArchetype}}|
								/setvar key=tempFemaleGenitaliaCharacterArchetype {{pipe}}|
								
								/var selected_btn {{noop}}|
								/ife ( tempFemaleGenitaliaCharacterType != '' ) {:
									/buttons labels=["Yes", "No"] Do you want to change the character type?|
									/var selected_btn {{pipe}}|
									/ife ( selected_btn == '') {:
										/echo Aborting|
										/abort
									:}|
								:}|
								/ife ( (selected_btn == 'Yes') or (tempFemaleGenitaliaCharacterType == '')) {:
									/setvar key=tempFemaleGenitaliaCharacterType None|
								:}|
								/ife (((tempFemaleGenitaliaCharacterType == 'None') or ( selected_btn == 'Yes')) and (( tempFemaleGenitaliaCharacterArchetype == 'Anthropomorphic') or ( tempFemaleGenitaliaCharacterArchetype == 'Beastkin') or ( tempFemaleGenitaliaCharacterArchetype == 'Digimon') or ( tempFemaleGenitaliaCharacterArchetype == 'Pokémon'))) {:
									/buttons labels=["Pokémon", "Digimon", "Animalistic"] Select the type you want?|
									/setvar key=tempFemaleGenitaliaCharacterType {{pipe}}|
									/ife ( tempFemaleGenitaliaCharacterType == '') {:
										/echo Aborting|
										/abort
									:}|
								:}|
								/setvar key=privatesFemale {{getvar::temp}}|
								/setvar key=searchPrivatesFemale {{getvar::tempFemaleGenitaliaCharacterArchetype}}: {{getvar::tempFemaleGenitaliaCharacterType}}: {{getvar::temp}}|
							:}|
							
							/elseif ( selected_btn == 'Yes') {:
							/buttons labels=["Yes", "No"] <div>Do you want to use the same base for the male genitalia as the base character?</div><div>{{getvar::characterArchetype}}: {{getvar::characterType}}</div>|
							/let key=tempPrivateMale {{pipe}}|
							/ife (tempPrivateMale == 'Yes') {:
								/setvar key=privatesMale {{getvar::characterArchetype}}: {{getvar::characterType}}: {{getvar::temp}}|
							:}|
							/elseif (tempPrivateMale == 'No') {:
								/buttons labels=["Help me Decide", "Human", "Anthropomorphic\n(Anthropomorphic is a character that combines both human and animal traits, often featuring an animal body with human-like posture, facial expressions, speech, and behavior.)", "Mythfolk\n(Mythfolk is races that mostly looks like humans like Dwarfs, Elves etc...)", "Tauric\n(Tauric are hybrid species with a humanoid upper body and an animal-like lower body, such as centaurs, lamias, and mermaids.)", "Beastkin\n(Beastkin is a character with animal features like ears and tail but otherwise human appearance.)", "Animalistic\n(Animalistic refers to standard animals, fantasy creatures, or monsters that behave and appear primarily as non-human beings, typically walking on all fours and lacking human speech or reasoning.)", "Pokémon", "Digimon", "Android\n(Android is a robot that looks and acts like a Human.)"] What type of character are you making? |
								/re-replace find="/(\n\()[\s\S]*$/g" replace="" {{pipe}}|
								/setvar key=tempMaleGenitaliaCharacterArchetype {{pipe}}|
								/re-replace find="/\(.*$/g" replace="" {{getvar::tempMaleGenitaliaCharacterArchetype}}|
								/setvar key=tempMaleGenitaliaCharacterArchetype {{pipe}}|
								
								/var selected_btn {{noop}}|
								/ife ( tempMaleGenitaliaCharacterType != '' ) {:
									/buttons labels=["Yes", "No"] Do you want to change the character type?|
									/var selected_btn {{pipe}}|
									/ife ( selected_btn == '') {:
										/echo Aborting|
										/abort
									:}|
								:}|
								/ife ( (selected_btn == 'Yes') or (tempMaleGenitaliaCharacterType == '')) {:
									/setvar key=tempMaleGenitaliaCharacterType None|
								:}|
								/ife (((tempMaleGenitaliaCharacterType == 'None') or ( selected_btn == 'Yes')) and (( tempMaleGenitaliaCharacterArchetype == 'Anthropomorphic') or ( tempMaleGenitaliaCharacterArchetype == 'Beastkin') or ( tempMaleGenitaliaCharacterArchetype == 'Digimon') or ( tempMaleGenitaliaCharacterArchetype == 'Pokémon'))) {:
									/buttons labels=["Pokémon", "Digimon", "Animalistic"] Select the type you want?|
									/setvar key=tempMaleGenitaliaCharacterType {{pipe}}|
									/ife ( tempMaleGenitaliaCharacterType == '') {:
										/echo Aborting|
										/abort
									:}|
								:}|
								/setvar key=privatesMale {{getvar::tempMaleGenitaliaCharacterArchetype}}: {{getvar::tempMaleGenitaliaCharacterType}}{{getvar::temp}}|
							:}|
						:}|
						/elseif ( selected_btn == 'No') {:
							/setvar key=privates{{var::item}} {{getvar::characterArchetype}}: {{getvar::characterType}}: {{getvar::temp}}|
						:}|
					:}|
				:}|
				/else {:
					/setvar key=privates{{var::item}} "To be selected"|
					/getvar key=loopGenitalia index=1|
					/setvar key=check {{pipe}}|
					/ife (check == '') {:
						/ife (item != 'Male') {:
							/setvar key=privatesFemale None|
							/setvar key=searchPrivatesFemale None|
						:}|
						/ife (item != 'Female') {:
							/setvar key=privatesMale None|
							/setvar key=seachPrivatesMale None|
						:}|
					:}|
				:}|
			:}|
		:}|
	:}|
	/elseif (selected_btn == 'No') {:
		/ife (animalBase == 'Fantasy') {:
			/ife (futanari == 'Yes') {:
				/setvar key=privatesFemale "To be selected"|
				/setvar key=privatesMale "To be selected"|
			:}|
			/elseif (gender == 'Male') {:
				/setvar key=privatesFemale None|
				/setvar key=privatesMale "To be selected"|
			:}|
			/elseif (gender == 'Female') {:
				/setvar key=privatesFemale "To be selected"|
				/setvar key=privatesMale None|
			:}|
		:}|
		/elseif (futanari == 'Yes') {:
			/setvar key=privatesFemale {{getvar::characterArchetype}}: {{getvar::characterType}}: {{getvar::animalBase}}|
			/setvar key=privatesMale {{getvar::characterArchetype}}: {{getvar::characterType}}: {{getvar::animalBase}}|
		:}|
		/elseif (gender == 'Male') {:
			/setvar key=privatesFemale None|
			/setvar key=privatesMale {{getvar::characterArchetype}}: {{getvar::characterType}}: {{getvar::animalBase}}|
		:}|
		/else {:
			/setvar key=privatesFemale {{getvar::characterArchetype}}: {{getvar::characterType}}: {{getvar::animalBase}}|
			/setvar key=privatesMale None|
		:}|
	:}|
	/flushvar temp|
	/flushvar temp1|
	/flushvar loopGenitalia|
	/flushvar tempMaleGenitaliaCharacterArchetype|
	/flushvar tempFemaleGenitaliaCharacterArchetype|
	/flushvar tempPrivateFemale|
	/flushvar tempPrivateMale|
	
:}|