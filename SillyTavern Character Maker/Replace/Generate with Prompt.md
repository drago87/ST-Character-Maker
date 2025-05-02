/let GenerateWithPrompt {: wi_book_f="CMC Generation Prompts" wi_book_key_f= genIsList_f= genIsSentence_f= needOutput_f= useContext_f=  contextKey_f={{noop}}
	
	--TextParse--
	
	--SaveGen--
	
	/let key=wi_uid |
	/let key=actionType |
	/let key=context |
	/let key=find|
	/let key=examples {{noop}}|

	/ife ( useContext_f == 'Yes') {:
		/findentry field=comment file="CMC Information" "{{Base Information}}"|
		/var key=wi_uid {{pipe}}|
		/getentryfield field=content file="CMC Information" {{var::wi_uid}}|
		/let key=context {{pipe}}|
		/ife ( real == 'Yes') {:
			/var key=context {{var::context}}{{var::realParced}}|
		:}|
		/ife ( contextKey_f != '') {:
			/foreach {{var::contextKey_f}} {:
				/var key=find "{{var::item}}: Context"|
				/findentry field=comment file="CMC Information" "{{var::find}}"|
				/var key=wi_uid {{pipe}}|
				/ife ( wi_uid != '') {:
					/getentryfield field=content file="CMC Information" {{var::wi_uid}}|
					/var key=context "{\{newline}}{\{newline}}{{var::context}}"|
				:}|
			:}|
		:}|
	:}|
	
	/var key=find "{{var::contextKey_f}}: Examples"|
	/findentry field=comment file={{var::wi_book_f}} "{{var::find}}"|
	/var key=wi_uid {{pipe}}|
	/ife ( wi_uid != '') {:
		/getentryfield field=content file={{var::wi_book_f}} {{var::wi_uid}}|
		/var key=examples {{pipe}}|
	:}|
	/var key=find "{{var::contextKey_f}}: Task"|
	/findentry field=comment file="{{var::wi_book_f}}" "{{var::find}}"|
	/var key=wi_uid {{pipe}}|
	/getentryfield field=content file={{var::wi_book_f}} {{var::wi_uid}}|
	/let key=task {{pipe}}|
	/var key=find "{{var::contextKey_f}}: Instruction"|
	/findentry field=comment file="{{var::wi_book_f}}" "{{var::find}}"|
	/var key=wi_uid {{pipe}}|
	/getentryfield field=content file={{var::wi_book_f}} {{var::wi_uid}}|
	/let key=instruct {{pipe}}|
	
	/let key=genState []|
	/let key=selected_btn |
	
	/let key=isGeneration 'Yes'|
	/setvar as=array key=tempList []|
	/setvar key=output {{noop}}|
	
	/ife ( outputIsList == 'Yes') {:
		/let key=actionType add|
	:}|
	/else {:
		/let key=actionType set|
	:}|
	/let key=man "Manually {{var::actionType}}"|
	
	/let t |
	/whilee ( output == '') {:
		/echo Generating {{var::wi_book_key_f}}|
		/var key=genState []|
		/genraw "{{var::context}}{{var::task}}{\{newline}}{\{newline}}{{var::instruct}}"|
	
		/var key=t {{pipe}}|
		/reasoning-parse return=content {{var::t}}|
		/var key=t {{pipe}}|
		/ife (genIsList_f == 'Yes') {:
			/split find=":" {{var::t}}|
			/var key=t {{pipe}}|
			/foreach {{var::t}} {:
				/re-replace find="/\./g" replace="" {{var::item}}|
				/let key=t1 {{pipe}}|
				/re-replace find="/_/g" replace=" " {{pipe}}|
				/var key=t1 {{pipe}}|
				/to-lower {{var::t1}}|
				/var key=t1 {{pipe}}|
				/re-replace find="/\b([a-z])/" cmd="/to-upper $1" replace="$1" {{var::t1}}|
				/var key=t1 {{pipe}}|
				/wait 1|
				/setat index={{var::index}} value={{var::t}} {{var::t1}}|
				/var key=t {{pipe}}|
			:}|
			/var key=genState {{pipe}}|
		:}|
		/else {:
			/len {{var::genState}}|
			/var key=genState index={{pipe}} {{var::t}}|
		:}|
	
		/ife ( (wi_book_key_f == 'Time Period') and ( 'Modern Day' not in genState)) {:
			/len {{var::genState}}|
			/var key=genState index={{pipe}} Modern Day|
		:}|
		/ife ((genIsList_f == 'Yes') and ( man not in genState)) {:
			/len {{var::genState}}|
			/var key=genState index={{pipe}} {{var::man}}|
		:}|
	
		/ife ( 'Generate New' not in genState) {:
			/len {{var::genState}}|
			/var key=genState index={{pipe}} Generate New|
		:}|
		/ife (('Done' not in genState) and (((outputIsList == 'Yes') and (tempList != '')) or ((outputIsList != 'Yes') and (needOutput_f == 'No')))) {:
			/len {{var::genState}}|
			/var key=genState index={{pipe}} "Done"|
		:}|
	  
		/buttons labels={{var::genState}} Select the {{var::wi_book_key_f}} you want {{getvar:firstName}} to have.|
		/var key=selected_btn {{pipe}}|
	
	
	
		/ife ( selected_btn == ''){:
			/echo Aborting |
			/abort
		:}|
		/elseif ( selected_btn =='Generate New') {::}|
		/elseif ( selected_btn == man) {:
			/ife ( genIsSentence_f == 'Yes' ){:
				/getat index=0 {{var::genState}} |
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
			/:SaveGen input={{var::selected_btn}}|
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