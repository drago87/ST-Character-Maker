/qr-list CMC Main|
/getat index=1 {{pipe}}|
/let qrlabel {{pipe}}|
/qr-get set="CMC Main" label={{var::qrlabel}}|
/getat index="message" {{pipe}}|
/qr-update set="CMC Main" label={{var::qrlabel}} newlabel="Continue Generating Appearance & Anatomy" {{pipe}}|

/:"CMC Logic.Get Char info"|

/setvar key=dataBaseNames []|
/flushvar genSettings|

/setvar key=stepVar Step3|

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

/let key=do {{noop}}|
/let key=variableName {{noop}}|
/let selected_btn {{noop}}|

/buttons labels=["Metric", "Imperial"] What type of measuring system do you want to use during these generations?|
/setvar key=unitType {{pipe}}|
/ife ( unitType == ''){:
	/echo Aborting |
	/abort
:}|

/ife ((characterArchetype == 'Animalistic') or (characterArchetype == 'Pokémon') or (characterArchetype == 'Digimon') or (characterArchetype == 'Tauric')) {:
	/buttons labels=["Length (Their body is horizontal or animal-like — e.g., snake, lizard, quadruped)", "Height (They stand upright like a human or humanoid)", "Both (They have both vertical and elongated traits — e.g., centaur, dragon)"] <div>How should this character's body be measured?</div><div>Choose the option that best fits their physical structure:</div>|
	/var key=selected_btn {{pipe}}|
	/re-replace find="/\s\(.*$/g" replace="" {{var::selected_btn}}|
	/var key=selected_btn {{pipe}}|
:}|

//**Length**|

/ife ((( selected_btn == 'Length') or ( selected_btn == 'Both')) and (((characterArchetype == 'Animalistic') or (characterArchetype == 'Pokémon') or (characterArchetype == 'Digimon') or (characterArchetype == 'Tauric')))) {:
	/var key=do No|
	/var key=variableName "length"|
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
		/setvar key=genSettings index=wi_book_key "Length"|
		/setvar key=genSettings index=genIsList Yes|
		/setvar key=genSettings index=inputIsTaskList No|
		/setvar key=genSettings index=genIsSentence No|
		/setvar key=genSettings index=needOutput Yes|
		/setvar key=genSettings index=outputIsList No|
		/setvar key=genSettings index=useContext Yes|
		/setvar key=extra []|
		/addvar key=extra "- Unit Type: {{getvar::unitType}}"|
		/setvar key=genSettings index=extraContext {{getvar::extra}}|
		/flushvar extra|
		/setvar key=genSettings index=contextKey []|
		/wait {{getvar::wait}}|
		
		/getvar key=genSettings index=inputIsList|
		/let key=inputIsList {{pipe}}|
		/getvar key=genSettings index=inputIsList|
		/let key=outputIsList {{pipe}}|
		
		
		/ife ((outputIsList == 'Yes') or (outputIsList == 'Yes')) {:
			/setvar as=array key={{var::variableName}} []|
		:}|
		/else {:
			/setvar as=string key={{var::variableName}} {{noop}}|
		:}|
		//[[Generate with Prompt]]|
		
			/:"CMC Logic.GenerateWithPrompt"|
			/setvar key={{var::variableName}} {{getvar::output}}|
		/addvar key=dataBaseNames {{var::variableName}}|
		/flushvar output|
		/flushvar genOrder|
		/flushvar genContent|
		/flushvar genSettings|
	:}|
	/else {:
		/addvar key=dataBaseNames {{var::variableName}}|
	:}|
:}|
/else {:
	/setvar key=length None|
	/addvar key=dataBaseNames length|
:}|
//-----------|

