/getvar key=genSettings index=wi_book|
/let key=wi_book_f {{pipe}}|
/ife ( wi_book_f == '') {:
	/var key=wi_book_f "CMC Generation Prompts"|
:}|
/getvar key=genSettings index=wi_book_key|
/let key=wi_book_key_f {{pipe}}|
/ife ( wi_book_key_f == '') {:
	/abort quiet=false Missing wi_book_key name in input.|
:}|
/getvar key=genSettings index=genIsList|
/let key=genIsList_f {{pipe}}|
/ife ( genIsList_f == '') {:
	/abort quiet=false Missing genIsList setting in input.|
:}|
/getvar key=genSettings index=genIsSentence|
/let key=genIsSentence_f {{pipe}}|
/ife ( genIsSentence_f == '') {:
	/abort quiet=false Missing genIsSentence setting in input.|
:}|
/getvar key=genSettings index=needOutput|
/let key=needOutput_f {{pipe}}|
/ife ( needOutput_f == '') {:
	/var key=needOutput_f Yes|
:}|
/getvar key=genSettings index=useContext|
/let key=useContext_f {{pipe}}|
/ife ( useContext_f == '') {:
	/abort quiet=false Missing useContext setting in input.|
:}|

/getvar key=genSettings index=contextKey|
/let key=contextKey_f {{pipe}}|

/let key=wi_uid {{noop}}|
/let key=actionType {{noop}}|
/let key=context {{noop}}|
/let key=find {{noop}}|
/let key=examples {{noop}}|
/let key=taskList {{noop}}|

/getvar key=genSettings index=inputIsTaskList|
/let key=inputIsTaskList_f {{pipe}}|
/ife ( inputIsTaskList_f == 'Yes') {:
	/var key=find {{var::wi_book_key_f}}: Task List|
	/findentry field=comment file="CMC Generation Prompts" "{{var::find}}"|
	/var key=wi_uid {{pipe}}|
	/ife ( wi_uid != '') {:
		/getentryfield field=content file="CMC Generation Prompts" {{var::wi_uid}}|
		/var key=taskList {{pipe}}|
		/split find=":" {{var::taskList}}|
		/var key=taskList {{pipe}}|
		/ife ( taskList == '') {:
			/abort quiet=false No task list named {{var::find}}.|
		:}|
	:}|
:}|


/ife ( useContext_f == 'Yes') {:
	/findentry field=comment file="CMC Information" "Base Information"|
	/var key=wi_uid {{pipe}}|
	/getentryfield field=content file="CMC Information" {{var::wi_uid}}|
	/var key=context {{pipe}}|
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
				/var key=context "{{newline}}{{newline}}{{var::context}}"|
			:}|
		:}|
	:}|
	/var key=context "{{var::context}}{{newline}}{{newline}}"|
:}|
/setvar key=a1 {{var::context}}|
/var key=find "{{var::wi_book_key_f}}: Examples"|
/findentry field=comment file={{var::wi_book_f}} "{{var::find}}"|
/var key=wi_uid {{pipe}}|
/ife ( wi_uid != '') {:
	/getentryfield field=content file={{var::wi_book_f}} {{var::wi_uid}}|
	/var key=examples {{pipe}}|
:}|
/setvar key=a2 {{var::examples}}|
/var key=find "{{var::wi_book_key_f}}: Task"|
/findentry field=comment file="{{var::wi_book_f}}" "{{var::find}}"|
/var key=wi_uid {{pipe}}|
/getentryfield field=content file={{var::wi_book_f}} {{var::wi_uid}}|
/let key=task {{pipe}}|
/setvar key=a3 {{var::task}}|
/var key=find "{{var::wi_book_key_f}}: Instruction"|
/findentry field=comment file="{{var::wi_book_f}}" "{{var::find}}"|
/var key=wi_uid {{pipe}}|
/getentryfield field=content file={{var::wi_book_f}} {{var::wi_uid}}|
/let key=instruct {{pipe}}|
/setvar key=a4 {{var::instruct}}|
/let key=genState []|
/let key=selected_btn |
/let key=man|

/let key=isGeneration 'Yes'|
/setvar as=array key=tempList []|
/setvar key=output {{noop}}|

/ife ( genIsSentence != 'Yes') {:
	/ife ( outputIsList == 'Yes') {:
		/var key=actionType add|
	:}|
	/else {:
		/var key=actionType set|
	:}|
	/var key=man "Manually {{var::actionType}}"|
:}|
/else {:
	/var key=man "Edit output"|
:}|
/setvar key=b {{var::context}}{{var::task}}{{newline}}{{newline}}{{var::instruct}}|
/let t |
/whilee ( output == '') {:
	/echo Generating {{var::wi_book_key_f}}|
	/var key=genState []|

	/ife (genIsList_f == 'Yes') {:
		/ife ( inputIsTaskList_f == 'Yes') {:
			/foreach {{var::taskList}} {:
				/setvar key=item {{var::item}}|
				/var key=find "{{var::wi_book_key_f}}: Task"|
				/findentry field=comment file="{{var::wi_book_f}}" "{{var::find}}"|
				/var key=wi_uid {{pipe}}|
				/getentryfield field=content file="{{var::wi_book_f}}" {{var::wi_uid}}|
				/let key=task {{pipe}}|
				/let key=same Yes|
				
				/whilee ( same == 'Yes') {:
					/let tempItem {{noop}}|
					/genraw "{{var::context}}{{var::task}}{{newline}}{{newline}}{{var::instruct}}"|
					/var tempItem {{pipe}}|
					/reasoning-parse return=content {{var::tempItem}}|
					/var tempItem {{pipe}}|
					/ife (tempItem not in t) {:
						/ife (t != '') {:
							/var key=t "{{var::t}}: {{var::tempItem}}"|
						:}|
						/else {:
							/var key=t "{{var::tempItem}}"|
						:}|
						/var same No|
					:}|
				:}|
			:}|
		:}|
		/else {:
			/genraw "{{var::context}}{{var::task}}{{newline}}{{newline}}{{var::instruct}}"|
			/var key=t {{pipe}}|
			/reasoning-parse return=content {{var::t}}|
			/var key=t {{pipe}}|
		:}|
	:}|
	/else {:
		
		/genraw length=50 "{{var::context}}{{var::task}}{{newline}}{{newline}}{{var::instruct}}"|
		/var key=t {{pipe}}|
		/reasoning-parse return=content {{var::t}}|
		/var key=t {{pipe}}|
		/trimend {{var::t}}|
		/var key=t {{pipe}}|
	:}|
	/ife (genIsList_f == 'Yes') {:
		/split find="," {{var::t}}|
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
	/ife ( ((genIsSentence == 'Yes') or (genIsList_f == 'Yes')) and ( man not in genState)) {:
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
  
	/buttons labels={{var::genState}} Select the {{var::wi_book_key_f}} you want {{getvar::firstName}} to have.|
	/var key=selected_btn {{pipe}}|



	/ife ( selected_btn == ''){:
		/echo Aborting |
		/abort
	:}|
	/elseif ( selected_btn =='Generate New') {:
		/var key=t {{noop}}|
	:}|
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
		/setvar key=save {{var::selected_btn}}|
		/:"CMC Logic.SaveGen"|
	:}|
	/else {:
		/ife (( genState == 'Done') and (((outputIsList == 'Yes') and (tempList == '')) or (needOutput_f == 'No'))) {:
			/setvar key=save None|
			/:"CMC Logic.SaveGen"|
		:}|
		/else {:
			/setvar key=save {{var::selected_btn}}|
			/:"CMC Logic.SaveGen"|
		:}|
	:}|
:}|