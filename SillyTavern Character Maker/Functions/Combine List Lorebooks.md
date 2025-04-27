/wi-list-entries "{{var::wi_book}}"|
/var key=wi_temp {{pipe}}|
/map {{pipe}} {:
    /getat index=entries {{var::item}} |
    /map {{pipe}} {:
        /getat index=comment {{var::item}}
    :}
:} |
/setvar key=wi_input_entreis {{pipe}}|
/wait {{getvar::wait}}|
/getat index=0 {{var::wi_input_entreis}}|
/var key=wi_input_entreis {{pipe}}|
/map {{var::wi_temp}} {:
    /getat index=entries {{var::item}} |
    /map {{pipe}} {:
        /getat index=content {{var::item}}
    :}
:} |
/var key=wi_input_content {{pipe}}|
/wait {{getvar::wait}}|
/getat  index=0 {{var::wi_input_content}}|
/var key=wi_input_content {{pipe}}|

/var key=workingList1 {{getvar::wi_input_entreis}}|
/len {{var::wi_input_entreis}}|
/var key=workingList1 index={{pipe}} Done|
/var key=workingList2 {{getvar::wi_input_content}}|

/var as=array key=genOrder []|
/var as=array key=genOrderContent []|

/var key=selected_btn {{noop}}|
/whilee (selected_btn != 'Done') {:
  /buttons labels={{var::workingList1}} Select what and in what order you want the characters information to be selected. Press done when you are happy|
  /var key=selected_btn {{pipe}}|

  /ife ( selected_btn == ''){:
	//[[FlushVar]]|
	/echo Aborting | /ife ( quickRoll == 'Yes' ) {: /setvar key=debug {{getvar::tempDebug}}| :}| /:"CMC Logic.Flushvar"|
  :}|
  /elseif ( selected_btn == 'Done') {:
    /pop workingList1|
  :}|
  /else {:
    /re-replace find="/\b(?:Female\|Male\|Both)\s/" replace="" {{var::selected_btn}}|
    /var key=parcedInput {{pipe}}|
    /ife (parcedInput in genOrder) {:
      /find index=true {{var::workingList1}} {:
        /test left={{var::item}} rule=eq right={{var::selected_btn}}|
      :}|
      /var key=workingIndex {{pipe}}|
      /getat index={{var::workingIndex}} {{var::workingList2}}|
      /var key=workingContent2 {{pipe}}|
      /find index=true {{var::genOrder}} {:
        /test left={{var::item}} rule=eq right={{var::parcedInput}}|
      :}|
      /var key=genOrderindex {{pipe}}|
      
      /getat index={{var::genOrderindex}} {{var::genOrderContent}}|
      /var key=parce1 {{pipe}}|
      /var key=parce2 {{var::workingContent2}}|
      /split find=":" {{var::parce1}}|
      /var key=parce1 {{pipe}}|
      /split find=":" {{var::parce2}}|
      /setvar key=parce2 {{pipe}}|
      
      /foreach {{var::parce1}} {:
      	/var key=it {{var::item}}|
        /ife (it in parce2) {:
          /find index=true {{var::parce2}} {:
            /test left={{var::item}} rule=eq right={{var::it}}|
          :}|
          /splice start={{pipe}} delete=1 {{var::parce2}}|
          /var key=parce2 {{pipe}}|
        :}|
      :}|
      /join glue=":{{space}}" {{var::parce1}}|
      /var key=parce1 {{pipe}}|
      /join glue=":{{space}}" {{var::parce2}}|
      /var key=parce2 {{pipe}}|
      /var key=genOrderContent index={{var::genOrderindex}} {{var::parce1}}: {{var::parce2}}|
    :}|
    /else {:
      /find index=true {{var::workingList1}} {:
        /test left={{var::item}} rule=eq right={{var::selected_btn}}|
      :}|
      /var key=workingIndex {{pipe}}|
      /len {{var::genOrder}}
      /var key=genOrder index={{pipe}} {{getvar::parcedInput}}|
      /var key=workingList2 index={{var::workingIndex}}|
      /var key=t {{pipe}}|
      /len {{var::genOrderContent}}|
      /var key=genOrderContent index={{pipe}} {{var::t}}|
      /var key=t {{noop}}|
    :}|
    /find index=true {{var::workingList1}} {:
      /test left={{var::item}} rule=eq right={{var::selected_btn}}|
    :}|
    /var key=workingIndex {{pipe}}|
    /splice start={{var::workingIndex}} delete=1 {{var::workingList1}}|
    /var key=workingList1 {{pipe}}|
    /splice start={{var::workingIndex}} delete=1 {{var::workingList2}}|
    /var key=workingList2 {{pipe}}|
  :}|
:}|