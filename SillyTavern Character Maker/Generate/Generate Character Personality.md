/qr-list CMC Main|
/getat index=1 {{pipe}}|
/let qrlabel {{pipe}}|
/qr-get set="CMC Main" label={{var::qrlabel}}|
/getat index="message" {{pipe}}|
/qr-update set="CMC Main" label={{var::qrlabel}} newlabel="Continue Generating Character Personality" {{pipe}}|

/:"CMC Logic.Get Char info"|

/setvar key=dataBaseNames []|
/flushvar genSettings|

/setvar key=stepVar Step4|

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

//Archetype|
/var key=do No|
/var key=variableName "archetype"|
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
	/setvar key=genSettings index=wi_book_key "Archetype Base"|
	/setvar key=genSettings index=genIsList No|
	/setvar key=genSettings index=inputIsTaskList No|
	/setvar key=genSettings index=genIsSentence Yes|
	/setvar key=genSettings index=needOutput Yes|
	/setvar key=genSettings index=useContext Yes|
	/setvar key=genSettings index=contextKey []|
	/wait {{getvar::wait}}|
	
	/setvar key=settingModifier {Modifier}|
	/setvar key=settingArchetype {Archetype}|
	/setvar key=settingAddition {Addition}|
	
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
	/flushvar genOrder|
	/flushvar genContent|
	/flushvar genSettings|
:}|
/else {:
	/addvar key=dataBaseNames {{var::variableName}}|
:}|
//--------|


//Archetype Details|
/var key=do No|
/var key=variableName "archetypeDetails"|
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
	/setvar key=genSettings index=wi_book_key "Archetype Details"|
	/setvar key=genSettings index=genIsList No|
	/setvar key=genSettings index=inputIsTaskList No|
	/setvar key=genSettings index=genIsSentence Yes|
	/setvar key=genSettings index=needOutput Yes|
	/setvar key=genSettings index=useContext Yes|
	/setvar key=extra []|
	/addvar key=extra "- Archetype: {{getvar::archetype}}"|
	/setvar key=genSettings index=extraContext {{getvar::extra}}|
	/flushvar extra|
	/setvar key=genSettings index=contextKey []|
	/wait {{getvar::wait}}|
	
	/setvar key=settingModifier {Modifier}|
	/setvar key=settingArchetype {Archetype}|
	/setvar key=settingAddition {Addition}|
	
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
	/flushvar genOrder|
	/flushvar genContent|
	/flushvar genSettings|
	/flushvar settingModifier|
	/flushvar settingArchetype|
	/flushvar settingAddition|
:}|
/else {:
	/addvar key=dataBaseNames {{var::variableName}}|
:}|
//--------|


//Reasoning|
/var key=do No|
/var key=variableName "archetypeReasoning"|
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
	/setvar key=genSettings index=wi_book_key "Archetype Reasoning"|
	/setvar key=genSettings index=genIsList No|
	/setvar key=genSettings index=inputIsTaskList No|
	/setvar key=genSettings index=genIsSentence Yes|
	/setvar key=genSettings index=needOutput Yes|
	/setvar key=genSettings index=useContext Yes|
	/setvar key=extra []|
	/addvar key=extra "- Archetype: {{getvar::archetype}}"|
	/addvar key=extra "  ↳ Archetype Details: {{getvar::archetypeDetails}}"|
	/setvar key=genSettings index=extraContext {{getvar::extra}}|
	/flushvar extra|
	/setvar key=genSettings index=contextKey []|
	/wait {{getvar::wait}}|
	
	/setvar key=settingModifier {Modifier}|
	/setvar key=settingArchetype {Archetype}|
	/setvar key=settingAddition {Addition}|
	
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
	/flushvar genOrder|
	/flushvar genContent|
	/flushvar genSettings|
	/flushvar settingModifier|
	/flushvar settingArchetype|
	/flushvar settingAddition|
:}|
/else {:
	/addvar key=dataBaseNames {{var::variableName}}|
:}|
//--------|

/findentry field=comment file="CMC Templates" "Archetype Template"|
/getentryfield field=content file="CMC Templates" {{pipe}}|
/setvar key=parsedArchetype {{pipe}}|

