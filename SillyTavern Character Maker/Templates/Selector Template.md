/* Setup before Selector QR
//--------|
/var key=do Yes|
/var key=variableName "timePeriod"|
/ife ( {{var::variableName}} != '') {:
	/buttons labels=["Yes", "No"] Do you want to redo redo {{getvar::varibleName}}|
	/var key=do {{pipe}}|
:}|
/ife ( do == 'Yes ) {:
	/var key=wi_book ""|//The Lorebook Name|
	/var key=wi_book_key {{noop}}|//The name of the entry to get|
	/var key=combineLorebookEntries No|//Combines the lorebook entries|
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
*|