//**Height**|
/ife ((( selected_btn == 'Height') or ( selected_btn == 'Both')) or  (((characterArchetype != 'Animalistic') and (characterArchetype != 'Pokémon') and (characterArchetype != 'Digimon')))) {:
	/var key=do No|
	/var key=variableName "height"|
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
		/setvar key=genSettings index=wi_book_key "Height"|
		/setvar key=genSettings index=genIsList Yes|
		/setvar key=genSettings index=inputIsTaskList No|
		/setvar key=genSettings index=genIsSentence No|
		/setvar key=genSettings index=needOutput Yes|
		/setvar key=genSettings index=outputIsList No|
		/setvar key=genSettings index=useContext Yes|
		/setvar key=extra []|
		/addvar key=extra "- Unit Type: {{getvar::unitType}}"|
		/setvar key=genSettings index=extraContext {{getvar::extra}}|
		/flushvar extra|
		/setvar key=genSettings index=contextKey []|
		/wait {{getvar::wait}}|
		
		/getvar key=genSettings index=inputIsList|
		/let key=inputIsList {{pipe}}|
		/getvar key=genSettings index=inputIsList|
		/let key=outputIsList {{pipe}}|
		
		
		/ife ((outputIsList == 'Yes') or (outputIsList == 'Yes')) {:
			/setvar as=array key={{var::variableName}} []|
		:}|
		/else {:
			/setvar as=string key={{var::variableName}} {{noop}}|
		:}|
		//[[Generate with Prompt]]|
		
			/:"CMC Logic.GenerateWithPrompt"|
			/setvar key={{var::variableName}} {{getvar::output}}|
		/addvar key=dataBaseNames {{var::variableName}}|
		/flushvar output|
		/flushvar genOrder|
		/flushvar genContent|
		/flushvar genSettings|
	:}|
	/else {:
		/addvar key=dataBaseNames {{var::variableName}}|
	:}|
:}|
/else {:
	/setvar key=height None|
	/addvar key=dataBaseNames height|
:}|

//-----------|

//**Face**|
/var key=do No|
/var key=variableName "appearanceFace"|
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
	/setvar key=genSettings index=wi_book_key "Appearance Face"|
	/setvar key=genSettings index=genIsList No|
	/setvar key=genSettings index=inputIsTaskList No|
	/setvar key=genSettings index=genIsSentence Yes|
	/setvar key=genSettings index=needOutput Yes|
	/setvar key=genSettings index=outputIsList No|
	/setvar key=genSettings index=useContext Yes|
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
	/setvar key=genSettings index=contextKey {{getvar::extra}}|
	/flushvar extra|
	/wait {{getvar::wait}}|
	
	/getvar key=genSettings index=inputIsList|
	/let key=inputIsList {{pipe}}|
	/getvar key=genSettings index=inputIsList|
	/let key=outputIsList {{pipe}}|
	
	
	/ife ((outputIsList == 'Yes') or (outputIsList == 'Yes')) {:
		/setvar as=array key={{var::variableName}} []|
	:}|
	/else {:
		/setvar as=string key={{var::variableName}} {{noop}}|
	:}|
	//[[Generate with Prompt]]|
	/:"CMC Logic.GenerateWithPrompt"|
	/setvar key={{var::variableName}} {{getvar::output}}|
	/addvar key=dataBaseNames {{var::variableName}}|
	/flushvar output|
	/flushvar genOrder|
	/flushvar genContent|
	/flushvar genSettings|
:}|
/else {:
	/addvar key=dataBaseNames {{var::variableName}}|
:}|
//-----------|

//**Hair**|
/var key=do No|
/var key=variableName "appearanceHair"|
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
	/setvar key=genSettings index=wi_book_key "Appearance Hair"|
	/setvar key=genSettings index=genIsList No|
	/setvar key=genSettings index=inputIsTaskList No|
	/setvar key=genSettings index=genIsSentence Yes|
	/setvar key=genSettings index=needOutput Yes|
	/setvar key=genSettings index=outputIsList No|
	/setvar key=genSettings index=useContext Yes|
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
	/setvar key=genSettings index=contextKey {{getvar::extra}}|
	/flushvar extra|
	/wait {{getvar::wait}}|
	
	/getvar key=genSettings index=inputIsList|
	/let key=inputIsList {{pipe}}|
	/getvar key=genSettings index=inputIsList|
	/let key=outputIsList {{pipe}}|
	
	
	/ife ((outputIsList == 'Yes') or (outputIsList == 'Yes')) {:
		/setvar as=array key={{var::variableName}} []|
	:}|
	/else {:
		/setvar as=string key={{var::variableName}} {{noop}}|
	:}|
	//[[Generate with Prompt]]|
	/:"CMC Logic.GenerateWithPrompt"|
	/setvar key={{var::variableName}} {{getvar::output}}|
	/addvar key=dataBaseNames {{var::variableName}}|
	/flushvar output|
	/flushvar genOrder|
	/flushvar genContent|
	/flushvar genSettings|