/ife (( alignmentChoice == '') or ( alignmentChoice == 'Yes')) {:
	/buttons labels=["Yes", "No"] Do you want to select and generate an Alignment and its details?|
	/setvar key=alignmentChoice {{pipe}}|
	/ife ( alignmentChoice == ''){:
		/echo Aborting |
		/abort
	:}|
	/elseif ( selected_btn == 'Yes') {:
		//Alignment|
		/var key=do No|
		/var key=variableName "alignment"|
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
			/setvar key=genSettings index=wi_book_key "Alignment"|
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
			/flushvar genOrder|
			/flushvar genContent|
			/flushvar it|
			/flushvar genSettings|
		:}|
		/else {:
			/addvar key=dataBaseNames {{var::variableName}}|
		:}|
		//--------|
		
		
		//Alignment Details|
		/var key=do No|
		/var key=variableName "alignmentDetails"|
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
			/setvar key=genSettings index=wi_book_key "Alignment Details"|
			/setvar key=genSettings index=genIsList No|
			/setvar key=genSettings index=inputIsTaskList No|
			/setvar key=genSettings index=genIsSentence Yes|
			/setvar key=genSettings index=needOutput Yes|
			/setvar key=genSettings index=useContext Yes|
			/setvar key=extra []|
			/addvar key=extra "{{getvar::parsedArchetype}}"|
			/addvar key=extra "- Alignment: {{getvar::alignment}}"|
			/setvar key=genSettings index=extraContext {{getvar::extra}}|
			/flushvar extra|
			/setvar key=genSettings index=contextKey []|
			/wait {{getvar::wait}}|
			
			/setvar key=settingModifier {Modifier}|
			/setvar key=settingArchetype {Archetype}|
			/setvar key=settingAddition {Addition}|
			
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
			/flushvar genOrder|
			/flushvar genContent|
			/flushvar genSettings|
			/flushvar settingModifier|
			/flushvar settingArchetype|
			/flushvar settingAddition|
		:}|
		/else {:
			/addvar key=dataBaseNames {{var::variableName}}|
		:}|
		//--------|
		
		
		//Alignment Ideals|
		/var key=do No|
		/var key=variableName "alignmentIdeals"|
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
			/setvar key=genSettings index=wi_book_key "Alignment Ideals"|
			/setvar key=genSettings index=genIsList No|
			/setvar key=genSettings index=inputIsTaskList No|
			/setvar key=genSettings index=genIsSentence Yes|
			/setvar key=genSettings index=needOutput Yes|
			/setvar key=genSettings index=useContext Yes|
			/setvar key=extra []|
			/addvar key=extra "{{getvar::parsedArchetype}}"|
			/addvar key=extra "- Alignment: {{getvar::alignment}}"|
			/addvar key=extra "  ↳ Ideals: {{getvar::alignmentDetails}}"|
			/setvar key=genSettings index=extraContext {{getvar::extra}}|
			/flushvar extra|
			/setvar key=genSettings index=contextKey []|
			/wait {{getvar::wait}}|
			
			/setvar key=settingModifier {Modifier}|
			/setvar key=settingArchetype {Archetype}|
			/setvar key=settingAddition {Addition}|
			
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
			/flushvar genOrder|
			/flushvar genContent|
			/flushvar genSettings|
			/flushvar settingModifier|
			/flushvar settingArchetype|
			/flushvar settingAddition|
		:}|
		/else {:
			/addvar key=dataBaseNames {{var::variableName}}|
		:}|
		//--------|
	:}|
	/else {:
		/setvar key=alignment Nope|
		/setvar key=alignmentDetails Nope|
		/setvar key=alignmentIdeals Nope|
	:}|
:}|

/ife (( alignment != 'Nope') and ( alignment != '')) {:
	/findentry field=comment file="CMC Templates" "Alignment Template"|
	/getentryfield field=content file="CMC Templates" {{pipe}}|
	/setvar key=parsedAlignment {{pipe}}|
:}|
/else {:
	/setvar key=parsedAlignment None|
:}|

