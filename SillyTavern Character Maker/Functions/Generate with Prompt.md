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
/getvar key=genSettings index=outputIsList|
/let key=outputIsList_f {{pipe}}|
/ife ( outputIsList_f == '') {:
	/var key=outputIsList_f No|
:}|
/getvar key=genSettings index=maxSizeOfList|
/let key=maxSizeOfList_f {{pipe}}|
/ife ( (outputIsList_f == 'Yes') and (maxSizeOfList_f == '')) {:
	
:}|
/elseif ( (outputIsList_f == 'Yes') and (maxSizeOfList_f is string)) {:
	/abort quiet=false maxSizeOfList needs to be empty or Number.|
:}|
/getvar key=genSettings index=random|
/let as=array key=random_f {{pipe}}|
/getvar key=genSettings index=contextKey|
/let as=array key=contextKey_f {{pipe}}|
/getvar key=genSettings index=extraContext|
/let as=array key=extraContext_f {{pipe}}|


/let key=wi_uid {{noop}}|
/let key=actionType {{noop}}|
/let key=context {{noop}}|
/let key=find {{noop}}|
/let key=examples {{noop}}|


/ife ( useContext_f == 'Yes') {:
	/setvar key=gen Yes|
	/:"CMC Logic.Get Char info"|
	/:"CMC Logic.Set Base Context"|
	/var key=context {{pipe}}|
	/flushvar gen|
:}|
/ife (( useContext_f == 'No') and ( extraContext_f != '')) {:
/var key=context "### **CONTEXT (for your reference—do not include in the answer):**"
:}|

/ife ( extraContext_f != '') {:

	/foreach {{var::extraContext_f}} {:
		/var key=context {{var::context}}{{newline}}{{var::item}}|
	:}|
:}|

/ife ( contextKey_f != '') {:
	/foreach {{var::contextKey_f}} {:
		/var key=find "{{var::item}}: Context"|
		/findentry field=comment file="CMC Information" "{{var::find}}"|
		/var key=wi_uid {{pipe}}|
		/ife ( wi_uid != '') {:
			/getentryfield field=content file="CMC Information" {{var::wi_uid}}|
			/let key=c {{pipe}}|
			/ife (context != '') {:
				/var key=context "{{var::context}}{{newline}}{{newline}}{{var:c}}"|
			:}|
			/else {:
				/var key=context "{{var:c}}"|
			:}|
		:}|
	:}|
:}|
/ife (context != '') {:
	/var key=context "{{var::context}}{{newline}}{{newline}}"|
:}|

/ife (debug == 'Yes') {:
	/setvar key="01 Context" {{var::context}}|
:}|
/else {:
	/flushvar "01 Context"|
:}|
/var key=find "{{var::wi_book_key_f}}: Examples"|
/findentry field=comment file={{var::wi_book_f}} "{{var::find}}"|
/var key=wi_uid {{pipe}}|
/ife (( wi_uid != '') or ( wi_uid == 0)) {:
	/getentryfield field=content file={{var::wi_book_f}} {{var::wi_uid}}|
	/var key=examples {{pipe}}|
:}|
/ife (debug == 'Yes') {:
	/setvar key="02 Examples" {{var::examples}}|
:}|
/else {:
	/flushvar "02 Examples"|
:}|
/var key=find "{{var::wi_book_key_f}}: Task"|
/findentry field=comment file="{{var::wi_book_f}}" "{{var::find}}"|
/var key=wi_uid {{pipe}}|
/getentryfield field=content file={{var::wi_book_f}} {{var::wi_uid}}|
/let key=task {{pipe}}|
/ife (debug == 'Yes') {:
	/setvar key="03 Task" {{var::task}}|
:}|
/else {:
	/flushvar "03 Task"|
:}|
/var key=find "{{var::wi_book_key_f}}: Instruction"|
/findentry field=comment file="{{var::wi_book_f}}" "{{var::find}}"|
/var key=wi_uid {{pipe}}|
/getentryfield field=content file={{var::wi_book_f}} {{var::wi_uid}}|
/let key=instruct {{pipe}}|
/ife (debug == 'Yes') {:
	/setvar key="04 Instruktions" {{var::instruct}}|
:}|
/else {:
	/flushvar "04 Instruktions"|
:}|
/let key=genState []|
/let key=selected_btn |
/let key=man|