:}|
/else {:
	/addvar key=dataBaseNames {{var::variableName}}|
:}|
//-----------|

//**Eyes**|
/var key=do No|
/var key=variableName "appearanceEyes"|
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
	/setvar key=genSettings index=wi_book_key "Appearance Eyes"|
	/setvar key=genSettings index=genIsList No|
	/setvar key=genSettings index=inputIsTaskList No|
	/setvar key=genSettings index=genIsSentence Yes|
	/setvar key=genSettings index=needOutput Yes|
	/setvar key=genSettings index=outputIsList No|
	/setvar key=genSettings index=useContext Yes|
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
	/setvar key=genSettings index=contextKey {{getvar::extra}}|
	/flushvar extra|
	/wait {{getvar::wait}}|
	
	/getvar key=genSettings index=inputIsList|
	/let key=inputIsList {{pipe}}|
	/getvar key=genSettings index=inputIsList|
	/let key=outputIsList {{pipe}}|
	
	
	/ife ((outputIsList == 'Yes') or (outputIsList == 'Yes')) {:
		/setvar as=array key={{var::variableName}} []|
	:}|
	/else {:
		/setvar as=string key={{var::variableName}} {{noop}}|
	:}|
	//[[Generate with Prompt]]|
	/:"CMC Logic.GenerateWithPrompt"|
	/setvar key={{var::variableName}} {{getvar::output}}|
	/addvar key=dataBaseNames {{var::variableName}}|
	/flushvar output|
	/flushvar genOrder|
	/flushvar genContent|
	/flushvar genSettings|
:}|
/else {:
	/addvar key=dataBaseNames {{var::variableName}}|
:}|
//-----------|

//**Features**|
/var key=do No|
/var key=variableName "appearanceFeatures"|
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
	/setvar key=genSettings index=wi_book_key "Appearance Features"|
	/setvar key=genSettings index=genIsList No|
	/setvar key=genSettings index=inputIsTaskList No|
	/setvar key=genSettings index=genIsSentence Yes|
	/setvar key=genSettings index=needOutput Yes|
	/setvar key=genSettings index=outputIsList No|
	/setvar key=genSettings index=useContext Yes|
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
	/setvar key=genSettings index=contextKey {{getvar::extra}}|
	/flushvar extra|
	/wait {{getvar::wait}}|
	
	/getvar key=genSettings index=inputIsList|
	/let key=inputIsList {{pipe}}|
	/getvar key=genSettings index=inputIsList|
	/let key=outputIsList {{pipe}}|
	
	
	/ife ((outputIsList == 'Yes') or (outputIsList == 'Yes')) {:
		/setvar as=array key={{var::variableName}} []|
	:}|
	/else {:
		/setvar as=string key={{var::variableName}} {{noop}}|
	:}|
	//[[Generate with Prompt]]|
	/:"CMC Logic.GenerateWithPrompt"|
	/setvar key={{var::variableName}} {{getvar::output}}|
	/addvar key=dataBaseNames {{var::variableName}}|
	/flushvar output|
	/flushvar genOrder|
	/flushvar genContent|
	/flushvar genSettings|
:}|
/else {:
	/addvar key=dataBaseNames {{var::variableName}}|
:}|
//-----------|

//**Body**|
/var key=do No|
/var key=variableName "appearanceBody"|
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
	/setvar key=genSettings index=wi_book_key "Appearance Body"|
	/setvar key=genSettings index=genIsList No|
	/setvar key=genSettings index=inputIsTaskList No|
	/setvar key=genSettings index=genIsSentence Yes|
	/setvar key=genSettings index=needOutput Yes|
	/setvar key=genSettings index=outputIsList No|
	/setvar key=genSettings index=useContext Yes|
	/setvar key=extra []|
	/addvar key=extra "- Features: {{getvar::appearanceFeatures}}"|
	/setvar key=genSettings index=extraContext {{getvar::extra}}|
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
	/setvar key=genSettings index=contextKey {{getvar::extra}}|
	/flushvar extra|
	/wait {{getvar::wait}}|
	
	/getvar key=genSettings index=inputIsList|
	/let key=inputIsList {{pipe}}|
	/getvar key=genSettings index=inputIsList|
	/let key=outputIsList {{pipe}}|
	
	
	/ife ((outputIsList == 'Yes') or (outputIsList == 'Yes')) {:
		/setvar as=array key={{var::variableName}} []|
	:}|
	/else {:
		/setvar as=string key={{var::variableName}} {{noop}}|
	:}|
	//[[Generate with Prompt]]|
	/:"CMC Logic.GenerateWithPrompt"|
	/setvar key={{var::variableName}} {{getvar::output}}|
	/addvar key=dataBaseNames {{var::variableName}}|
	/flushvar output|
	/flushvar genOrder|
	/flushvar genContent|
	/flushvar genSettings|
