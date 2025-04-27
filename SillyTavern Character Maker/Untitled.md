
/* Setup before Selector QR
/setvar key=wi_book ""|//The Lorebook Name|
/setvar key=outputIsList Yes|//Yes or No|
/setvar key=variableName ""|



/:"CMC Logic.Selector"|
/setvar key={{getvar::variableName}} {{getvar::output}}|

*|

/* Selector QR content

/setvar key=workingList1 {{getvar::wi_input_entreis}}|
/addvar key=workingList1 Done|
/setvar key=workingList2 {{getvar::wi_input_content}}|

/setvar as=array key=genOrder []|
/setvar as=array key=genOrderContent []|


/wi-list-entries "{{getvar::wi_book}}"|
/setvar key=wi_temp {{pipe}}|
/map {{pipe}} {:
    /getat index=entries {{var::item}} |
    /map {{pipe}} {:
        /getat index=comment {{var::item}}
    :}
:} |
/setvar key=wi_input_entreis {{pipe}}|
/wait {{getvar::wait}}|
/getvar key=wi_input_entreis index=0|
/setvar key=wi_input_entreis {{pipe}}|
/getvar key=wi_temp|
/map {{pipe}} {:
    /getat index=entries {{var::item}} |
    /map {{pipe}} {:
        /getat index=content {{var::item}}
    :}
:} |
/setvar key=wi_input_content {{pipe}}|
/wait {{getvar::wait}}|
/getvar key=wi_input_content index=0|
/setvar key=wi_input_content {{pipe}}|
/flushvar wi_temp|

/setvar key=selected_btn {{noop}}|
/whilee (selected_btn != 'Done') {:
  /buttons labels={{getvar::workingList1}} Select what and in what order you want the characters information to be selected. Press done when you are happy|
  /setvar key=selected_btn {{pipe}}|

  /ife ( selected_btn == ''){:
    /echo Aborting | /ife ( quickRoll == 'Yes' ) {: /setvar key=debug {{getvar::tempDebug}}| :}| /:"Character Maker V4.Flushvar"|
  :}|
  /elseif ( selected_btn == 'Done') {:
    /pop workingList1|
  :}|
  /else {:
    /re-replace find="/\b(?:Female\|Male\|Both)\s/" replace="" {{getvar::selected_btn}}|
    /setvar key=parcedInput {{pipe}}|
    /ife (parcedInput in genOrder) {:
      /find index=true {{getvar::workingList1}} {:
        /test left={{var::item}} rule=eq right={{getvar::selected_btn}}|
      :}|
      /setvar key=workingIndex {{pipe}}|
      /getvar key=workingList2 index={{getvar::workingIndex}}|
      /setvar key=workingContent2 {{pipe}}|
      /find index=true {{getvar::genOrder}} {:
        /test left={{var::item}} rule=eq right={{getvar::parcedInput}}|
      :}|
      /setvar key=genOrderindex {{pipe}}|
      
      /getvar key=genOrderContent index={{getvar::genOrderindex}}|
      /setvar key=parce1 {{pipe}}|
      /setvar key=parce2 {{getvar::workingContent2}}|
      /split find=":" {{getvar::parce1}}|
      /setvar key=parce1 {{pipe}}|
      /split find=":" {{getvar::parce2}}|
      /setvar key=parce2 {{pipe}}|
      
      /foreach {{getvar::parce1}} {:
      	/setvar key=it {{var::item}}|
        /ife (it in parce2) {:
          /find index=true {{getvar::parce2}} {:
            /test left={{var::item}} rule=eq right={{getvar::it}}|
          :}|
          /splice start={{pipe}} delete=1 {{getvar::parce2}}|
          /setvar key=parce2 {{pipe}}|
        :}|
      :}|
      /join glue=":{{space}}" {{getvar::parce1}}|
      /setvar key=parce1 {{pipe}}|
      /join glue=":{{space}}" {{getvar::parce2}}|
      /setvar key=parce2 {{pipe}}|
      /setvar key=genOrderContent index={{getvar::genOrderindex}} {{getvar::parce1}}: {{getvar::parce2}}|
    :}|
    /else {:
      /find index=true {{getvar::workingList1}} {:
        /test left={{var::item}} rule=eq right={{getvar::selected_btn}}|
      :}|
      /setvar key=workingIndex {{pipe}}|
      /addvar key=genOrder {{getvar::parcedInput}}|
      /getvar key=workingList2 index={{getvar::workingIndex}}|
      /addvar key=genOrderContent {{pipe}}|
    :}|
    /find index=true {{getvar::workingList1}} {:
      /test left={{var::item}} rule=eq right={{getvar::selected_btn}}|
    :}|
    /setvar key=workingIndex {{pipe}}|
    /splice start={{getvar::workingIndex}} delete=1 {{getvar::workingList1}}|
    /setvar key=workingList1 {{pipe}}|
    /splice start={{getvar::workingIndex}} delete=1 {{getvar::workingList2}}|
    /setvar key=workingList2 {{pipe}}|
  :}|
:}|

/foreach {{getvar::genOrder}} {:
	/setvar key=itemInput {{var::item}}|
	/setvar key=in {{var::index}}|
	/getvar key=genOrderContent index={{getvar::in}}|
	/split find=":" {{pipe}}|
	/setvar key=genState {{pipe}}|
	
	/setvar as=array key=tempList []|
	/setvar key=output {{noop}}|
	/setvar key=uI "User Input"|

	  /whilee ( output == '') {:
	    /ife ( 'Random' not in genState) {:
	      /addvar key=genState "Random"|
	    :}|
	    /ife ( ('Done' not in genState) and ( outputIsList == 'Yes')) {:
	      /addvar key=genState "Done"|
	    :}|
	    /ife ( uI not in genState) {:
	      /addvar key=genState {{getvar::Ui}}|
	    :}|
	
	    /buttons labels={{getvar::genState}} Select the {{getvar::itemInput}} you want {{getvar:fname}} to have.|
	    /setvar key=selected_btn {{pipe}}|
	
	
	
	    /ife ( selected_btn == ''){:
	      /echo Aborting | /ife ( quickRoll == 'Yes' ) {: /setvar key=debug {{getvar::tempDebug}}| :}| /:"Character Maker V4.Flushvar"|
	    :}|
	    /elseif ( selected_btn == 'Done') {:
	      /setvar key=output {{getvar::outputList}}|
	    :}|
	    /elseif ( selected_btn == uI) {:
	      /find index=true {{getvar::genState}} {:
	        /test left={{var::item}} rule=eq right="Random"|
	      :}|
	      /slice start=0 end={{pipe}} {{getvar::genState}}|
	      /input What would you want to add manually set as {{getvar::itemInput}}?|
	      /addvar key=add {{pipe}}|
	      /ife ( add == ''){:
	    		/echo Aborting | /ife ( quickRoll == 'Yes' ) {: /setvar key=debug {{getvar::tempDebug}}| :}| /:"Character Maker V4.Flushvar"|
	    	:}|
	      /else {:
	        /ife ( outputIsList == 'Yes') {:
	          /addvar key=outputList {{getvar::parcedInput}}: {{getvar::add}}|
	        :}|
	        /else {:
	          /setvar key=output {{getvar::parcedInput}}: {{getvar::add}}|
	        :}|
	      :}|
	    :}|
	    /elseif (selected_btn == 'Random') {:
	      /find index=true {{getvar::genState}} {:
	        /test left={{var::item}} rule=eq right="Random"|
	      :}|
	      /slice start=0 end={{pipe}} {{getvar::genState}}|
	      /pick items=1 {{getvar::genState}}|
	      /setvar key=add {{pipe}}|
	      /ife ( add == ''){:
	    		/echo Aborting | /ife ( quickRoll == 'Yes' ) {: /setvar key=debug {{getvar::tempDebug}}| :}| /:"Character Maker V4.Flushvar"|
	    	:}|
	      /else {:
	        /ife ( outputIsList == 'Yes') {:
	          /addvar key=outputList {{getvar::parcedInput}}: {{getvar::add}}|
	        :}|
	        /else {:
	          /setvar key=output {{getvar::parcedInput}}: {{getvar::add}}|
	        :}|
	      :}|
	    :}|
	    /else {:
	      /elseif (outputIsList == 'Yes') {:
	        /addvar key=tempList {{getvar::parcedInput}}: {{getvar::selected_btn}}|
	      :}|
	      /else {:
	        /setvar key=output {{getvar::parcedInput}}: {{getvar::selected_btn}}|
	      :}|
	    :}|
	  :}|
:}|
*|