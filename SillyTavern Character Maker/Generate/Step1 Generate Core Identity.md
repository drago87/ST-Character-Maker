/qr-list CMC Main|
/getat index=1 {{pipe}}|
/let qrlabel {{pipe}}|
/qr-get set="CMC Main" label={{var::qrlabel}}|
/getat index="message" {{pipe}}|
/qr-update set="CMC Main" label={{var::qrlabel}} newlabel="Start Generating Core Identity" {{pipe}}|

/:"CMC Logic.Get Char info"|

/setvar key=dataBaseNames []|
/flushvar genSettings|

/setvar key=stepVar Step1|

/setvar key=skip Update|
/ife ( stepDone == 'No') {:
	/buttons labels=["Skip", "Update"] Do you want to skip or update already generated content? You will get a question for each already done if you select Update.|
	/setvar key=skip {{pipe}}|
	/ife ( skip == ''){:
		/echo Aborting |
		/abort
	:}|
:}|

/setvar key=stepDone No|


//Character Overview|
/let key=do {{noop}}|
/let key=variableName {{noop}}|


//Time Period|
/var key=do No|
/var key=variableName "timePeriod"|
/ife ({{var::variableName}} == '') {:
    /var key=do Yes|
:}|
/elseif (skip == 'Update') {:
    /getvar key={{var::variableName}}|
    /buttons labels=["Yes", "No"] Do you want to set or redo {{var::variableName}} (current value: {{pipe}})?|
    /var key=do {{pipe}}|
    /ife (do == '') {:
        /echo Aborting |
        /abort
    :}|
:}|
/ife ( do == 'Yes' ) {:
	/setvar key=genSettings {}|
	/setvar key=genSettings index=wi_book_key "Time Period"|
	/setvar key=genSettings index=combineLorebookEntries No|
	/setvar key=genSettings index=genIsSentence No|
	/setvar key=genSettings index=inputIsList No|
	/setvar key=genSettings index=inputIsTaskList No|
	/setvar key=genSettings index=genIsList Yes|
	/setvar key=genSettings index=outputIsList No|
	/setvar key=genSettings index=needOutput Yes|
	/setvar key=genSettings index=useContext No|
	
	
	/getvar key=genSettings index=inputIsList|
	/let key=inputIsList {{pipe}}|
	/getvar key=genSettings index=combineLorebookEntries|
	/let key=combineLorebookEntries {{pipe}}|
	
	
	/ife ( inputIsList == 'Yes') {:
		/setvar key={{var::variableName}} []|
		/ife ( combineLorebookEntries == 'Yes') {:
			/:"CMC Logic.Combine List Lorebooks"
		:}|
		/foreach {{getvar::genOrder}} {:
			/setvar key=it {{var::item}}|
			/getat index={{var::index}} {{var::genOrderContent}} |
			/var key=content {{pipe}}|
			/:"CMC Logic.GenerateWithSelector"|
			/ife (output != '') {:
				/addvar key={{var::variableName}} {{getvar::output}}|
			:}|
		:}|
	:}|
	/else {:
		/getvar key=genSettings index=wi_book_key|
		/setvar key=it {{pipe}}|
		/:"CMC Logic.GenerateWithSelector"|
		/ife (output != '') {:
			/setvar key={{var::variableName}} {{getvar::output}}|
		:}|
		
	:}|
	/addvar key=dataBaseNames {{var::variableName}}|
	/flushvar output|
	/flushvar guidance|
	/flushvar genOrder|
	/flushvar genContent|
	/flushvar it|
	/flushvar genSettings|
:}|
/else {:
	/addvar key=dataBaseNames {{var::variableName}}|
:}|
//-----------|

//--------|
/var key=do No|
/var key=variableName "settingType"|
/ife ({{var::variableName}} == '') {:
    /var key=do Yes|
:}|
/elseif (skip == 'Update') {:
    /getvar key={{var::variableName}}|
    /buttons labels=["Yes", "No"] Do you want to set or redo {{var::variableName}} (current value: {{pipe}})?|
    /var key=do {{pipe}}|
    /ife (do == '') {:
        /echo Aborting |
        /abort
    :}|
:}|
/ife ( do == 'Yes' ) {:
	/setvar key=genSettings {}|
	/setvar key=genSettings index=wi_book_key "Setting Type"|
	/setvar key=genSettings index=combineLorebookEntries No|
	/setvar key=genSettings index=genIsSentence No|
	/setvar key=genSettings index=genIsList Yes|
	/setvar key=genSettings index=inputIsList No|
	/setvar key=genSettings index=outputIsList No|
	/setvar key=genSettings index=needOutput Yes|
	/setvar key=genSettings index=useContext No|
	/wait {{getvar::wait}}|
	
	/getvar key=genSettings index=wi_book_key|
	/let key=wi_book_key {{pipe}}|
	/getvar key=genSettings index=inputIsList|
	/let key=inputIsList {{pipe}}|
	/getvar key=genSettings index=combineLorebookEntries|
	/let key=combineLorebookEntries {{pipe}}|
	
	
	/ife ( inputIsList == 'Yes') {:
		/setvar key={{var::variableName}} []|
		/ife ( combineLorebookEntries == 'Yes') {:
			/:"CMC Logic.Combine List Lorebooks"
		:}|
		/foreach {{getvar::genOrder}} {:
			/setvar key=it {{var::item}}|
			/getat index={{var::index}} {{getvar::genContent}}|
			/var key=content {{pipe}}|
			/:"CMC Logic.GenerateWithSelector"|
			/addvar key={{var::variableName}} {{getvar::output}}|
		:}|
	:}|
	/else {:
		/setvar key=it {{var::wi_book_key}}|
		/:"CMC Logic.GenerateWithSelector"|
		/setvar key={{var::variableName}} {{getvar::output}}|
	:}|
	/addvar key=dataBaseNames {{var::variableName}}|
	/flushvar output|
	/flushvar guidance|
	/flushvar genOrder|
	/flushvar genContent|
	/flushvar genSettings|
	
:}|
/else {:
	/addvar key=dataBaseNames {{var::variableName}}|
:}|
//-------|

