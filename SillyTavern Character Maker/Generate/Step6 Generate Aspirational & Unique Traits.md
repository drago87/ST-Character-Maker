/qr-list CMC Main|
/getat index=1 {{pipe}}|
/let qrlabel {{pipe}}|
/qr-get set="CMC Main" label={{var::qrlabel}}|
/getat index="message" {{pipe}}|
/qr-update set="CMC Main" label={{var::qrlabel}} newlabel="Start Generating Aspirational & Unique Traits" {{pipe}}|

/:"CMC Logic.Get Char info"|

/setvar key=dataBaseNames []|
/flushvar genSettings|

/setvar key=stepVar Step6|

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

/flushvar guidance|

//Main Aspiration|
/var key=do No|
/var key=variableName "aspirationMain"|
/ife ({{var::variableName}} == '') {:
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
:}|
/ife ( do == 'Yes' ) {:
	/setvar key=genSettings {}|
	/setvar key=genSettings index=wi_book_key "Aspiration Main"|
	/setvar key=genSettings index=genIsList No|
	/setvar key=genSettings index=inputIsTaskList No|
	/setvar key=genSettings index=genIsSentence Yes|
	/setvar key=genSettings index=needOutput Yes|
	/setvar key=genSettings index=outputIsList No|
	/setvar key=genSettings index=useContext Yes|
	/setvar key=extra []|
	/addvar key=extra "{{getvar::parsedArchetype}}"|
	/ife (parsedAlignment != 'None') {:
		/addvar key=extra "{{newline}}{{getvar::parsedAlignment}}{{newline}}"|
	:}|
	/addvar key=extra "- Intelligence Level: {{getvar::personalityIntelligenceLevel}}"|
	/ife (personalitycognitiveAbilities != 'None') {:
		/addvar key=extra "- Cognitive Abilities: {{getvar::personalitycognitiveAbilities}}{{newline}}"|
	:}|
	/addvar key=extra "- Social Behavior: {{getvar::personalitySocialBehavior}}"|
	/ife (personalitySocialSkills != 'None') {:
		/addvar key=extra "- Social Skills and Integration Into Society: {{getvar::personalitySocialSkills}}{{newline}}"|
	:}|
	/addvar key=extra "- Backstory: {{getvar::backstory}}"|
	/addvar key=extra "- Character Overview: {{getvar::characterOverview}}"|
	/setvar key=genSettings index=extraContext {{getvar::extra}}|
	/flushvar extra|
	/setvar key=genSettings index=contextKey []|
	/wait {{getvar::wait}}|
	
	/getvar key=genSettings index=inputIsList|
	/let key=inputIsList {{pipe}}|
	/getvar key=genSettings index=inputIsList|
	/let key=outputIsList {{pipe}}|
	
	
	/ife ((inputIsList== 'Yes') or (outputIsList == 'Yes')) {:
		/setvar as=array key={{var::variableName}} []|
	:}|
	/else {:
		/setvar as=string key={{var::variableName}} {{noop}}|
	:}|
	//[[Generate with Prompt]]|
	/ife (inputIsList == 'Yes') {:
		
	:}|
	/else {:
		/:"CMC Logic.GenerateWithPrompt"|
		/addvar key={{var::variableName}} {{getvar::output}}|
	:}|
	/addvar key=dataBaseNames {{var::variableName}}|
	/flushvar output|
	/flushvar guidance|
	/flushvar genOrder|
	/flushvar genContent|
	/flushvar genSettings|
:}|
/else {:
	/addvar key=dataBaseNames {{var::variableName}}|
:}|
//--------|


