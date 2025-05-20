/qr-list CMC Main|
/getat index=1 {{pipe}}|
/let qrlabel {{pipe}}|
/qr-get set="CMC Main" label={{var::qrlabel}}|
/getat index="message" {{pipe}}|
/qr-update set="CMC Main" label={{var::qrlabel}} newlabel="Continue Generating Core Identity" {{pipe}}|

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
		/setvar key=genSettings index=wi_book_key "Species"|
		/setvar key=genSettings index=genIsList Yes|
		/setvar key=genSettings index=genIsSentence No|
		/setvar key=genSettings index=inputIsTaskList No|
		/setvar key=genSettings index=needOutput Yes|
		/setvar key=genSettings index=useContext No|
		/setvar key=genSettings index=contextKey []|
		/ife (characterArchetype == 'Demi-Human') {:
			/setvar key=speciesExamples Elf, Dwarf, Vampire, Succubus, Angel, Demon, Halfling, Fairy
		:}|
		/elseif ((characterArchetype != 'Pokémon') and (characterArchetype != 'Digimon')) {:
			
			/let key=find "Reproductive {{getvar::animalBase}}: List"
			/findentry field=comment file="CMC Variables" {{var::find}}|
			/getentryfield file="CMC Information" {{pipe}}| 
			/let key=temp {{pipe}}|
			/split find="/\n/" {{var::temp}}|
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

/ife (characterArchetype == 'Demi-Human') {:
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
		/setvar key=genSettings index=wi_book_key "Ethnicities"|
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
		
		/setvar key={{var::variableName}} {{getvar::output}}|
		/addvar key=dataBaseNames {{var::variableName}}|
	:}|
	/else {:
		/addvar key=dataBaseNames {{var::variableName}}|
	:}|
	//-----------|
	
	/ife ((( nationality != '') and ( nationality != 'None')) and (( ethnicity != '') and ( ethnicity != 'None'))) {:
		/genraw "## **TASK:**  
Using the inputs below, combine them into a natural descriptor of origin.

## **INPUT:**  
Ethnicity: {{getvar::ethnicity}}
Nationality: {{getvar::nationality}}

## **INSTRUCTIONS:**  
1. Return a short phrase in the format: `{{ethnicity}} from {{placeName}}`.
2. Convert the nationality to the most likely place name if needed (e.g., “American” → “America”).
3. Use proper capitalization.
4. Do not include any extra text, punctuation, or formatting — return the phrase only."|
   /setvar key=parsedOrigin {{pipe}}|
	:}|
	/ife ((( nationality != '') and ( nationality != 'None')) and (( ethnicity == '') or ( ethnicity == 'None'))) {:
		/genraw "## **TASK:**
Generate a natural origin phrase from a single nationality.

## **INPUT:**
Nationality: {{getvar::nationality}}

## **INSTRUCTIONS:**  
1. Convert the nationality to a proper place name (e.g., “French” → “France”).
2. Return the phrase in the format: `From {{placeName}}`.
3. Use correct capitalization and no extra text or punctuation."|
		/setvar key=parsedOrigin {{pipe}}|
	:}|
	/ife ((( ethnicity != '') and ( ethnicity != 'None')) and (( nationality == '') or ( nationality == 'None'))) {:
		/genraw "## **TASK:**
Create a short origin phrase using only the character's ethnicity.

## **INPUT:**
Ethnicity: {{getvar::ethnicity}}

## **INSTRUCTIONS:**  
1. Format the phrase as: `Of {{ethnicity}} origin`.
2. Use capitalization as appropriate.
3. Return only the phrase — no commentary or extras.
"|
		/setvar key=parsedOrigin {{pipe}}|
	:}||
	/addvar key=dataBaseNames parsedOrigin

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
		/setvar key=genSettings index=wi_book_key "First Name"|
		/setvar key=genSettings index=genIsList Yes|
		/setvar key=genSettings index=inputIsTaskList No|
		/setvar key=genSettings index=genIsSentence No|
		/setvar key=genSettings index=needOutput Yes|
		/setvar key=genSettings index=useContext Yes|
		/setvar key=genSettings index=contextKey []|
		/ife () {:
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
		/setvar key=genSettings index=wi_book_key "Last Name"|
		/setvar key=genSettings index=genIsList Yes|
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
	/setvar key=genSettings index=wi_book_key "Nickname"|
	/setvar key=genSettings index=genIsList Yes|
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

/let key=filename {{datetimeformat YYYY-MM-DD HH h mm}}|
/re-replace find="/\s(?=\d{2}$)/g" replace="h " {{var::filename}}|
/setvar key=filename {{pipe}}|
/addvar key=filename " m {{getvar::firstName}} {{getvar::lastName}}"|
/sendas name={{char}} del|
/renamechat {{getvar::filename}}|
/del {{lastMessageId}}|
/flushvar filename|
/forcesave|