/getvar key=genSettings index=wi_book|
/let key=wi_book_f {{pipe}}|
/ife ( wi_book_f == '') {:
	/var key=wi_book_f "CMC Variables"|
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
/getvar key=genSettings index=outputIsList|
/let key=outputIsList_f {{pipe}}|
/ife ( outputIsList_f == '') {:
	/abort quiet=false Missing outputIsList name in input.|
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
/getvar key=genSettings index=content|
/let key=content_f {{pipe}}|


/let genState {{noop}}|
/let key=wi_uid {{noop}}|
/let key=find {{noop}}|

/let key=exRules ["Explicitness Level", "User Input Style", "Response Length", "Consent Reaction Tone", "Emotional Responsiveness", "Conflict Handling", "Social Openness", "Empathy Attunement", "Verbal Style Communication", "Physical Expressiveness", "Narration Formatting Rule", "Narrative Tone Rule", "Perspective Rule", "Formatting Style" ]|
/ife ( combineLorebookEntries != 'Yes') {:
	/let key=tempGenState {{noop}}|
	/ife (( inputIsList == 'Yes') and (wi_book_key_f is list)) {:
		/var key=find {{getvar::it}}|
		/findentry field=comment file="{{var::wi_book_f}}" "{{var::find}}"|
		/getentryfield field=content file={{var::wi_book_f}} {{pipe}}|
		/var key=genState {{pipe}}|
	:}|
	/elseif (wi_book_key_f is list) {:
		/foreach {{var::wi_book_key_f}} {:
			/var key=find {{var::item}}: List|
			/findentry field=comment file={{var::wi_book_f}} {{var::find}}|
			/let key=UID {{pipe}}|
			/getentryfield field=content file={{var::wi_book_f}} {{var::UID}}|
			/let key=tempL {{pipe}}|
			/ife (index > 0) {:
				/var key=tempGenState "{{var::tempGenState}}: {{var::tempL}}"|
			:}|
			/else {:
				/var key=tempGenState "{{var::tempL}}"|
			:}|
		:}|
		/var key=genState {{var::tempGenState}}|
	:}|
	/elseif (wi_book_key_f in exRules) {:
		/var key=find {{var::wi_book_key_f}}|
		/findentry field=comment file={{var::wi_book_f}} {{var::find}}|
		/let key=UID {{pipe}}|
		/getentryfield field=content file={{var::wi_book_f}} {{var::UID}}|
		/var key=genState {{pipe}}|
	:}|
	/else {:
		/var key=find {{var::wi_book_key_f}}: List|
		/findentry field=comment file={{var::wi_book_f}} {{var::find}}|
		/let key=UID {{pipe}}|
		/getentryfield field=content file={{var::wi_book_f}} {{var::UID}}|
		/var key=genState {{pipe}}|
	:}|
	
:}|
/else {:
	/var key=genState {{var::content}}|
:}|
/ife (debug == 'Yes') {:
	/setvar key="06 Selector" {{var::genState}}|
:}|
/else {:
	/flushvar 06 Selector|
:}|
/let key=exemptRules ["Text Style Rules", "Graphical Detail Rules"]|
/ife (wi_book_key_f in exemptRules) {:
	/split find="{{newline}}" {{var::genState}}|
	/var as=array key=genState {{pipe}}|
:}|
/elseif (wi_book_key_f in exRules) {:
	/split find="{{newline}}" {{var::genState}}|
	/let key=tempArr {{pipe}}|
	/var key=genState []|
	/let key=userSkip ["Consent Reaction Tone"]|
	/foreach {{var::tempArr}} {:
		/ife (wi_book_key_f not in userSkip) {:
			/len {{var::genState}}|
			/var key=genState index={{pipe}} {{var::item}}|
		:}|
		/else {:
			/ife ('--User--' not in item) {:
				/len {{var::genState}}|
				/var key=genState index={{pipe}} {{var::item}}|
			:}|
		:}|
	:}|
:}|
/else {:
	/split find=":" {{var::genState}}|
	/var as=array key=genState {{pipe}}|
:}|

/let key=selected_btn {{noop}}|

/let key=isGeneration 'No'|
/setvar key=output {{noop}}|
/setvar as=array key=tempList []|
/let actionType {{noop}}|

/ife ( outputisList_f == 'Yes') {:
	/var key=actionType add|
:}|
/else {:
	/var key=actionType set|
:}|
/let key=man "Manually {{var::actionType}}"|

/whilee ( output == '') {:
	
	/foreach {{var::genState}} {:
		/re-replace find="/\b([a-z])/" cmd="/to-upper $1" replace="$1" {{var::item}}|
		/var key=genState index={{var::index}} {{pipe}}|
	:}|
	
	/ife ( 'Random' not in genState) {:
		/len {{var::genState}}|
		/var key=genState index={{pipe}} "Random"|
	:}|
	/ife ( man not in genState) {:
		/len {{var::genState}}|
		/var key=genState index={{pipe}} {{var::man}}|
	:}|
	/ife ( (wi_book_key_f is string) and (('Done' not in genState) and (((outputisList_f == 'Yes') and (tempList != '')) or (needOutput_f == 'No')))) {:
		/len {{var::genState}}|
		/var key=genState index={{pipe}} "Done"|
	:}|
	
	/getvar key=genSettings index=buttonPrompt|
	/let key=buttonPrompt_f {{pipe}}|
	/ife ( buttonPrompt_f == '') {:
		/var key=buttonPrompt_f "Select the {{getvar::wi_book_key_f}} you want {{getvar::it}} to have."|
	:}|
	
	/ife (wi_book_key_f is list) {:
		/buttons multiple=true labels={{var::genState}} {{var::buttonPrompt_f}}|
		/var key=selected_btn {{pipe}}|
	:}|
	/else {:
		/buttons labels={{var::genState}} {{var::buttonPrompt_f}}|
		/var key=selected_btn {{pipe}}|
		/ife (wi_book_key_f not in exemptRules) {:
			/re-replace find="/\s\(.*$/g" replace="" {{var::selected_btn}}|
			/var key=selected_btn {{pipe}}|
		:}|
	:}|
	/ife (( selected_btn == '') and (wi_book_f != 'CMC Rules')) {:
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
		/setvar key=save {{var::selected_btn}}|
		/:"CMC Logic.SaveGen"|
	:}|
	/elseif ( selected_btn == man) {:
		/ife ( genIsSentence_f == 'Yes' ){:
			/getat index=0 {{var::genState}}|
			/input default={{pipe}} Edit the output to your liking.|
		:}|
		/else {:
			/ife (outputisList_f == 'Yes') {:
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
		/ife (( genState == 'Done') and (((outputisList_f == 'Yes') and (tempList == '')) or (needOutput_f == 'No'))) {:
			/setvar key=save None|
			/:"CMC Logic.SaveGen"|
		:}|
		/else {:
			/ife (wi_book_key_f == 'Kink Awareness') {:
				/ife (selected_btn == 'Unaware') {:
					/var key=selected_btn "Unaware (**IMPORTANT: The character does not consciously know about this kink. Do not mention it in dialogue or inner thoughts unless discovery is explicitly triggered.**)"|
				:}|
				/ife (selected_btn == 'Suppressed') {:
					/var key=selected_btn "Suppressed (**IMPORTANT: The character avoids thinking about this kink and will not admit to it unless emotionally or situationally forced.**)"|
				:}|
				/ife (selected_btn == 'Curious') {:
					/var key=selected_btn "Curious (**IMPORTANT: The character feels drawn to this kink but doesn’t recognize it as a kink yet. Express through confused reactions, not direct acknowledgment.**)"|
				:}|
			:}|
			/setvar key=save {{var::selected_btn}}|
			/:"CMC Logic.SaveGen"|
		:}|
	:}|
:}|