//Aspiration Details|
/var key=do No|
/var key=variableName "aspirationDetails"|
/ife ({{var::variableName}} == '') {:
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
:}|
/ife ( do == 'Yes' ) {:
	/setvar key=genSettings {}|
	/setvar key=genSettings index=wi_book_key "Aspiration Details"|
	/setvar key=genSettings index=genIsList No|
	/setvar key=genSettings index=inputIsTaskList No|
	/setvar key=genSettings index=genIsSentence No|
	/setvar key=genSettings index=needOutput Yes|
	/setvar key=genSettings index=outputIsList No|
	/setvar key=genSettings index=useContext Yes|
	/setvar key=extra []|
	/addvar key=extra "{{getvar::parsedArchetype}}"|
	/ife (parsedAlignment != 'None') {:
		/addvar key=extra "{{newline}}{{getvar::parsedAlignment}}{{newline}}"|
	:}|
	/addvar key=extra "- Intelligence Level: {{getvar::personalityIntelligenceLevel}}"|
	/ife (personalitycognitiveAbilities != 'None') {:
		/addvar key=extra "- Cognitive Abilities: {{getvar::personalitycognitiveAbilities}}{{newline}}"|
	:}|
	/addvar key=extra "- Social Behavior: {{getvar::personalitySocialBehavior}}"|
	/ife (personalitySocialSkills != 'None') {:
		/addvar key=extra "- Social Skills and Integration Into Society: {{getvar::personalitySocialSkills}}{{newline}}"|
	:}|
	/addvar key=extra "- Backstory: {{getvar::backstory}}"|
	/addvar key=extra "- Main Aspiration: {{getvar::aspirationMain}}"|
	/addvar key=extra "- Character Overview: {{getvar::characterOverview}}"|
	/setvar key=genSettings index=extraContext {{getvar::extra}}|
	/flushvar extra|
	/setvar key=genSettings index=contextKey []|
	/wait {{getvar::wait}}|
	
	/getvar key=genSettings index=inputIsList|
	/let key=inputIsList {{pipe}}|
	/getvar key=genSettings index=inputIsList|
	/let key=outputIsList {{pipe}}|
	
	
	/ife ((inputIsList== 'Yes') or (outputIsList == 'Yes')) {:
		/setvar as=array key={{var::variableName}} []|
	:}|
	/else {:
		/setvar as=string key={{var::variableName}} {{noop}}|
	:}|
	//[[Generate with Prompt]]|
	/ife (inputIsList == 'Yes') {:
		
	:}|
	/else {:
		/:"CMC Logic.GenerateWithPrompt"|
		/addvar key={{var::variableName}} {{getvar::output}}|
	:}|
	/addvar key=dataBaseNames {{var::variableName}}|
	/flushvar output|
	/flushvar guidance|
	/flushvar genOrder|
	/flushvar genContent|
	/flushvar genSettings|
:}|
/else {:
	/addvar key=dataBaseNames {{var::variableName}}|
:}|
//--------|


//Aspiration Goals|
/var key=do No|
/var key=variableName "aspirationGoals"|
/ife ({{var::variableName}} == '') {:
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
:}|
/ife ( do == 'Yes' ) {:
	/setvar key=genSettings {}|
	/setvar key=genSettings index=wi_book_key "Aspiration Goals"|
	/setvar key=genSettings index=genIsList No|
	/setvar key=genSettings index=inputIsTaskList No|
	/setvar key=genSettings index=genIsSentence No|
	/setvar key=genSettings index=needOutput Yes|
	/setvar key=genSettings index=outputIsList No|
	/setvar key=genSettings index=useContext Yes|
	/setvar key=extra []|
	/addvar key=extra "- Occupation: {{getvar::occupationBase}}"|
	/addvar key=extra "- Time Period: {{getvar::timePeriod}}"|
	/addvar key=extra "- Setting Type: {{getvar::settingType}}"|
	/addvar key=extra "{{getvar::parsedArchetype}}"|
	/ife (parsedAlignment != 'None') {:
		/addvar key=extra "{{newline}}{{getvar::parsedAlignment}}{{newline}}"|
	:}|
	/addvar key=extra "- Intelligence Level: {{getvar::personalityIntelligenceLevel}}"|
	/ife (personalitycognitiveAbilities != 'None') {:
		/addvar key=extra "- Cognitive Abilities: {{getvar::personalitycognitiveAbilities}}{{newline}}"|
	:}|
	/addvar key=extra "- Social Behavior: {{getvar::personalitySocialBehavior}}"|
	/ife (personalitySocialSkills != 'None') {:
		/addvar key=extra "- Social Skills and Integration Into Society: {{getvar::personalitySocialSkills}}{{newline}}"|
	:}|
	/addvar key=extra "- Backstory: {{getvar::backstory}}"|
	/addvar key=extra "- Main Aspiration: {{getvar::aspirationMain}}"|
	/addvar key=extra "  - Aspiration Details: {{getvar::aspirationDetails}}"|
	//addvar key=extra " - Scenario Overview: {{getvar::scenarioOverview}}"|
	/addvar key=extra "- Character Overview: {{getvar::characterOverview}}"|
	/setvar key=genSettings index=extraContext {{getvar::extra}}|
	/flushvar extra|
	/setvar key=genSettings index=contextKey []|
	/wait {{getvar::wait}}|
	
	/getvar key=genSettings index=inputIsList|
	/let key=inputIsList {{pipe}}|
	/getvar key=genSettings index=inputIsList|
	/let key=outputIsList {{pipe}}|
	
	
	/ife ((inputIsList== 'Yes') or (outputIsList == 'Yes')) {:
		/setvar as=array key={{var::variableName}} []|
	:}|
	/else {:
		/setvar as=string key={{var::variableName}} {{noop}}|
	:}|
	//[[Generate with Prompt]]|
	/ife (inputIsList == 'Yes') {:
		
	:}|
	/else {:
		/:"CMC Logic.GenerateWithPrompt"|
		/setvar key={{var::variableName}} {{getvar::output}}|
	:}|
	/addvar key=dataBaseNames {{var::variableName}}|
	/flushvar output|
	/flushvar guidance|
	/flushvar genOrder|
	/flushvar genContent|
	/flushvar genSettings|
:}|
/else {:
	/addvar key=dataBaseNames {{var::variableName}}|
:}|
//--------|


