/getvar key=genSettings index=wi_book|
/var key=wi_book_f {{pipe}}|
/ife ( wi_book_f == '') {:
	/abort quiet=false Missing wi_book name in input.|
:}|
/getvar key=genSettings index=wi_book_key|
/var key=wi_book_key_f {{pipe}}|
/ife ( wi_book_key_f == '') {:
	/abort quiet=false Missing wi_book_key name in input.|
:}|
/getvar key=genSettings index=genIsList|
/var key=genIsList_f {{pipe}}|
/ife ( genIsList_f == '') {:
	/abort quiet=false Missing genIsList setting in input.|
:}|
/getvar key=genSettings index=genIsSentence|
/var key=genIsSentence_f {{pipe}}|
/ife ( genIsSentence_f == '') {:
	/abort quiet=false Missing genIsSentence setting in input.|
:}|
/getvar key=genSettings index=needOutput|
/var key=needOutput_f {{pipe}}|
/ife ( needOutput_f == '') {:
	/var key=needOutput_f Yes|
:}|
/getvar key=genSettings index=useContext|
/var key=useContext_f {{pipe}}|
/ife ( useContext_f == '') {:
	/abort quiet=false Missing useContext setting in input.|
:}|
/getvar key=genSettings index=useContext|
/var key=useContext_f {{pipe}}|
/getvar key=genSettings index=content|
/var key=content_f {{pipe}}|


/let genStat {{noop}}|
/let key=wi_uid {{noop}}|
/let key=find {{noop}}|

/ife ( combineLorebookEntries != 'Yes') {:
	/ife (( inputIsList == 'Yes') and (wi_book_key_f is list)) {:
		/var key=find {{getvar::it}}|
		/findentry field=comment file="{{var::wi_book_f}}" "{{var::find}}"|
		/getentryfield field=content file={{var::wi_book_f}} {{pipe}}|
	:}|
	/else {:
		/var key=find {{var::wi_book_key_f}}: List|
		/findentry field=comment file={{var::wi_book_f}} {{var::find}}|
		/getentryfield field=content file={{var::wi_book_f}} {{pipe}}|
	:}|
	/var key=genState {{pipe}}|
:}|
/else {:
	/var key=genState {{var::content}}|
:}|
/split find=":" {{var::genState}}|
/var as=array key=genState {{pipe}}|

/let key=selected_btn {{noop}}|

/let key=isGeneration 'No'|
/let key=output {{noop}}|
/setvar as=array key=tempList []|
/let actionType {{noop}}|

/ife ( outputIsList == 'Yes') {:
	/var key=actionType add|
:}|
/else {:
	/var key=actionType set|
:}|
/let key=man "Manually {{var::actionType}}"|

/whilee ( output == '') {:
	
	/ife ( 'Random' not in genState) {:
		/len {{var::genState}}|
		/var key=genState index={{pipe}} "Ramdom"|
	:}|
	/ife ( man not in genState) {:
		/len {{var::genState}}|
		/var key=genState index={{pipe}} {{getvar::man}}|
	:}|
	/ife (('Done' not in genState) and (((outputIsList == 'Yes') and (tempList != '')) or (needOutput_f == 'No'))) {:
		/len {{var::genState}}|
		/var key=genState index={{pipe}} "Done"|
	:}|
	/buttons labels={{var::genState}} Select the {{var::it}} you want to use.|
	/var key=selected_btn {{pipe}}|
	
	/ife ( selected_btn == ''){:
		/echo Aborting |
		/abort
	:}|
	/elseif (selected_btn == 'Random') {:
		/find index=true {{var::genState}} {:
			/test left={{var::item}} rule=eq right="Random"|
		:}|
		/slice start=0 end={{pipe}} {{var::genState}}|
		/pick items=1 {{var::genState}}|
		/var key=selected_btn {{pipe}}|
		/:"CMC Logic.SaveGen"|
	:}|
	/elseif ( selected_btn == man) {:
		/ife ( genIsSentence_f == 'Yes' ){:
			/getat index=0 {{var::genState}}|
			/input default={{pipe}} Edit the output to your liking.|
		:}|
		/else {:
			/ife (outputIsList == 'Yes') {:
				/input rows=8 What {{var::wi_book_key_f}} do you like to add to the {{var::wi_book_key_f}} list?|
			:}|
			/else {:
				/input rows=8 What {{var::wi_book_key_f}} do you like to set as {{var::wi_book_key_f}} list?|
			:}|
		:}|
		/var key=selected_btn {{pipe}}|
		/:"CMC Logic.SaveGen"|
	:}|
	/else {:
		/ife (( genState == 'Done') and (((outputIsList == 'Yes') and (tempList == '')) or (needOutput_f == 'No'))) {:
			/setvar key=save None|
			/:"CMC Logic.SaveGen"|
		:}|
		/else {:
			/:"CMC Logic.SaveGen"|
		:}|
	:}|
:}|