/* Setup before Selector QR
//--------|
/var key=do Yes|
/var key=variableName ""|
/ife ( {{var::variableName}} != '') {:
	/buttons labels=["Yes", "No"] Do you want to redo redo {{var::variableName}}|
	/var key=do {{pipe}}|
:}|
/ife ( do == 'Yes' ) {:
	/var key=wi_book ""|//The Lorebook Name|
	/var key=wi_book_key ""|//The name of the entry to get|
	/var key=combineLorebookEntries No|//Combines the lorebook entries|
	/var key=inputIsList No|//Yes or No|
	/var key=outputIsList No|//Yes or No|
	/var key=needOutput No|//Yes or No|
	
	
	/ife ( inputIsList == 'Yes') {:
		/setvar key={{var::variableName}} []|
		/ife ( combineLorebookEntries == 'Yes') {:
			/:"CMC Logic.Combine List Lorebooks"
		:}|
		/foreach {{getvar::genOrder}} {:
			/var key=it {{var::item}}|
			/getat index={{var::index}} {{var::genOrderContent}} |
			/var key=content {{pipe}}|
			/:GenerateWithSelector wi_book_f="{{var::wi_book}}" wi_book_key_f="{{var::wi_book_key}}" genIsList_f="{{var::genIsList}}" genIsSentence_f="{{var::genIsSentence}}" needOutput_f="{{var::needOutput}}" contextKey_f="{{var::contextKey}}"|
			/addvar key={{var::variableName}} {{pipe}}|
		:}|
	:}|
	/else {:
		/var key=it {{getvar::wi_book_key}}|
		/:GenerateWithSelector wi_book_f="{{var::wi_book}}" wi_book_key_f="{{var::wi_book_key}}" genIsList_f="{{var::genIsList}}" genIsSentence_f="{{var::genIsSentence}}" needOutput_f="{{var::needOutput}}" contextKey_f="{{var::contextKey}}"|
		/setvar key={{var::variableName}} {{pipe}}|
		
	:}|
	/addvar key=dataBaseNames {{var::variableName}}|
	/var key=context {{noop}}|
	/var key=examples {{noop}}|
	/var key=task {{pipe}}|
	/var key=instruct {{pipe}}|
	/var key=content {{pipe}}|
	/flushvar genOrder|
:}|
//-------|
*|