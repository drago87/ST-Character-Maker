/qr-list CMC Main|
/getat index=1 {{pipe}}|
/let qrlabel {{pipe}}|
/qr-get set="CMC Main" label={{var::qrlabel}}|
/getat index="message" {{pipe}}|
/qr-update set="CMC Main" label={{var::qrlabel}} newlabel="Continue Generating Extras" {{pipe}}|

/:"CMC Logic.Get Char info"|

/setvar key=dataBaseNames []|
/flushvar genSettings|

/setvar key=stepVar Step10|

/setvar key=skip Update|
/ife ( stepDone == 'No') {:
	/buttons labels=["Skip", "Update"] Do you want to skip or update already generated content? You will get a question for each already done if you select Update.|
	/setvar key=skip {{pipe}}|
	/ife ( skip == ''){:
		/echo Aborting |
		/abort
	:}|
:}|

/setvar key=stepDone No|

/let key=do {{noop}}|
/let key=variableName {{noop}}|
/let selected_btn {{noop}}|
/let key=len {{noop}}|





//--------|
/ife (((characterArchetype != 'Animalistic') and (characterArchetype != 'Pokémon')) or ('Fully Sapient' in parsedSentientLevel)) {:
  /setvar key=skipQA No|
:}|
/else {:
  /setvar key=skipQA Yes|
:}|