//Personality Tags|
/var key=do No|
/var key=variableName "foundTags"|
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
	/setvar key=genSettings index=wi_book_key "Identify Personality Tag"|
	/setvar key=genSettings index=genIsList No|
	/setvar key=genSettings index=inputIsTaskList No|
	/setvar key=genSettings index=genIsSentence Yes|
	/setvar key=genSettings index=needOutput Yes|
	/setvar key=genSettings index=useContext No|
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
	/flushvar output|
	/flushvar genOrder|
	/flushvar genContent|
	/flushvar genSettings|
:}|

/var key=do No|
/var key=variableName "personalityTags"|
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
	/setvar key=genSettings index=wi_book_key "Personality Tags"|
	/setvar key=genSettings index=genIsList Yes|
	/setvar key=genSettings index=inputIsTaskList No|
	/setvar key=genSettings index=genIsSentence Yes|
	/setvar key=genSettings index=needOutput Yes|
	/setvar key=genSettings index=useContext Yes|
	/setvar key=extra []|
	/addvar key=extra "{{getvar::parsedArchetype}}"|
	/ife (parsedAlignment != 'None') {:
		/addvar key=extra "{{getvar::parsedAlignment}}"|
	:}|
	/setvar key=genSettings index=extraContext {{getvar::extra}}|
	/flushvar extra|
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
	/flushvar genOrder|
	/flushvar genContent|
	/flushvar genSettings|
:}|
/else {:
	/addvar key=dataBaseNames {{var::variableName}}|
:}|
//--------|


//Cognitive Abilities|
/var key=do No|
/var key=variableName "intelligenceLevel"|
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
	/setvar key=genSettings index=wi_book_key "Intelligence Level"|
	/setvar key=genSettings index=combineLorebookEntries No|
	/setvar key=genSettings index=genIsSentence No|
	/setvar key=genSettings index=inputIsList No|
	/setvar key=genSettings index=genIsList Yes|
	/setvar key=genSettings index=outputIsList No|
	/setvar key=genSettings index=needOutput Yes|
	/setvar key=genSettings index=useContext Yes|
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
	/flushvar genOrder|
	/flushvar genContent|
	/flushvar it|
	/flushvar genSettings|
:}|
/else {:
	/addvar key=dataBaseNames {{var::variableName}}|
:}|


/var key=do No|
/var key=variableName "cognitiveAbilities"|
/ife (( 'Average' not in intelligenceLevel) or (normal_form == 'Animalistic') ) {:
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
		/setvar key=genSettings index=wi_book_key "Cognitive Abilities"|
		/setvar key=genSettings index=genIsList No|
		/setvar key=genSettings index=inputIsTaskList No|
		/setvar key=genSettings index=genIsSentence Yes|
		/setvar key=genSettings index=needOutput Yes|
		/setvar key=genSettings index=useContext Yes|
		/setvar key=extra []|
		/addvar key=extra "{{newline}}{{getvar::parsedArchetype}}"|
		/ife (parsedAlignment != 'None') {:
			/addvar key=extra "{{newline}}{{getvar::parsedAlignment}}{{newline}}"|
		:}|
		/addvar key=extra "- Intelligence Level: {{getvar::intelligenceLevel}}"|
		/setvar key=genSettings index=extraContext {{getvar::extra}}|
		/flushvar extra|
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
		/flushvar genOrder|
		/flushvar genContent|
		/flushvar genSettings|
	:}|
	/else {:
		/addvar key=dataBaseNames {{var::variableName}}|
	:}|
:}|
/else {:
	/setvar key={{var::variableName}} None|
	/addvar key=dataBaseNames {{var::variableName}}|
:}|
//--------|


//Social Skills and Integration Into Society|
/var key=do No|
/var key=variableName "socialBehavior"|
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
	/setvar key=genSettings index=wi_book_key "Social Behavior"|
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
	/flushvar genOrder|
	/flushvar genContent|
	/flushvar it|
	/flushvar genSettings|
:}|
/else {:
	/addvar key=dataBaseNames {{var::variableName}}|
:}|

