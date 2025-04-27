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

/ife ( combineLorebookEntries != 'Yes) {:
	/ife (( inputIsList == 'Yes') and (wi_book_key is list)) {:
		/findentry field=comment file={{var::wi_book}} {{var::it}}|
		/var key=wi_uid {{pipe}}|
		/getentryfield field=content file={{var::wi_book}} {{var::wi_uid}}|
	:}|
	/else {:
		/findentry field=comment file={{var::wi_book}} {{var::wi_book_key}}: List|
		/var key=wi_uid {{pipe}}|
		/getentryfield field=content file={{var::wi_book}} {{var::wi_uid}}|
	:}|
	/var key=genState {{pipe}}|
:}|
/else {:
	/var key=genState {{var::content}}|
:}|
/split find=":" {{var::genState}}|
/var as=array key=genState {{pipe}}|

/var key=isGeneration 'No'|
/var key=output {{noop}}|
/var as=array key=tempList []|

/ife ( outputIsList == 'Yes') {:
	/var key=actionType add|
:}|
/else {:
	/var key=actionType set|
:}|
/var key=man "Manually {{var::actionType}}"|

/whilee ( output == '') {:
	
	/ife ( 'Random' not in genState) {:
		/len {{var::genState}}|
		/var key=genState index={{pipe}} "Ramdom"|
	:}|
	/ife ( man not in genState) {:
		/len {{var::genState}}|
		/var key=genState index={{pipe}} {{getvar::man}}|
	:}|
	/ife (('Done' not in genState) and (((outputIsList == 'Yes') and (tempList != '')) or (needOutput == 'No'))) {:
		/len {{var::genState}}|
		/var key=genState index={{pipe}} "Done"|
	:}|
	/buttons lable={{var::genState}} Select the {{var::it}} you want to use.|
	/var key=selected_btn {{pipe}}|
	
	/ife ( selected_btn == ''){:
		/echo Aborting | /ife ( quickRoll == 'Yes' ) {: /setvar key=debug {{getvar::tempDebug}}| :}| /:"CMC Logic.Flushvar"|
	:}|
	/elseif (selected_btn == 'Random') {:
		/find index=true {{var::genState}} {:
	        /test left={{var::item}} rule=eq var="Random"|
		:}|
		/slice start=0 end={{pipe}} {{var::genState}}|
		/pick items=1 {{var::genState}}|
		/var key=selected_btn {{pipe}}|
		/:SaveGen input="{{var::selected_btn}}"|
	:}|
	/elseif ( selected_btn == man) {:
		/ife ( genIsSentence == 'Yes' ){:
			/getat index=0 {{var::genState}}|
			/input default={{pipe}} Edit the output to your liking.|
		:}|
		/else {:
			/ife (outputIsList == 'Yes') {:
				/input rows=8 What {{var::genKey}} do you like to add to the {{var::genKey}} list?|
			:}|
			/else {:
				/input rows=8 What {{var::genKey}} do you like to set as {{var::genKey}} list?|
			:}|
		:}|
		/var key=selected_btn {{pipe}}|
		/:SaveGen input="{{var::selected_btn}}"|
	:}|
	/else {:
		/ife (( genState == 'Done') and (((outputIsList == 'Yes') and (tempList == '')) or (needOutput == 'No'))) {:
			/:SaveGen input="None"|
		:}|
		/else {:
			/:SaveGen input="{{var::selected_btn}}"|
		:}|
	:}|
:}|