//Race/Species|
/ife ( (characterArchetype != 'Human') and (characterArchetype != 'Android')) {:
	/var key=do No|
	/var key=variableName "species"|
	/ife ({{var::variableName}} == '') {:
	    /var key=do Yes|
	:}|
	/elseif (skip == 'Update') {:
	    /getvar key={{var::variableName}}|
	    /buttons labels=["Yes", "No"] Do you want to set or redo {{var::variableName}} (current value: {{pipe}})?|
	    /var key=do {{pipe}}|
	    /ife (do == '') {:
	        /echo Aborting |
	        /abort
	    :}|
	:}|
	/elseif (skip == 'Update') {:
		/getvar key={{var::variableName}}|
	    /buttons labels=["Yes", "No"] Do you want to redo {{var::variableName}} (current value: {{pipe}})?|
	    /var key=do {{pipe}}|
	    /ife (do == '') {:
	        /echo Aborting |
	        /abort
	    :}|
	:}|
	/ife ( do == 'Yes' ) {:
		/setvar key=genSettings {}|
		/setvar key=genSettings index=wi_book_key "Species"|
		/setvar key=genSettings index=genIsList Yes|
		/setvar key=genSettings index=genAmount 8|
		/setvar key=genSettings index=genIsSentence No|
		/setvar key=genSettings index=inputIsTaskList No|
		/setvar key=genSettings index=needOutput Yes|
		/setvar key=genSettings index=useContext No|
		/setvar key=genSettings index=contextKey []|
		/ife (characterArchetype == 'Mythfolk') {:
			/setvar key=speciesExamples Elf, Dwarf, Vampire, Succubus, Angel, Demon, Halfling, Fairy
		:}|
		/elseif ((characterArchetype != 'Pokémon') and (characterArchetype != 'Digimon')) {:
			
			/let key=find "Reproductive {{getvar::animalBase}}: List"|
			/findentry field=comment file="CMC Static Variables" {{var::find}}|
			/getentryfield file="CMC Static Variables" {{pipe}}| 
			/let key=temp {{pipe}}|
			/split find="/---/" {{var::temp}}|
			/var key=temp {{pipe}}|
			/setvar key=speciesExamples []|
			/ife (parsedAnimalType != animalBase) {:
				/foreach {{var::temp}} {:
					/re-replace find="/(\s*\([^)]*\))/g" replace="" {{var::item}}|
					/let key=tempItem {{pipe}}|
					/ife (('general' not in tempItem)) {:
						/addvar key=speciesExamples {{var::tempItem}}|
					:}|
				:}|
			:}|
			/else {:
				/foreach {{var::temp}} {:
					/re-replace find="/^([^\(]+)/g" replace="" {{var::item}}|
					/addvar key=speciesExamples {{pipe}}|
				:}|
			:}|
			/join {{getvar::speciesExamples}}|
			/setvar key=speciesExamples {{pipe}}|
		:}|
		/elseif (characterArchetype == 'Pokémon') {:
			/setvar key=speciesExamples "Pikachu, Charizard, Bulbasaur, Squirtle, Jigglypuff, Mewtwo, Eevee, Gengar, Lucario, Snorlax"|
		:}|
		/elseif (characterArchetype == 'Digimon') {:
			/setvar key=speciesExamples "Agumon, Gabumon, Patamon, Gatomon, Greymon, Garurumon, Angemon, Tentomon, Biyomon, Omnimon"|
		:}|
		
		/ife ((characterArchetype == 'Anthropomorphic') or (characterArchetype == 'Beastkin') or (characterArchetype == 'Animalistic')) {:
		    /setvar key=formattedSpeciesDescriptor "a {{getvar::parsedAnimalType}} character"|
		:}|
		/elseif (characterArchetype == 'Tauric') {:
		    /setvar key=formattedSpeciesDescriptor "a Tauric {{getvar::parsedAnimalType}} character"|
		:}|
		/elseif (characterArchetype == 'Mythfolk') {:
		    /setvar key=formattedSpeciesDescriptor "a fantasy humanoid character"|
		:}|
		/elseif ((characterArchetype == 'Pokémon') or (characterArchetype == 'Digimon')) {:
		    /setvar key=formattedSpeciesDescriptor "a {{getvar::characterArchetype}} inspired by a {{getvar::parsedAnimalType}}"|
		:}|
		/else {:
		    /setvar key=formattedSpeciesDescriptor "a {{getvar::characterArchetype}} {{getvar::parsedAnimalType}} character"|
		:}|
		
		/setvar key=speciesInstruction {{noop}}|

		/ife ((characterArchetype == 'Anthropomorphic') or (characterArchetype == 'Beastkin') or (characterArchetype == 'Animalistic')) {:
			/setvar key=speciesInstruction "Return a common, real-world animal type in singular form (e.g., Dog, Fox, Tiger)."|
		:}|
		/elseif (characterArchetype == 'Tauric') {:
			/setvar key=speciesInstruction "Return a real-world or mythic animal that could suit a centaur-like body (e.g., Horse, Panther, Dragon)."|
		:}|
		/elseif (characterArchetype == 'Mythfolk') {:
			/setvar key=speciesInstruction "Return a mythological or fantasy humanoid type in singular form (e.g., Elf, Vampire, Succubus)."|
		:}|
		/elseif (characterArchetype == 'Pokémon') {:
			/setvar key=speciesInstruction "Return a canonical Pokémon species name (e.g., Pikachu, Lucario, Eevee)."|
		:}|
		/elseif (characterArchetype == 'Digimon') {:
			/setvar key=speciesInstruction "Return a canonical Digimon species name (e.g., Agumon, Gatomon, Greymon)."|
		:}|
		
		/wait {{getvar::wait}}|
		
		/getvar key=genSettings index=inputIsList|
		/let key=inputIsList {{pipe}}|
		
		
		/ife (outputIsList == 'Yes') {:
			/setvar as=array key={{var::variableName}} []|
		:}|
		/else {:
			/setvar as=string key={{var::variableName}} {{noop}}|
		:}|
		//[[Generate with Prompt]]|
		/:"CMC Logic.GenerateWithPrompt"|
		/ife (output != '') {:
			/setvar key={{var::variableName}} {{getvar::output}}|
		:}|
		/addvar key=dataBaseNames {{var::variableName}}|
		/flushvar output|
		/flushvar guidance|
		/flushvar genOrder|
		/flushvar genContent|
		/flushvar genSettings|
	:}|
	/else {:
		/addvar key=dataBaseNames {{var::variableName}}|
	:}|
:}|
/else {:
	/setvar key=species Human|
	/addvar key=dataBaseNames species|
:}|
//-----------|