/var key=do No|
/var key=variableName "socialSkills"|
/ife (( 'Average' not in intelligenceLevel) or (normal_form == 'Animalistic') ) {:
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
		/setvar key=genSettings index=wi_book_key "Social Profile"|
		/setvar key=genSettings index=genIsList No|
		/setvar key=genSettings index=inputIsTaskList No|
		/setvar key=genSettings index=genIsSentence Yes|
		/setvar key=genSettings index=needOutput Yes|
		/setvar key=genSettings index=useContext Yes|
		/setvar key=extra []|
		/addvar key=extra "{{newline}}{{getvar::parsedArchetype}}"|
		/ife (parsedAlignment != 'None') {:
			/addvar key=extra "{{newline}}{{getvar::parsedAlignment}}{{newline}}"|
		:}|
		/addvar key=extra "- Intelligence Level: {{getvar::intelligenceLevel}}"|
		/ife (cognitiveAbilities != 'None') {:
			/addvar key=extra "- Cognitive Abilities: {{getvar::cognitiveAbilities}}{{newline}}"|
		:}|
		/addvar key=extra "- Social Behavior: {{getvar::socialBehavior}}"|
		/setvar key=genSettings index=extraContext {{getvar::extra}}|
		/flushvar extra|
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
		/flushvar genOrder|
		/flushvar genContent|
		/flushvar genSettings|
	:}|
	/else {:
		/addvar key=dataBaseNames {{var::variableName}}|
	:}|
:}|
/else {:
	/setvar key={{var::variableName}} None|
	/addvar key=dataBaseNames {{var::variableName}}|
:}|
//--------|


//Main Aspiration|
/var key=do No|
/var key=variableName "aspirationMain"|
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
	/setvar key=genSettings index=wi_book_key "Aspiration Main"|
	/setvar key=genSettings index=genIsList No|
	/setvar key=genSettings index=inputIsTaskList No|
	/setvar key=genSettings index=genIsSentence Yes|
	/setvar key=genSettings index=needOutput Yes|
	/setvar key=genSettings index=outputIsList No|
	/setvar key=genSettings index=useContext No|
	/setvar key=extra []|
	/addvar key=extra "{{newline}}{{getvar::parsedArchetype}}"|
	/ife (parsedAlignment != 'None') {:
		/addvar key=extra "{{newline}}{{getvar::parsedAlignment}}{{newline}}"|
	:}|
	/addvar key=extra "- Intelligence Level: {{getvar::intelligenceLevel}}"|
	/ife (cognitiveAbilities != 'None') {:
		/addvar key=extra "- Cognitive Abilities: {{getvar::cognitiveAbilities}}{{newline}}"|
	:}|
	/addvar key=extra "- Social Behavior: {{getvar::socialBehavior}}"|
	/ife (socialSkills != 'None') {:
		/addvar key=extra "- Social Skills and Integration Into Society: {{getvar::socialSkills}}{{newline}}"|
	:}|
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
	/ife (inputIsList == 'Yes') {:
		
	:}|
	/else {:
		/:"CMC Logic.GenerateWithPrompt"|
		/addvar key={{var::variableName}} {{getvar::output}}|
	:}|
	/flushvar output|
	/flushvar genOrder|
	/flushvar genContent|
	/flushvar genSettings|
:}|
//--------|


