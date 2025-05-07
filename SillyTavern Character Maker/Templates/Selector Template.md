/* Setup before Selector QR
//--------|
/var key=do Yes|
/var key=variableName ""|
/ife ( {{var::variableName}} != '') {:
	/buttons labels=["Yes", "No"] Do you want to redo {{var::variableName}}|
	/var key=do {{pipe}}|
:}|
/ife ( do == 'Yes' ) {:
	/setvar key=genSettings index=wi_book ""|
	/setvar key=genSettings index=wi_book_key ""|
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
	/flushvar output|
	/flushvar genOrder|
	/flushvar genContent|
	/flushvar it|
	/flushvar genSettings|
:}|
//-------|
*|