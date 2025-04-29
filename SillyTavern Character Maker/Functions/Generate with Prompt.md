/* Setup before Selector QR
//--------|
/var key=do Yes|
/var key=variableName ""|
/ife ( {{var::variableName}} != '') {:
	/buttons labels=["Yes", "No"] Do you want to redo redo {{var::varibleName}}|
	/var key=do {{pipe}}|
:}|
/ife ( do == 'Yes ) {:
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

/var key=wi_book "CMC Generation Prompts"|
/ife ( contextKey != '') {:
	/findentry field=comment file={{var::wi_book}} {{var::contextKey}}: Context|
	/var key=wi_uid {{pipe}}|
	/ife ( wi_uid != '') {:
		/getentryfield field=content file={{var::wi_book}} {{var::wi_uid}}|
		/var key=context {{pipe}}|
		/ife ( real == 'Yes') {:
			/var key=context {{var::context}}{{var::realParced}}|
		:}|
		/var key=context {{var::context}}{{newline}}{{newline}}|
	:}|
:}|

/var key=examples {{noop}}|
/findentry field=comment file={{var::wi_book}} {{var::genKey}}: Examples|
/var key=wi_uid {{pipe}}|
/ife ( wi_uid != '') {:
	/getentryfield field=content file={{var::wi_book}} {{var::wi_uid}}|
	/var key=examples {{pipe}}|
:}|
/findentry field=comment file={{var::wi_book}} {{var::genKey}}: Task|
/var key=wi_uid {{pipe}}|
/getentryfield field=content file={{var::wi_book}} {{var::wi_uid}}|
/var key=task {{pipe}}|
/findentry field=comment file={{var::wi_book}} {{var::genKey}}: Instruction|
/var key=wi_uid {{pipe}}|
/getentryfield field=content file={{var::wi_book}} {{var::wi_uid}}|
/var key=instruct {{pipe}}|

/var key=genState []|

/var key=isGeneration 'Yes'|
/var key=output {{noop}}|
/var as=array key=tempList []|

/ife ( outputIsList == 'Yes') {:
	/var key=actionType add|
:}|
/else {:
	/var key=actionType set|
:}|
/var key=man "Manually {{var::actionType}}"|

/var key=ecT "Edit Context(Temp)"|
/var key=epT "Edit Prompt(Temp)"|
/var key=epP "Edit Prompt(Perm)"|
/var key=eiT "Edit Instruct(Temp)"|
/var key=eiP "Edit Instruct(Perm)"|

/whilee ( output == '') {:
	/echo Generating {{var::genKey}}|
	/var key=genState []|
	/genraw "{{var::context}}{{var::task}}{{newline}}{{newline}}{{var::instruct}}"|

	/var key=t {{pipe}}|
	/reasoning-parse return=content {{var::t}}|
	/var key=t {{pipe}}|
	/ife (genIsList == 'Yes') {:
		/re-replace find="/\./g" replace="" {{var::t}}|
		/var key=t {{pipe}}|
		/to-lower {{var::t}}|
		/var key=t {{pipe}}|
		/re-replace find="/\b([a-z])/" cmd="/to-upper $1" replace="$1" {{var::t}}|
		/var key=t {{pipe}}|
		/wait 1|
		/split find=":" {{var::t}}|
		/var key=genState {{pipe}}|
	:}|
	/else {:
		/len {{var::genState}}|
		/var key=genState index={{pipe}} {{var::t}}|
	:}|

	/ife ( (genKey == 'Time Period') and ( 'Modern Day' not in genState)) {:
		/len {{var::genState}}|
		/var key=genState index={{pipe}} Modern Day|
	:}|
	/ife ((genIsList == 'Yes') and ( man not in genState)) {:
		/len {{var::genState}}|
		/var key=genState index={{pipe}} {{var::man}}|
	:}|

	/ife ( 'Generate New' not in genState) {:
		/len {{var::genState}}|
		/var key=genState index={{pipe}} Generate New|
	:}|
	/ife ( ecT not in genState) {:
		/len {{var::genState}}|
		/var key=genState index={{pipe}} {{var::ecT}}|
	:}|
	/ife ( epT not in genState) {:
		/len {{var::genState}}|
		/var key=genState index={{pipe}} {{var::epT}}|
	:}|
	/ife ( epP not in genState) {:
		/len {{var::genState}}|
		/var key=genState index={{pipe}} {{var::epP}}|
	:}|
	/ife ( eiT not in genState) {:
		/len {{var::genState}}|
		/var key=genState index={{pipe}} {{var::eiT}}|
	:}|
	/ife ( eiP not in genState) {:
		/len {{var::genState}}|
		/var key=genState index={{pipe}} {{var::eiP}}|
	:}|
	/ife (('Done' not in genState) and (((outputIsList == 'Yes') and (tempList != '')) or (needOutput == 'No'))) {:
		/len {{var::genState}}|
		/var key=genState index={{pipe}} "Done"|
	:}|
  
	/buttons labels={{var::genState}} Select the {{var::genKey}} you want {{getvar:firstName}} to have.|
	/var key=selected_btn {{pipe}}|



	/ife ( selected_btn == ''){:
		/echo Aborting |
		/abort
	:}|
	/elseif ( selected_btn == man) {:
		/ife ( genIsSentence == 'Yes' ){:
			/getat index=0 {{var::genState}} |
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
		/:SaveGen input={{var::selected_btn}}|
	:}|
	/elseif ( selected_btn == ecT) {:
	    /:textParse input="{{var::context}}"|
	    /input labels={{pipe}} Edit the context temporarily.|
	    /var key=add {{pipe}}|
	    /ife ( add == ''){:
			/echo Aborting |
			/abort
		:}|
	    /else {:
			/:textParse input="{{var::add}}"|
			/var key=context {{var::pipe}}|
		:}|
	:}|
	/elseif ( selected_btn == epT) {:
	    /:textParse input="{{getvar::prompt}}"|
	    /input labels={{pipe}} Edit the prompt temporarily.|
	    /var key=add {{pipe}}|
	    /ife ( add == ''){:
			/echo Aborting |
			/abort
		:}|
	    /else {:
			/:textParse input="{{var::add}}"|
			/var key=prompt {{pipe}}|
		:}|
	:}|
	/elseif ( selected_btn == eiT) {:
	    /:textParse input="{{var::instruct}}"|
	    /input labels={{pipe}} Edit the instructions temporarily.|
	    /var key=add {{pipe}}|
	    /ife ( add == ''){:
			/echo Aborting |
			/abort
		:}|
		/else {:
			/:textParse input="{{var::add}}"|
			/var key=instruct {{pipe}}|
		:}|
	:}|
	/elseif ( selected_btn == epP) {:
		/:textParse input="{{var::prompt}}"|
	    /input default={{pipe}} How would you like to change the prompt permanently?|
	    /var key=add {{pipe}}|
	    /ife ( add == ''){:
			/echo Aborting |
			/abort
	    :}|
	    /else {:
			/findentry field=comment file={{var::wi_book}} {{var::genKey}}: Prompt|
			/var key=wi_uid {{pipe}}|
			/:textParse input="{{var::add}}"|
			/var key=add {{pipe}}|
			/setentryfield file={{getvar::wi_book}} uid={{var::key=wi_uid}} {{pipe}}|
			/var key=prompt {{getvar::add}}|
		:}|
	:}|
	/elseif ( selected_btn == eiP) {:
		/:textParse input="{{var::instruct}}"|
	    /input default={{pipe}} How would you like to change the instructions permanently?|
	    /var key=add {{pipe}}|
	    /ife ( add == ''){:
			/echo Aborting |
			/abort
	    :}|
	    /else {:
			/findentry field=comment file={{var::wi_book}} {{var::genKey}}: Instruction|
			/var key=wi_uid {{pipe}}|
			/:textParse input="{{var::add}}"|
			/var key=add {{pipe}}|
			/setentryfield file={{var::wi_book}} uid={{var::key=wi_uid}} {{pipe}}|
			/var key=prompt {{var::add}}|
	    :}|
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