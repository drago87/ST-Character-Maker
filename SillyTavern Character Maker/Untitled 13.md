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