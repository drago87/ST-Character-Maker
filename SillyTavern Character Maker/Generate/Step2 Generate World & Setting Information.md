/qr-list CMC Main|
/getat index=1 {{pipe}}|
/let qrlabel {{pipe}}|
/qr-get set="CMC Main" label={{var::qrlabel}}|
/getat index="message" {{pipe}}|
/qr-update set="CMC Main" label={{var::qrlabel}} newlabel="Start Generating World & Setting Information" {{pipe}}|
/:"CMC Logic.Get Char info"|

/setvar key=dataBaseNames []|
/flushvar genSettings|

/setvar key=stepVar Step2|

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

//Seasons|
/var key=do No|
/var key=variableName "seasons"|
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
	/setvar key=genSettings index=wi_book_key "Seasons"|
	/setvar key=genSettings index=combineLorebookEntries No|
	/setvar key=genSettings index=genIsSentence No|
	/setvar key=genSettings index=genIsList Yes|
	/setvar key=genSettings index=useContext No|
	/setvar key=genSettings index=inputIsList No|
	/setvar key=genSettings index=outputIsList No|
	/setvar key=genSettings index=needOutput No|
	
	
	/getvar key=genSettings index=inputIsList|
	/let key=inputIsList {{pipe}}|
	/getvar key=genSettings index=combineLorebookEntries|
	/let key=combineLorebookEntries {{pipe}}|
	
	
	/ife ( inputIsList == 'Yes') {:
		/setvar key={{var::variableName}} []|
		/ife ( combineLorebookEntries == 'Yes') {:
			/:"CMC Logic.Combine List Lorebooks"|
		:}|
		/foreach {{getvar::genOrder}} {:
			/setvar key=it {{var::item}}|
			/getat index={{var::index}} {{getvar::genContent}} |
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

//World Tone|
/var key=do No|
/var key=variableName "worldTone"|
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
	/setvar key=genSettings index=wi_book_key "World Tone"|
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
	/flushvar output|
	/flushvar genOrder|
	/flushvar genContent|
	/flushvar it|
	/flushvar genSettings|
:}|
//-----------|

/ife (worldTone == 'Light') {:
	/setvar key=toneDescriptor "{{getvar::worldTone}} — optimistic, stable, or nostalgic"|
:}|
/elseif (worldTone == 'Bright') {:
	/setvar key=toneDescriptor "{{getvar::worldTone}} — bold, adventurous, full of potential"|
:}|
/elseif (worldTone == 'Neutral') {:
	/setvar key=toneDescriptor "{{getvar::worldTone}} — descriptive and impartial"|
:}|
/elseif (worldTone == 'Dark') {:
	/setvar key=toneDescriptor "{{getvar::worldTone}} — conflicted, uncertain, and power-driven|
:}|
/elseif (worldTone == 'Bleak') {:
	/setvar key=toneDescriptor "{{getvar::worldTone}} — dystopian, broken, and hopeless"|
:}|

//World Type|
/var key=do No|
/var key=variableName "worldType"|
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
	/setvar key=genSettings index=wi_book_key "World Type"|
	/setvar key=genSettings index=genIsList Yes|
	/setvar key=genSettings index=inputIsTaskList No|
	/setvar key=genSettings index=outputIsList No|
	/setvar key=genSettings index=genIsSentence No|
	/setvar key=genSettings index=needOutput Yes|
	/setvar key=genSettings index=useContext No|
	/setvar key=genSettings index=contextKey {{noop}}|
	
	
	/getvar key=genSettings index=inputIsList|
	/let key=inputIsList {{pipe}}|
	/getvar key=genSettings index=combineLorebookEntries|
	/let key=combineLorebookEntries {{pipe}}|
	
	
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

//WorldDetails|
/var key=do No|
/var key=variableName "worldDetails"|
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
	/setvar key=genSettings index=wi_book_key "World Details"|
	/setvar key=genSettings index=genIsList No|
	/setvar key=genSettings index=inputIsTaskList No|
	/setvar key=genSettings index=outputIsList No|
	/setvar key=genSettings index=genIsSentence Yes|
	/setvar key=genSettings index=needOutput Yes|
	/setvar key=genSettings index=useContext No|
	/setvar key=genSettings index=contextKey {{noop}}|
	
	
	/getvar key=genSettings index=inputIsList|
	/let key=inputIsList {{pipe}}|
	/getvar key=genSettings index=combineLorebookEntries|
	/let key=combineLorebookEntries {{pipe}}|
	
	
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

//--User--'s Role|
/var key=do No|
/var key=variableName "userRole"|
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
	/setvar key=genSettings index=wi_book_key "User Role"|
	/setvar key=genSettings index=genIsList No|
	/setvar key=genSettings index=inputIsTaskList No|
	/setvar key=genSettings index=genIsSentence Yes|
	/setvar key=genSettings index=needOutput Yes|
	/setvar key=genSettings index=outputIsList No|
	/setvar key=genSettings index=useContext Yes|
	/setvar key=extra []|
	/addvar key=extra "- World Tone: {{getvar::toneDescriptor}}"|
	/addvar key=extra "- World Type: {{getvar::worldType}}"|
	/addvar key=extra "- World Details: {{getvar::worldDetails}}"|
	/ife (user == 'No') {:
		/addvar key=extra "--User-- is a Narrator"|
	:}|
	
	/setvar key=genSettings index=extraContext {{getvar::extra}}|
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
	
	/buttons labels=["Male", "Female", "Gender Neutral", "Anything"] What gender should the generation assume --User-- is?|
	/setvar key=userGender {{pipe}}|
	/ife ( userGender == ''){:
		/echo Aborting |
		/abort
	:}|
	/elseif (( userGender == 'Male') or ( userGender == 'Female')) {:
		/ife (userGender == 'Female') {:
			/setvar key=userSubjPronoun she|
			/setvar key=userObjPronoun her|
			/setvar key=userPossAdjPronoun her|
			/setvar key=userPossPronoun hers|
			/setvar key=userReflexivePronoun herself|
		:}|
		/elseif (userGender == 'Male') {:
			/setvar key=userSubjPronoun he|
			/setvar key=userObjPronoun him|
			/setvar key=userPossAdjPronoun his|
			/setvar key=userPossPronoun his|
			/setvar key=userReflexivePronoun himself|
		:}|
		/setvar key=userIdentityDescriptor "--User-- is a {{getvar::userGender}}"|
	:}|
	/elseif ( userGender == 'Gender Neutral') {:
		/setvar key=userSubjPronoun they|
		/setvar key=userObjPronoun them|
		/setvar key=userPossAdjPronoun their|
		/setvar key=userPossPronoun theirs|
		/setvar key=userReflexivePronoun themself|
		/setvar key=userIdentityDescriptor "--User-- is gender neutral and should be described using neutral language and tone, avoiding gendered assumptions."
	:}|
	/elseif ( userGender == 'Anything') {:
		/setvar key=userSubjPronoun they|
		/setvar key=userObjPronoun them|
		/setvar key=userPossAdjPronoun their|
		/setvar key=userPossPronoun theirs|
		/setvar key=userReflexivePronoun themself|
		/setvar key=userIdentityDescriptor "--User--’s gender is unspecified and should be described using flexible or inclusive language, avoiding gendered pronouns or assumptions."|
	:}|
	
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
	/flushvar guidance|
	/flushvar genOrder|
	/flushvar genContent|
	/flushvar genSettings|
:}|
/else {:
	/addvar key=dataBaseNames {{var::variableName}}|
:}|
//-----------|