//Aspiration Details|
/var key=do No|
/var key=variableName "aspirationDetails"|
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
	/setvar key=genSettings index=wi_book_key "Aspiration Details"|
	/setvar key=genSettings index=genIsList No|
	/setvar key=genSettings index=inputIsTaskList No|
	/setvar key=genSettings index=genIsSentence No|
	/setvar key=genSettings index=needOutput Yes|
	/setvar key=genSettings index=outputIsList No|
	/setvar key=genSettings index=useContext No|
	/setvar key=extra []|
	/addvar key=extra "{{newline}}{{getvar::parsedArchetype}}"|
	/ife (parsedAlignment != 'None') {:
		/addvar key=extra "{{newline}}{{getvar::parsedAlignment}}{{newline}}"|
	:}|
	/addvar key=extra "- Intelligence Level: {{getvar::intelligenceLevel}}"|
	/ife (cognitiveAbilities != 'None') {:
		/addvar key=extra "- Cognitive Abilities: {{getvar::cognitiveAbilities}}{{newline}}"|
	:}|
	/addvar key=extra "- Social Behavior: {{getvar::socialBehavior}}"|
	/ife (socialSkills != 'None') {:
		/addvar key=extra "- Social Skills and Integration Into Society: {{getvar::socialSkills}}{{newline}}"|
	:}|
	/addvar key=extra "- Main Aspiration: {{getvar::aspirationMain}}"|
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
	/ife (inputIsList == 'Yes') {:
		
	:}|
	/else {:
		/:"CMC Logic.GenerateWithPrompt"|
		/addvar key={{var::variableName}} {{getvar::output}}|
	:}|
	/flushvar output|
	/flushvar genOrder|
	/flushvar genContent|
	/flushvar genSettings|
:}|
//--------|


//Aspiration Goals|
/var key=do No|
/var key=variableName "aspirationGoals"|
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
	/setvar key=genSettings index=wi_book_key "Aspiration Goals"|
	/setvar key=genSettings index=genIsList No|
	/setvar key=genSettings index=inputIsTaskList No|
	/setvar key=genSettings index=genIsSentence No|
	/setvar key=genSettings index=needOutput Yes|
	/setvar key=genSettings index=outputIsList No|
	/setvar key=genSettings index=useContext No|
	/setvar key=extra []|
	/addvar key=extra "{{newline}}{{getvar::parsedArchetype}}"|
	/ife (parsedAlignment != 'None') {:
		/addvar key=extra "{{newline}}{{getvar::parsedAlignment}}{{newline}}"|
	:}|
	/addvar key=extra "- Intelligence Level: {{getvar::intelligenceLevel}}"|
	/ife (cognitiveAbilities != 'None') {:
		/addvar key=extra "- Cognitive Abilities: {{getvar::cognitiveAbilities}}{{newline}}"|
	:}|
	/addvar key=extra "- Social Behavior: {{getvar::socialBehavior}}"|
	/ife (socialSkills != 'None') {:
		/addvar key=extra "- Social Skills and Integration Into Society: {{getvar::socialSkills}}{{newline}}"|
	:}|
	/addvar key=extra "- Main Aspiration: {{getvar::aspirationMain}}"|
	/addvar key=extra "  ↳ Aspiration Details: {{getvar::aspirationDetails}}"|
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
	/ife (inputIsList == 'Yes') {:
		
	:}|
	/else {:
		/:"CMC Logic.GenerateWithPrompt"|
		/setvar key={{var::variableName}} {{getvar::output}}|
	:}|
	/flushvar output|
	/flushvar genOrder|
	/flushvar genContent|
	/flushvar genSettings|
:}|
//--------|


/findentry field=comment file="CMC Templates" "Aspiration Template"|
/getentryfield field=content file="CMC Templates" {{pipe}}|
/setvar key=parsedAspiration {{pipe}}|



//Unique Traits|
/var key=do No|
/var key=variableName "uniqueTraits"|
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
	/setvar key=genSettings index=wi_book_key "Unique Traits"|
	/setvar key=genSettings index=genIsList Yes|
	/setvar key=genSettings index=inputIsTaskList No|
	/setvar key=genSettings index=genIsSentence No|
	/setvar key=genSettings index=needOutput No|
	/setvar key=genSettings index=outputIsList Yes|
	/setvar key=genSettings index=useContext Yes|
	/setvar key=extra []|
	/addvar key=extra "- Intelligence Level: {{getvar::intelligenceLevel}}"|
	/addvar key=extra "- Social Behavior: {{getvar::socialBehavior}}"|
	/ife (socialSkills != 'None') {:
		/addvar key=extra "- Social Skills and Integration Into Society: {{getvar::socialSkills}}{{newline}}"|
	:}|
	/setvar key=genSettings index=extraContext {{getvar::extra}}|
	/flushvar extra|
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
	/flushvar output|
	/flushvar genOrder|
	/flushvar genContent|
	/flushvar genSettings|