/findentry field=comment file="CMC Templates" "Aspiration Template"|
/getentryfield field=content file="CMC Templates" {{pipe}}|
/setvar key=parsedAspiration {{pipe}}|
/addvar key=dataBaseNames parsedAspiration|


//Unique Traits|
/var key=do No|
/var key=variableName "uniqueTraits"|
/ife ({{var::variableName}} == '') {:
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
:}|
/ife ( do == 'Yes' ) {:
	/setvar key=genSettings {}|
	/setvar key=genSettings index=wi_book_key "Unique Traits"|
	/setvar key=genSettings index=genIsList Yes|
	/setvar key=genSettings index=inputIsTaskList No|
	/setvar key=genSettings index=genIsSentence No|
	/setvar key=genSettings index=needOutput No|
	/setvar key=genSettings index=outputIsList Yes|
	/setvar key=genSettings index=useContext Yes|
	/setvar key=extra []|
	/addvar key=extra "- Intelligence Level: {{getvar::personalityIntelligenceLevel}}"|
	/addvar key=extra "- Social Behavior: {{getvar::personalitySocialBehavior}}"|
	/ife (personalitySocialSkills != 'None') {:
		/addvar key=extra "- Social Skills and Integration Into Society: {{getvar::personalitySocialSkills}}{{newline}}"|
	:}|
	/addvar key=extra "- Character Overview: {{getvar::characterOverview}}"|
	/setvar key=genSettings index=extraContext {{getvar::extra}}|
	/flushvar extra|
	/setvar key=genSettings index=contextKey []|
	/wait {{getvar::wait}}|
	
	/getvar key=genSettings index=inputIsList|
	/let key=inputIsList {{pipe}}|
	
	
	/ife (outputIsList == 'Yes') {:
		/setvar as=array key={{var::variableName}} []|
	:}|
	/else {:
		/setvar as=string key={{var::variableName}} {{noop}}|
	:}|
	//[[Generate with Prompt]]|
	/:"CMC Logic.GenerateWithPrompt"|
	/ife (output != '') {:
		/setvar key={{var::variableName}} {{getvar::output}}|
	:}|
	/addvar key=dataBaseNames {{var::variableName}}|
	/flushvar output|
	/flushvar guidance|
	/flushvar genOrder|
	/flushvar genContent|
	/flushvar genSettings|
:}|
/else {:
	/addvar key=dataBaseNames {{var::variableName}}|
:}|