//Residence|
/var key=do No|
/var key=variableName "residence"|
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
	/setvar key=genSettings index=wi_book_key "Residence"|
	/setvar key=genSettings index=genIsList No|
	/setvar key=genSettings index=inputIsTaskList No|
	/setvar key=genSettings index=genIsSentence Yes|
	/setvar key=genSettings index=needOutput Yes|
	/setvar key=genSettings index=outputIsList No|
	/setvar key=genSettings index=useContext Yes|
	/setvar key=extra []|
	/ife (seasons != 'None') {:
		/addvar key=extra "- Time Period: {{getvar::timePeriod}} — Season: {{getvar::seasons}}"|
	:}|
	/else {:
		/addvar key=extra "- Time Period: {{getvar::timePeriod}}"|
	:}|
	/addvar key=extra "- World Type: {{getvar::worldType}}"|
	/addvar key=extra "- World Details: {{getvar::worldDetails}}"|
	/ife (user == 'Yes') {:
		/addvar key=extra "- --User--'s Role: {{getvar::userRole}}"|
		/setvar key=logicBasedInstruction "- Only include --User-- in the description if their role implies shared or nearby living space — such as a family member they still live with, a roommate, or a close neighbor.{{newline}}- If --User-- is not part of the same household or residential area, do not reference them at all in this section."|
	:}|
	/setvar key=genSettings index=extraContext {{getvar::extra}}|
	/flushvar extra|
	/setvar key=genSettings index=contextKey []|
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
	/flushvar logicBasedInstruction|
	/flushvar guidance|
	/flushvar genOrder|
	/flushvar genContent|
	/flushvar genSettings|
