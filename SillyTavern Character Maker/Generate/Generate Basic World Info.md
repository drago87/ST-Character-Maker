/setvar key=stepDone No|
/setvar key=stepVar Step2|

/qr-list CMC Main|
/getat index=1 {{pipe}}|
/let qrlabel {{pipe}}|
/qr-get set="CMC Main" label={{var::qrlabel}}|
/getat index="message" {{pipe}}|
/qr-update set="CMC Main" label={{var::qrlabel}} newlabel="Continue Generating Basic World Information" {{pipe}}|
/:"CMC Logic.Get Char info"|

/setvar key=dataBaseNames []|


//Time Period|
/var key=do Yes|
/var key=variableName "timePeriod"|
/ife ( {{var::variableName}} != '') {:
	/buttons labels=["Yes", "No"] Do you want to redo {{var::variableName}}|
	/var key=do {{pipe}}|
:}|
/ife ( do == 'Yes' ) {:
	/setvar key=genSettings index=wi_book_key "Time Period"|
	/setvar key=genSettings index=genIsList Yes|
	/setvar key=genSettings index=outputIsList No|
	/setvar key=genSettings index=genIsSentence No|
	/setvar key=genSettings index=needOutput No|
	/setvar key=genSettings index=useContext No|
	/setvar key=genSettings index=contextKey {{noop}}|
	
	
	/getvar key=genSettings index=outputIsList|
	/let key=outputIsList {{pipe}}|
	
	
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
	/flushvar genSettings|
	/flushvar output|
:}|
//-----------|

//Seasons|
/var key=do Yes|
/var key=variableName "seasons"|
/ife ( {{var::variableName}} != '') {:
	/buttons labels=["Yes", "No"] Do you want to redo {{var::variableName}}|
	/var key=do {{pipe}}|
:}|
/ife ( do == 'Yes' ) {:
	/setvar key=genSettings index=wi_book "CMC Variables"|
	/setvar key=genSettings index=wi_book_key "Seasons"|
	/setvar key=genSettings index=combineLorebookEntries No|
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
			/addvar key={{var::variableName}} {{getvar::output}}|
		:}|
	:}|
	/else {:
		/setvar key=it {{getvar::wi_book_key}}|
		/:"CMC Logic.GenerateWithSelector"|
		/setvar key={{var::variableName}} {{pipe}}|
		
	:}|
	/addvar key=dataBaseNames {{var::variableName}}|
	/flushvar output|
	/flushvar genOrder|
	/flushvar genContent|
	/flushvar it|
	/flushvar genSettings|
:}|
//-----------|

//--------|
/var key=do Yes|
/var key=variableName "settingType"|
/ife ( {{var::variableName}} != '') {:
	/buttons labels=["Yes", "No"] Do you want to redo {{var::varibleName}}|
	/var key=do {{pipe}}|
:}|
/ife ( do == 'Yes' ) {:
	
	/setvar key=genSettings index=wi_book "CMC Variables"|
	/setvar key=genSettings index=wi_book_key "Setting Type"|
	/setvar key=genSettings index=combineLorebookEntries No|
	/setvar key=genSettings index=inputIsList No|
	/setvar key=genSettings index=outputIsList No|
	/setvar key=genSettings index=needOutput Yes|
	
	
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
		/setvar key={{getvar::variableName}} {{getvar::output}}|
	:}|
	/addvar key=dataBaseNames {{var::variableName}}|
	/flushvar output|
	/flushvar genOrder|
	/flushvar genContent|
:}|
//-------|

//World Type|
/var key=do Yes|
/var key=variableName "worldType"|
/ife ( {{var::variableName}} != '') {:
	/buttons labels=["Yes", "No"] Do you want to redo {{var::variableName}}|
	/var key=do {{pipe}}|
:}|
/ife ( do == 'Yes' ) {:
	
	/setvar key=genSettings index=wi_book_key "World Type"|
	/setvar key=genSettings index=genIsList Yes|
	/setvar key=genSettings index=outputIsList No|
	/setvar key=genSettings index=genIsSentence No|
	/setvar key=genSettings index=needOutput No|
	/setvar key=genSettings index=useContext No|
	/setvar key=genSettings index=contextKey {{noop}}|
	
	
	/getvar key=genSettings index=outputIsList|
	/let key=outputIsList {{pipe}}|
	
	/var key=wi_book_key "World Type"|
	/var key=genIsList Yes|
	/var key=outputIsList No|
	/var key=genIsSentence No|
	/var key=contextKey {{noop}}|
	
	
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
	/flushvar output|
	/flushvar genOrder|
	/flushvar genContent|
:}|
//-----------|

//WorldDetails|
/var key=do Yes|
/var key=variableName "worldDetails"|
/ife ( {{var::variableName}} != '') {:
	/buttons labels=["Yes", "No"] Do you want to redo {{var::variableName}}|
	/var key=do {{pipe}}|
:}|
/ife ( do == 'Yes' ) {:
	/var key=wi_book_key "World Details"|
	/var key=genIsList No|
	/var key=outputIsList No|
	/var key=genIsSentence No|
	/var key=contextKey {{noop}}|
	
	
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
//-----------|

//Lore|

//-----------|

//Scenario Overview|

//-----------|

--JEDParse--
/findentry field=comment file="CMC Variables" Character Template|
/getentryfield file="CMC Variables" {{pipe}}|
/:JEDParse input={{pipe}}|
/setvar key=t {{pipe}}|
/:"CMC Logic.Parse"|
/message-edit message=0 {{pipe}}|
/flushvar t|

/:"CMC Logic.Save DataBase"|

/setvar key=stepDone Yes|
/qr-list CMC Main|
/getat index=1 {{pipe}}|
/var qrlabel {{pipe}}|
/qr-get set="CMC Main" label={{var::qrlabel}}|
/getat index="message" {{pipe}}|
/qr-update set="CMC Main" label={{var::qrlabel}} newlabel="Start Generating Basic World Information" {{pipe}}|