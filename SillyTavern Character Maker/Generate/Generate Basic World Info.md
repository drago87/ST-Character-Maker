/setvar key=stepDone 'No'|
/setvar key=stepVar Step2|

--VarReplace--

/qr-list CMC Main|
/getat index=1 {{pipe}}|
/qr-update set="CMC Main" label={{pipe}} newlabel="Continue Generating Basic World Information"|
/:"CMC Logic.Get Char info"|

//Time Period|
/var key=do Yes|
/var key=variableName "timePeriod"|
/ife ( {{var::variableName}} != '') {:
	/buttons labels=["Yes", "No"] Do you want to redo redo {{var::variableName}}|
	/var key=do {{pipe}}|
:}|
/ife ( do == 'Yes ) {:
	/var key=genKey "Time Period"|
	/var key=genIsList Yes|//Yes or No|
	/var key=outputIsList Yes|//Yes or No|
	/var key=genIsSentence No|//Yes or No|
	/var key=needOutput Yes|//Yes or No|
	/var key=contextKey "Character"|
	
	
	/ife (outputIsList == 'Yes') {:
		/var as=array key={{var::variableName}} []|
	:}|
	/else {:
		/var as=string key={{var::variableName}} {{noop}}|
	:}|
	//[[Generate with Prompt]]|
	/:"CMC Logic.Generator"|
	
	/setvar key={{var::variableName}} {{var::output}}|
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
/ife ( do == 'Yes ) {:
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
			/:"CMC Logic.Selector"|
			/addvar key={{var::variableName}} {{var::output}}|
		:}|
	:}|
	/else {:
		/var key=it {{getvar::wi_book_key}}|
		/:"CMC Logic.Selector"|
		/setvar key={{var::variableName}} {{var::output}}|
		
	:}|
	/ife ( '{{var::variableName}}' in databaseList){:
		/getvar key={{var::variableName}}|
		/db-add source=chat name={{var::variableName}} {{pipe}}|
		/db-disable source=chat {{var::variableName}}|
	:}|
	/else {:
		/getvar key={{var::variableName}}|
		/db-update source=chat name={{var::variableName}} {{pipe}}|
		/db-disable source=chat {{var::variableName}}|
	:}|
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
/ife ( do == 'Yes ) {:
	/var key=wi_book "CMC Variables"|
	/var key=wi_book_key Setting Type|
	/var key=combineLorebookEntries No|
	/var key=inputIsList No|//Yes or No|
	/var key=outputIsList Yes|//Yes or No|
	/var key=needOutput Yes|//Yes or No|
	
	
	/ife ( inputIsList == 'Yes') {:
		/setvar key={{var::variableName}} []|
		/ife ( combineLorebookEntries == 'Yes') {:
			/:"CMC Logic.Combine List Lorebooks"
		:}|
		/foreach {{var::genOrder}} {:
			/var key=it {{var::item}}|
			/getat index={{var::index}} {{var::genOrderContent}}|
			/var key=content {{pipe}}|
			/:"CMC Logic.Selector"|
			/addvar key={{var::variableName}} {{var::output}}|
		:}|
	:}|
	/else {:
		/var key=it {{var::wi_book_key}}|
		/:"CMC Logic.Selector"|
		/setvar key={{getvar::variableName}} {{var::output}}|
	:}|
	/ife ( '{{var::variableName}}' in databaseList){:
		/getvar key={{var::variableName}}|
		/db-add source=chat name={{var::variableName}} {{pipe}}|
		/db-disable source=chat {{var::variableName}}|
	:}|
	/else {:
		/getvar key={{var::variableName}}|
		/db-update source=chat name={{var::variableName}} {{pipe}}|
		/db-disable source=chat {{var::variableName}}|
	:}|
	/var key=context {{noop}}|
	/var key=examples {{noop}}|
	/var key=task {{pipe}}|
	/var key=instruct {{pipe}}|
	/var key=content {{pipe}}|
:}|
//-------|

//World Type|
/var key=do Yes|
/var key=variableName "worldDetails"|
/ife ( {{var::variableName}} != '') {:
	/buttons labels=["Yes", "No"] Do you want to redo redo {{var::variableName}}|
	/var key=do {{pipe}}|
:}|
/ife ( do == 'Yes ) {:
	/var key=genKey "World Details"|
	/var key=genIsList Yes|
	/var key=outputIsList No|
	/var key=genIsSentence No|
	/var key=contextKey {{noop}}|
	
	
	/ife (outputIsList == 'Yes') {:
		/var as=array key={{var::variableName}}|
	:}|
	/else {:
		/var as=string key={{var::variableName}} {{noop}}|
	:}|
	//[[Generate with Prompt]]|
	/:"CMC Logic.Generator"|
	
	/setvar key={{var::variableName}} {{var::output}}|
	/ife ( '{{var::variableName}}' in databaseList){:
		/getvar key={{var::variableName}}|
		/db-add source=chat name={{var::variableName}} {{pipe}}|
		/db-disable source=chat {{var::variableName}}|
	:}|
	/else {:
		/getvar key={{var::variableName}}|
		/db-update source=chat name={{var::variableName}} {{pipe}}|
		/db-disable source=chat {{var::variableName}}|
	:}|
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
/ife ( do == 'Yes ) {:
	/var key=genKey "World Details"|//The name of the Lorebook entry to load|
	/var key=genIsList Yes|//Yes or No|
	/var key=outputIsList Yes|//Yes or No|
	/var key=genIsSentence No|//Yes or No|
	/var key=contextKey {{noop}}|//The name of context template to use|
	
	
	/ife (outputIsList == 'Yes') {:
		/var as=array key={{var::variableName}}|
	:}|
	/else {:
		/var as=string key={{var::variableName}} {{noop}}|
	:}|
	//[[Generate with Prompt]]|
	/:"CMC Logic.Generator"|
	
	/setvar key={{var::variableName}} {{var::output}}|
	/ife ( '{{var::variableName}}' in databaseList){:
		/getvar key={{var::variableName}}|
		/db-add source=chat name={{var::variableName}} {{pipe}}|
		/db-disable source=chat {{var::variableName}}|
	:}|
	/else {:
		/getvar key={{var::variableName}}|
		/db-update source=chat name={{var::variableName}} {{pipe}}|
		/db-disable source=chat {{var::variableName}}|
	:}|
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

/setvar key=stepDone 'Yes'|
/qr-list CMC Main|
/getat index=1 {{pipe}}|
/qr-update set="CMC Main" label={{pipe}} newlabel="Start Generating Basic World Information"|