:}|
/else {:
	/addvar key=dataBaseNames {{var::variableName}}|
:}|
//-----------|

//Occupation|
/var key=do No|
/var key=variableName "occupationBase"|
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
	/setvar key=genSettings index=wi_book_key "Occupation Base"|
	/setvar key=genSettings index=genIsList Yes|
	/setvar key=genSettings index=genAmount 10|
	/setvar key=genSettings index=inputIsTaskList No|
	/setvar key=genSettings index=genIsSentence Yes|
	/setvar key=genSettings index=needOutput Yes|
	/setvar key=genSettings index=outputIsList No|
	/setvar key=genSettings index=useContext Yes|
	/setvar key=extra []|
	/addvar key=extra "- Time Period: {{getvar::timePeriod}} —  World Type: {{getvar::worldType}}"|
	/addvar key=extra "- World Details: {{getvar::worldDetails}}"|
	/addvar key=extra "- Residence: {{getvar::residence}}"|
	/setvar key=genSettings index=extraContext {{getvar::extra}}|
	/setvar key=extra []|
	/:"CMC Logic.Get Basic Type Context"|//Remove if not in use|
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
	/flushvar output|
	/flushvar guidance|
	/flushvar genOrder|
	/flushvar genContent|
	/flushvar genSettings|
:}|

/ife ( occupationBase != 'None') {:
	/var key=do No|
	/var key=variableName "occupationDuties"|
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
		/setvar key=genSettings index=wi_book_key "Occupation Duties"|
		/setvar key=genSettings index=genIsList No|
		/setvar key=genSettings index=inputIsTaskList No|
		/setvar key=genSettings index=genIsSentence Yes|
		/setvar key=genSettings index=needOutput Yes|
		/setvar key=genSettings index=outputIsList No|
		/setvar key=genSettings index=useContext Yes|
		/setvar key=extra []|
		/addvar key=extra "- Time Period: {{getvar::timePeriod}} —  World Type: {{getvar::worldType}}"|
		/addvar key=extra "- World Details: {{getvar::worldDetails}}"|
		/addvar key=extra "- Residence: {{getvar::residence}}"|
		/setvar key=genSettings index=extraContext {{getvar::extra}}|
		/flushvar extra|
		/setvar key=genSettings index=contextKey []|
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
		/flushvar output|
		/flushvar guidance|
		/flushvar genOrder|
		/flushvar genContent|
		/flushvar genSettings|
	:}|
	
	/var key=do No|
	/var key=variableName "occupationSkills"|
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
		/setvar key=genSettings index=wi_book_key "Occupation Skills"|
		/setvar key=genSettings index=genIsList No|
		/setvar key=genSettings index=inputIsTaskList No|
		/setvar key=genSettings index=genIsSentence Yes|
		/setvar key=genSettings index=needOutput No|
		/setvar key=genSettings index=outputIsList No|
		/setvar key=genSettings index=useContext Yes|
		/setvar key=extra []|
		/addvar key=extra "- Occupation: {{getvar::occupationBase}}"|
		/addvar key=extra "- Duties: {{getvar::occupationDuties}}"|
		/addvar key=extra "- Time Period: {{getvar::timePeriod}} —  World Type: {{getvar::worldType}}"|
		/addvar key=extra "- World Details: {{getvar::worldDetails}}"|
		/setvar key=genSettings index=extraContext {{getvar::extra}}|
		/flushvar extra|
		/setvar key=genSettings index=contextKey []|
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
		/flushvar output|
		/flushvar guidance|
		/flushvar genOrder|
		/flushvar genContent|
		/flushvar genSettings|
	:}|
	//-----------|
	
	
	/findentry field=comment file="CMC Templates" "Occupation Template"|
	/let key=wi_uid {{pipe}}|
	/getentryfield field=content file="CMC Templates" {{var::wi_uid}}|
	/let key=template {{pipe}}|
	/ife (occupationSkills != 'None') {:
		/re-replace find="/--OccupationSkills--/g" replace="{{newline}}  - Skills: {{getvar::occupationSkills}}" {{var::template}}|
		/setvar key=parsedOccupation {{pipe}}|
	:}|
	/else {:
		/re-replace find="/--OccupationSkills--/g" replace="" {{var::template}}|
		/setvar key=parsedOccupation {{pipe}}|
	:}|
	
	 /addvar key=dataBaseNames parsedOccupation|