/let key=isGeneration 'Yes'|
/setvar as=array key=tempList []|
/setvar key=output {{noop}}|

/ife ( genIsSentence_f != 'Yes') {:
	/ife ( outputIsList_f == 'Yes') {:
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
/let t |
/whilee ( output == '') {:
	/ife ( (outputIsList_f == 'Yes') and (maxSizeOfList_f is number)) {:
		/len {{getvar::tempList}}|
		/let key=len {{pipe}}|
		/ife (len == maxSizeOfList_f) {:
			/setvar key=save Done|
			/:"CMC Logic.SaveGen"|
			/break|
		:}|
	:}|
	/echo Generating {{var::wi_book_key_f}}|
	/ife ((random_f != '') and ( wi_book_key == 'Speech Single Ticks')) {:
		/var key=instruct {{noop}}|
		/pick {{var::random_f}}|
		/setvar key=rand {{pipe}}|
	:}|
	/var key=genState []|
	/ife (genIsList_f == 'Yes') {:
		/var key=task {{noop}}|
		/var key=find "{{var::wi_book_key_f}}: Task"|
		/findentry field=comment file="{{var::wi_book_f}}" "{{var::find}}"|
		/var key=wi_uid {{pipe}}|
		/getentryfield field=content file={{var::wi_book_f}} {{var::wi_uid}}|
		/var key=task {{pipe}}|
		/var key=find "{{var::wi_book_key_f}}: Instruction"|
		/findentry field=comment file="{{var::wi_book_f}}" "{{var::find}}"|
		/var key=wi_uid {{pipe}}|
		/getentryfield field=content file={{var::wi_book_f}} {{var::wi_uid}}|
		/var key=instruct {{pipe}}|
		/genraw "{{var::context}}{{var::examples}}{{newline}}{{newline}}{{var::task}}{{newline}}{{newline}}{{var::instruct}}"|
		/var key=t {{pipe}}|
		/re-replace find="/^[;\s]+/g" replace="" {{var::t}}|
		/var key=t {{pipe}}|
		/ife (debug == 'Yes') {:
			/setvar key="05 Output" {{var::t}}|
		:}|
		/else {:
			/flushvar "05 Output"|
		:}|
		/reasoning-parse return=content {{var::t}}|
		/var key=t {{pipe}}|
	:}|
	/else {:
		/ife ( wi_book_key_f == 'Speech Examples') {:
			/let key=d Not Done|
			/whilee (d == 'Not Done') {:
				/split {{var::random_f}}|
				/pick {{pipe}}|
				/setvar key=target {{pipe}}|
				/ife (('--User--' in speechPromptClaim) and (target == '--User--')) {:
				:}|
				/else {:
					/var key=d Done|
				:}|
			:}|
			/re-replace find="/{target}/g" replace="{{getvar::target}}" {{getvar::speechPromptClaim}}|
			/setvar key=speechPromptClaimRand {{pipe}}|
		:}|
		/var key=task {{noop}}|
		/var key=find "{{var::wi_book_key_f}}: Task"|
		/findentry field=comment file="{{var::wi_book_f}}" "{{var::find}}"|
		/var key=wi_uid {{pipe}}|
		/getentryfield field=content file={{var::wi_book_f}} {{var::wi_uid}}|
		/var key=task {{pipe}}|
		/var key=find "{{var::wi_book_key_f}}: Instruction"|
		/findentry field=comment file="{{var::wi_book_f}}" "{{var::find}}"|
		/var key=wi_uid {{pipe}}|
		/getentryfield field=content file={{var::wi_book_f}} {{var::wi_uid}}|
		/var key=instruct {{pipe}}|
		/genraw "{{var::context}}{{var::examples}}{{newline}}{{newline}}{{var::task}}{{newline}}{{newline}}{{var::instruct}}"|
		/var key=t {{pipe}}|
		/re-replace find="/^[;\s]+/g" replace="" {{var::t}}|
		/var key=t {{pipe}}|
		/re-replace find="/^\*/g" replace="" {{var::t}}|
		/re-replace find="/\*$/g" replace="" {{pipe}}|
		/var key=t {{pipe}}|
		/ife (debug == 'Yes') {:
			/setvar key="05 Output" {{var::t}}|
		:}|
		/else {:
			/flushvar "05 Output"|
		:}|
		/reasoning-parse return=content {{var::t}}|
		/var key=t {{pipe}}|
		/trimend {{var::t}}|
		/var key=t {{pipe}}|
	:}|
	/ife (genIsList_f == 'Yes') {:
		/split find="," {{var::t}}|
		/var key=t {{pipe}}|
		/ife ((wi_book_key_f != 'Height') and (wi_book_key_f != 'Length')) {:
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
			/var key=genState {{var::t}}|
		:}|
		/ife ((wi_book_key_f == 'Personality Tags' ) and (personalityFoundTags != '')) {:
			/split {{getvar::personalityFoundTags}}|
			/let key=temp {{pipe}}|
			/reverse {{var::temp}}|
			/var key=temp {{pipe}}|
			/foreach {{var::genState}} {:
				/ife ( item not in temp) {:
					/len {{var::temp}}|
					/var key=temp index={{pipe}} {{var::item}}|
				:}|
			:}|
			/var key=genState {{var::temp}}|
			/join glue=", " {{var::genState}}|
			/let key=tempItem {{pipe}}|
			/var as=array key=genState []|
			/var key=genState index=0 {{var::tempItem}}|
		:}|
	:}|
	/else {:
		/len {{var::genState}}|
		/var key=genState index={{pipe}} {{var::t}}|
	:}|
	
	/ife (debug == 'Yes') {:
		/setvar key="00 Genraw" "{{var::context}}{{var::examples}}{{newline}}{{newline}}{{var::task}}{{newline}}{{newline}}{{var::instruct}}"|
		/setvar key="01 Context" {{var::context}}|
		/setvar key="02 Examples" {{var::examples}}|
		/setvar key="03 Task" {{var::task}}|
		/setvar key="04 Instruktions" {{var::instruct}}|
	:}|
	
	
	/ife (('Outfit' in wi_book_key_f) and ('Description' not in wi_book_key_f)) {:
		/unshift genState "None"|
		/var key=genState {{pipe}}|
	:}|
	
	
	/ife ( ('Random' not in genState) and (genIsList_f == 'Yes')) {:
		/len {{var::genState}}|
		/var key=genState index={{pipe}} "Random"|
	:}|
	/let key=manualBlacklist ["seasons"]|
	/ife ( (wi_book_key_f not in manualBlacklist) and ( man not in genState)) {:
		/len {{var::genState}}|
		/var key=genState index={{pipe}} {{var::man}}|
	:}|
	/let key=guidenceBlacklist ["Age Gen", "Age Species"]|
	/ife (( 'Guidance' not in genState) and (wi_book_key_f not in guidenceBlacklist)) {:
		/len {{var::genState}}|
		/var key=genState index={{pipe}} Guidance|
	:}|
	/ife ( 'Generate New' not in genState) {:
		/len {{var::genState}}|
		/var key=genState index={{pipe}} Generate New|
	:}|
	/ife (( 'Customize Parts of the generation' not in genState) and (wi_book_key_f == 'Archetype Base' )) {:
		/len {{var::genState}}|
		/var key=genState index={{pipe}} Customize Parts of the generation|
	:}|
	/let key=forsedOutputWhitelist ["Appearance Features Humanoid", "Appearance Features Other"]|
	/ife (('Done' not in genState) and (((outputIsList_f == 'Yes') and (tempList != '')) or ((outputIsList_f != 'Yes') and (needOutput_f == 'No')) or ( wi_book_key_f in forsedOutputWhitelist))) {:
		/len {{var::genState}}|
		/var key=genState index={{pipe}} "Done"|
	:}|
	
	/let key=basicBlacklist ["Identify Personality Tag", "Personality QA", "Personality Tags", "Speech Examples", "Ability Proficiency", "Ability Description"]|
	/ife (wi_book_key_f not in basicBlacklist) {:
		/buttons labels={{var::genState}} Select the {{var::wi_book_key_f}} you want {{getvar::firstName}} to have.|
		/var key=selected_btn {{pipe}}|
	:}|
	/elseif ( wi_book_key_f == 'Identify Personality Tag') {:
		/buttons labels={{var::genState}} <div>Are these the correct Personality tags found in {{getvar::firstName}}'s Archetype?</div><div>{{getvar::archetype}}</div>|
		/var key=selected_btn {{pipe}}|
	:}|
	/elseif (wi_book_key_f == 'Personality Tags') {:
		/buttons labels={{var::genState}} Is this list of Personality Traits correct for {{getvar::firstName}}?|
		/var key=selected_btn {{pipe}}|
	:}|
	/elseif (wi_book_key_f == 'Personality QA') {:
		/buttons labels={{var::genState}} <div>Is this a good Answer by {{getvar::firstName}} for the question:</div><div>{{getvar::question}}</div>|
		/var key=selected_btn {{pipe}}|
	:}|
	/elseif (wi_book_key_f == 'Speech Examples') {:
		/buttons labels={{var::genState}} <div>Is this a good reaction to:</div><div>{{getvar::speechPromptClaimRand}}</div>|
		/var key=selected_btn {{pipe}}|
	:}|
	/elseif (wi_book_key_f == 'Ability Proficiency') {:
		/buttons labels={{var::genState}} <div>Does this feel like the right level or state for {{getvar::firstName}}'s {{getvar::abilityName}}?</div>|
		/var key=selected_btn {{pipe}}|
	:}|
	/elseif (wi_book_key_f == 'Ability Description') {:
		/buttons labels={{var::genState}} <div>Does this feel a good description for: {{getvar::abilityName}}?</div>|
		/var key=selected_btn {{pipe}}|
	:}|


	/ife ( selected_btn == ''){:
		/echo Aborting |
		/abort
	:}|
	/elseif (selected_btn == 'Random') {:
		/find index=true {{var::genState}} {:
			/test left={{var::item}} rule=eq right="Random"|
		:}|
		/let key=i {{pipe}}|
		/slice start=0 end={{var::i}} {{var::genState}}|
		/pick items=1 {{var::genState}}|
		/var key=selected_btn {{pipe}}|
		/setvar key=save {{var::selected_btn}}|
		/:"CMC Logic.SaveGen"|
	:}|
	/elseif (selected_btn == 'Guidance') {:
		/let key=gu {{noop}}|
		/ife (guidance != '') {:
			/buttons labels=["Remove", "Set", "Change", "Cancel"] What do you want to do with the respons guidance?|
			/var key=gu {{pipe}}|
		:}|
		/else {:
			/buttons labels=["Set", "Cancel"] What do you want to do with the respons guidance?|
			/var key=gu {{pipe}}|
		:}|
		/ife ( gu == ''){:
			/echo Aborting |
			/abort
		:}|
		/elseif ( gu == 'Remove') {:
			/setvar key=guidance {{noop}}|
		:}|
		/elseif ( gu == 'Set') {:
			/input Write what you want the response shoud be guided towards.|
			/setvar key=guidance "The response should be guided toward: {{pipe}}"|
		:}|
		/elseif ( gu == 'Change') {:
			/input default={{getvar::guidance}} Edit what you want the response shoud be guided towards.|
			/setvar key=guidance "{{pipe}}"|
		:}|
		/var key=task {{noop}}|
		/var key=find "{{var::wi_book_key_f}}: Task"|
		/findentry field=comment file="{{var::wi_book_f}}" "{{var::find}}"|
		/var key=wi_uid {{pipe}}|
		/getentryfield field=content file={{var::wi_book_f}} {{var::wi_uid}}|
		/var key=task {{pipe}}|
	:}|
	/elseif ( selected_btn =='Customize Parts of the generation') {:
		/buttons labels=["Yes", "Reset", "No"] Do you want to Customize the {Modifier} of the formula {Modifier} + {Archetype} + {Addition}?|
		/let key=sel "{{pipe}}"|
		/ife (sel == '') {:
			/echo Aborting |
			/abort
		:}|
		/elseif ( sel == 'Yes') {:
			/input Write what you want to have as a Modifier.|
			/setvar key=settingModifier {{pipe}}|
			/ife (sel == '') {:
				/echo Aborting |
				/abort
			:}|
			/else {:
				/setvar key=settingModifier "{Modifier} = {{getvar::settingModifier}}"|
			:}|
		:}|
		/elseif ( sel == 'Reset') {:
			/setvar key=settingModifier {Modifier}|
		:}|
		/buttons labels=["Yes", "Reset", "No"] Do you want to Customize the {Archetype} of the formula {Modifier} + {Archetype} + {Addition}?|
		/var key=sel {{pipe}}|
		/ife (sel == '') {:
			/echo Aborting |
			/abort
		:}|
		/elseif ( sel == 'Yes') {:
			/input Write what you want to have as a Archetype.|
			/setvar key=settingArchetype {{pipe}}|
			/ife (sel == '') {:
				/echo Aborting |
				/abort
			:}|
			/else {:
				/setvar key=settingArchetype "{Archetype} = {{getvar::settingArchetype}}"|
			:}|
		:}|
		/elseif ( sel == 'Reset') {:
			/setvar key=settingArchetype {Archetype}|
		:}|
		/buttons labels=["Yes", "Reset", "No"] Do you want to Customize the {Addition} of the formula {Modifier} + {Archetype} + {Addition}?|
		/var key=sel {{pipe}}|
		/ife (sel == '') {:
			/echo Aborting |
			/abort
		:}|
		/elseif ( sel == 'Yes') {:
			/input Write what you want to have as a Addition.|
			/setvar key=settingAddition {{pipe}}|
			/ife (sel == '') {:
				/echo Aborting |
				/abort
			:}|
			/else {:
				/setvar key=settingAddition "{Addition} = {{getvar::settingAddition}}"|
			:}|
		:}|
		/elseif ( sel == 'Reset') {:
			/setvar key=settingAddition {Addition}|
		:}|
		/var key=task {{noop}}|
		/var key=find "{{var::wi_book_key_f}}: Task"|
		/findentry field=comment file="{{var::wi_book_f}}" "{{var::find}}"|
		/var key=wi_uid {{pipe}}|
		/getentryfield field=content file={{var::wi_book_f}} {{var::wi_uid}}|
		/var key=task {{pipe}}|
		/ife (debug == 'Yes') {:
			/setvar key="03 Task" {{var::task}}|
		:}|
		/else {:
			/flushvar "03 Task"|
		:}|
		/var key=find "{{var::wi_book_key_f}}: Instruction"|
		/findentry field=comment file="{{var::wi_book_f}}" "{{var::find}}"|
		/var key=wi_uid {{pipe}}|
		/getentryfield field=content file={{var::wi_book_f}} {{var::wi_uid}}|
		/var key=instruct {{pipe}}|
		/ife (debug == 'Yes') {:
			/setvar key="04 Instruktions" {{var::instruct}}|
		:}|
		/else {:
			/flushvar "04 Instruktions"|
		:}|
		/var key=t {{noop}}|
	:}|
	/elseif ( selected_btn =='Generate New') {:
		/var key=t {{noop}}|
	:}|
	/elseif ( selected_btn == man) {:
		/echo genIsSentence_f = {{var::genIsSentence_f}}|
		/ife ( genIsSentence_f == 'Yes' ){:
			
			/getat index=0 {{var::genState}}|
			/input default={{pipe}} Edit the output to your liking.|
		:}|
		/else {:
			/ife (outputIsList_f == 'Yes') {:
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
		/ife (( genState == 'Done') and (((outputIsList_f == 'Yes') and (tempList == '')) or (needOutput_f == 'No'))) {:
			/setvar key=save None|
			/:"CMC Logic.SaveGen"|
		:}|
		/else {:
			/setvar key=save {{var::selected_btn}}|
			/:"CMC Logic.SaveGen"|
		:}|
	:}|
:}|