/ife (((setBreed == '') or (skip == 'Update')) and (characterArchetype != 'Human') and (characterArchetype != 'Android')) {:
	/buttons labels=["Yes", "No"] Do you want to so set the breed of the character?|
	/setvar key=setBreed {{pipe}}|
	/ife (setBreed == '') {:
		/echo Aborting |
		/abort
	:}|
:}|

//Breed|
/ife ( (characterArchetype != 'Human') and (characterArchetype != 'Android') and (setBreed == 'Yes')) {:
	/var key=do No|
	/var key=variableName "breed"|
	/ife ({{var::variableName}} == '') {:
	    /var key=do Yes|
	:}|
	/elseif (skip == 'Update') {:
	    /getvar key={{var::variableName}}|
	    /buttons labels=["Yes", "No"] Do you want to set or redo {{var::variableName}} (current value: {{pipe}})?|
	    /var key=do {{pipe}}|
	    /ife (do == '') {:
	        /echo Aborting |
	        /abort
	    :}|
	:}|
	/elseif (skip == 'Update') {:
		/getvar key={{var::variableName}}|
	    /buttons labels=["Yes", "No"] Do you want to redo {{var::variableName}} (current value: {{pipe}})?|
	    /var key=do {{pipe}}|
	    /ife (do == '') {:
	        /echo Aborting |
	        /abort
	    :}|
	:}|
	/ife ( do == 'Yes' ) {:
		/setvar key=genSettings {}|
		/setvar key=genSettings index=wi_book_key "Breed"|
		/setvar key=genSettings index=genIsList Yes|
		/setvar key=genSettings index=genAmount 8|
		/setvar key=genSettings index=genIsSentence No|
		/setvar key=genSettings index=inputIsTaskList No|
		/setvar key=genSettings index=needOutput Yes|
		/setvar key=genSettings index=useContext No|
		/setvar key=genSettings index=contextKey []|
		/*
		/ife (characterArchetype == 'Mythfolk') {:
			/setvar key=speciesExamples Elf, Dwarf, Vampire, Succubus, Angel, Demon, Halfling, Fairy
		:}|
		/elseif ((characterArchetype != 'Pokémon') and (characterArchetype != 'Digimon')) {:
			
			/let key=find "Reproductive {{getvar::animalBase}}: List"|
			/findentry field=comment file="CMC Static Variables" {{var::find}}|
			/getentryfield file="CMC Static Variables" {{pipe}}| 
			/let key=temp {{pipe}}|
			/split find="/---/" {{var::temp}}|
			/var key=temp {{pipe}}|
			/setvar key=speciesExamples []|
			/ife (parsedAnimalType != animalBase) {:
				/foreach {{var::temp}} {:
					/re-replace find="/(\s*\([^)]*\))/g" replace="" {{var::item}}|
					/let key=tempItem {{pipe}}|
					/ife (('general' not in tempItem)) {:
						/addvar key=speciesExamples {{var::tempItem}}|
					:}|
				:}|
			:}|
			/else {:
				/foreach {{var::temp}} {:
					/re-replace find="/^([^\(]+)/g" replace="" {{var::item}}|
					/addvar key=speciesExamples {{pipe}}|
				:}|
			:}|
			/join {{getvar::speciesExamples}}|
			/setvar key=speciesExamples {{pipe}}|
		:}|
		/elseif (characterArchetype == 'Pokémon') {:
			/setvar key=speciesExamples "Pikachu, Charizard, Bulbasaur, Squirtle, Jigglypuff, Mewtwo, Eevee, Gengar, Lucario, Snorlax"|
		:}|
		/elseif (characterArchetype == 'Digimon') {:
			/setvar key=speciesExamples "Agumon, Gabumon, Patamon, Gatomon, Greymon, Garurumon, Angemon, Tentomon, Biyomon, Omnimon"|
		:}|
		*|
		/wait {{getvar::wait}}|
		
		/getvar key=genSettings index=inputIsList|
		/let key=inputIsList {{pipe}}|
		
		
		/ife (outputIsList == 'Yes') {:
			/setvar as=array key={{var::variableName}} []|
		:}|
		/else {:
			/setvar as=string key={{var::variableName}} {{noop}}|
		:}|
		//[[Generate with Prompt]]|
		/:"CMC Logic.GenerateWithPrompt"|
		/ife (output != '') {:
			/setvar key={{var::variableName}} {{getvar::output}}|
		:}|
		/addvar key=dataBaseNames {{var::variableName}}|
		/flushvar output|
		/flushvar guidance|
		/flushvar genOrder|
		/flushvar genContent|
		/flushvar genSettings|
	:}|
	/else {:
		/addvar key=dataBaseNames {{var::variableName}}|
	:}|
:}|
/else {:
	/setvar key=breed None|
	/addvar key=dataBaseNames breed|
:}|
//-----------|

/ife ((characterArchetype == 'Mythfolk') and (animalBase == 'None')) {:
	/setvar key=animalBase {{getvar::species}}|
	/addvar key=dataBaseNames animalBase|
	/ife ( ((gender == 'Female') or (futanari == 'Yes')) and (privatesFemale != 'None') ) {:
		/setvar key=privatesFemale {{getvar::species}}|
		/addvar key=dataBaseNames privatesFemale|
	:}|
	/ife ( ((gender == 'Male') or (futanari == 'Yes')) and (privatesFemale != 'None') ) {:
		/setvar key=privatesMale {{getvar::species}}|
		/addvar key=dataBaseNames privatesMale|
	:}|
:}|


/ife ( (characterArchetype != 'Anthropomorphic') and (characterArchetype != 'Beastkin') and (characterArchetype != 'Animalistic') and (characterArchetype != 'Pokémon') and (characterArchetype != 'Digimon')) {:
	//Nationality|
	/var key=do No|
	/var key=variableName "nationality"|
	/ife ({{var::variableName}} == '') {:
	    /var key=do Yes|
	:}|
	/elseif (skip == 'Update') {:
	    /getvar key={{var::variableName}}|
	    /buttons labels=["Yes", "No"] Do you want to set or redo {{var::variableName}} (current value: {{pipe}})?|
	    /var key=do {{pipe}}|
	    /ife (do == '') {:
	        /echo Aborting |
	        /abort
	    :}|
	:}|
	/ife ( do == 'Yes' ) {:
		/setvar key=genSettings {}|
		/setvar key=genSettings index=wi_book_key "Nationalities"|
		/setvar key=genSettings index=genIsList Yes|
		/setvar key=genSettings index=genIsSentence No|
		/setvar key=genSettings index=inputIsTaskList No|
		/setvar key=genSettings index=needOutput Yes|
		/setvar key=genSettings index=useContext Yes|
		/setvar key=genSettings index=contextKey []|
		/wait {{getvar::wait}}|
		
		
		/getvar key=genSettings index=inputIsList|
		/let key=inputIsList {{pipe}}|
		
		
		/ife (outputIsList == 'Yes') {:
			/setvar as=array key={{var::variableName}} []|
		:}|
		/else {:
			/setvar as=string key={{var::variableName}} {{noop}}|
		:}|
		//[[Generate with Prompt]]|
		/:"CMC Logic.GenerateWithPrompt"|
		/ife (output != '') {:
			/setvar key={{var::variableName}} {{getvar::output}}|
		:}|
		/addvar key=dataBaseNames {{var::variableName}}|
		/flushvar output|
		/flushvar guidance|
		/flushvar genOrder|
		/flushvar genContent|
		/flushvar genSettings|
	:}|
	/else {:
		/addvar key=dataBaseNames {{var::variableName}}|
	:}|
	//-----------|



	//Ethnicity|
	/var key=do No|
	/var key=variableName "ethnicity"|
	/ife ({{var::variableName}} == '') {:
	    /var key=do Yes|
	:}|
	/elseif (skip == 'Update') {:
	    /getvar key={{var::variableName}}|
	    /buttons labels=["Yes", "No"] Do you want to set or redo {{var::variableName}} (current value: {{pipe}})?|
	    /var key=do {{pipe}}|
	    /ife (do == '') {:
	        /echo Aborting |
	        /abort
	    :}|
	:}|
	/ife ( do == 'Yes' ) {:
		/setvar key=genSettings {}|
		/setvar key=genSettings index=wi_book_key "Ethnicities"|
		/setvar key=genSettings index=genIsList Yes|
		/setvar key=genSettings index=genAmount 8|
		/setvar key=genSettings index=inputIsTaskList No|
		/setvar key=genSettings index=genIsSentence No|
		/setvar key=genSettings index=needOutput Yes|
		/setvar key=genSettings index=useContext Yes|
		/setvar key=genSettings index=contextKey []|
		/wait {{getvar::wait}}|
		
		
		/getvar key=genSettings index=inputIsList|
		/let key=inputIsList {{pipe}}|
		
		
		/ife (outputIsList == 'Yes') {:
			/setvar as=array key={{var::variableName}} []|
		:}|
		/else {:
			/setvar as=string key={{var::variableName}} {{noop}}|
		:}|
		//[[Generate with Prompt]]|
		/:"CMC Logic.GenerateWithPrompt"|
		
		/setvar key={{var::variableName}} {{getvar::output}}|
		/addvar key=dataBaseNames {{var::variableName}}|
	:}|
	/else {:
		/addvar key=dataBaseNames {{var::variableName}}|
	:}|
	//-----------|
	
	/ife ((( nationality != '') and ( nationality != 'None')) and (( ethnicity != '') and ( ethnicity != 'None'))) {:
		/let key=find Origin1: Task|
		/findentry field=comment file="CMC Generation Prompts {{getglobalvar::model}}" "{{var::find}}"|
		/getentryfield field=content file="CMC Generation Prompts {{getglobalvar::model}}" {{pipe}}|
		/let key=task|
		/var key=find Origin1: Instruction|
		/findentry field=comment file="CMC Generation Prompts {{getglobalvar::model}}" "{{var::find}}"|
		/getentryfield field=content file="CMC Generation Prompts {{getglobalvar::model}}" {{pipe}}|
		/let key=instruct|
		/genraw "{{var::task}}{{newline}}{{newline}}{{var::instruct}}"|
		/setvar key=parsedOrigin {{pipe}}|
	:}|
	/elseif ((( nationality != '') and ( nationality != 'None')) and (( ethnicity == '') or ( ethnicity == 'None'))) {:
		/let key=find Origin2: Task|
		/findentry field=comment file="CMC Generation Prompts {{getglobalvar::model}}" "{{var::find}}"|
		/getentryfield field=content file="CMC Generation Prompts {{getglobalvar::model}}" {{pipe}}|
		/let key=task|
		/var key=find Origin2: Instruction|
		/findentry field=comment file="CMC Generation Prompts {{getglobalvar::model}}" "{{var::find}}"|
		/getentryfield field=content file="CMC Generation Prompts {{getglobalvar::model}}" {{pipe}}|
		/let key=instruct|
		/genraw "{{var::task}}{{newline}}{{newline}}{{var::instruct}}"|
		/setvar key=parsedOrigin {{pipe}}|
	:}|
	/elseif ((( ethnicity != '') and ( ethnicity != 'None')) and (( nationality == '') or ( nationality == 'None'))) {:
		/let key=find Origin3: Task|
		/findentry field=comment file="CMC Generation Prompts {{getglobalvar::model}}" "{{var::find}}"|
		/getentryfield field=content file="CMC Generation Prompts {{getglobalvar::model}}" {{pipe}}|
		/let key=task|
		/var key=find Origin3: Instruction|
		/findentry field=comment file="CMC Generation Prompts {{getglobalvar::model}}" "{{var::find}}"|
		/getentryfield field=content file="CMC Generation Prompts {{getglobalvar::model}}" {{pipe}}|
		/let key=instruct|
		/genraw "{{var::task}}{{newline}}{{newline}}{{var::instruct}}"|
		/setvar key=parsedOrigin {{pipe}}|
	:}|
	/else {:
		/setvar key=parsedOrigin None|
	:}|
	/addvar key=dataBaseNames parsedOrigin|

:}|
/elseif ( skip != 'Skip') {:
	/setvar key=nationality None|
	/setvar key=ethnicity None|
	/setvar key=parsedOrigin None|
	/addvar key=dataBaseNames nationality|
	/addvar key=dataBaseNames ethnicity|
	/addvar key=dataBaseNames parsedOrigin|
:}|
/else {:
	/addvar key=dataBaseNames nationality|
	/addvar key=dataBaseNames ethnicity|
	/addvar key=dataBaseNames parsedOrigin|
:}|

//Life stage|
/var key=do No|
/var key=variableName "lifeStage"|
/ife ({{var::variableName}} == '') {:
    /var key=do Yes|
:}|
/elseif (skip == 'Update') {:
    /getvar key={{var::variableName}}|
    /buttons labels=["Yes", "No"] Do you want to set or redo {{var::variableName}} (current value: {{pipe}})?|
    /var key=do {{pipe}}|
    /ife (do == '') {:
        /echo Aborting |
        /abort
    :}|
:}|
/ife ( do == 'Yes' ) {:
	/setvar key=genSettings {}|
	/ife ( characterArchetype != 'Animalistic') {:
		/setvar key=genSettings index=wi_book_key "Life Stage Humanoid"|
	:}|
	/else {:
		/setvar key=genSettings index=wi_book_key "Life Stage Animalistic"|
	:}|
	/setvar key=genSettings index=combineLorebookEntries No|
	/setvar key=genSettings index=genIsSentence No|
	/setvar key=genSettings index=inputIsList No|
	/setvar key=genSettings index=genIsList Yes|
	/setvar key=genSettings index=outputIsList No|
	/setvar key=genSettings index=needOutput Yes|
	/setvar key=genSettings index=useContext No|
	/wait {{getvar::wait}}|
	
	
	/getvar key=genSettings index=wi_book_key|
	/let key=wi_book_key {{pipe}}|
	/getvar key=genSettings index=inputIsList|
	/let key=inputIsList {{pipe}}|
	/getvar key=genSettings index=combineLorebookEntries|
	/let key=combineLorebookEntries {{pipe}}|
	
	
	/ife ( inputIsList == 'Yes') {:
		/setvar key={{var::variableName}} []|
		/ife ( combineLorebookEntries == 'Yes') {:
			/:"CMC Logic.Combine List Lorebooks"
		:}|
		/foreach {{getvar::genOrder}} {:
			/setvar key=it {{var::item}}|
			/getat index={{var::index}} {{var::genOrderContent}} |
			/setvar key=genSettings index=content {{pipe}}|
			/:"CMC Logic.GenerateWithSelector"|
			/ife (output != '') {:
				/addvar key={{var::variableName}} {{getvar::output}}|
			:}|
		:}|
	:}|
	/else {:
		/getvar key=genSettings index=wi_book_key|
		/setvar key=it {{pipe}}|
		/:"CMC Logic.GenerateWithSelector"|
		/ife (output != '') {:
			/setvar key={{var::variableName}} {{getvar::output}}|
		:}|
		
	:}|
	/addvar key=dataBaseNames {{var::variableName}}|
	/flushvar output|
	/flushvar guidance|
	/flushvar genOrder|
	/flushvar genContent|
	/flushvar it|
	/flushvar genSettings|
:}|
/else {:
	/addvar key=dataBaseNames {{var::variableName}}|
:}|
//-------|



//Age|
/var key=do No|
/var key=variableName "age"|
/ife ({{var::variableName}} == '') {:
    /var key=do Yes|
:}|
/elseif (skip == 'Update') {:
    /getvar key={{var::variableName}}|
    /buttons labels=["Yes", "No"] Do you want to set or redo {{var::variableName}} (current value: {{pipe}})?|
    /var key=do {{pipe}}|
    /ife (do == '') {:
        /echo Aborting |
        /abort
    :}|
:}|
/ife ( do == 'Yes' ) {:
	/setvar key=genSettings {}|
	/setvar key=genSettings index=wi_book_key "Age Gen"|
	/setvar key=genSettings index=genIsList Yes|
	/setvar key=genSettings index=inputIsTaskList No|
	/setvar key=genSettings index=genIsSentence No|
	/setvar key=genSettings index=needOutput Yes|
	/setvar key=genSettings index=useContext Yes|
	/ife ( characterArchetype != 'Animalistic') {:
		/setvar key=genSettings index=contextKey ["Life Stage Humanoid"]|
	:}|
	/else {:
		/setvar key=genSettings index=contextKey ["Life Stage Animalistic"]|
	:}|
	/wait {{getvar::wait}}|
	
	/getvar key=genSettings index=inputIsList|
	/let key=inputIsList {{pipe}}|
	
	
	/ife (outputIsList == 'Yes') {:
		/setvar as=array key={{var::variableName}} []|
	:}|
	/else {:
		/setvar as=string key={{var::variableName}} {{noop}}|
	:}|
	//[[Generate with Prompt]]|
	/:"CMC Logic.GenerateWithPrompt"|
	/ife (output != '') {:
		/setvar key={{var::variableName}} {{getvar::output}}|
	:}|
	/addvar key=dataBaseNames {{var::variableName}}|
	/flushvar output|
	/flushvar guidance|
	/flushvar genOrder|
	/flushvar genContent|
	/flushvar genSettings|
:}|
/else {:
	/addvar key=dataBaseNames {{var::variableName}}|
:}|
//-----------|

/ife ((humanEquivalentAge == age) and (age != '')) {:
	/setvar key=parcedAge {{getvar::age}} years-old|
:}|
/elseif ((humanEquivalentAge != '') and (humanEquivalentAge != 'None') and (humanEquivalentAge != age)) {:
	/setvar key=parcedAge {{getvar::age}} years-old — roughly {{getvar::humanEquivalentAge}} years-old in human years.|
:}|
/else (age != '') {:
	/setvar key=parcedAge {{getvar::age}} years-old|
:}|

//Race Age|
/ife ( characterArchetype != 'Human') {:
	/var key=do No|
	/var key=variableName "humanEquivalentAge"|
	/ife ({{var::variableName}} == '') {:
	    /var key=do Yes|
	:}|
	/elseif (skip == 'Update') {:
	    /getvar key={{var::variableName}}|
	    /buttons labels=["Yes", "No"] Do you want to set or redo {{var::variableName}} (current value: {{pipe}})?|
	    /var key=do {{pipe}}|
	    /ife (do == '') {:
	        /echo Aborting |
	        /abort
	    :}|
	:}|
	/ife ( do == 'Yes' ) {:
		/setvar key=genSettings {}|
		/setvar key=genSettings index=wi_book_key "Age Species"|
		/setvar key=genSettings index=genIsList Yes|
		/setvar key=genSettings index=inputIsTaskList No|
		/setvar key=genSettings index=genIsSentence No|
		/setvar key=genSettings index=needOutput Yes|
		/setvar key=genSettings index=useContext Yes|
		/setvar key=genSettings index=contextKey []|
		/wait {{getvar::wait}}|
		
		/getvar key=genSettings index=inputIsList|
		/let key=inputIsList {{pipe}}|
		
		
		/ife (outputIsList == 'Yes') {:
			/setvar as=array key={{var::variableName}} []|
		:}|
		/else {:
			/setvar as=string key={{var::variableName}} {{noop}}|
		:}|
		//[[Generate with Prompt]]|
		/:"CMC Logic.GenerateWithPrompt"|
		/ife (output != '') {:
			/setvar key={{var::variableName}} {{getvar::output}}|
		:}|
		/addvar key=dataBaseNames {{var::variableName}}|
		/flushvar output|
		/flushvar guidance|
		/flushvar genOrder|
		/flushvar genContent|
		/flushvar genSettings|
	:}|
	/else {:
		/addvar key=dataBaseNames {{var::variableName}}|
	:}|
:}|
/elseif ( skip != 'Skip') {:
	/setvar key=humanEquivalentAge {{getvar::age}}|
	/addvar key=dataBaseNames humanEquivalentAge|
:}|
/else {:
	/addvar key=dataBaseNames humanEquivalentAge|
:}|
//-----------|

//Parse character Age|
/setvar key=parcedAge {{noop}}|
/ife ((humanEquivalentAge == age) and (age != '')) {:
	/setvar key=parcedAge {{getvar::age}} years-old|
:}|
/elseif ((humanEquivalentAge != '') and (humanEquivalentAge != 'None') and (humanEquivalentAge != age)) {:
	/setvar key=parcedAge {{getvar::age}} years-old — roughly {{getvar::humanEquivalentAge}} years-old in human years.|
:}|
/else (age != '') {:
	/setvar key=parcedAge {{getvar::age}} years-old|
:}|
//-----------|

//Parse character Species|
/setvar key=parsedSpecies {{noop}}|
/ife ((characterType == 'None') or ( characterType ==  characterArchetype)) {:
	/setvar key=characterType {{noop}}|
:}|
/ife (characterArchetype == species) {:
    /ife ((breed != 'None') and (breed != '')) {:
        /setvar key=parsedSpecies "{{getvar::species}} – {{getvar::breed}}"|
    :}|
    /else {:
        /setvar key=parsedSpecies "{{getvar::species}}"|
    :}|
:}|
/else {:
    /ife ((breed != 'None') and (breed != '')) {:
        /setvar key=parsedSpecies "{{getvar::characterArchetype}} {{getvar::species}} – {{getvar::breed}}"|
    :}|
    /else {:
        /setvar key=parsedSpecies "{{getvar::characterArchetype}} {{getvar::species}}"|
    :}|
:}|

/ife ( real != 'Yes') {:
	//First Name|
	/var key=do No|
	/var key=variableName "firstName"|
	/ife ({{var::variableName}} == '') {:
	    /var key=do Yes|
	:}|
	/elseif (skip == 'Update') {:
	    /getvar key={{var::variableName}}|
	    /buttons labels=["Yes", "No"] Do you want to set or redo {{var::variableName}} (current value: {{pipe}})?|
	    /var key=do {{pipe}}|
	    /ife (do == '') {:
	        /echo Aborting |
	        /abort
	    :}|
	:}|
	/ife ( do == 'Yes' ) {:
		/setvar key=genSettings {}|
		/setvar key=genSettings index=wi_book_key "First Name"|
		/setvar key=genSettings index=genIsList Yes|
		/setvar key=genSettings index=genAmount 8|
		/setvar key=genSettings index=inputIsTaskList No|
		/setvar key=genSettings index=genIsSentence No|
		/setvar key=genSettings index=needOutput Yes|
		/setvar key=genSettings index=useContext No|
		/setvar key=genSettings index=contextKey []|
		/ife (( nationality != 'None') and ( ethnicity != 'None')) {:
			4. Use {{getvar::nationality}} and/or {{getvar::ethnicity}} to influence cultural tone, spelling, or structure of the names when applicable — but do not include country names or descriptors in the output.

		:}|
		/wait {{getvar::wait}}|
		
		/getvar key=genSettings index=inputIsList|
		/let key=inputIsList {{pipe}}|
		
		/ife (outputIsList == 'Yes') {:
			/setvar as=array key={{var::variableName}} []|
		:}|
		/else {:
			/setvar as=string key={{var::variableName}} {{noop}}|
		:}|
		//[[Generate with Prompt]]|
		/:"CMC Logic.GenerateWithPrompt"|
		
		/setvar key={{var::variableName}} {{getvar::output}}|
		/addvar key=dataBaseNames {{var::variableName}}|
	:}|
	/else {:
		/addvar key=dataBaseNames {{var::variableName}}|
	:}|
	//-----------|
	
	
	
	//Last Name|
	/var key=do No|
	/var key=variableName "lastName"|
	/ife ({{var::variableName}} == '') {:
	    /var key=do Yes|
	:}|
	/elseif (skip == 'Update') {:
	    /getvar key={{var::variableName}}|
	    /buttons labels=["Yes", "No"] Do you want to set or redo {{var::variableName}} (current value: {{pipe}})?|
	    /var key=do {{pipe}}|
	    /ife (do == '') {:
	        /echo Aborting |
	        /abort
	    :}|
	:}|
	/ife ( do == 'Yes' ) {:
		/setvar key=genSettings {}|
		/setvar key=genSettings index=wi_book_key "Last Name"|
		/setvar key=genSettings index=genIsList Yes|
		/setvar key=genSettings index=genAmount 8|
		/setvar key=genSettings index=inputIsTaskList No|
		/setvar key=genSettings index=genIsSentence No|
		/setvar key=genSettings index=needOutput No|
		/setvar key=genSettings index=useContext Yes|
		/setvar key=genSettings index=contextKey []|
		/wait {{getvar::wait}}|
		
		/getvar key=genSettings index=inputIsList|
		/let key=inputIsList {{pipe}}|
		
		/ife (outputIsList == 'Yes') {:
			/setvar as=array key={{var::variableName}} []|
		:}|
		/else {:
			/setvar as=string key={{var::variableName}} {{noop}}|
		:}|
		//[[Generate with Prompt]]|
		/:"CMC Logic.GenerateWithPrompt"|
		
		/setvar key={{var::variableName}} {{getvar::output}}|
		/addvar key=dataBaseNames {{var::variableName}}|
	:}|
	/else {:
		/addvar key=dataBaseNames {{var::variableName}}|
	:}|
	//-----------|
:}|
/ife ( lastName == 'None') {:
	/setvar key=lastName {{noop}}|
:}|

//Nickname|
/var key=do No|
/var key=variableName "alias"|
/ife ({{var::variableName}} == '') {:
    /var key=do Yes|
:}|
/elseif (skip == 'Update') {:
    /getvar key={{var::variableName}}|
    /buttons labels=["Yes", "No"] Do you want to set or redo {{var::variableName}} (current value: {{pipe}})?|
    /var key=do {{pipe}}|
    /ife (do == '') {:
        /echo Aborting |
        /abort
    :}|
:}|
/ife ( do == 'Yes' ) {:
	/setvar key=genSettings {}|
	/setvar key=genSettings index=wi_book_key "Nickname"|
	/setvar key=genSettings index=genIsList Yes|
	/setvar key=genSettings index=genAmount 8|
	/setvar key=genSettings index=inputIsTaskList No|
	/setvar key=genSettings index=genIsSentence No|
	/setvar key=genSettings index=needOutput No|
	/setvar key=genSettings index=useContext Yes|
	/setvar key=genSettings index=contextKey []|
	/wait {{getvar::wait}}|
	
	/getvar key=genSettings index=inputIsList|
	/let key=inputIsList {{pipe}}|
	
	
	/ife (outputIsList == 'Yes') {:
		/setvar as=array key={{var::variableName}} []|
	:}|
	/else {:
		/setvar as=string key={{var::variableName}} {{noop}}|
	:}|
	//[[Generate with Prompt]]|
	/:"CMC Logic.GenerateWithPrompt"|
	
	/setvar key={{var::variableName}} {{getvar::output}}|
	/addvar key=dataBaseNames {{var::variableName}}|
:}|
/else {:
	/addvar key=dataBaseNames {{var::variableName}}|
:}|
//-----------|

/ife ( nationality == '' ) {:
	/setvar key=nationality None|
:}|
/ife ( ethnicity == '' ) {:
	/setvar key=ethnicity None|
:}|
/ife ( lastName == '' ) {:
	/setvar key=lastName None|
:}|

/:"CMC Logic.JEDParse"|

/:"CMC Logic.Save DataBase"|

/setvar key=stepDone Yes|
/qr-list CMC Main|
/getat index=1 {{pipe}}|
/var qrlabel {{pipe}}|
/qr-get set="CMC Main" label={{var::qrlabel}}|
/getat index="message" {{pipe}}|
/qr-update set="CMC Main" label={{var::qrlabel}} newlabel="Start Generating World & Setting Information" {{pipe}}|

/setvar key=filename/setvar key=filename {{date}}, {{isotime}}|
/re-replace find="/:/g" replace="h" {{pipe}}|
/setvar key=filename {{pipe}}|
/ife (lastName != 'None') {:
	/addvar key=filename "m {{getvar::characterArchetype}} {{getvar::firstName}} {{getvar::lastName}}"|
:}|
/else {:
	/addvar key=filename "m {{getvar::characterArchetype}} {{getvar::firstName}}"|
:}|
/sendas name={{char}} del|
/renamechat {{getvar::filename}}|
/del {{lastMessageId}}|
/flushvar filename|
/forcesave|