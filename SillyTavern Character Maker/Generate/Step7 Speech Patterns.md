/qr-list CMC Main|
/getat index=1 {{pipe}}|
/let qrlabel {{pipe}}|
/qr-get set="CMC Main" label={{var::qrlabel}}|
/getat index="message" {{pipe}}|
/qr-update set="CMC Main" label={{var::qrlabel}} newlabel="Continue Generating Speech Patterns" {{pipe}}|

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

/setvar key=randomTags {{getvar::personalityFoundTags}}, {{getvar::personalityTags}}|
/split {{getvar::randomTags}}|
/setvar key=randomTags {{pipe}}|

//Speech Style|
/var key=do No|
/var key=variableName "speechStyle"|
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
	/setvar key=genSettings index=wi_book_key "Speech Style"|
	/setvar key=genSettings index=genIsList No|
	
	/setvar key=genSettings index=genIsSentence Yes|
	/setvar key=genSettings index=needOutput Yes|
	/setvar key=genSettings index=outputIsList No|
	/setvar key=genSettings index=useContext Yes|
	/setvar key=extra []|
	/addvar key=extra "- Personality Trait Tags: {{getvar::personalityFoundTags}}, {{getvar::personalityTags}}"|
	/addvar key=extra "- Intelligence Level: {{getvar::personalityIntelligenceLevel}}"|
	/ife (personalitycognitiveAbilities != 'None') {:
		/addvar key=extra "- Cognitive Abilities: {{getvar::personalitycognitiveAbilities}}"|
	:}|
	/ife (personalitySocialSkills != 'None') {:
		/addvar key=extra "- Social Skills and Integration Into Society: {{getvar::personalitySocialSkills}}"|
	:}|
	/ife (personalitySocialBehavior != 'Normal') {:
		/addvar key=extra "- Social Behavior: {{getvar::personalitySocialBehavior}}"|
	:}|
	/addvar key=extra "- Time Period: {{getvar::timePeriod}}"|
	/addvar key=extra "- Setting Type: {{getvar::settingType}}"|
	/addvar key=extra "- Backstory: {{getvar::backstory}}"|
	/setvar key=genSettings index=extraContext {{getvar::extra}}|
	/setvar key=extra []|
	/:"CMC Logic.Get Basic Type Context"|//Remove if not in use|
	/ife (extra != '') {:
		/setvar key=genSettings index=contextKey {{getvar::extra}}|
	:}|
	/flushvar extra|
	/wait {{getvar::wait}}|
	
	/ife (settingType == 'Realistic'){:
			/setvar key=logicBasedInstruction "6. Avoid anachronistic or fantastical speech patterns — stay grounded in the character's setting and time period."|
		:}|
		/else {:
			/setvar key=logicBasedInstruction "6. You may include stylized, thematic, or exaggerated phrasing appropriate for the world’s tone or genre."|
		:}|
	
	/getvar key=genSettings index=inputIsList|
	/let key=inputIsList {{pipe}}|
	/getvar key=genSettings index=inputIsList|
	/let key=outputIsList {{pipe}}|
	
	
	/ife ((inputIsList == 'Yes') or (outputIsList == 'Yes')) {:
		/setvar as=array key={{var::variableName}} []|
	:}|
	/else {:
		/setvar as=string key={{var::variableName}} {{noop}}|
	:}|
	//[[Generate with Prompt]]|
	/:"CMC Logic.GenerateWithPrompt"|
	/setvar key={{var::variableName}} {{getvar::output}}|
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

