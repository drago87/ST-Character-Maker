/qr-list CMC Main|
/getat index=1 {{pipe}}|
/let qrlabel {{pipe}}|
/qr-get set="CMC Main" label={{var::qrlabel}}|
/getat index="message" {{pipe}}|
/qr-update set="CMC Main" label={{var::qrlabel}} newlabel="Start Generating Appearance & Anatomy" {{pipe}}|

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

/ife (unitType == '') {:
	/buttons labels=["Metric", "Imperial"] What type of measuring system do you want to use during these generations?|
	/setvar key=unitType {{pipe}}|
	/ife ( unitType == ''){:
		/echo Aborting |
		/abort
	:}|
:}|

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
	/setvar key=genSettings {}|
	/ife ((characterArchetype == 'Human') or (characterArchetype == 'Android')) {:
		/setvar key=genSettings index=wi_book_key "Appearance Features Humanoid"|
	:}|
	/else {:
		/setvar key=genSettings index=wi_book_key "Appearance Features Other"|
	:}|
	/setvar key=genSettings index=genIsList Yes|
	/setvar key=genSettings index=inputIsTaskList No|
	/setvar key=genSettings index=genIsSentence No|
	/setvar key=genSettings index=needOutput No|
	/setvar key=genSettings index=outputIsList Yes|
	/setvar key=genSettings index=useContext Yes|
	/setvar key=extra []|
	/addvar key=extra "- Species Group: {{getvar::speciesGroup}}"|
	/addvar key=extra "- Setting Type: {{getvar::settingType}}"|
	/setvar key=genSettings index=extraContext {{getvar::extra}}|
	/setvar key=extra []|
	/:"CMC Logic.Get Basic Type Context"|
	/ife (extra != '') {:
		/setvar key=genSettings index=contextKey {{getvar::extra}}|
	:}|
	/flushvar extra|
	/wait {{getvar::wait}}|
	
	/getvar key=genSettings index=inputIsList|
	/let key=inputIsList {{pipe}}|
	/getvar key=genSettings index=inputIsList|
	/let key=outputIsList {{pipe}}|
	
	
	/ife ((inputIsList== 'Yes') or (outputIsList == 'Yes')) {:
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
	/flushvar guidance|
	/flushvar genOrder|
	/flushvar genContent|
	/flushvar genSettings|
:}|
/else {:
	/addvar key=dataBaseNames {{var::variableName}}|
:}|
//-----------|