:}|
/else {:
	/ife (occupationDuties == '') {:
		/buttons labels=["Unemployed", "Idle", "None"] What type of unemployment do you want {{getvar::firstName}} to have? None will remove it from the generations.|
		/setvar key=parsedOccupation {{pipe}}|
	:}|
	/setvar key=occupationDuties None|
	/addvar key=dataBaseNames occupationDuties|
	/setvar key=occupationSkills None|
	/addvar key=dataBaseNames occupationSkills|
	
	/addvar key=dataBaseNames parsedOccupation|
:}|


//Lore|
/ife (loreSelect == '') {:
	/buttons labels=["Yes", "No"] Do you want to have Lore for the world?|
	/setvar key=loreSelect {{pipe}}|
	/ife (loreSelect == '') {:
		/echo Aborting |
		/abort
	:}|
:}|
/ife ( loreSelect == 'Yes') {:
	/var key=do No|
	/var key=variableName "lore"|
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
		/setvar key=genSettings index=wi_book_key "Lore"|
		/setvar key=genSettings index=genIsList No|
		/setvar key=genSettings index=genIsSentence Yes|
		/setvar key=genSettings index=inputIsTaskList No|
		/setvar key=genSettings index=needOutput Yes|
		/setvar key=genSettings index=useContext Yes|
		/setvar key=extra []|
		/ife (seasons != '') {:
			/addvar key=extra "- Time/Period: {{getvar::timePeriod}} — {{getvar::seasons}}"|
		:}|
		/else {:
			/addvar key=extra "- Time/Period: {{getvar::timePeriod}}"|
		:}|
		/addvar key=extra "- World Type: {{getvar::worldType}}"|
		/addvar key=extra "- World Details: {{getvar::worldDetails}}"|
		/setvar key=genSettings index=extraContext {{getvar::extra}}|
		/flushvar extra|
		/setvar key=genSettings index=contextKey {{noop}}|
		
		/getvar key=genSettings index=inputIsList|
		/let key=inputIsList {{pipe}}|
		/getvar key=genSettings index=combineLorebookEntries|
		/let key=combineLorebookEntries {{pipe}}|
		
		
		/ife (outputIsList == 'Yes') {:
			/setvar as=array key={{var::variableName}} []|
		:}|
		/else {:
			/setvar as=string key={{var::variableName}} {{noop}}|
		:}|
		
		/setvar key=genSettings index=guidencePrompt **GUIDANCE:**{{newline}}The following is a user-written concept or description for the world setting. Use it as an **inspirational seed** — it defines tone, structure, and cultural logic, but should **not** be copied or paraphrased.{{newline}}{{newline}}Your output must:{{newline}}- Treat this as background lore, encyclopedia-style — **objective, atmospheric, and character-free**.{{newline}}- Expand upon the mood, logic, and worldbuilding ideas without restating any full lines or bullet points.{{newline}}- Match the genre, tone, and level of detail implied by the user's input.{{newline}}{{newline}}|
		
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
	/setvar key=lore None|
	/addvar key=dataBaseNames lore|
	/flushvar selected_btn|
:}|
//-----------|


//Backstory|
/var key=do No|
/var key=variableName "backstory"|
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
	/setvar key=genSettings index=wi_book_key "Backstory"|
	/setvar key=genSettings index=genIsList No|
	/setvar key=genSettings index=inputIsTaskList No|
	/setvar key=genSettings index=genIsSentence Yes|
	/setvar key=genSettings index=needOutput Yes|
	/setvar key=genSettings index=outputIsList No|
	/setvar key=genSettings index=useContext Yes|
	/setvar key=extra []|
	/ife (seasons != 'None') {:
		/addvar key=extra "- Time Period: {{getvar::timePeriod}} — Season: {{getvar::seasons}}"|
	:}|
	/else {:
		/addvar key=extra "- Time Period: {{getvar::timePeriod}}"|
	:}|
	/addvar key=extra "- World Type: {{getvar::worldType}}"|
	/addvar key=extra "- World Details: {{getvar::worldDetails}}"|
	/ife (user == 'Yes') {:
		/addvar key=extra "- --User--'s Role: {{getvar::userRole}}"|
	:}|
	/setvar key=genSettings index=extraContext {{getvar::extra}}|
	/setvar key=extra []|
	/:"CMC Logic.Get Basic Type Context"|//Remove if not in use|
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
	
	/setvar key=genSettings index=guidencePrompt **GUIDANCE:**{{newline}}The following user-provided notes reflect key ideas about {{getvar::firstName}}’s upbringing, personality, or environment. Use these as **directional context** to inspire the backstory — not as facts to restate directly.{{newline}}{{newline}}Your output must:{{newline}}- Prioritize emotional and narrative insight into {{getvar::firstName}}.{{newline}}- Weave setting, culture, or social rules **through** the character’s experiences.{{newline}}- Never restate the guidance verbatim or list it point by point.{{newline}}- Assume the guidance reflects the **logic of the world** — write as if it’s already true.{{newline}}{{newline}}|
	
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

