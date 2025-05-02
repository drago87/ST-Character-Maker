/let combineLore {: wi_book_f=
	/let key=parcedInput|
	/let key=workingIndex|
	/wi-list-entries "{{var::wi_book_f}}"|
	/let key=wi_temp {{pipe}}|
	/map {{pipe}} {:
	    /getat index=entries {{var::item}} |
	    /map {{pipe}} {:
	        /getat index=comment {{var::item}}
	    :}
	:} |
	/let key=wi_input_entreis {{pipe}}|
	/wait {{getvar::wait}}|
	/getat index=0 {{var::wi_input_entreis}}|
	/var key=wi_input_entreis {{pipe}}|
	/map {{var::wi_temp}} {:
	    /getat index=entries {{var::item}} |
	    /map {{pipe}} {:
	        /getat index=content {{var::item}}
	    :}
	:} |
	/let key=wi_input_content {{pipe}}|
	/wait {{getvar::wait}}|
	/getat  index=0 {{var::wi_input_content}}|
	/var key=wi_input_content {{pipe}}|
	
	/let key=workingList1 {{var::wi_input_entreis}}|
	/len {{var::wi_input_entreis}}|
	/var key=workingList1 index={{pipe}} Done|
	/let key=workingList2 {{getvar::wi_input_content}}|
	
	/setvar as=array key=genOrder []|
	/setvar as=array key=genOrderContent []|
	
	/let key=selected_btn {{noop}}|
	/whilee (selected_btn != 'Done') {:
		/buttons labels={{var::workingList1}} Select what and in what order you want the characters information to be selected. Press done when you are happy|
		/var key=selected_btn {{pipe}}|
	
		/ife ( selected_btn == ''){:
			/echo Aborting |
			/break
		:}|
		/elseif ( selected_btn == 'Done') {:
		:}|
		/else {:
		    /re-replace find="/\b(?:Female\|Male\|Both)\s/" replace="" {{var::selected_btn}}|
		    /let key=parcedInput {{pipe}}|
		    /ife (parcedInput not in genOrder) {:
			    /push genOrder {{var::parcedInput}}|
			    /find index=true {{var::workingList1}} {:
					/test left={{var::item}} rule=eq right={{var::selected_btn}}|
				:}|
				/let key=workingIndex1 {{pipe}}|
				/getat index={{var::workingIndex1}} {{var::workingList2}}|
				/push genContent {{pipe}}|
				/splice start={{var::workingIndex1}} delete=1 {{var::workingList1}}|
				/var key=workingList1 {{pipe}}|
				/splice start={{var::workingIndex1}} delete=1 {{var::workingList2}}|
				/var key=workingList2 {{pipe}}|
			:}|
			/else {:
				/find index=true {{getvar::genOrder}} {:
					/test left={{var::item}} rule=eq right={{var::parcedInput}}|
				:}|
				/let key=genOrderIndex {{pipe}}|
				/find index=true {{var::workingList1}} {:
					/test left={{var::item}} rule=eq right={{var::selected_btn}}|
				:}|
				/let key=workingIndex1 {{pipe}}|
				/getat index={{var::workingIndex1}} {{var::workingList2}}|
				/setat value={{getvar::genContent}} index=genOrderIndex ": {{pipe}}"|
				/setvar key=genContent {{pipe}}|
				/splice start={{var::workingIndex1}} delete=1 {{var::workingList1}}|
				/var key=workingList1 {{pipe}}|
				/splice start={{var::workingIndex1}} delete=1 {{var::workingList2}}|
				/var key=workingList2 {{pipe}}|
			:}|
		:}|
	:}|
:}||