/var key=do No|
/var key=variableName "uniqueTraitsEffects"|
/ife (uniqueTraits != 'None') {:
	/ife ({{var::variableName}} == '') {:
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
	:}|
	/ife ( do == 'Yes' ) {:
		/setvar key=genSettings {}|
		/setvar key=genSettings index=wi_book_key "Unique Traits Effects"|
		/setvar key=genSettings index=genIsList No|
		/setvar key=genSettings index=inputIsTaskList No|
		/setvar key=genSettings index=inputIsList Yes|
		/setvar key=genSettings index=genIsSentence Yes|
		/setvar key=genSettings index=needOutput Yes|
		/setvar key=genSettings index=useContext Yes|
		/setvar key=extra []|
		/addvar key=extra "{{getvar::parsedArchetype}}"|
		/ife (parsedAlignment != 'None') {:
			/addvar key=extra "{{newline}}{{getvar::parsedAlignment}}{{newline}}"|
		:}|
		/addvar key=extra "- Intelligence Level: {{getvar::personalityIntelligenceLevel}}"|
		/ife (personalitycognitiveAbilities != 'None') {:
			/addvar key=extra "- Cognitive Abilities: {{getvar::personalitycognitiveAbilities}}{{newline}}"|
		:}|
		/addvar key=extra "- Social Behavior: {{getvar::personalitySocialBehavior}}"|
		/ife (personalitySocialSkills != 'None') {:
			/addvar key=extra "- Social Skills and Integration Into Society: {{getvar::personalitySocialSkills}}{{newline}}"|
		:}|
		/addvar key=extra "{{newline}}{{getvar::parsedAspiration}}"|
		/addvar key=extra "- Character Overview: {{getvar::characterOverview}}"|
		/setvar key=genSettings index=extraContext {{getvar::extra}}|
		/flushvar extra|
		/setvar key=genSettings index=contextKey []|
		/wait {{getvar::wait}}|
		
		/getvar key=genSettings index=inputIsList|
		/let key=inputIsList {{pipe}}|
		/getvar key=genSettings index=inputIsList|
		/let key=outputIsList {{pipe}}|
		
		
		/ife (settingType == 'Realistic'){:
			/setvar key=logicBasedInstruction "7. Avoid supernatural, magical, or heroic-fantasy phrasing in goals. Focus on emotionally grounded, plausible actions."|
		:}|
		/else {:
			/setvar key=logicBasedInstruction "7. You may include exaggerated, symbolic, or physically extreme behaviors suited to the world context."|
		:}|
		
		
		/ife ((inputIsList== 'Yes') or (outputIsList == 'Yes')) {:
			/setvar as=array key={{var::variableName}} []|
		:}|
		/else {:
			/setvar as=string key={{var::variableName}} {{noop}}|
		:}|
		//[[Generate with Prompt]]|
		/ife (inputIsList == 'Yes') {:
			/foreach {{getvar::uniqueTraits}} {:
				/setvar key={{var::variableName}}Item {{var::item}}|
				/:"CMC Logic.GenerateWithPrompt"|
			/addvar key={{var::variableName}} {{getvar::output}}|
			/flushvar output|
			:}|
			/flushvar {{var::variableName}}Item|
		:}|
		/else {:
			/:"CMC Logic.GenerateWithPrompt"|
			/setvar key={{var::variableName}} {{getvar::output}}|
		:}|
		/addvar key=dataBaseNames {{var::variableName}}|
		/flushvar output|
		/flushvar guidance|
		/flushvar genOrder|
		/flushvar genContent|
		/flushvar genSettings|
	:}|
:}|
/else {:
	/setvar key={{var::variableName}} None|
	/addvar key=dataBaseNames {{var::variableName}}|
:}|
//--------|

/ife (uniqueTraits != 'None') {:
	/setvar key=parsedTraits []|
	/foreach {{getvar::uniqueTraits}} {:
		/let key=trait {{var::item}}|
		/getvar key=uniqueTraitsEffects index={{var::index}}|
		/let key=effect {{pipe}}|
		/findentry field=comment file="CMC Templates" "Unique Trait Template"|
		/getentryfield field=content file="CMC Templates" {{pipe}}|
		/re-replace find="/--UniqueTrait--/g" replace="{{var::item}}" {{pipe}}|
		/re-replace find="/--Effect--/g" replace="{{var::effect}}" {{pipe}}|
		/addvar key=parsedTraits {{pipe}}|
	:}|
	/join glue="{{newline}}{{newline}}" {{getvar::parsedTraits}}|
	/setvar key=parsedTraits {{pipe}}|
:}|
/else {:
	/setvar key=parsedTraits None|
:}|
/addvar key=dataBaseNames parsedTraits|


/:"CMC Logic.JEDParse"|

/:"CMC Logic.Save DataBase"|

/setvar key=stepDone Yes|
/qr-list CMC Main|
/getat index=1 {{pipe}}|
/var qrlabel {{pipe}}|
/qr-get set="CMC Main" label={{var::qrlabel}}|
/getat index="message" {{pipe}}|
/qr-update set="CMC Main" label={{var::qrlabel}} newlabel="Start Generating Speech Patterns" {{pipe}}|
/forcesave|