//Speech Quirks|
/var key=do No|
/var key=variableName "speechQuirks"|
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
	/setvar key=genSettings index=wi_book_key "Speech Quirks"|
	/setvar key=genSettings index=genIsList No|
	
	/setvar key=genSettings index=genIsSentence Yes|
	/setvar key=genSettings index=needOutput Yes|
	/setvar key=genSettings index=outputIsList No|
	/setvar key=genSettings index=useContext Yes|
	/setvar key=extra []|
	/addvar key=extra "- Main Personality Trait: {{getvar::personalityMainTrait}}"| 
	/addvar key=extra "{{getvar::parsedArchetype}}"|
	/addvar key=extra "- Personality Trait Tags: {{getvar::personalityFoundTags}}, {{getvar::personalityTags}}"|
	/addvar key=extra "- Intelligence Level: {{getvar::personalityIntelligenceLevel}}"|
	/ife (personalitycognitiveAbilities != 'None') {:
		/addvar key=extra "- Cognitive Abilities: {{getvar::personalitycognitiveAbilities}}"|
	:}|
	/ife (personalitySocialSkills != 'None') {:
		/addvar key=extra "- Social Skills and Integration Into Society: {{getvar::personalitySocialSkills}}"|
	:}|
	/addvar key=extra "- Social Behavior: {{getvar::personalitySocialBehavior}}"|
	/addvar key=extra "- Time Period: {{getvar::timePeriod}}"|
	/addvar key=extra "- Setting Type: {{getvar::settingType}}"|
	/addvar key=extra "- Backstory: {{getvar::backstory}}"|
	/setvar key=genSettings index=extraContext {{getvar::extra}}|
	/setvar key=extra []|
	/:"CMC Logic.Get Basic Type Context"|//Remove if not in use|
	/ife (extra != '') {:
		/setvar key=genSettings index=contextKey {{getvar::extra}}|
	:}|
	/flushvar extra|
	/wait {{getvar::wait}}|
	
	/ife (settingType == 'Realistic'){:
			/setvar key=logicBasedInstruction "8. Avoid overly fantastical, magical, or exaggerated quirks unless justified by culture, trauma, or setting norms."|
		:}|
		/else {:
			/setvar key=logicBasedInstruction "8. You may include symbolic, magical, or genre-specific quirks if they suit the character’s archetype and setting."|
		:}|
	
	/getvar key=genSettings index=inputIsList|
	/let key=inputIsList {{pipe}}|
	/getvar key=genSettings index=inputIsList|
	/let key=outputIsList {{pipe}}|
	
	
	/ife ((inputIsList == 'Yes') or (outputIsList == 'Yes')) {:
		/setvar as=array key={{var::variableName}} []|
	:}|
	/else {:
		/setvar as=string key={{var::variableName}} {{noop}}|
	:}|
	//[[Generate with Prompt]]|
	/:"CMC Logic.GenerateWithPrompt"|
	/setvar key={{var::variableName}} {{getvar::output}}|
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