:}|

/var key=do No|
/var key=variableName "uniqueTraitsEffects"|
/ife (uniqueTraits != 'None') {:
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
		/setvar key=genSettings index=wi_book_key "Unique Traits Effects"|
		/setvar key=genSettings index=genIsList No|
		/setvar key=genSettings index=inputIsTaskList No|
		/setvar key=genSettings index=inputIsList Yes|
		/setvar key=genSettings index=genIsSentence Yes|
		/setvar key=genSettings index=needOutput Yes|
		/setvar key=genSettings index=useContext Yes|
		/setvar key=extra []|
		/addvar key=extra "{{newline}}{{getvar::parsedArchetype}}"|
		/ife (parsedAlignment != 'None') {:
			/addvar key=extra "{{newline}}{{getvar::parsedAlignment}}{{newline}}"|
		:}|
		/addvar key=extra "- Intelligence Level: {{getvar::intelligenceLevel}}"|
		/ife (cognitiveAbilities != 'None') {:
			/addvar key=extra "- Cognitive Abilities: {{getvar::cognitiveAbilities}}{{newline}}"|
		:}|
		/addvar key=extra "- Social Behavior: {{getvar::socialBehavior}}"|
		/ife (socialSkills != 'None') {:
			/addvar key=extra "- Social Skills and Integration Into Society: {{getvar::socialSkills}}{{newline}}"|
		:}|
		/addvar key=extra "{{newline}}{{getvar::parsedAspiration}}"|
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
		/ife (inputIsList == 'Yes') {:
			/let key=tempTraits []|
			/foreach {{getvar::uniqueTraits}} {:
				/setvar key={{var::variableName}}Item {{var::item}}|
				/:"CMC Logic.GenerateWithPrompt"|
				/len tempTraits|
				/setat index={{pipe}} key=tempTraits {{getvar::output}}|
				/var key=tempTraits {{pipe}}|
				/flushvar output|
			:}|
			/setvar key={{var::variableName}} {{var::tempTraits}}|
			/flushvar {{var::variableName}}Item|
		:}|
		/else {:
			/:"CMC Logic.GenerateWithPrompt"|
			/setvar key={{var::variableName}} {{getvar::output}}|
		:}|
		/flushvar output|
		/flushvar genOrder|
		/flushvar genContent|
		/flushvar genSettings|
	:}|
:}|
/else {:
	/setvar key={{var::variableName}} None|
:}|
//--------|

/ife (uniqueTraits != 'None') {:
	/setvar key=parsedTraits []|
	/foreach {{getvar::uniqueTraits}} {:
		/let key=trait {{var::item}}|
		/getvar key=uniqueTraitsEffects index={{var::index}}|
		/let key=effect {{pipe}}|
		/findentry field=comment file="CMC Templates" "Unique Trait Template"|
		/getentryfield field=content file="CMC Templates" {{pipe}}|
		/re-replace find="/--UniqueTrait--/g" replace="{{var::item}}" {{pipe}}|
		/re-replace find="/--Effect--/g" replace="{{var::effect}}" {{pipe}}|
		/addvar key=parsedTraits {{pipe}}|
	:}|
	/join glue="{{newline}}{{newline}}" {{getvar::parsedTraits}}|
	/setvar key=parsedTraits {{pipe}}|
:}|
/else {:
	/setvar key=parsedTraits None|
:}|

