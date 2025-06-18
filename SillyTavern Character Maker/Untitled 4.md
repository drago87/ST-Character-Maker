/:"CMC Logic.Get Char info"|
//Features Type|
/let key=do {{noop}}|
/let key=variableName {{noop}}|
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
			/echo Output: {{getvar::output}}|
			/len {{var::tempOutputList}}|
			/var key=tempOutputList index={{pipe}} {{getvar::output}}|
			/echo tempOutputList: {{var::tempOutputList}}|
			/flushvar output|
			/flushvar guidance|
		:}|
		/setvar key=00 {{var::tempOutputList}}|
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