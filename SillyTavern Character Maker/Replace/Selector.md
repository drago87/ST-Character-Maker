/let GenerateWithSelector {: wi_book_f= wi_book_key_f= genIsList_f= genIsSentence_f= needOutput_f=  contextKey_f={{noop}}
	/let genStat {{noop}}|
	/ife ( combineLorebookEntries != 'Yes') {:
		/ife (( inputIsList == 'Yes') and (wi_book_key_f is list)) {:
			/findentry field=comment file={{var::wi_book_f}} {{getvar::it}}|
			/getentryfield field=content file={{var::wi_book_f}} {{pipe}}|
		:}|
		/else {:
			/findentry field=comment file={{var::wi_book_f}} {{var::wi_book_key_f}}: List|
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
			/:SaveGen input="{{var::selected_btn}}"|
		:}|
		/else {:
			/ife (( genState == 'Done') and (((outputIsList == 'Yes') and (tempList == '')) or (needOutput_f == 'No'))) {:
				/:SaveGen input="None"|
			:}|
			/else {:
				/:SaveGen input="{{var::selected_btn}}"|
			:}|
		:}|
	:}|
:}|