/*
//Personality Q&A|
/var key=do No|
/var key=variableName "personalityQA"|
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
	/setvar key=genSettings index=wi_book_key "Personality QA"|
	/setvar key=genSettings index=genIsList No|
	/setvar key=genSettings index=inputIsTaskList No|
	/setvar key=genSettings index=inputIsList Yes|
	/setvar key=genSettings index=genIsSentence Yes|
	/setvar key=genSettings index=needOutput Yes|
	/setvar key=genSettings index=outputIsList No|
	/setvar key=genSettings index=useContext No|
	/setvar key=extra []|
	/addvar key=extra "{{newline}}{{getvar::parsedArchetype}}"|
	/ife (parsedAlignment != 'None') {:
		/addvar key=extra "{{newline}}{{getvar::parsedAlignment}}{{newline}}"|
	:}|
	/addvar key=extra "- Intelligence Level: {{getvar::intelligenceLevel}}"|
	/ife (cognitiveAbilities != 'None') {:
		/addvar key=extra "- Cognitive Abilities: {{getvar::cognitiveAbilities}}{{newline}}"|
	:}|
	/addvar key=extra "- Social Behavior: {{getvar::socialBehavior}}"|
	/ife (socialSkills != 'None') {:
		/addvar key=extra "- Social Skills and Integration Into Society: {{getvar::socialSkills}}{{newline}}"|
	:}|
	/addvar key=extra "{{newline}}{{getvar::parsedAspiration}}"|
	/setvar key=genSettings index=extraContext {{getvar::extra}}|
	/flushvar extra|
	/setvar key=genSettings index=contextKey []|
	/wait {{getvar::wait}}|
	
	
	/ife (qestions == '') {: 
		/findentry field=comment file="CMC Questions" "Personality: Q"|
		/let key=wi_uid {{pipe}}|
		/getentryfield field=content file="CMC Information" {{var::wi_uid}}|
		/let key=unfilteredQuestions {{pipe}}|
		/split find="\n" {{var::unfilteredQuestions}}|
		/var key=unfilteredQuestions {{pipe}}|
	
	
		/setvar key=qestions []|
		/foreach {{var::unfilteredQuestions}} {:
			/ife (( user != 'Yes') and ('--User--' not in item)) or ( user == 'Yes') {:
				/buttons labels=["Yes", "No"] <div>Do you want to have this question?</div><div>{{var::item}}</div>|
				/let key=exp {{pipe}}|
				/ife ( exp == ''){:
					/echo Aborting |
					/abort
				:}|
				/elseif ( exp == 'Yes') {:
					/addvar key=qestions {{var::item}}|
				:}|
			:}| 
		:}|
	:}|
	/let key=stop Yes|
	/whilee (stop != 'Yes') {:
		/buttons labels=["Yes", "No"] Do you want to add another question?|
		/var key=stop {{pipe}}|
		/ife ( stop == '') {:
			/echo Aborting |
			/abort
		:}|
		/ife ( stop == 'Yes') {:
			/input What is the question you want {{getvar::firstName}} to answer?|
			/let key=q {{pipe}}|
			/ife ( q == '') {:
				/echo Aborting |
				/abort
			:}|
			/addvar key=qestions {{var::q}}|
		:}|
	:}|
	
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
	/ife (inputIsList == 'Yes') {:
		/foreach {{getvar::qestions}} {:
			/setvar key=question {{var::item}}|
			/:"CMC Logic.GenerateWithPrompt"|
			/addvar key={{var::variableName}} Q: {{getvar::question}}{{newline}}A: {{getvar::output}}|
			/flushvar output|
		:}|
		/flushvar {{var::variableName}}Item|
	:}|
	/else {:
		/:"CMC Logic.GenerateWithPrompt"|
		/setvar key={{var::variableName}} {{getvar::output}}|
	:}|
	/addvar key=dataBaseNames {{var::variableName}}|
	/flushvar output|
	/flushvar genOrder|
	/flushvar genContent|
	/flushvar genSettings|
:}|
/else {:
	/addvar key=dataBaseNames {{var::variableName}}|
:}|
//--------|

/join glue="{{newline}}{{newline}}" {{getvar::personalityQA}}|
/setvar key=personalityQA {{pipe}}|


/:"CMC Logic.JEDParse"|

/:"CMC Logic.Save DataBase"|

/setvar key=stepDone Yes|
/qr-list CMC Main|
/getat index=1 {{pipe}}|
/var qrlabel {{pipe}}|
/qr-get set="CMC Main" label={{var::qrlabel}}|
/getat index="message" {{pipe}}|
/qr-update set="CMC Main" label={{var::qrlabel}} newlabel="Start Generating Personality" {{pipe}}|
*|