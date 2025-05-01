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