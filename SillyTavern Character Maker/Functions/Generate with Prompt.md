/let GenerateWithPrompt {: wi_book="CMC Generation Prompts" contextKey= genKey=
	--TextParse--
	
	"CMC Generation Prompts"|
	/ife ( contextKey != '') {:
		/findentry field=comment file={{var::wi_book}} {{var::contextKey}}: Context|
		/let key=wi_uid {{pipe}}|
		/ife ( wi_uid != '') {:
			/getentryfield field=content file={{var::wi_book}} {{var::wi_uid}}|
			/let key=context {{pipe}}|
			/ife ( real == 'Yes') {:
				/var key=context {{var::context}}{{var::realParced}}|
			:}|
			/var key=context {{var::context}}{{newline}}{{newline}}|
		:}|
	:}|
	
	/let key=examples {{noop}}|
	/findentry field=comment file={{var::wi_book}} {{var::genKey}}: Examples|
	/var key=wi_uid {{pipe}}|
	/ife ( wi_uid != '') {:
		/getentryfield field=content file={{var::wi_book}} {{var::wi_uid}}|
		/var key=examples {{pipe}}|
	:}|
	/findentry field=comment file={{var::wi_book}} {{var::genKey}}: Task|
	/var key=wi_uid {{pipe}}|
	/getentryfield field=content file={{var::wi_book}} {{var::wi_uid}}|
	/let key=task {{pipe}}|
	/findentry field=comment file={{var::wi_book}} {{var::genKey}}: Instruction|
	/var key=wi_uid {{pipe}}|
	/getentryfield field=content file={{var::wi_book}} {{var::wi_uid}}|
	/let key=instruct {{pipe}}|
	
	/let key=genState []|
	
	/let key=isGeneration 'Yes'|
	/let key=output {{noop}}|
	/let as=array key=tempList []|
	
	/ife ( outputIsList == 'Yes') {:
		/let key=actionType add|
	:}|
	/else {:
		/let key=actionType set|
	:}|
	/let key=man "Manually {{var::actionType}}"|
	
	/let key=ecT "Edit Context(Temp)"|
	/let key=epT "Edit Prompt(Temp)"|
	/let key=epP "Edit Prompt(Perm)"|
	/let key=eiT "Edit Instruct(Temp)"|
	/let key=eiP "Edit Instruct(Perm)"|
	
	/let t {{noop}}|
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
:}|