:}|
/else {:
	/addvar key=dataBaseNames {{var::variableName}}|
:}|
//-----------|

/ife (gender == 'Female') {:
	//**Breasts**|
	/var key=do No|
	/var key=variableName "appearanceBreasts"|
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
		/setvar key=genSettings index=wi_book_key "Appearance Breasts"|
		/setvar key=genSettings index=genIsList No|
		/setvar key=genSettings index=inputIsTaskList No|
		/setvar key=genSettings index=genIsSentence Yes|
		/setvar key=genSettings index=needOutput Yes|
		/setvar key=genSettings index=outputIsList No|
		/setvar key=genSettings index=useContext Yes|
		/setvar key=extra []|
		/addvar key=extra "- Body: {{getvar::appearanceBody}}"|
		/addvar key=extra "- Features: {{getvar::appearanceFeatures}}"|
		/setvar key=genSettings index=extraContext {{getvar::extra}}|
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
		/setvar key=genSettings index=contextKey {{getvar::extra}}|
		/flushvar extra|
		/wait {{getvar::wait}}|
		
		/getvar key=genSettings index=inputIsList|
		/let key=inputIsList {{pipe}}|
		/getvar key=genSettings index=inputIsList|
		/let key=outputIsList {{pipe}}|
		
		
		/ife ((outputIsList == 'Yes') or (outputIsList == 'Yes')) {:
			/setvar as=array key={{var::variableName}} []|
		:}|
		/else {:
			/setvar as=string key={{var::variableName}} {{noop}}|
		:}|
		//[[Generate with Prompt]]|
		/:"CMC Logic.GenerateWithPrompt"|
		/setvar key={{var::variableName}} {{getvar::output}}|
		/addvar key=dataBaseNames {{var::variableName}}|
		/flushvar output|
		/flushvar genOrder|
		/flushvar genContent|
		/flushvar genSettings|
	:}|
	/else {:
		/addvar key=dataBaseNames {{var::variableName}}|
	:}|

//-----------|

//**Nipples**|
	/var key=do No|
	/var key=variableName "appearanceNipples"|
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
		/setvar key=genSettings index=wi_book_key "Appearance Nipples"|
		/setvar key=genSettings index=genIsList No|
		/setvar key=genSettings index=inputIsTaskList No|
		/setvar key=genSettings index=genIsSentence Yes|
		/setvar key=genSettings index=needOutput Yes|
		/setvar key=genSettings index=outputIsList No|
		/setvar key=genSettings index=useContext Yes|
		/setvar key=extra []|
		/addvar key=extra "- Breasts: {{getvar::appearanceBreasts}}"|
		/addvar key=extra "- Body: {{getvar::appearanceBody}}"|
		/addvar key=extra "- Features: {{getvar::appearanceFeatures}}"|
		/setvar key=genSettings index=extraContext {{getvar::extra}}|
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
		/setvar key=genSettings index=contextKey {{getvar::extra}}|
		/flushvar extra|
		/wait {{getvar::wait}}|
		
		/getvar key=genSettings index=inputIsList|
		/let key=inputIsList {{pipe}}|
		/getvar key=genSettings index=inputIsList|
		/let key=outputIsList {{pipe}}|
		
		
		/ife ((outputIsList == 'Yes') or (outputIsList == 'Yes')) {:
			/setvar as=array key={{var::variableName}} []|
		:}|
		/else {:
			/setvar as=string key={{var::variableName}} {{noop}}|
		:}|
		//[[Generate with Prompt]]|
		/:"CMC Logic.GenerateWithPrompt"|
		/setvar key={{var::variableName}} {{getvar::output}}|
		/addvar key=dataBaseNames {{var::variableName}}|
		/flushvar output|
		/flushvar genOrder|
		/flushvar genContent|
		/flushvar genSettings|
	:}|
	/else {:
		/addvar key=dataBaseNames {{var::variableName}}|
	:}|