//Character Overview|
/var key=do No|
/var key=variableName "characterOverview"|
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
	/buttons labels=["User Input", "No Input"] Do you want to have to it generate a Character Overview by itself (You can still give it some guidance) or do you want to give it something to work from?|
	/let key=choice {{pipe}}|
	/ife (choice == '') {:
		/echo Aborting |
		/abort
	:}|
	/ife (choice == 'User Input') {:
		/input default="Example: She's a quiet but observant teen who often sketches in the margins of her notebooks. She's not confrontational, but notices everything — and tends to show up when people least expect it."
<div>What is this character like in daily life?</div><div>How would others describe them?</div>|
		/setvar key=characterOverviewIde {{pipe}}|
		/setvar key=genSettings index=wi_book_key "Character Overview User"|
	:}|
	/else {:
		/setvar key=genSettings index=wi_book_key "Character Overview Create"|
	:}|
	/setvar key=genSettings index=genIsList No|
	/setvar key=genSettings index=inputIsList No|
	/setvar key=genSettings index=genIsSentence Yes|
	/setvar key=genSettings index=needOutput Yes|
	/setvar key=genSettings index=outputIsList No|
	/setvar key=genSettings index=useContext No|
	/setvar key=extra []|
	/ife (parsedOccupation != 'None') {:
		/addvar key=extra "{{getvar::parsedOccupation}}"|
	:}|
	/addvar key=extra "- Residence: {{getvar::residence}}"|
	/addvar key=extra "- Backstory: {{getvar::backstory}}"|
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
	
	/ife (variable == 'conent') {:
		
		/ife ( logicBasedInstruction != '') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "- Rule"|
		
	:}|
	
	
	
	/ife ((inputIsList == 'Yes') or (outputIsList == 'Yes')) {:
		/setvar as=array key={{var::variableName}} []|
	:}|
	/else {:
		/setvar as=string key={{var::variableName}} {{noop}}|
	:}|
	
	/setvar key=genSettings index=guidencePrompt **GUIDANCE:**{{newline}}**Use** the following as a conceptual anchor or inspirational seed. It reflects the emotional tone, world logic, and personality direction that {{getvar::firstName}} is built around. You **must** honor the purpose and atmosphere suggested — but do **not** copy phrasing or summarize directly.{{newline}}{{newline}}|
	
	//[[Generate with Prompt]]|
	/ife (inputIsList == 'Yes') {:
		/let key=tempOutputList []|
		/foreach {{getvar::CHANGE_REMOVE_THIS}} {:
			/setvar key={{var::variableName}}Item {{var::item}}|
			/:"CMC Logic.GenerateWithPrompt"|
			/len {{var::tempOutputList}}|
			/var key=tempOutputList index={{pipe}} {{getvar::output}}|
			/flushvar output|
			/flushvar guidance|
		:}|
		/foreach {{tempOutputList}} {:
			/addvar key={{var::variableName}} {{var::item}}|
		:}|
		/flushvar {{var::variableName}}Item|
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

//Scenario Overview|
/var key=do Yes|
/var key=variableName "scenarioOverview"|
/ife ( {{var::variableName}} != '') {:
	/buttons labels=["Yes", "No"] Do you want to redo {{var::variableName}}|
	/var key=do {{pipe}}|
:}|
/ife ( do == 'Yes' ) {:
	
	/setvar key=genSettings {}|
	/buttons labels=["User Input", "No Input"] Do you want to have to it generate a Scenario Overview by itself (You can still give it some guidence) or do you want to give it something to work from?|
	/let key=choice {{pipe}}|
	/ife (choice == '') {:
		/echo Aborting |
		/abort
	:}|
	/ife (choice == 'User Input') {:
		/input default="Example: --User-- is a neighbor of {{getvar::firstName}} and is often hired by {{getvar::firstName}}'s parents to babysit {{getvar::firstName}}, which has led to [...]" <div>What is this scenario about?</div><div>What is the main idea?</div>|
		/setvar key=scenarioIde {{pipe}}|
		/setvar key=genSettings index=wi_book_key "Scenario User"|
	:}|
	/else {:
		/setvar key=genSettings index=wi_book_key "Scenario Create"|
	:}|
	/setvar key=genSettings index=genIsList No|
	/setvar key=genSettings index=genIsSentence Yes|
	/setvar key=genSettings index=needOutput Yes|
	/setvar key=genSettings index=useContext Yes|
	/setvar key=extra []|
	/ife (seasons != 'None') {:
		/addvar key=extra "- Time Period: {{getvar::timePeriod}} — Season: {{getvar::seasons}}"|
	:}|
	/else {:
		/addvar key=extra "- Time Period: {{getvar::timePeriod}}"|
	:}|
	/addvar key=extra "- World Type: {{getvar::worldType}}"|
	/addvar key=extra "- World Details: {{getvar::worldDetails}}"|
	/addvar key=extra "- Residence: {{getvar::residence}}"|
	/addvar key=extra "- Backstory: {{getvar::backstory}}"|
	/ife (user == 'Yes') {:
		/addvar key=extra "- --User--'s Role: {{getvar::userRole}}"|
		/getvar key=genSettings index=wi_book_key|
		/let key=inputIsList {{pipe}}|
		/ife (inputIsList =='Scenario User') {:
			/setvar key=logicBasedInstruction "- Any mention of user should be replaced with '--User--'.{{newline}}- Consider how the --User--'s Role ({{getvar::userRole}}) influences the character’s tone, visibility, or behavior — are they being watched, admired, judged, or misunderstood?"|
		:}|
		/elseif (inputIsList =='Scenario Create') {:
			/setvar key=logicBasedInstruction "- Introduce a conflict, discovery, or dynamic involving --User-- if applicable, but do not assign them a name or alias.{{newline}}- Always refer to them as --User--, not by a proper name or description. Maintain placeholder syntax exactly.{{newline}}- Consider how the --User--'s Role ({{getvar::userRole}}) influences the character’s tone, visibility, or behavior — are they being watched, admired, judged, or misunderstood?"|
		:}|

	:}|
	/setvar key=genSettings index=extraContext {{getvar::extra}}|
	/flushvar extra|
	/setvar key=genSettings index=contextKey {{noop}}|
	
	/getvar key=genSettings index=inputIsList|
	/let key=inputIsList {{pipe}}|
	/getvar key=genSettings index=combineLorebookEntries|
	/let key=combineLorebookEntries {{pipe}}|
	
	
	/ife (outputIsList == 'Yes') {:
		/setvar as=array key={{var::variableName}} []|
	:}|
	/else {:
		/setvar as=string key={{var::variableName}} {{noop}}|
	:}|
	
	/setvar key=genSettings index=guidencePrompt **GUIDANCE:**{{newline}}**Use** the following as a scene-setting compass for the scenario. It represents key tone, logic, and world context that must shape the moment. Whether expanding or generating a new scene, you **must** align with its intent — but do **not** reuse or copy phrases directly:{{newline}}{{newline}}|
	
	//[[Generate with Prompt]]|
	/:"CMC Logic.GenerateWithPrompt"|
	/ife (output != '') {:
		/setvar key={{var::variableName}} {{getvar::output}}|
	:}|
	/addvar key=dataBaseNames {{var::variableName}}|
	/flushvar output|
	/flushvar logicBasedInstruction|
	/flushvar guidance|
	/flushvar genOrder|
	/flushvar genContent|
	/flushvar genSettings|
:}|
//-----------|

/:"CMC Logic.JEDParse"|

/:"CMC Logic.Save DataBase"|

/setvar key=stepDone Yes|
/qr-list CMC Main|
/getat index=1 {{pipe}}|
/var qrlabel {{pipe}}|
/qr-get set="CMC Main" label={{var::qrlabel}}|
/getat index="message" {{pipe}}|
/qr-update set="CMC Main" label={{var::qrlabel}} newlabel="Start Generating Appearance & Anatomy" {{pipe}}|
/forcesave|