//Speech Tics|
/var key=do No|
/var key=variableName "speechSingleTics"|
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
	/setvar key=genSettings index=wi_book_key "Speech Single Ticks"|
	/setvar key=genSettings index=genIsList No|
	/setvar key=genSettings index=genIsSentence Yes|
	/setvar key=genSettings index=needOutput Yes|
	/setvar key=genSettings index=outputIsList Yes|
	/setvar key=genSettings index=maxSizeOfList 2|
	/setvar key=genSettings index=useContext Yes|
	/setvar key=genSettings index=random {{getvar::randomTags}}|
	/setvar key=extra []|
	/addvar key=extra "- Main Personality Trait: {{getvar::personalityMainTrait}}"| 
	//addvar key=extra "{{getvar::parsedArchetype}}"|
	//addvar key=extra "- Personality Trait Tags: {{getvar::personalityFoundTags}}, {{getvar::personalityTags}}"|
	/addvar key=extra "- Intelligence Level: {{getvar::personalityIntelligenceLevel}}"|
	/ife (personalitycognitiveAbilities != 'None') {:
		/addvar key=extra "- Cognitive Abilities: {{getvar::personalitycognitiveAbilities}}"|
	:}|
	/ife (personalitySocialSkills != 'None') {:
		/addvar key=extra "- Social Skills and Integration Into Society: {{getvar::personalitySocialSkills}}"|
	:}|
	/addvar key=extra "- Social Behavior: {{getvar::personalitySocialBehavior}}"|
	/addvar key=extra "- Time Period: {{getvar::timePeriod}}"|
	/addvar key=extra "- Setting Type: {{getvar::settingType}}"|
	//addvar key=extra "- Backstory: {{getvar::backstory}}"|
	/setvar key=genSettings index=extraContext {{getvar::extra}}|
	/setvar key=extra []|
	/:"CMC Logic.Get Basic Type Context"|//Remove if not in use|
	/ife (extra != '') {:
		/setvar key=genSettings index=contextKey {{getvar::extra}}|
	:}|
	/flushvar extra|
	/wait {{getvar::wait}}|
	
	/ife (settingType == 'Realistic'){:
		/setvar key=logicBasedInstruction "7. Avoid magical, theatrical, or exaggerated genre behaviors unless clearly tied to species or neurodivergence."|
	:}|
	/else {:
		/setvar key=logicBasedInstruction "7. Stylized or dramatic tics are allowed if appropriate to the character’s world or design (e.g., glitch-speech, echoing, verbal echoes from magic)."|
	:}|
		
	
	/getvar key=genSettings index=inputIsList|
	/let key=inputIsList {{pipe}}|
	/getvar key=genSettings index=inputIsList|
	/let key=outputIsList {{pipe}}|
	
	
	/ife ((inputIsList == 'Yes') or (outputIsList == 'Yes')) {:
		/setvar as=array key={{var::variableName}} []|
	:}|
	/else {:
		/setvar as=string key={{var::variableName}} {{noop}}|
	:}|
	//[[Generate with Prompt]]|
	/:"CMC Logic.GenerateWithPrompt"|
	/setvar key={{var::variableName}} {{getvar::output}}|
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
/var key=variableName "speechTics"|
/len {{getvar::speechSingleTics}}|
/let key=len {{pipe}}|
/ife (len == 2) {:
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
		/setvar key=genSettings index=wi_book_key "Speech Tics"|
		/setvar key=genSettings index=genIsList No|
		/setvar key=genSettings index=genIsSentence No|
		/setvar key=genSettings index=needOutput Yes|
		/setvar key=genSettings index=outputIsList No|
		/setvar key=genSettings index=useContext No|
		/setvar key=extra []|
		/ife (extra != '') {:
			/setvar key=genSettings index=contextKey {{getvar::extra}}|
		:}|
		/flushvar extra|
		/wait {{getvar::wait}}|
		
		/getvar key=genSettings index=inputIsList|
		/let key=inputIsList {{pipe}}|
		/getvar key=genSettings index=inputIsList|
		/let key=outputIsList {{pipe}}|
		
		/setvar key=i 1|
		/foreach {{getvar::speechSingleTics}} {:
			/setvar key=tic{{getvar::i}} {{var::item}}|
			/incvar i|
			/setvar key=i {{pipe}}|
		:}|
		/flushvar i|
		
		
		/ife ((inputIsList == 'Yes') or (outputIsList == 'Yes')) {:
			/setvar as=array key={{var::variableName}} []|
		:}|
		/else {:
			/setvar as=string key={{var::variableName}} {{noop}}|
		:}|
		//[[Generate with Prompt]]|
		/:"CMC Logic.GenerateWithPrompt"|
		/setvar key={{var::variableName}} {{getvar::output}}|
		/addvar key=dataBaseNames {{var::variableName}}|
		/flushvar output|
		/flushvar guidance|
		/flushvar genOrder|
		/flushvar genContent|
		/flushvar genSettings|
		/flushvar tic1|
		/flushvar tic2|
	:}|
	/else {:
		/addvar key=dataBaseNames {{var::variableName}}|
	:}|
	
:}|
/else {:
	/getvar key=speechSingleTics index=0|
	/setvar key={{var::variableName}} {{pipe}}|
	/addvar key=dataBaseNames {{var::variableName}}|
:}|
//--------|



/flushvar randomTags|


/:"CMC Logic.JEDParse"|

/:"CMC Logic.Save DataBase"|

/setvar key=stepDone Yes|
/qr-list CMC Main|
/getat index=1 {{pipe}}|
/var qrlabel {{pipe}}|
/qr-get set="CMC Main" label={{var::qrlabel}}|
/getat index="message" {{pipe}}|
/qr-update set="CMC Main" label={{var::qrlabel}} newlabel="Start Generating Aspirational & Unique Traits" {{pipe}}|
/forcesave|