//-----------|
:}|


/ife (gender != 'Male') {:
	//**Pussy**|
	/var key=do No|
	/var key=variableName "appearancePussy"|
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
		/setvar key=genSettings index=wi_book_key "Appearance Pussy"|
		/setvar key=genSettings index=genIsList No|
		/setvar key=genSettings index=inputIsTaskList No|
		/setvar key=genSettings index=genIsSentence Yes|
		/setvar key=genSettings index=needOutput Yes|
		/setvar key=genSettings index=outputIsList No|
		/setvar key=genSettings index=useContext Yes|
		/setvar key=extra []|
		/addvar key=extra "- Body: {{getvar::appearanceBody}}"|
		/addvar key=extra "- Features: {{getvar::appearanceFeatures}}"|
		/addvar key=extra "- Female  Genital Type: {{getvar::privatesFemale}}"|
		/addvar key=extra "- Species Group: {{getvar::speciesGroup}}"|
		/ife (futanari == 'Yes') {:
			/addvar key=extra "Important: {{getvar::firstName}} is a futanari, so she has both a pussy and a cock."|
		:}|
		/setvar key=genSettings index=extraContext {{getvar::extra}}|
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
		/ife (futanari == 'Yes') {:
			/setvar key=logicBasedInstruction "6. Ensure description accounts for proximity to other anatomy but focuses **only** on the vulva.{{newline}}7. {{getvar::firstName}} is a futanari so they have both a pussy and a cock. Only describe the pussy here — do not mention the penis."|
		:}|
		/setvar key=genSettings index=contextKey {{getvar::extra}}|
		/flushvar extra|
		/wait {{getvar::wait}}|
		
		/getvar key=genSettings index=inputIsList|
		/let key=inputIsList {{pipe}}|
		/getvar key=genSettings index=inputIsList|
		/let key=outputIsList {{pipe}}|
		
		
		/ife ((outputIsList == 'Yes') or (outputIsList == 'Yes')) {:
			/setvar as=array key={{var::variableName}} []|
		:}|
		/else {:
			/setvar as=string key={{var::variableName}} {{noop}}|
		:}|
		//[[Generate with Prompt]]|
		/:"CMC Logic.GenerateWithPrompt"|
		/setvar key={{var::variableName}} {{getvar::output}}|
		/addvar key=dataBaseNames {{var::variableName}}|
		/flushvar output|
		/flushvar genOrder|
		/flushvar genContent|
		/flushvar genSettings|
		/flushvar logicBasedInstruction|
	:}|
	/else {:
		/addvar key=dataBaseNames {{var::variableName}}|
	:}|
	//-----------|
:}|