/ife ((appearanceFeatures != 'None') and (appearanceFeatures != '')) {:
	//Features Type|
	/var key=do No|
	/var key=variableName "appearanceFeaturesTypes"|
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
		/setvar key=genSettings index=wi_book_key "Appearance Features Type"|
		/setvar key=genSettings index=genIsList No|
		/setvar key=genSettings index=inputIsList Yes|
		/setvar key=genSettings index=genIsSentence Yes|
		/setvar key=genSettings index=needOutput No|
		/setvar key=genSettings index=outputIsList No|
		/setvar key=genSettings index=useContext Yes|
		/setvar key=extra []|
		/addvar key=extra "- Species Group: {{getvar::speciesGroup}}"|
		/addvar key=extra "- Setting Type: {{getvar::settingType}}"|
		/setvar key=genSettings index=extraContext {{getvar::extra}}|
		/setvar key=extra []|
		/:"CMC Logic.Get Basic Type Context"|
		/ife (extra != '') {:
			/setvar key=genSettings index=contextKey {{getvar::extra}}|
		:}|
		/flushvar extra|
		/wait {{getvar::wait}}|
		
		/getvar key=genSettings index=inputIsList|
		/let key=inputIsList {{pipe}}|
		/getvar key=genSettings index=inputIsList|
		/let key=outputIsList {{pipe}}|
		
		
		/ife ((inputIsList == 'Yes') or (outputIsList == 'Yes')) {:
			/setvar as=array key={{var::variableName}} []|
		:}|
		/else {:
			/setvar as=string key={{var::variableName}} {{noop}}|
		:}|
		//[[Generate with Prompt]]|
		/ife (inputIsList == 'Yes') {:
			/let key=tempOutputList []|
			/foreach {{getvar::appearanceFeatures}} {:
				/setvar key=feature {{var::item}}|
				/setvar key=genSettings index=buttonPrompt Is this the feature type you want for the {{getvar::feature}}?|
				/:"CMC Logic.GenerateWithPrompt"|
				/len {{var::tempOutputList}}|
				/var key=tempOutputList index={{pipe}} {{getvar::output}}|
				/flushvar output|
				/flushvar guidance|
			:}|
			/foreach {{var::tempOutputList}} {:
				/addvar key={{var::variableName}} {{var::item}}|
			:}|
			/flushvar {{var::variableName}}Item|
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
	
	//Features Placement|
	
	/var key=do No|
	/var key=variableName "appearanceFeaturesPlacements"|
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
		/setvar key=genSettings index=wi_book_key "Appearance Features Placement"|
		/setvar key=genSettings index=genIsList No|
		/setvar key=genSettings index=inputIsList Yes|
		/setvar key=genSettings index=genIsSentence Yes|
		/setvar key=genSettings index=needOutput Yes|
		/setvar key=genSettings index=outputIsList No|
		/setvar key=genSettings index=useContext Yes|
		/setvar key=extra []|
		/addvar key=extra "- Species Group: {{getvar::speciesGroup}}"|
		/addvar key=extra "- Setting Type: {{getvar::settingType}}"|
		/setvar key=genSettings index=extraContext {{getvar::extra}}|
		/setvar key=extra []|
		/:"CMC Logic.Get Basic Type Context"|
		/ife (extra != '') {:
			/setvar key=genSettings index=contextKey {{getvar::extra}}|
		:}|
		/flushvar extra|
		/wait {{getvar::wait}}|
		
		/getvar key=genSettings index=inputIsList|
		/let key=inputIsList {{pipe}}|
		/getvar key=genSettings index=inputIsList|
		/let key=outputIsList {{pipe}}|
		
		
		/ife ((inputIsList == 'Yes') or (outputIsList == 'Yes')) {:
			/setvar as=array key={{var::variableName}} []|
		:}|
		/else {:
			/setvar as=string key={{var::variableName}} {{noop}}|
		:}|
		//[[Generate with Prompt]]|
		/ife (inputIsList == 'Yes') {:
			/let key=tempOutputList []|
			/foreach {{getvar::appearanceFeatures}} {:
				/setvar key=feature {{var::item}}|
				/getvar key=appearanceFeaturesTypes index={{var::index}}|
				/setvar key=featureType {{pipe}}|
				/ife (featureType == 'None') {:
					/setvar key=featureType {{noop}}|
				:}|
				/else {:
					/setvar key=featureType "Let the phrasing be influenced by its {{getvar::featureType}} form."
				:}|
				/setvar key=genSettings index=buttonPrompt Is this the feature placement you want for the {{getvar::feature}}?|
				/:"CMC Logic.GenerateWithPrompt"|
				/len {{var::tempOutputList}}|
				/var key=tempOutputList index={{pipe}} {{getvar::output}}|
				/flushvar output|
				/flushvar guidance|
				/flushvar featureType|
				/flushvar featureDescription|
			:}|
			/foreach {{var::tempOutputList}} {:
				/addvar key={{var::variableName}} {{var::item}}|
			:}|
			/flushvar {{var::variableName}}Item|
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
	
	//Features Description|
	
	/var key=do No|
	/var key=variableName "appearanceFeaturesDescriptions"|
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
		/setvar key=genSettings index=wi_book_key "Appearance Features Description"|
		/setvar key=genSettings index=genIsList No|
		/setvar key=genSettings index=inputIsList Yes|
		/setvar key=genSettings index=genIsSentence Yes|
		/setvar key=genSettings index=needOutput Yes|
		/setvar key=genSettings index=outputIsList No|
		/setvar key=genSettings index=useContext Yes|
		/setvar key=extra []|
		/addvar key=extra "- Species Group: {{getvar::speciesGroup}}"|
		/addvar key=extra "- Setting Type: {{getvar::settingType}}"|
		/setvar key=genSettings index=extraContext {{getvar::extra}}|
		/setvar key=extra []|
		/:"CMC Logic.Get Basic Type Context"|
		/ife (extra != '') {:
			/setvar key=genSettings index=contextKey {{getvar::extra}}|
		:}|
		/flushvar extra|
		/wait {{getvar::wait}}|
		
		/getvar key=genSettings index=inputIsList|
		/let key=inputIsList {{pipe}}|
		/getvar key=genSettings index=inputIsList|
		/let key=outputIsList {{pipe}}|
		
		
		/ife ((inputIsList == 'Yes') or (outputIsList == 'Yes')) {:
			/setvar as=array key={{var::variableName}} []|
		:}|
		/else {:
			/setvar as=string key={{var::variableName}} {{noop}}|
		:}|
		//[[Generate with Prompt]]|
		/ife (inputIsList == 'Yes') {:
			/let key=tempOutputList []|
			/foreach {{getvar::appearanceFeatures}} {:
				/setvar key=feature {{var::item}}|
				/getvar key=appearanceFeaturesTypes index={{var::index}}|
				/setvar key=featureType {{pipe}}|
				/ife (featureType == 'None') {:
					/setvar key=featureType {{noop}}|
				:}|
				/else {:
					/setvar key=featureType ", incorporating {{getvar::featureType}} if it adds clarity"|
				:}|
				/getvar key=appearanceFeaturesPlacements index={{var::index}}|
				/setvar key=featuresPlacement {{pipe}}|
				/setvar key=logicBasedInstruction {{noop}}|
				/setvar key=x 5|
				
				/ife (featureType != '') {:
					/incvar x|
					/ife ( logicBasedInstruction != '') {:
						/addvar key=logicBasedInstruction {{newline}}|
					:}|
					/addvar key=logicBasedInstruction "{{getvar::x}}. Use any descriptive terms provided about the feature’s style, texture, or form naturally in the sentence. Do not label them or repeat the feature name."|
					
				:}|
				/flushvar x|
				/setvar key=genSettings index=buttonPrompt Is this the feature description you want for the {{getvar::feature}}?|
				/:"CMC Logic.GenerateWithPrompt"|
				/len {{var::tempOutputList}}|
				/var key=tempOutputList index={{pipe}} {{getvar::output}}|
				/flushvar output|
				/flushvar guidance|
				/flushvar logicBasedInstruction|
			:}|
			/foreach {{var::tempOutputList}} {:
				/addvar key={{var::variableName}} {{var::item}}|
			:}|
			/flushvar {{var::variableName}}Item|
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
:}|
/else {:
	/setvar key=appearanceFeaturesTypes None|
	/addvar key=dataBaseNames appearanceFeaturesTypes|
	/setvar key=appearanceFeaturesPlacements None|
	/addvar key=dataBaseNames appearanceFeaturesPlacements|
	/setvar key=appearanceFeaturesDescriptions None|
	/addvar key=dataBaseNames appearanceFeaturesDescriptions|
:}|

/setvar key=parsedAppearanceFeatures {{noop}}|
/ife ((appearanceFeatures != '') and (appearanceFeatures != 'None') and (appearanceFeatures is list)) {:
	/foreach {{getvar::appearanceFeatures}} {:
		/ife ( index > 0) {:
			/addvar key=parsedAppearanceFeatures "{{newline}}{{newline}}"|
		:}|
		/addvar key=parsedAppearanceFeatures "- Feature: {{var::item}}"|
		/getvar key=appearanceFeaturesTypes index={{var::index}}|
		/let key=aType {{pipe}}|
		/ife (aType != 'None') {:
			/addvar key=parsedAppearanceFeatures "{{newline}}  - Type: {{var::aType}}"|
		:}|
		/getvar key=appearanceFeaturesPlacements index={{var::index}}|
		/addvar key=parsedAppearanceFeatures "{{newline}}  - Placement: {{pipe}}"|
		/getvar key=appearanceFeaturesDescriptions index={{var::index}}|
		/addvar key=parsedAppearanceFeatures "{{newline}}  - Description: {{pipe}}"|
	:}|
:}|
/else {:
	/setvar key=parsedAppearanceFeatures None|
	/addvar key=dataBaseNames parsedAppearanceFeatures|
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
		/setvar key=genSettings {}|
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
		/setvar key=extra []|
		/:"CMC Logic.Get Basic Type Context"|
		/ife (extra != '') {:
			/setvar key=genSettings index=contextKey {{getvar::extra}}|
		:}|
		/else {:
			/setvar key=genSettings index=contextKey []|
		:}|
		/flushvar extra|
		/wait {{getvar::wait}}|
		
		/getvar key=genSettings index=inputIsList|
		/let key=inputIsList {{pipe}}|
		/getvar key=genSettings index=inputIsList|
		/let key=outputIsList {{pipe}}|
		
		
		/ife ((inputIsList== 'Yes') or (outputIsList == 'Yes')) {:
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
		/setvar key=genSettings {}|
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
		/setvar key=extra []|
		/:"CMC Logic.Get Basic Type Context"|
		/ife (extra != '') {:
			/setvar key=genSettings index=contextKey {{getvar::extra}}|
		:}|
		/else {:
			/setvar key=genSettings index=contextKey []|
		:}|
		/flushvar extra|
		/wait {{getvar::wait}}|
		
		/getvar key=genSettings index=inputIsList|
		/let key=inputIsList {{pipe}}|
		/getvar key=genSettings index=inputIsList|
		/let key=outputIsList {{pipe}}|
		
		
		/ife ((inputIsList== 'Yes') or (outputIsList == 'Yes')) {:
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
	/setvar key=genSettings {}|
	/setvar key=genSettings index=wi_book_key "Appearance Face"|
	/setvar key=genSettings index=genIsList No|
	/setvar key=genSettings index=inputIsTaskList No|
	/setvar key=genSettings index=genIsSentence Yes|
	/setvar key=genSettings index=needOutput Yes|
	/setvar key=genSettings index=outputIsList No|
	/setvar key=genSettings index=useContext Yes|
	/setvar key=extra []|
	/:"CMC Logic.Get Basic Type Context"|
	/ife (extra != '') {:
		/setvar key=genSettings index=contextKey {{getvar::extra}}|
	:}|
	/flushvar extra|
	/wait {{getvar::wait}}|
	
	/getvar key=genSettings index=inputIsList|
	/let key=inputIsList {{pipe}}|
	/getvar key=genSettings index=inputIsList|
	/let key=outputIsList {{pipe}}|
	
	
	/ife ((inputIsList== 'Yes') or (outputIsList == 'Yes')) {:
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
	/flushvar guidance|
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
	/setvar key=genSettings {}|
	/setvar key=genSettings index=wi_book_key "Appearance Hair"|
	/setvar key=genSettings index=genIsList No|
	/setvar key=genSettings index=inputIsTaskList No|
	/setvar key=genSettings index=genIsSentence Yes|
	/setvar key=genSettings index=needOutput Yes|
	/setvar key=genSettings index=outputIsList No|
	/setvar key=genSettings index=useContext Yes|
	/setvar key=extra []|
	/addvar key=extra "- Face Description: {{getvar::appearanceFace}}"|
	/setvar key=genSettings index=extraContext {{getvar::extra}}|
	/setvar key=extra []|
	/:"CMC Logic.Get Basic Type Context"|
	/ife (extra != '') {:
		/setvar key=genSettings index=contextKey {{getvar::extra}}|
	:}|
	/flushvar extra|
	/wait {{getvar::wait}}|
	
	/getvar key=genSettings index=inputIsList|
	/let key=inputIsList {{pipe}}|
	/getvar key=genSettings index=inputIsList|
	/let key=outputIsList {{pipe}}|
	
	
	/ife ((inputIsList== 'Yes') or (outputIsList == 'Yes')) {:
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
	/flushvar guidance|
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
	/setvar key=genSettings {}|
	/setvar key=genSettings index=wi_book_key "Appearance Eyes"|
	/setvar key=genSettings index=genIsList No|
	/setvar key=genSettings index=inputIsTaskList No|
	/setvar key=genSettings index=genIsSentence Yes|
	/setvar key=genSettings index=needOutput Yes|
	/setvar key=genSettings index=outputIsList No|
	/setvar key=genSettings index=useContext Yes|
	/setvar key=extra []|
	/addvar key=extra "- Face Description: {{getvar::appearanceFace}}"|
	/setvar key=genSettings index=extraContext {{getvar::extra}}|
	/setvar key=extra []|
	/:"CMC Logic.Get Basic Type Context"|
	/ife (extra != '') {:
		/setvar key=genSettings index=contextKey {{getvar::extra}}|
	:}|
	/flushvar extra|
	/wait {{getvar::wait}}|
	
	/getvar key=genSettings index=inputIsList|
	/let key=inputIsList {{pipe}}|
	/getvar key=genSettings index=inputIsList|
	/let key=outputIsList {{pipe}}|
	
	
	/ife ((inputIsList== 'Yes') or (outputIsList == 'Yes')) {:
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
	/flushvar guidance|
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
	/setvar key=genSettings {}|
	/setvar key=genSettings index=wi_book_key "Appearance Body"|
	/setvar key=genSettings index=genIsList No|
	/setvar key=genSettings index=inputIsTaskList No|
	/setvar key=genSettings index=genIsSentence Yes|
	/setvar key=genSettings index=needOutput Yes|
	/setvar key=genSettings index=outputIsList No|
	/setvar key=genSettings index=useContext Yes|
	/setvar key=extra []|
	/ife (appearanceFeatures != 'None') {:
		/addvar key=extra "{{getvar::parsedAppearanceFeatures}}"|
	:}|
	/setvar key=genSettings index=extraContext {{getvar::extra}}|
	/setvar key=extra []|
	/:"CMC Logic.Get Basic Type Context"|
	/ife (extra != '') {:
		/setvar key=genSettings index=contextKey {{getvar::extra}}|
	:}|
	/flushvar extra|
	/wait {{getvar::wait}}|
	
	/getvar key=genSettings index=inputIsList|
	/let key=inputIsList {{pipe}}|
	/getvar key=genSettings index=inputIsList|
	/let key=outputIsList {{pipe}}|
	
	/setvar key=logicBasedInstruction {{noop}}|
	/setvar key=x 9|
	
	/ife (( characterArchetype == 'Human') or ( characterArchetype == 'Android')) {:
		/incvar x|
		/ife ( logicBasedInstruction != '') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. Do not include tails, wings, hooves, digitigrade legs, animalistic limbs, or non-human anatomy. Use human structure only."|
		/incvar x|
		/ife ( logicBasedInstruction != '') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. Describe only human anatomical structure — posture should be upright and bipedal, with no tails or animalistic features. Focus on general proportions and center of gravity if relevant."|
		
	:}|
	/elseif (( characterArchetype != 'Human') and ( characterArchetype != 'Android') and (appearanceFeatures != 'None')) {:
		/incvar x|
		/ife ( logicBasedInstruction != '') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. If '{{getvar::appearanceFeatures}}' includes non-human traits (e.g., tail, claws, digitigrade stance), describe how they affect posture, balance, or silhouette."|
		/incvar x|
		/ife ( logicBasedInstruction != '') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. Incorporate any relevant non-human traits (e.g., tails, hooves, digitigrade legs) from '{{getvar::appearanceFeatures}}' into descriptions of balance, movement, or posture."|
	:}|
	/elseif (( characterArchetype != 'Human') and ( characterArchetype != 'Android') and (appearanceFeatures == 'None')) {:
		/incvar x|
		/ife ( logicBasedInstruction != '') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. Use a species-appropriate body structure, but do not describe any extra non-human features unless clearly implied by species type."|
		/incvar x|
		/ife ( logicBasedInstruction != '') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. Do not invent tails, claws, wings, or non-human limbs unless strongly implied by species type. Focus on body shape, stance, or balance based on general archetype alone."|		
	:}|
	/flushvar x|
	
	/ife ((inputIsList== 'Yes') or (outputIsList == 'Yes')) {:
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
	/flushvar guidance|
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
		/buttons labels=["Flat", "Small", "Medium", "Large", "Huge"] What size is {{getvar::firstName}}'s Breasts?|
		/setvar key=breastSize {{pipe}}|
		/ife (breastSize == '') {:
	        /echo Aborting |
	        /abort
	    :}|
		/setvar key=genSettings {}|
		/setvar key=genSettings index=wi_book_key "Appearance Breasts"|
		/setvar key=genSettings index=genIsList No|
		/setvar key=genSettings index=inputIsTaskList No|
		/setvar key=genSettings index=genIsSentence Yes|
		/setvar key=genSettings index=needOutput Yes|
		/setvar key=genSettings index=outputIsList No|
		/setvar key=genSettings index=useContext Yes|
		/setvar key=extra []|
		/addvar key=extra "- Body: {{getvar::appearanceBody}}"|
		/addvar key=extra "- Breast Size: {{getvar::breastSize}}"|
		/ife (appearanceFeatures != 'None') {:
			/addvar key=extra "{{getvar::parsedAppearanceFeatures}}"|
		:}|
		/setvar key=genSettings index=extraContext {{getvar::extra}}|
		/setvar key=extra []|
		/:"CMC Logic.Get Basic Type Context"|
		/ife (extra != '') {:
			/setvar key=genSettings index=contextKey {{getvar::extra}}|
		:}|
		/flushvar extra|
		/wait {{getvar::wait}}|
		
		/getvar key=genSettings index=inputIsList|
		/let key=inputIsList {{pipe}}|
		/getvar key=genSettings index=inputIsList|
		/let key=outputIsList {{pipe}}|
		
		/setvar key=logicBasedInstruction {{noop}}|
		/setvar key=x 7|
		
		/ife (characterArchetype == 'Tauric') {:
			/incvar x|
			/ife ( logicBasedInstruction != '') {:
				/addvar key=logicBasedInstruction {{newline}}|
			:}|
			/addvar key=logicBasedInstruction "{{getvar::x}}. Breasts are located on the humanoid torso — do not describe them as part of the lower animal body."|
			
		:}|
		/elseif ((characterArchetype == 'Animalistic') and (speciesGroup != 'Fantasy')) {:
			/incvar x|
			/ife ( logicBasedInstruction != '') {:
				/addvar key=logicBasedInstruction {{newline}}|
			:}|
			/addvar key=logicBasedInstruction "{{getvar::x}}. Do not describe breasts — most realistic Animalistic species lack humanoid chest anatomy. Focus on muscular bulk or species-appropriate chest traits."|
			
		:}|
		/elseif ((characterArchetype == 'Animalistic') and ((speciesGroup == 'Fantasy') or (speciesGroup == 'Alien') or (speciesGroup == 'Demonic') or (speciesGroup == 'Mammal'))) {:
			/incvar x|
			/ife ( logicBasedInstruction != '') {:
				/addvar key=logicBasedInstruction {{newline}}|
			:}|
			/addvar key=logicBasedInstruction "{{getvar::x}}. Breasts may be described only if the species is explicitly humanoid or mammalian in design. Use anatomical framing consistent with fantasy physiology."|
			
		:}|
		/flushvar x|
		
		
		/ife ((inputIsList== 'Yes') or (outputIsList == 'Yes')) {:
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
		/flushvar guidance|
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
		/setvar key=genSettings {}|
		/setvar key=genSettings index=wi_book_key "Appearance Nipples"|
		/setvar key=genSettings index=genIsList No|
		/setvar key=genSettings index=inputIsTaskList No|
		/setvar key=genSettings index=genIsSentence Yes|
		/setvar key=genSettings index=needOutput Yes|
		/setvar key=genSettings index=outputIsList No|
		/setvar key=genSettings index=useContext Yes|
		/setvar key=extra []|
		/addvar key=extra "- Body: {{getvar::appearanceBody}}"|
		/addvar key=extra "- Breasts: {{getvar::appearanceBreasts}}"|
		/ife (appearanceFeatures != 'None') {:
			/addvar key=extra "{{getvar::parsedAppearanceFeatures}}"|
		:}|
		/setvar key=genSettings index=extraContext {{getvar::extra}}|
		/setvar key=extra []|
		/:"CMC Logic.Get Basic Type Context"|
		/ife (extra != '') {:
			/setvar key=genSettings index=contextKey {{getvar::extra}}|
		:}|
		/flushvar extra|
		/wait {{getvar::wait}}|
		
		/getvar key=genSettings index=inputIsList|
		/let key=inputIsList {{pipe}}|
		/getvar key=genSettings index=inputIsList|
		/let key=outputIsList {{pipe}}|
		
		/setvar key=logicBasedInstruction {{noop}}|
		/setvar key=x 7|
		
		/ife (characterArchetype == 'Tauric') {:
			/incvar x|
			/ife ( logicBasedInstruction != '') {:
				/addvar key=logicBasedInstruction {{newline}}|
			:}|
			/addvar key=logicBasedInstruction "{{getvar::x}}. Nipples are placed on the humanoid upper torso. Do not describe any features on the lower animal body."|
			
		:}|
		/ife (( 'fur' in logicBasedInstruction) or ( 'Fur' in logicBasedInstruction)) {:
			/incvar x|
			/ife ( logicBasedInstruction != '') {:
				/addvar key=logicBasedInstruction {{newline}}|
			:}|
			/addvar key=logicBasedInstruction "{{getvar::x}}. Areolae may be partially obscured by fur or lightly visible beneath it. Use fur-based skin logic for color and contrast."|
			
		:}|
		/elseif (( 'scales' in logicBasedInstruction) or ( 'Scales' in logicBasedInstruction)) {:
			/incvar x|
			/ife ( logicBasedInstruction != '') {:
				/addvar key=logicBasedInstruction {{newline}}|
			:}|
			/addvar key=logicBasedInstruction "{{getvar::x}}. Areolae may appear slightly raised or differently textured than surrounding scales. Coloration and contrast should match scaled coverage."|
			
		:}|
		/elseif (( 'fur' not in logicBasedInstruction) and ( 'Fur' not in logicBasedInstruction) and ( 'scales' not in logicBasedInstruction) and ( 'Scales' not in logicBasedInstruction)) {:
			/incvar x|
			/ife ( logicBasedInstruction != '') {:
				/addvar key=logicBasedInstruction {{newline}}|
			:}|
			/addvar key=logicBasedInstruction "{{getvar::x}}. Use skin-based detail — focus on tone, contour, and texture. Keep all surface description rooted in visible, uncovered human-like anatomy."|
			
		:}|
		/flushvar x|
		
		
		/ife ((inputIsList== 'Yes') or (outputIsList == 'Yes')) {:
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
		/flushvar guidance|
		/flushvar genOrder|
		/flushvar genContent|
		/flushvar genSettings|
	:}|
	/else {:
		/addvar key=dataBaseNames {{var::variableName}}|
	:}|
//-----------|
:}|
/else {:
	/setvar key=appearanceBreasts None|
	/setvar key=appearanceNipples None|
	/addvar key=dataBaseNames appearanceBreasts|
	/addvar key=dataBaseNames appearanceNipples|
:}|

//**Pussy**|
/var key=do No|
/var key=variableName "appearancePussy"|
/ife ((gender == 'Female') or (futanari == 'Yes')) {:
	
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
		/buttons labels=["Hidden", "Visible", "Visible and Prominent"] Is {{getvar::firstName}}'s Clit Visible?|
		/setvar key=clitVisability {{pipe}}|
		/ife (clitVisability == '') {:
			/echo Aborting |
			/abort
		:}|
		/buttons labels=["Hidden", "Visible", "Visible and Prominent"] Is {{getvar::firstName}}'s Labia Minora Visible?|
		/setvar key=labiaMinoraVisability {{pipe}}|
		/ife (labiaMinoraVisability == '') {:
			/echo Aborting |
			/abort
		:}|
		
		/buttons labels=["Smooth", "Shaven with stubble", "Unshaven and bushy", "Trimmed"] Is {{getvar::firstName}}'s Labia Minora Visible?|
		/setvar key=pubicHair {{pipe}}|
		/ife (pubicHair == '') {:
			/echo Aborting |
			/abort
		:}|
		/setvar key=genSettings {}|
		/setvar key=genSettings index=wi_book_key "Appearance Pussy"|
		/setvar key=genSettings index=genIsList No|
		/setvar key=genSettings index=inputIsTaskList No|
		/setvar key=genSettings index=genIsSentence Yes|
		/setvar key=genSettings index=needOutput Yes|
		/setvar key=genSettings index=outputIsList No|
		/setvar key=genSettings index=useContext Yes|
		/setvar key=extra []|
		/addvar key=extra "- Body: {{getvar::appearanceBody}}"|
		/ife (appearanceFeatures != 'None') {:
			/addvar key=extra "{{getvar::parsedAppearanceFeatures}}"|
		:}|
		/addvar key=extra "- Female  Genital Type: {{getvar::privatesFemale}}"|
		/addvar key=extra "- Species Group: {{getvar::speciesGroup}}"|
		/addvar key=extra "- Animal Base: {{getvar::animalBase}}"|
		/addvar key=extra "- Clit Visability: {{getvar::clitVisability}}"|
		/addvar key=extra "- Labia Minora Visability: {{getvar::labiaMinoraVisability}}"|
		/ife (futanari == 'Yes') {:
			/addvar key=extra "Important: {{getvar::firstName}} is a futanari, so she has both a pussy and a cock."|
		:}|
		/setvar key=genSettings index=extraContext {{getvar::extra}}|
		/setvar key=extra []|
		/:"CMC Logic.Get Basic Type Context"|
		/ife (extra != '') {:
			/setvar key=genSettings index=contextKey {{getvar::extra}}|
		:}|
		/wait {{getvar::wait}}|
		
		/getvar key=genSettings index=inputIsList|
		/let key=inputIsList {{pipe}}|
		/getvar key=genSettings index=inputIsList|
		/let key=outputIsList {{pipe}}|
		
		/setvar key=logicBasedInstruction {{noop}}|
		/setvar key=x 8|
		
		/ife (futanari == 'Yes') {:
			/incvar x|
			/ife ( logicBasedInstruction != '') {:
				/addvar key=logicBasedInstruction {{newline}}|
			:}|
			/addvar key=logicBasedInstruction "{{getvar::x}}. Only describe the vulva — do not mention or reference the cock, even by proximity."|
			
		:}|
		/ife (privatesFemale == 'Mammal') {:
			/incvar x|
			/ife ( logicBasedInstruction != '') {:
				/addvar key=logicBasedInstruction {{newline}}|
			:}|
			/addvar key=logicBasedInstruction "{{getvar::x}}. The vulva may include outer and inner lips, a visible slit, or light pubic hair or fur. Use anatomical terms like “folds,” “cleft,” or “labia” as appropriate."|
			
		:}|
		/elseif (privatesFemale == 'Reptile') {:
			/incvar x|
			/ife ( logicBasedInstruction != '') {:
				/addvar key=logicBasedInstruction {{newline}}|
			:}|
			/addvar key=logicBasedInstruction "{{getvar::x}}. The slit may appear smooth, scaled, or slightly ridged. Do not describe fur, hair, or soft fleshy folds. Placement may be flush with surrounding scale plates."|
			
		:}|
		/elseif (privatesFemale == 'Bird') {:
			/incvar x|
			/ife ( logicBasedInstruction != '') {:
				/addvar key=logicBasedInstruction {{newline}}|
			:}|
			/addvar key=logicBasedInstruction "{{getvar::x}}. The vulva may be recessed or hidden beneath feathers. If the species uses a cloacal structure, describe it as smooth and integrated near the tail base. Avoid mammalian terminology."|
			
		:}|
		/elseif (privatesFemale == 'Fish') {:
			/incvar x|
			/ife ( logicBasedInstruction != '') {:
				/addvar key=logicBasedInstruction {{newline}}|
			:}|
			/addvar key=logicBasedInstruction "{{getvar::x}}. Use phrases like “smooth slit,” “recessed fold,” or “ventral placement.” Avoid fur or lip-based descriptions. The texture should reflect aquatic biology."|
			
		:}|
		/elseif (privatesFemale == 'Amphibian') {:
			/incvar x|
			/ife ( logicBasedInstruction != '') {:
				/addvar key=logicBasedInstruction {{newline}}|
			:}|
			/addvar key=logicBasedInstruction "{{getvar::x}}. The vulva may be soft, moist-looking, and smooth-skinned. Avoid terms like fur, hair, or lips. Structure should appear simple and subtle."|
			
		:}|
		/elseif (privatesFemale == 'Invertebrate') {:
			/incvar x|
			/ife ( logicBasedInstruction != '') {:
				/addvar key=logicBasedInstruction {{newline}}|
			:}|
			/addvar key=logicBasedInstruction "{{getvar::x}}. Structure may appear segmented, chitinous, or soft-bodied. Use terms like “opening,” “ventral slit,” or “intersegmental ridge.” Avoid all mammalian descriptors."|
			
		:}|
		/elseif (privatesFemale == 'Cephalopod') {:
			/incvar x|
			/ife ( logicBasedInstruction != '') {:
				/addvar key=logicBasedInstruction {{newline}}|
			:}|
			/addvar key=logicBasedInstruction "{{getvar::x}}. The vulva may appear smooth, ringed, or recessed between soft folds or tentacle bases. Avoid describing labia or lips unless the species is hybridized."|
			
		:}|
		/elseif (privatesFemale == 'Synthetic') {:
			/incvar x|
			/ife ( logicBasedInstruction != '') {:
				/addvar key=logicBasedInstruction {{newline}}|
			:}|
			/addvar key=logicBasedInstruction "{{getvar::x}}. If the vulva is synthetic or sculpted, describe it as smooth, artificial, or bio-mimetic. Do not reference organic function, fluids, or reproductive cues."|
			
		:}|
		/elseif (privatesFemale == 'Fantasy') {:
			/incvar x|
			/ife ( logicBasedInstruction != '') {:
				/addvar key=logicBasedInstruction {{newline}}|
			:}|
			/addvar key=logicBasedInstruction "{{getvar::x}}. Vulva structure may include subtle magical, exotic, or hybrid traits — but keep all language anatomical and grounded. Avoid metaphor, emotion, or subjective tone."|
			
		:}|
		/elseif (privatesFemale == 'Alien') {:
			/incvar x|
			/ife ( logicBasedInstruction != '') {:
				/addvar key=logicBasedInstruction {{newline}}|
			:}|
			/addvar key=logicBasedInstruction "{{getvar::x}}. Vulva may appear asymmetrical, oddly colored, or biologically unique. Keep tone anatomical — do not invent behavior or function unless implied by the context."|
			
		:}|
		/elseif ( (privatesFemale == 'Feline') or (privatesFemale == 'Canine') or (privatesFemale == 'Ursine') or (privatesFemale == 'Leporidae') ) {:
			/incvar x|
			/ife ( logicBasedInstruction != '') {:
				/addvar key=logicBasedInstruction {{newline}}|
			:}|
			/addvar key=logicBasedInstruction "{{getvar::x}}. You may describe soft fur or pubic hair around the vulva if the character’s surface features indicate fur. Do not use fur-related descriptors if none are present."|
			
		:}|
		/elseif ( (privatesFemale == 'Draconic') or (privatesFemale == 'Lacertilian') or (privatesFemale == 'Serpentine') or (privatesFemale == 'Crocodilian') ) {:
			/incvar x|
			/ife ( logicBasedInstruction != '') {:
				/addvar key=logicBasedInstruction {{newline}}|
			:}|
			/addvar key=logicBasedInstruction "{{getvar::x}}. The vulva may be partially hidden by or integrated into scale patterns. Avoid soft or fleshy mammalian terms unless hybridized."|
			
		:}|
		/elseif ( (privatesFemale == 'Passerine') or (privatesFemale == 'Raptor') or (privatesFemale == 'Ratite') or (privatesFemale == 'Aviary') ) {:
			/incvar x|
			/ife ( logicBasedInstruction != '') {:
				/addvar key=logicBasedInstruction {{newline}}|
			:}|
			/addvar key=logicBasedInstruction "{{getvar::x}}. Vulva may be positioned beneath feathers or integrated into a cloacal structure. Keep surface detail minimal and avoid fur, lips, or fleshy folds."|
			
		:}|
		
		
		/flushvar x|
		
		
		/ife ((inputIsList== 'Yes') or (outputIsList == 'Yes')) {:
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
		/flushvar guidance|
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
/else {:
	/setvar key={{var::variableName}} None|
	/addvar key=dataBaseNames {{var::variableName}}|
:}|


//**Cock**|
/var key=do No|
/var key=variableName "appearanceCock"|
/ife ((gender == 'Male') or (futanari == 'Yes' )) {:
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
		/setvar key=genSettings index=wi_book_key "Appearance Cock"|
		/setvar key=genSettings index=genIsList No|
		/setvar key=genSettings index=inputIsTaskList No|
		/setvar key=genSettings index=genIsSentence Yes|
		/setvar key=genSettings index=needOutput Yes|
		/setvar key=genSettings index=outputIsList No|
		/setvar key=genSettings index=useContext Yes|
		/setvar key=extra []|
		/addvar key=extra "- Body: {{getvar::appearanceBody}}"|
		/ife (appearanceFeatures != 'None') {:
			/addvar key=extra "{{getvar::parsedAppearanceFeatures}}"|
		:}|
		/ife (futanari == 'Yes') {:
			/addvar key=extra "- Pussy Appearance: {{getvar::appearancePussy}}"|
		:}|
		/addvar key=extra "- Male Genital Type:: {{getvar::privatesMale}}"|
		/addvar key=extra "- Species Group: {{getvar::speciesGroup}}"|
		/addvar key=extra "- Animal Base: {{getvar::animalBase}}"|
		/ife (futanari == 'Yes') {:
			/addvar key=extra "Important: {{getvar::firstName}} is a futanari, so she has both a pussy and a cock."|
		:}|
		/setvar key=genSettings index=extraContext {{getvar::extra}}|
		/setvar key=extra []|
		/:"CMC Logic.Get Basic Type Context"|
		/ife (extra != '') {:
			/setvar key=genSettings index=contextKey {{getvar::extra}}|
		:}|
		/flushvar extra|
		
		/wait {{getvar::wait}}|
		
		/getvar key=genSettings index=inputIsList|
		/let key=inputIsList {{pipe}}|
		/getvar key=genSettings index=inputIsList|
		/let key=outputIsList {{pipe}}|
		
		
		/setvar key=logicBasedInstruction {{noop}}|
		/setvar key=x 8|
		
		/ife (futanari == 'Yes') {:
			/incvar x|
			/ife ( logicBasedInstruction != '') {:
				/addvar key=logicBasedInstruction {{newline}}|
			:}|
			/addvar key=logicBasedInstruction "{{getvar::x}}. Rule"|
			
		:}|
		/ife (privatesMale == 'Mammal') {:
			/incvar x|
			/ife ( logicBasedInstruction != '') {:
				/addvar key=logicBasedInstruction {{newline}}|
			:}|
			/addvar key=logicBasedInstruction "{{getvar::x}}. The shaft may include a foreskin or remain uncovered. Use standard anatomical terms for glans, shaft, and scrotum. Testicles may be furred or bare depending on features."|
			
		:}|
		/elseif (privatesMale == 'Canine') {:
			/incvar x|
			/ife ( logicBasedInstruction != '') {:
				/addvar key=logicBasedInstruction {{newline}}|
			:}|
			/addvar key=logicBasedInstruction "{{getvar::x}}. The shaft may emerge from a sheath and taper to a point. Include a prominent knot at the base if erect. The scrotum may be fur-covered and sit close to the base."|
			
		:}|
		/elseif (privatesMale == 'Feline') {:
			/incvar x|
			/ife ( logicBasedInstruction != '') {:
				/addvar key=logicBasedInstruction {{newline}}|
			:}|
			/addvar key=logicBasedInstruction "{{getvar::x}}. The shaft may feature fine ridges or barbs. When erect, describe a tapered form with slight texture variation. The testicles may be small and soft-furred."|
			
		:}|
		/elseif (privatesMale == 'Equine') {:
			/incvar x|
			/ife ( logicBasedInstruction != '') {:
				/addvar key=logicBasedInstruction {{newline}}|
			:}|
			/addvar key=logicBasedInstruction "{{getvar::x}}. The penis is long, thick, and partially sheathed when flaccid. When erect, it may feature a flared head and medial ring. The testicles are large, pendulous, and smooth-skinned."|
			
		:}|
		/elseif ((privatesMale == 'Reptile') or (privatesMale == 'Draconic')) {:
			/incvar x|
			/ife ( logicBasedInstruction != '') {:
				/addvar key=logicBasedInstruction {{newline}}|
			:}|
			/addvar key=logicBasedInstruction "{{getvar::x}}. The penis may be scaled, muscular, or ridged. It can be tucked into a slit or retractable area. When erect, emphasize texture, internal pressure, or unusual shape without exaggeration."|
			
		:}|
		/elseif ((privatesMale == 'Insectoid') or (privatesMale == 'Arachnid') or (privatesMale == 'Cephalopod')) {:
			/incvar x|
			/ife ( logicBasedInstruction != '') {:
				/addvar key=logicBasedInstruction {{newline}}|
			:}|
			/addvar key=logicBasedInstruction "{{getvar::x}}. The shaft may be segmented, chitinous, or soft-bodied. Avoid human terminology. Use terms like “appendage,” “ventral organ,” or “spiral sheath” depending on structure."|
			
		:}|
		/elseif (privatesMale == 'Synthetic') {:
			/incvar x|
			/ife ( logicBasedInstruction != '') {:
				/addvar key=logicBasedInstruction {{newline}}|
			:}|
			/addvar key=logicBasedInstruction "{{getvar::x}}. The shaft may be artificial, sculpted, or bioengineered. Describe design features such as texture, joint seams, or material finish. Avoid organic function or reproductive cues."|
			
		:}|
		/elseif (privatesMale == 'Alien') {:
			/incvar x|
			/ife ( logicBasedInstruction != '') {:
				/addvar key=logicBasedInstruction {{newline}}|
			:}|
			/addvar key=logicBasedInstruction "{{getvar::x}}. The penis may be asymmetrical, multi-textured, or unusually shaped. Describe with anatomical clarity, not metaphor. You may include multiple elements if the form justifies it."|
			
		:}|
		/elseif (privatesMale == 'Fantasy') {:
			/incvar x|
			/ife ( logicBasedInstruction != '') {:
				/addvar key=logicBasedInstruction {{newline}}|
			:}|
			/addvar key=logicBasedInstruction "{{getvar::x}}. If the anatomy blends known and exotic traits, describe it with neutral detail. Do not invent abilities or hybrid function — structure only."|
			
		:}|
		
		/ife (('fur' in appearanceFeatures) or ('Fur' in appearanceFeatures)) {:
			/incvar x|
			/ife ( logicBasedInstruction != '') {:
				/addvar key=logicBasedInstruction {{newline}}|
			:}|
			/addvar key=logicBasedInstruction "{{getvar::x}}. If the character has fur, you may describe fur around the sheath or scrotum. Keep texture consistent with body coverage."|
			
		:}|
		/elseif (('scales' in appearanceFeatures) or ('Scales' in appearanceFeatures)) {:
			/incvar x|
			/ife ( logicBasedInstruction != '') {:
				/addvar key=logicBasedInstruction {{newline}}|
			:}|
			/addvar key=logicBasedInstruction "{{getvar::x}}. If the character has scales, the shaft may appear ridged or recessed, with the scrotum partially armored or integrated into surrounding body texture."|
			
		:}|
		
		/flushvar x|
		
		
		/ife ((inputIsList== 'Yes') or (outputIsList == 'Yes')) {:
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
		/flushvar guidance|
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
/else {:
	/setvar key={{var::variableName}} None|
	/addvar key=dataBaseNames {{var::variableName}}|
:}|

//**Privates Sync**|
/var key=do No|
/var key=variableName "appearanceGenitals"|
/ife (futanari == 'Yes') {:
	
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
		/setvar key=genSettings index=wi_book_key "Appearance Genitals Sync"|
		/setvar key=genSettings index=genIsList No|
		/setvar key=genSettings index=inputIsTaskList No|
		/setvar key=genSettings index=genIsSentence Yes|
		/setvar key=genSettings index=needOutput Yes|
		/setvar key=genSettings index=outputIsList No|
		/setvar key=genSettings index=useContext Yes|
		/setvar key=extra []|
		/addvar key=extra "- Body: {{getvar::appearanceBody}}"|
		/ife (appearanceFeatures != 'None') {:
			/addvar key=extra "{{getvar::parsedAppearanceFeatures}}"|
		:}|
		/addvar key=extra "- Pussy Appearance: {{getvar::appearancePussy}}"|
		/addvar key=extra "- Female Genital Type:: {{getvar::privatesFemale}}"|
		/addvar key=extra "- Cock Appearance: {{getvar::appearanceCock}}"|
		/addvar key=extra "- Male Genital Type:: {{getvar::privatesMale}}"|
		
		/addvar key=extra "- Species Group: {{getvar::speciesGroup}}"|
		/setvar key=genSettings index=extraContext {{getvar::extra}}|
		/setvar key=extra []|
		/:"CMC Logic.Get Basic Type Context"|
		/ife (extra != '') {:
			/setvar key=genSettings index=contextKey {{getvar::extra}}|
		:}|
		/flushvar extra|
		/wait {{getvar::wait}}|
		
		/getvar key=genSettings index=inputIsList|
		/let key=inputIsList {{pipe}}|
		/getvar key=genSettings index=inputIsList|
		/let key=outputIsList {{pipe}}|
		
		
		/ife ((inputIsList== 'Yes') or (outputIsList == 'Yes')) {:
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
		/flushvar guidance|
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
/else {:
	/setvar key={{var::variableName}} None|
	/addvar key=dataBaseNames {{var::variableName}}|
:}|


//**Anus**|
/var key=do No|
/var key=variableName "appearanceAnus"|
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
	/setvar key=genSettings index=wi_book_key "Appearance Anus"|
	/setvar key=genSettings index=genIsList No|
	/setvar key=genSettings index=inputIsTaskList No|
	/setvar key=genSettings index=genIsSentence Yes|
	/setvar key=genSettings index=needOutput Yes|
	/setvar key=genSettings index=outputIsList No|
	/setvar key=genSettings index=useContext Yes|
	/setvar key=extra []|
	/addvar key=extra "- Body: {{getvar::appearanceBody}}"|
	/ife (appearanceFeatures != 'None') {:
		/addvar key=extra "{{getvar::parsedAppearanceFeatures}}"|
	:}|
	/addvar key=extra "- Species Group: {{getvar::speciesGroup}}"|
	/setvar key=genSettings index=extraContext {{getvar::extra}}|
	/ife (futanari == 'Yes') {:
		/setvar key=logicBasedInstruction "7. {{getvar::firstName}} is a futanari. The anus should be described neutrally and anatomically, with no reference to the cock or pussy."|
	:}|
	/ife ('Tail' in appearanceFeatures) {:
		/ife (logicBasedInstruction == '') {:
			/setvar key=logicBasedInstruction "7. {{getvar::firstName}} has a tail. Describe the anus in relation to the tail's base if visible."|
		:}|
		/else {:
			/addvar key=logicBasedInstruction "{{newline}}7. {{getvar::firstName}} has a tail. Describe the anus in relation to the tail's base if visible."
		:}|
	:}|
	/setvar key=extra []|
	/:"CMC Logic.Get Basic Type Context"|
	/ife (extra != '') {:
		/setvar key=genSettings index=contextKey {{getvar::extra}}|
	:}|
	/flushvar extra|
	/wait {{getvar::wait}}|
	
	/getvar key=genSettings index=inputIsList|
	/let key=inputIsList {{pipe}}|
	/getvar key=genSettings index=inputIsList|
	/let key=outputIsList {{pipe}}|
	
	
	/ife ((inputIsList== 'Yes') or (outputIsList == 'Yes')) {:
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
	/flushvar guidance|
	/flushvar genOrder|
	/flushvar genContent|
	/flushvar genSettings|
	/flushvar logicBasedInstruction|
:}|
/else {:
	/addvar key=dataBaseNames {{var::variableName}}|
:}|
//-----------|

/setvar key=parsedApperance {{noop}}|
/addvar key=parsedApperance ### Appearance|
/ife (length != 'None') {:
	/addvar key=parsedApperance "{{newline}} - Length: {{getvar::length}}"|
:}|
/ife (height != 'None') {:
	/addvar key=parsedApperance "{{newline}} - Height: {{getvar::height}}"|
:}|
/ife (appearanceHair != 'None') {:
	/addvar key=parsedApperance "{{newline}} - Hair: {{getvar::appearanceHair}}"|
:}|
/ife (appearanceEyes != 'None') {:
	/addvar key=parsedApperance "{{newline}} - Eyes: {{getvar::appearanceEyes}}"|
:}|
/ife (appearanceFace != 'None') {:
	/addvar key=parsedApperance "{{newline}} - Face: {{getvar::appearanceFace}}"|
:}|
/addvar key=parsedApperance "{{newline}}### Body{{newline}}- Body:"|
/ife (appearanceBody != 'None') {:
	/addvar key=parsedApperance "{{newline}}  - Body: {{getvar::appearanceBody}}"|
:}|
/ife (appearanceBreasts != 'None') {:
	/addvar key=parsedApperance "{{newline}}  - Breasts: {{getvar::appearanceBreasts}}"|
:}|
/ife (appearanceNipples != 'None') {:
	/addvar key=parsedApperance "{{newline}}  - Nipples: {{getvar::appearanceNipples}}"|
:}|
/ife (appearanceGenitals != 'None') {:
	/addvar key=parsedApperance "{{newline}}  - Genitals: {{getvar::appearanceGenitals}}"|
:}|
/ife ((appearanceGenitals == 'None') and (appearancePussy != 'None')) {:
	/addvar key=parsedApperance "{{newline}}  - Pussy: {{getvar::appearancePussy}}"|
:}|
/ife ((appearanceGenitals == 'None') and (appearanceCock != 'None')) {:
	/addvar key=parsedApperance "{{newline}}  - Cock: {{getvar::appearanceCock}}"|
:}|
/ife (appearanceAnus != 'None') {:
	/addvar key=parsedApperance "{{newline}}  - Anus: {{getvar::appearanceAnus}}"|
:}|
/addvar key=parsedApperance "{{newline}}"|
/addvar key=dataBaseNames parsedApperance|


//**Appearance Traits**|
/var key=do No|
/var key=variableName "appearanceTraits"|
/buttons labels=["Yes", "No"] Do you want {{getvar::firstName}} to have any Appearance Traits?|
/var selected_btn {{pipe}}|
/ife ( selected_btn == 'Yes') {:
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
		/setvar key=appearanceTraitsDetails {{noop}}|
		/setvar key=appearanceTraitsEffect {{noop}}|
		/setvar key=genSettings index=wi_book_key "Appearance Trait Type"|
		/setvar key=genSettings index=genIsList Yes|
		/setvar key=genSettings index=inputIsTaskList No|
		/setvar key=genSettings index=genIsSentence No|
		/setvar key=genSettings index=needOutput No|
		/setvar key=genSettings index=outputIsList Yes|
		/setvar key=genSettings index=useContext Yes|
		/setvar key=extra []|
		/ife (extra != '') {:
			/setvar key=genSettings index=contextKey {{getvar::extra}}|
		:}|
		/flushvar extra|
		/wait {{getvar::wait}}|
		
		/getvar key=genSettings index=inputIsList|
		/let key=inputIsList {{pipe}}|
		/getvar key=genSettings index=inputIsList|
		/let key=outputIsList {{pipe}}|
		
		
		/ife ((inputIsList== 'Yes') or (outputIsList == 'Yes')) {:
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
		/flushvar guidance|
		/flushvar genOrder|
		/flushvar genContent|
		/flushvar genSettings|
		/flushvar logicBasedInstruction|
	:}|
	/else {:
		/addvar key=dataBaseNames {{var::variableName}}|
	:}|
:}|
/else {:
	/setvar key=appearanceTraits None|
	/addvar key=dataBaseNames appearanceTraits|
:}|

/ife ((appearanceTraits != '') and (appearanceTraits != 'None')) {:
	//Descriptions|
	/var key=do No|
	/var key=variableName "appearanceTraitsDetails"|
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
		/setvar key=genSettings index=wi_book_key "Appearance Trait Details"|
		/setvar key=genSettings index=genIsList No|
		/setvar key=genSettings index=inputIsTaskList No|
		/setvar key=genSettings index=inputIsList Yes|
		/setvar key=genSettings index=genIsSentence Yes|
		/setvar key=genSettings index=needOutput Yes|
		/setvar key=genSettings index=outputIsList No|
		/setvar key=genSettings index=useContext Yes|
		/setvar key=extra []|
		/:"CMC Logic.Get Basic Type Context"|
		/ife (extra != '') {:
			/setvar key=genSettings index=contextKey {{getvar::extra}}|
		:}|
		/flushvar extra|
		/wait {{getvar::wait}}|
		
		/getvar key=genSettings index=inputIsList|
		/let key=inputIsList {{pipe}}|
		/getvar key=genSettings index=inputIsList|
		/let key=outputIsList {{pipe}}|
		
		
		/ife ((inputIsList == 'Yes') or (outputIsList == 'Yes')) {:
			/setvar as=array key={{var::variableName}} []|
		:}|
		/else {:
			/setvar as=string key={{var::variableName}} {{noop}}|
		:}|
		//[[Generate with Prompt]]|
		/ife (inputIsList == 'Yes') {:
			/foreach {{getvar::appearanceTraits}} {:
				/setvar key=appearanceTrait {{var::item}}|
				/:"CMC Logic.GenerateWithPrompt"|
				/addvar key={{var::variableName}} {{getvar::output}}|
				/flushvar output|
				/flushvar guidance|
			:}|
			/flushvar appearanceTrait|
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
	
	//|
	/var key=do No|
	/var key=variableName "appearanceTraitsEffect"|
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
		/setvar key=genSettings index=wi_book_key "Appearance Trait Effect"|
		/setvar key=genSettings index=genIsList No|
		/setvar key=genSettings index=inputIsTaskList No|
		/setvar key=genSettings index=inputIsList Yes|
		/setvar key=genSettings index=genIsSentence Yes|
		/setvar key=genSettings index=needOutput Yes|
		/setvar key=genSettings index=outputIsList No|
		/setvar key=genSettings index=useContext Yes|
		/setvar key=extra []|
		/:"CMC Logic.Get Basic Type Context"|
		/ife (extra != '') {:
			/setvar key=genSettings index=contextKey {{getvar::extra}}|
		:}|
		/flushvar extra|
		/wait {{getvar::wait}}|
		
		/getvar key=genSettings index=inputIsList|
		/let key=inputIsList {{pipe}}|
		/getvar key=genSettings index=inputIsList|
		/let key=outputIsList {{pipe}}|
		
		
		/ife ((inputIsList == 'Yes') or (outputIsList == 'Yes')) {:
			/setvar as=array key={{var::variableName}} []|
		:}|
		/else {:
			/setvar as=string key={{var::variableName}} {{noop}}|
		:}|
		//[[Generate with Prompt]]|
		/ife (inputIsList == 'Yes') {:
			/foreach {{getvar::appearanceTraits}} {:
				/setvar key=appearanceTrait {{var::item}}|
				/getvar key=appearanceTraitsDetails index={{var::index}}|
				/setvar key=appearanceTraitDetails {{pipe}}|
				/:"CMC Logic.GenerateWithPrompt"|
				/addvar key={{var::variableName}} {{getvar::output}}|
				/flushvar output|
				/flushvar guidance|
			:}|
			/flushvar appearanceTrait|
			/flushvar appearanceTraitDetails|
		:}|
		/else {:
			/:"CMC Logic.GenerateWithPrompt"|
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
:}|
/else {:
	/setvar key=appearanceTraitsDetails None|
	/setvar key=appearanceTraitsEffect None|
	/addvar key=dataBaseNames appearanceTraitsDetails|
	/addvar key=dataBaseNames appearanceTraitsEffect|
:}|
/setvar key=parsedAppearanceTraits {{noop}}|
/ife (appearanceTraits != 'None') {:
	/setvar key=parsedAppearanceTraits |
	/foreach {{getvar::appearanceTraits}} {:
		/ife (index > 0) {:
			/addvar key=parsedAppearanceTraits "{{newline}}{{newline}}"|
		:}|
		/getvar key=appearanceTraitsDetails index={{var::index}}|
		/let key=details {{pipe}}|
		/getvar key=appearanceTraitsEffect index={{var::index}}|
		/let key=effect {{pipe}}|
		/addvar key=parsedAppearanceTraits "- Appearance Trait: {{var::item}}
  - Details: {{var::details}}
  - Effect: {{var::effect}}"
	:}|
:}|
/else {:
	/setvar key=parsedAppearanceTraits None|
:}|
/addvar key=dataBaseNames parsedAppearanceTraits|

/:"CMC Logic.JEDParse"|

/:"CMC Logic.Save DataBase"|

/setvar key=stepDone Yes|
/qr-list CMC Main|
/getat index=1 {{pipe}}|
/var qrlabel {{pipe}}|
/qr-get set="CMC Main" label={{var::qrlabel}}|
/getat index="message" {{pipe}}|
/qr-update set="CMC Main" label={{var::qrlabel}} newlabel="Start Generating Outfit" {{pipe}}|
/forcesave|