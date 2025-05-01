/setvar key=stepDone No|
/setvar key=stepVar Step2|

//SetTempVariables|
/let key=do {{noop}}|
/let key=variableName {{noop}}|
/let key=wi_book {{noop}}|
/let key=wi_book_key {{noop}}|
/let key=combineLorebookEntries {{noop}}|
/let key=inputIsList {{noop}}|
/let key=outputIsList {{noop}}|
/let key=needOutput {{noop}}|
/let key=content {{noop}}|
/let key=output {{noop}}|
/let key=wi_temp {{noop}}|
/let key=wi_input_entreis {{noop}}|
/let key=wi_input_content {{noop}}|
/let key=workingList1 {{noop}}|
/let key=workingList2 {{noop}}|
/let key=genOrder {{noop}}|
/let key=genOrderContent {{noop}}|
/let key=selected_btn {{noop}}|
/let key=parcedInput {{noop}}|
/let key=workingIndex {{noop}}|
/let key=workingContent2 {{noop}}|
/let key=genOrderindex {{noop}}|
/let key=parce1 {{noop}}|
/let key=parce2 {{noop}}|
/let key=t {{noop}}|
/let key=it {{noop}}|
/let key=wi_uid {{noop}}|
/let key=genState {{noop}}|
/let key=isGeneration {{noop}}|
/let key=tempList {{noop}}|
/let key=actionType {{noop}}|
/let key=man {{noop}}|
/let key=genKey {{noop}}|
/let key=genIsList {{noop}}|
/let key=genIsSentence {{noop}}|
/let key=contextKey {{noop}}|
/let key=context {{noop}}|
/let key=examples {{noop}}|
/let key=task {{noop}}|
/let key=instruct {{noop}}|
/let key=ecT {{noop}}|
/let key=epT {{noop}}|
/let key=epP {{noop}}|
/let key=eiT {{noop}}|
/let key=eiP {{noop}}|
/let key=add {{noop}}|
/let key=lastId {{noop}}|
/let key=mess {{noop}}|
/let key=message {{noop}}|
/let key=databaseList {{noop}}|
/let key=qrList {{noop}}|
/let key=typeGuide {{noop}}|
//-----|



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
	/buttons labels=["Yes", "No"] Do you want to redo redo {{var::variableName}}|
	/var key=do {{pipe}}|
:}|
/ife ( do == 'Yes' ) {:
	/var key=genKey "Time Period"|
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
	/:"CMC Logic.Generator"|
	
	/setvar key={{var::variableName}} {{var::output}}|
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
			/:"CMC Logic.Selector"|
			/addvar key={{var::variableName}} {{var::output}}|
		:}|
	:}|
	/else {:
		/var key=it {{getvar::wi_book_key}}|
		/:"CMC Logic.Selector"|
		/setvar key={{var::variableName}} {{var::output}}|
		
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
/var key=variableName "worldDetails"|
/ife ( {{var::variableName}} != '') {:
	/buttons labels=["Yes", "No"] Do you want to redo redo {{var::variableName}}|
	/var key=do {{pipe}}|
:}|
/ife ( do == 'Yes' ) {:
	/var key=genKey "World Details"|
	/var key=genIsList Yes|
	/var key=outputIsList No|
	/var key=genIsSentence No|
	/var key=contextKey {{noop}}|
	
	
	/ife (outputIsList == 'Yes') {:
		/setvar as=array key={{var::variableName}}|
	:}|
	/else {:
		/setvar as=string key={{var::variableName}} {{noop}}|
	:}|
	//[[Generate with Prompt]]|
	/:"CMC Logic.Generator"|
	
	/setvar key={{var::variableName}} {{var::output}}|
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
	/var key=genKey "World Details"|//The name of the Lorebook entry to load|
	/var key=genIsList Yes|//Yes or No|
	/var key=outputIsList Yes|//Yes or No|
	/var key=genIsSentence No|//Yes or No|
	/var key=contextKey {{noop}}|//The name of context template to use|
	
	
	/ife (outputIsList == 'Yes') {:
		/setvar as=array key={{var::variableName}}|
	:}|
	/else {:
		/setvar as=string key={{var::variableName}} {{noop}}|
	:}|
	//[[Generate with Prompt]]|
	/:"CMC Logic.Generator"|
	
	/setvar key={{var::variableName}} {{var::output}}|
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
/let qrlabel {{pipe}}|
/qr-get set="CMC Main" label={{var::qrlabel}}|
/getat index="message" {{pipe}}|
/qr-update set="CMC Main" label={{var::qrlabel}} newlabel="Start Generating Basic World Information" {{pipe}}|