/elseif (gender != 'Female') {:
	//**Cock**|
	/var key=do No|
	/var key=variableName "appearanceCock"|
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
		/setvar key=genSettings index=wi_book_key "Appearance Cock"|
		/setvar key=genSettings index=genIsList No|
		/setvar key=genSettings index=inputIsTaskList No|
		/setvar key=genSettings index=genIsSentence Yes|
		/setvar key=genSettings index=needOutput Yes|
		/setvar key=genSettings index=outputIsList No|
		/setvar key=genSettings index=useContext Yes|
		/setvar key=extra []|
		/addvar key=extra "- Body: {{getvar::appearanceBody}}"|
		/addvar key=extra "- Features: {{getvar::appearanceFeatures}}"|
		/ife (futanari == 'Yes') {:
			/addvar key=extra "- Pussy Appearance: {{getvar::appearancePussy}}"|
		:}|
		/addvar key=extra "- Male Genital Type:: {{getvar::privatesMale}}"|
		/addvar key=extra "- Species Group: {{getvar::speciesGroup}}"|
		/setvar key=genSettings index=extraContext {{getvar::extra}}|
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
		/ife (futanari == 'Yes') {:
			/setvar key=logicBasedInstruction "7. {{getvar::firstName}} is a futanari, so she has both a pussy and a cock. Describe only the cock here — do not mention the pussy directly, but ensure anatomical placement and proportions account for its presence."|
"|
		:}|
		/setvar key=genSettings index=contextKey {{getvar::extra}}|
		/flushvar extra|
		/wait {{getvar::wait}}|
		
		/getvar key=genSettings index=inputIsList|
		/let key=inputIsList {{pipe}}|
		/getvar key=genSettings index=inputIsList|
		/let key=outputIsList {{pipe}}|
		
		
		/ife ((outputIsList == 'Yes') or (outputIsList == 'Yes')) {:
			/setvar as=array key={{var::variableName}} []|
		:}|
		/else {:
			/setvar as=string key={{var::variableName}} {{noop}}|
		:}|
		//[[Generate with Prompt]]|
		/:"CMC Logic.GenerateWithPrompt"|
		/setvar key={{var::variableName}} {{getvar::output}}|
		/addvar key=dataBaseNames {{var::variableName}}|
		/flushvar output|
		/flushvar genOrder|
		/flushvar genContent|
		/flushvar genSettings|
		/flushvar logicBasedInstruction|
	:}|
	/else {:
		/addvar key=dataBaseNames {{var::variableName}}|
	:}|
	//-----------|
:}|
/elseif (futanari == 'Yes') {:
	//**Privates Sync**|
	/var key=do No|
	/var key=variableName "appearanceGenitals"|
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
		/setvar key=genSettings index=wi_book_key "Appearance Genitals Sync"|
		/setvar key=genSettings index=genIsList No|
		/setvar key=genSettings index=inputIsTaskList No|
		/setvar key=genSettings index=genIsSentence Yes|
		/setvar key=genSettings index=needOutput Yes|
		/setvar key=genSettings index=outputIsList No|
		/setvar key=genSettings index=useContext Yes|
		/setvar key=extra []|
		/addvar key=extra "- Body: {{getvar::appearanceBody}}"|
		/addvar key=extra "- Features: {{getvar::appearanceFeatures}}"|
		/addvar key=extra "- Pussy Appearance: {{getvar::appearancePussy}}"|
		/addvar key=extra "- Cock Appearance: {{getvar::appearanceCock}}"|
		/addvar key=extra "- Male Genital Type:: {{getvar::privatesMale}}"|
		/addvar key=extra "- Female Genital Type:: {{getvar::privatesFemale}}"|
		/addvar key=extra "- Species Group: {{getvar::speciesGroup}}"|
		/setvar key=genSettings index=extraContext {{getvar::extra}}|
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
		/setvar key=genSettings index=contextKey {{getvar::extra}}|
		/flushvar extra|
		/wait {{getvar::wait}}|
		
		/getvar key=genSettings index=inputIsList|
		/let key=inputIsList {{pipe}}|
		/getvar key=genSettings index=inputIsList|
		/let key=outputIsList {{pipe}}|
		
		
		/ife ((outputIsList == 'Yes') or (outputIsList == 'Yes')) {:
			/setvar as=array key={{var::variableName}} []|
		:}|
		/else {:
			/setvar as=string key={{var::variableName}} {{noop}}|
		:}|
		//[[Generate with Prompt]]|
		/:"CMC Logic.GenerateWithPrompt"|
		/setvar key={{var::variableName}} {{getvar::output}}|
		/addvar key=dataBaseNames {{var::variableName}}|
		/flushvar output|
		/flushvar genOrder|
		/flushvar genContent|
		/flushvar genSettings|
		/flushvar logicBasedInstruction|
	:}|
	/else {:
		/addvar key=dataBaseNames {{var::variableName}}|
	:}|
	//-----------|
:}|



//**Anus**|

//-----------|

//**Appearance Traits**|

//-----------|


/:"CMC Logic.JEDParse"|

/:"CMC Logic.Save DataBase"|

/setvar key=stepDone Yes|
/qr-list CMC Main|
/getat index=1 {{pipe}}|
/var qrlabel {{pipe}}|
/qr-get set="CMC Main" label={{var::qrlabel}}|
/getat index="message" {{pipe}}|
/qr-update set="CMC Main" label={{var::qrlabel}} newlabel="Start Generating Outfit" {{pipe}}|