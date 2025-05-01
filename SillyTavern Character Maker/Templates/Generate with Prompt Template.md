/* Setup before Selector QR
//--------|
/var key=do Yes|
/var key=variableName ""|
/ife ( {{var::variableName}} != '') {:
	/buttons labels=["Yes", "No"] Do you want to redo redo {{var::varibleName}}|
	/var key=do {{pipe}}|
:}|
/ife ( do == 'Yes' ) {:
	/var key=genKey ""|//The name of the Lorebook entry to load|
	/var key=genIsList Yes|//Yes or No|
	/var key=outputIsList Yes|//Yes or No|
	/var key=genIsSentence No|//Yes or No|
	/var key=contextKey {{noop}}|//The name of context template to use|
	
	
	/ife (outputIsList == 'Yes') {:
		/setvar as=array key={{var::variableName}} []|
	:}|
	/else {:
		/setvar as=string key={{var::variableName}} {{noop}}|
	:}|
	//[[Generate with Prompt]]|
	/:"CMC Logic.Generator"|
	
	/setvar key={{var::variableName}}  {{var::output}}|
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
//--------|
*|