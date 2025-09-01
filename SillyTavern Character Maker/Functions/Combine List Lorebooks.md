/getvar key=genSettings index=wi_book|
/setvar key=input {{pipe}}|
/wi-list-entries "{{getvar::input}}"|
/let key=wi_temp {{pipe}}|
/map {{pipe}} {:
	/getat index=entries {{var::item}} |
	/map {{pipe}} {:
		/getat index=comment {{var::item}}
	:}
:} |
/setvar key=wi_input_entries {{pipe}}|
/wait {{getvar::wait}}|
/getvar key=wi_input_entries index=0 |
/setvar key=wi_input_entries {{pipe}}|
/setvar as=array key=wi_input_content []|
/wait {{getvar::wait}}|
/foreach {{getvar::wi_input_entries}} {:
	/findentry field=comment file="{{getvar::input}} {{getglobalvar::model}}" "{{var::item}}"|
	/let key=wi_uid {{pipe}}|
	/getentryfield field=content file="{{getvar::input}} {{getglobalvar::model}}" {{var::wi_uid}}|
	/addvar key=wi_input_content {{pipe}}|
:}|

/setvar key=a {{getvar::wi_input_entries}}|
/addvar key=a Done|
/wait 10|
/setvar key=b {{getvar::wi_input_content}}|

/flushvar wi_input_entries|
/flushvar wi_input_content|

/setvar as=array key=genOrder []|
/setvar as=array key=genContent []|

/let key=selected_btn {{noop}}|
/whilee (selected_btn != 'Done') {:
	/buttons labels={{getvar::a}} Select what and in what order you want the characters information to be selected. Press done when you are happy|
	/var key=selected_btn {{pipe}}|

	/ife ( selected_btn == ''){:
		/echo Aborting |
		/break
	:}|
	/elseif ( selected_btn == 'Done') {:
		/flushvar a|
		/flushvar b|
	:}|
	/else {:
		/re-replace find="/\b(?:Female\|Male\|Both)\s/" replace="" {{var::selected_btn}}|
		/let key=parcedInput {{pipe}}|
		/ife (parcedInput not in genOrder) {:
			/addvar key=genOrder {{var::parcedInput}}|
			/find index=true {{getvar::a}} {:
				/test left={{var::item}} rule=eq right={{var::selected_btn}}|
			:}|
			/let as=number key=workingIndex1 {{pipe}}|
			/getat index={{var::workingIndex1}} {{getvar::b}}|
			/addvar key=genContent {{pipe}}|
			
			/splice start={{var::workingIndex1}} delete=1 {{getvar::a}}|
			/setvar key=a {{pipe}}|
			/splice start={{var::workingIndex1}} delete=1 {{getvar::b}}|
			/setvar key=b {{pipe}}|
		:}|
		/else {:
			/find index=true {{getvar::a}} {:
				/test left={{var::item}} rule=eq right={{var::selected_btn}}|
			:}|
			/let as=number key=workingIndex1 {{pipe}}|
			/find index=true {{getvar::genOrder}} {:
				/test left={{var::item}} rule=eq right={{var::parcedInput}}|
			:}|
			/let as=number key=workingIndex2 {{pipe}}|
			/getat index={{var::workingIndex1}} {{getvar::b}}|
			/setvar key=temp {{pipe}}|
			/re-replace find="/Bare/g" replace="" {{getvar::temp}}|
			/setvar key=temp {{pipe}}|
			/split find=":" {{getvar::temp}}|
			/setvar key=temp {{pipe}}|
			/getvar key=b index=workingIndex2|
			/split find=":" {{pipe}}|
			/setvar key=temp2 {{pipe}}|
			/setvar key=temp3 []|
			/foreach {{getvar::temp}} {:
				/ife ( (item not in temp2) and (item != 'Bare')) {:
					/addvar key=temp3 {{var::item}}|
				:}|
			:}|
			/join glue=": " {{getvar::temp3}}|
			/setvar key=temp {{pipe}}|
			
			
			/ife ( temp != '') {:
				/getvar key=genContent index={{getvar::workingIndex2}}|
				/setvar key=genContent index={{getvar::workingIndex2}} "{{pipe}}: {{getvar::temp}}"|
			:}|
			
			/splice start={{var::workingIndex1}} delete=1 {{getvar::a}}|
			/setvar key=a {{pipe}}|
			/splice start={{var::workingIndex1}} delete=1 {{getvar::b}}|
			/setvar key=b {{pipe}}|
			/flushvar temp|
			/flushvar temp2|
			/flushvar temp3|
		:}|
		
	:}|
:}|