/ife (skipQA != 'Yes') {:
	/len {{getvar::speechQuestions}}|
	/let key=sQLen {{pipe}}|
	/len {{getvar::speechExampleList}}|
	/let key=sELen {{pipe}}|
	//Speech Examples|
	/var key=do No|
	/var key=variableName "speechExampleList"|
	/ife (({{var::variableName}} == '') or (sQLen != sELen)) {:
	    /var key=do Yes|
	:}|
	/elseif (skip == 'Update') {:
	    /getvar key={{var::variableName}}|
	    /buttons labels=["Yes", "No"] Do you want to set or redo {{var::variableName}} (current value: {{pipe}})?|
	    /var key=do {{pipe}}|
	    /ife (do == '') {:
	        /echo Aborting |
	        /abort
	    :}|
	    /elseif (do == 'Yes') {:
		    /flushvar {{getvar::variableName}}|
	    :}|
	:}|
	/ife ( do == 'Yes' ) {:
		/setvar key=genSettings {}|
		/flushvar speechExample|
		/flushvar speechExampleList|
		/setvar key=genSettings index=wi_book_key "Speech Examples QA"|
		/setvar key=genSettings index=genIsList No|
		/setvar key=genSettings index=inputIsList Yes|
		/setvar key=genSettings index=genIsSentence Yes|
		/setvar key=genSettings index=needOutput Yes|
		/setvar key=genSettings index=outputIsList No|
		/setvar key=genSettings index=useContext Yes|
		/setvar key=extra []|
		/addvar key=extra "- Speech Style: {{getvar::speechStyle}}"|
		/addvar key=extra "- Speech Quirks: {{getvar::speechQuirks}}"|
		/addvar key=extra "- Speech Tics: {{getvar::speechTics}}"|
		
		/addvar key=extra "- Main Personality Trait: {{getvar::personalityMainTrait}}"|
		/addvar key=extra "- Personality Trait Tags: {{getvar::personalityFoundTags}}, {{getvar::personalityTags}}"|
		/ife (personalitycognitiveAbilities != 'None') {:
			/addvar key=extra "- Cognitive Abilities: {{getvar::personalitycognitiveAbilities}}{{newline}}"|
		:}|
		
		/ife (personalitySocialSkills != 'None') {:
			/addvar key=extra "- Social Skills and Integration Into Society: {{getvar::personalitySocialSkills}}"|
		:}|
		/ife (personalitySocialBehavior != 'Normal') {:
			/addvar key=extra "- Social Behavior: {{getvar::personalitySocialBehavior}}"|
		:}|
		
		/addvar key=extra "- Setting Type: {{getvar::settingType}}"|
		/ife (user != 'No') {:
			/addvar key=extra "- User Role: {{getvar::userRole}}"|
		:}|
		/ife (parsedSentientLevel != 'None') {:
			/addvar key=extra "{{getvar::parsedSentientLevel}}"|
		:}|
		/setvar key=genSettings index=extraContext {{getvar::extra}}|
		/flushvar extra|
		/setvar key=genSettings index=contextKey []|
		
		/setvar key=logicBasedInstruction {{noop}}|
		/ife (cognitiveAbilities != 'None') {:
			/addvar key=logicBasedInstruction "6. Adjust vocabulary, pacing, or complexity to reflect the character’s cognitive abilities."|
		:}|
		/ife (socialSkills != 'None') {:
			/ife (logicBasedInstruction != '') {:
				/addvar key=logicBasedInstruction "{{newline}}7. "|
			:}|
			/else {:
				/addvar key=logicBasedInstruction "6. "|
			:}|
			/addvar key=logicBasedInstruction "Reflect the character’s social integration level in tone, phrasing, or use of social cues like sarcasm, awkwardness, or formality."|
		:}|
		
		/wait {{getvar::wait}}|
		/ife ((speechQuestions is list) and (speechQuestions != '')) {:
			/buttons labels=["Yes", "No"] <div>Speech Examples</div><div>Do you want to redo the static Speech Questions?</div>|
			/var key=selected_btn {{pipe}}|
			/ife ( selected_btn == ''){:
				/echo Aborting |
				/abort
			:}|
			/elseif ( selected_btn == 'Yes'){:
				/flushvar speechQuestions|
			:}|
		:}|
		/else {:
			/setvar key=speechQuestions []|
		:}|
		
		/ife (speechQuestions == '') {: 
			/findentry field=comment file="CMC Questions" "Speech Situation: Q"|
			/let key=wi_uid {{pipe}}|
			/getentryfield field=content file="CMC Questions" {{var::wi_uid}}|
			/let key=unfilteredQuestions {{pipe}}|
			
			/split find="{{newline}}" {{var::unfilteredQuestions}}|
			/var key=unfilteredQuestions {{pipe}}|
			/let key=pop {{noop}}|
			/foreach {{var::unfilteredQuestions}} {:
				/var key=pop {{var::pop}}<div>{{var::item}}</div>| 
			:}|
			/popup wide=true okButton="Continue" <div>Here is the questions you have to choose from during generation.</div><div>{taget} is going to get randomised each time you redo the generation.</div><div>You will also be able to add your own.</div><div>---</div>{{var::pop}}|
			/let key=filteredQuestions []|
			/foreach {{var::unfilteredQuestions}} {:
				/ife (( user != 'Yes') and ('--User--' not in item)) or ( user == 'Yes') {:
					/var key=filteredQuestions index={{var::index}} {{var::item}}|
				:}| 
			:}|
			/buttons labels={{var::filteredQuestions}} multiple=true <div>Choose questions or prompts that will help define how {{getvar::firstName}} talks or reacts in conversation.</div><div>{target} will be a randomized person/entity</div><div>It is reccomended to select</div><div>**6–10** of **“What would you say if...”** questions</div></div><div>and</div><div>**3–6** of **“What is your opinion...”** questions</div>|
			/setvar key=speechQuestions {{pipe}}|
			/ife (speechQuestions == '') {:
				/echo Aborting |
				/abort
			:}|
		:}|
		/let key=stop Yes|
		/whilee (stop != 'No') {:
			/buttons labels=["Yes", "No"] Do you want to add another question or prompt?|
			/var key=stop {{pipe}}|
			/ife ( stop == '') {:
				/echo Aborting |
				/abort
			:}|
			/ife ( stop == 'Yes') {:
				/input default="What would you say if " 
	<div>You can use <code>{target}</code> to insert a randomized name or entity.</div><div>What situation or opinion do you want {{getvar::firstName}} to respond to?</div>
	<div style="text-align: center;">
	  <p>Your input will be used to complete one of the following phrases:</p>
	  <div>
	    <div>What would you say if...</div>
	    <div>What is your opinion on...</div>
	  </div>
	</div>|
				/let key=q {{pipe}}|
				/ife ( q == '') {:
					/echo Aborting |
					/abort
				:}|
				/addvar key=speechQuestions {{var::q}}|
			:}|
		:}|
		
		
		/findentry field=comment file="CMC Variables" "Someone Random"|
		/let key=wi_uid {{pipe}}|
		/getentryfield field=content file="CMC Variables" {{var::wi_uid}}|
		/let key=rnd {{pipe}}|
		/var key=do {{noop}}|
		/whilee (do != 'Done') {:
			/let key=work {{var::rnd}}|
			/input rows=1 <div>Input a person/entity to add to the randomization</div><div>{{var::work}}</div><div>Press cancel when done</div>|
			/var key=do {{pipe}}|
			/ife (do == '') {:
				/var key=do "Done"|
			:}|
			/else {:
				/var key=rnd {{var::rnd}}, {{var::do}}|
			:}|
		:}|
		
		/setvar key=genSettings index=random {{var::rnd}}|
		
		
		/getvar key=genSettings index=inputIsList|
		/let key=inputIsList {{pipe}}|
		/getvar key=genSettings index=inputIsList|
		/let key=outputIsList {{pipe}}|
		
		
		
		//[[Generate with Prompt]]|
		/ife (inputIsList == 'Yes') {:
			/let key=tempOutputList []|
			/foreach {{getvar::speechQuestions}} {:
				/setvar key=speechPromptClaim {{var::item}}|
				/echo extendedTimeout=0 timeout=0 awaitDismissal=true Test1|
				/:"CMC Logic.GenerateWithPrompt"|
				/echo extendedTimeout=0 timeout=0 awaitDismissal=true Test2|
				/ife ((output != '') and (output != 'None')) {:
					/re-replace find="/^\"/g" replace="" {{getvar::output}}|
					/re-replace find="/\"$/g" replace="" {{pipe}}|
					/let key=tOut {{pipe}}|
					/echo extendedTimeout=0 timeout=0 awaitDismissal=true Test3|
					/len {{var::tempOutputList}}|
					/var key=tempOutputList index={{pipe}} "\"{{var::tOut}}\""|
					/echo extendedTimeout=0 timeout=0 awaitDismissal=true Test4|
				:}|
				/flushvar output|
				/flushvar guidance|
			:}|
			/foreach {{var::tempOutputList}} {:
				/addvar key={{var::variableName}} {{var::item}}|
			:}|
			/flushvar speechPromptClaim|
		:}|
		/addvar key=dataBaseNames {{var::variableName}}|
		/flushvar output|
		/flushvar guidance|
		/flushvar genOrder|
		/flushvar genContent|
		/flushvar genSettings|
	:}|
	//--------|
:}|