/setvar key=stepDone No|
/setvar key=stepVar Step2|

--VarReplace--

/qr-list CMC Main|
/getat index=1 {{pipe}}|
/let qrlabel {{pipe}}|
/qr-get set="CMC Main" label={{var::qrlabel}}|
/getat index="message" {{pipe}}|
/qr-update set="CMC Main" label={{var::qrlabel}} newlabel="Continue Generating Basic World Information" {{pipe}}|
/:"CMC Logic.Get Char info"|

/setvar key=dataBaseNames []|

//Generation Functions|
--GenPrompt--

--GenSelector--
//----|

//Time Period|
/var key=do Yes|
/var key=variableName "timePeriod"|
/ife ( {{var::variableName}} != '') {:
	/buttons labels=["Yes", "No"] Do you want to redo redo {{var::variableName}}|
	/var key=do {{pipe}}|
:}|
/ife ( do == 'Yes' ) {:
	/var key=wi_book_key "Time Period"|
	/var key=genIsList Yes|//Yes or No|
	/var key=outputIsList Yes|//Yes or No|
	/var key=genIsSentence No|//Yes or No|
	/var key=needOutput Yes|//Yes or No|
	/var key=contextKey "Character"|
	
	
	/ife (outputIsList == 'Yes') {:
		/setvar as=array key={{var::variableName}} []|
	:}|
	/else {:
		/setvar as=string key={{var::variableName}} {{noop}}|
	:}|
	//[[Generate with Prompt]]|
	/:GenerateWithPrompt wi_book_key_f="{{var::wi_book_key}}" genIsList_f="{{var::genIsList}}" genIsSentence_f="{{var::genIsSentence}}" needOutput_f="{{var::needOutput}}" contextKey_f="{{var::contextKey}}"|
	
	/setvar key={{var::variableName}} {{getvar::output}}|
	/addvar key=dataBaseNames {{var::variableName}}|
	/var key=context {{noop}}|
	/var key=examples {{noop}}|
	/var key=task {{pipe}}|
	/var key=instruct {{pipe}}|
	/var key=content {{pipe}}|
:}|
//-----------|

//Seasons|
/var key=do Yes|
/var key=variableName "seasons"|
/ife ( {{var::variableName}} != '') {:
	/buttons labels=["Yes", "No"] Do you want to redo redo {{var::variableName}}|
	/var key=do {{pipe}}|
:}|
/ife ( do == 'Yes' ) {:
	/var key=wi_book "CMC Variables"|//The Lorebook Name|
	/var key=wi_book_key Seasons|//The name of the entry to get|
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
:}|
//-----------|

//--------|
/var key=do Yes|
/var key=variableName "settingType"|
/ife ( {{var::variableName}} != '') {:
	/buttons labels=["Yes", "No"] Do you want to redo redo {{getvar::varibleName}}|
	/var key=do {{pipe}}|
:}|
/ife ( do == 'Yes' ) {:
	/var key=wi_book "CMC Variables"|
	/var key=wi_book_key "Setting Type"|
	/var key=combineLorebookEntries No|
	/var key=inputIsList No|
	/var key=outputIsList No|
	/var key=needOutput Yes|
	
	
	/ife ( inputIsList == 'Yes') {:
		/setvar key={{var::variableName}} []|
		/ife ( combineLorebookEntries == 'Yes') {:
			/:"CMC Logic.Combine List Lorebooks"
		:}|
		/foreach {{var::genOrder}} {:
			/var key=it {{var::item}}|
			/getat index={{var::index}} {{var::genOrderContent}}|
			/var key=content {{pipe}}|
			/:GenerateWithSelector wi_book_f="{{var::wi_book}}" wi_book_key_f="{{var::wi_book_key}}" genIsList_f="{{var::genIsList}}" genIsSentence_f="{{var::genIsSentence}}" needOutput_f="{{var::needOutput}}" contextKey_f="{{var::contextKey}}"|
			/addvar key={{var::variableName}} {{getvar::output}}|
		:}|
	:}|
	/else {:
		/var key=it {{var::wi_book_key}}|
		/:GenerateWithSelector wi_book_f="{{var::wi_book}}" wi_book_key_f="{{var::wi_book_key}}" genIsList_f="{{var::genIsList}}" genIsSentence_f="{{var::genIsSentence}}" needOutput_f="{{var::needOutput}}" contextKey_f="{{var::contextKey}}"|
		/setvar key={{getvar::variableName}} {{getvar::output}}|
	:}|
	/addvar key=dataBaseNames {{var::variableName}}|
	/var key=context {{noop}}|
	/var key=examples {{noop}}|
	/var key=task {{pipe}}|
	/var key=instruct {{pipe}}|
	/var key=content {{pipe}}|
:}|
//-------|

//World Type|
/var key=do Yes|
/var key=variableName "worldType"|
/ife ( {{var::variableName}} != '') {:
	/buttons labels=["Yes", "No"] Do you want to redo redo {{var::variableName}}|
	/var key=do {{pipe}}|
:}|
/ife ( do == 'Yes' ) {:
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
	/:GenerateWithPrompt wi_book_key_f="{{var::wi_book_key}}" genIsList_f="{{var::genIsList}}" genIsSentence_f="{{var::genIsSentence}}" needOutput_f="{{var::needOutput}}" contextKey_f="{{var::contextKey}}"|
	
	/setvar key={{var::variableName}} {{getvar::output}}|
	/addvar key=dataBaseNames {{var::variableName}}|
	/var key=context {{noop}}|
	/var key=examples {{noop}}|
	/var key=task {{pipe}}|
	/var key=instruct {{pipe}}|
	/var key=content {{pipe}}|
:}|
//-----------|

//WorldDetails|
/var key=do Yes|
/var key=variableName "worldDetails"|
/ife ( {{var::variableName}} != '') {:
	/buttons labels=["Yes", "No"] Do you want to redo redo {{var::variableName}}|
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
	/:GenerateWithPrompt wi_book_key_f="{{var::wi_book_key}}" genIsList_f="{{var::genIsList}}" genIsSentence_f="{{var::genIsSentence}}" needOutput_f="{{var::needOutput}}" contextKey_f="{{var::contextKey}}"|
	
	/setvar key={{var::variableName}} {{getvar::output}}|
	/addvar key=dataBaseNames {{var::variableName}}|
	/var key=context {{noop}}|
	/var key=examples {{noop}}|
	/var key=task {{pipe}}|
	/var key=instruct {{pipe}}|
	/var key=content {{pipe}}|
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