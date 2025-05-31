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




//Behavior Notes|



/var key=do No|
/var key=variableName "behaviorNotes"|
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
	/setvar key=genSettings index=wi_book_key "Behavior Notes"|
	/setvar key=genSettings index=genIsList No|
	/setvar key=genSettings index=genIsSentence Yes|
	/setvar key=genSettings index=needOutput No|
	/setvar key=genSettings index=outputIsList Yes|
	/setvar key=genSettings index=useContext Yes|
	/setvar key=extra []|
		/addvar key=extra "- Setting Type: {{getvar::settingType}}"|
		/addvar key=extra "- Backstory: {{getvar::backstory}}"|
		/ife (user == 'Yes') {:
			/addvar key=extra "- User's Role: {{getvar::userRole}}"|
		:}|
		/addvar key=extra "- Personality Tags: {{getvar::personalityFoundTags}}, {{getvar::personalityTags}}"|
		/ife (parsedAbilities != None) {:
			/addvar key=extra "{{newline}}**Abilities**{{newline}}{{getvar::parsedAbilities}}"|
		:}|
		/ife (parsedAbilities != None) {:
			/addvar key=extra "{{newline}}**Items or Gear**{{newline}}{{getvar::parsedItems}}"|
		:}|
		/setvar key=genSettings index=extraContext {{getvar::extra}}|
	/setvar key=extra []|
	/:"CMC Logic.Get Basic Type Context"|//Remove if not in use|
	/ife (extra != '') {:
		/setvar key=genSettings index=contextKey {{getvar::extra}}|
	:}|
	/flushvar extra|
	/wait {{getvar::wait}}|
	
	
	
	
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
	/ife (inputIsList == 'Yes') {:
		/foreach {{getvar::CHANGE/REMOVE_THIS}} {:
			/setvar key={{var::variableName}}Item {{var::item}}|
			/:"CMC Logic.GenerateWithPrompt"|
			/addvar key={{var::variableName}} {{getvar::output}}|
			/flushvar output|
			/flushvar guidance|
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
/else {:
	/addvar key=dataBaseNames {{var::variableName}}|
:}|

/ife (behaviorNotes != '') {:
	/setvar key=behaviorNotes "{newline}}{newline}}- - -

## [BEHAVIOR_NOTES]
[IMPORTANT NOTE FOR AI: This section governs how --FirstName-- behaves moment to moment. In all interactions—especially intimate or emotionally charged scenes—adhere closely to the personality, social behavior, sexual role, and emotional boundaries established in this profile. Do not deviate from {{char}}’s defined orientation, role, or behavioral patterns unless a clear, in-character transformation is justified.]"|
	/foreach {{getvar::behaviorNotesList}} {:
		/addvar key=behaviorNotes "{{newline}}- {{var::item}}"|
	:}|
:}|
//--------|


//Speech Examples|
/var key=do No|
/var key=variableName "speechExampleList"|
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
	/flushvar speechExample|
	/flushvar speechExampleList|
	/setvar key=genSettings index=wi_book_key "Speech Examples"|
	/setvar key=genSettings index=genIsList No|
	/setvar key=genSettings index=inputIsList Yes|
	/setvar key=genSettings index=genIsSentence Yes|
	/setvar key=genSettings index=needOutput Yes|
	/setvar key=genSettings index=outputIsList No|
	/setvar key=genSettings index=useContext Yes|
	/findentry field=comment file="CMC Variables" "Someone Random"|
	/let key=wi_uid {{pipe}}|
	/getentryfield field=content file="CMC Variables" {{var::wi_uid}}|
	/setvar key=genSettings index=random {{pipe}}|
	/setvar key=extra []|
	/addvar key=extra "- Speech Style: {{getvar::speechStyle}}"|
	/addvar key=extra "- Speech Quirks: {{getvar::speechQuirks}}"|
	/addvar key=extra "- Speech Tics: {{getvar::speechTics}}"|
	
	
	/addvar key=extra "- Personality Trait Tags: {{getvar::personalityFoundTags}}, {{getvar::personalityTags}}"|
	/ife (cognitiveAbilities != 'None') {:
		/addvar key=extra "- Cognitive Abilities: {{getvar::cognitiveAbilities}}{{newline}}"|
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
	/ife (qestions != '') {:
		/buttons labels=["Yes", "No"] Do you want to redo the situations?|
		/var key=selected_btn {{pipe}}|
		/ife ( selected_btn == ''){:
			/echo Aborting |
			/abort
		:}|
		/elseif ( selected_btn == 'Yes'){:
			/flushvar qestions|
		:}|
	:}|
	
	/ife (qestions == '') {: 
		/findentry field=comment file="CMC Questions" "Speech Situation: Q"|
		/let key=wi_uid {{pipe}}|
		/getentryfield field=content file="CMC Questions" {{var::wi_uid}}|
		/let key=unfilteredQuestions {{pipe}}|
		/split find="{{newline}}" {{var::unfilteredQuestions}}|
		/var key=unfilteredQuestions {{pipe}}|
	
	
		/setvar key=qestions []|
		/foreach {{var::unfilteredQuestions}} {:
			/ife (( user != 'Yes') and ('--User--' not in item)) or ( user == 'Yes') {:
				/buttons labels=["Yes", "No"] <div>Do you want to have this situation?</div><div>{{var::item}}</div><div>{target} will be randomized</div>|
				/let key=exp {{pipe}}|
				/ife ( exp == ''){:
					/echo Aborting |
					/abort
				:}|
				/elseif ( exp == 'Yes') {:
					/addvar key=qestions {{var::item}}|
				:}|
			:}| 
		:}|
	:}|
	/let key=stop Yes|
	/whilee (stop != 'No') {:
		/buttons labels=["Yes", "No"] Do you want to add another situation?|
		/var key=stop {{pipe}}|
		/ife ( stop == '') {:
			/echo Aborting |
			/abort
		:}|
		/ife ( stop == 'Yes') {:
			/input default="What would you do if " <div>What is the situation you want {{getvar::firstName}} to react to?</div><div>if you use '{target}' it will be randomized.</div><div>It will be a continuation of this sentence</div><div>What would you do if</div><div>How would you react if</div><div>What would you think if</div><div>What would you say if</div>|
			/let key=q {{pipe}}|
			/ife ( q == '') {:
				/echo Aborting |
				/abort
			:}|
			/addvar key=qestions {{var::q}}|
		:}|
	:}|
	
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
		/foreach {{getvar::qestions}} {:
			/setvar key=speechPromptClaim {{var::item}}|
			/:"CMC Logic.GenerateWithPrompt"|
			/addvar key={{var::variableName}} {{getvar::output}}|
			/flushvar output|
			/flushvar guidance|
		:}|
		/flushvar speechPromptClaim|
	:}|
	/else {:
		/:"CMC Logic.GenerateWithPrompt"|
		/setvar key={{var::variableName}} {{getvar::output}}|
	:}|
	/flushvar output|
	/flushvar guidance|
	/flushvar genOrder|
	/flushvar genContent|
	/flushvar genSettings|
	/flushvar qestions|
:}|
//--------|

/setvar key=speechExample []|
/ife (speechExampleList != '') {:
	/foreach {{getvar::speechExampleList}} {:
		/addvar key=speechExample "- {{var::item}}"|
	:}|
	/join glue="{{newline}}" {{getvar::speechExample}}|
	/setvar key=speechExampleString {{pipe}}|
:}|
/addvar key=dataBaseNames speechExampleString|
/flushvar speechExampleList|

/buttons multiple=true labels={{getvar::speechExample}} <div>Select what you want to use as the example speech for the following Q&A.</div>Reccomended 3-5|
/setvar key=parsedSpeechExamples {{pipe}}|
/join glue="{{newline}}" {{getvar::parsedSpeechExamples}}|
/setvar key=parsedSpeechExamples {{pipe}}|
/addvar key=dataBaseNames parsedSpeechExamples|

//Appearance QA|


/ife (AppearanceQAList != '') {:
	/setvar key=appearanceQA "{newline}}{newline}}<Q&A>"
	/foreach {{getvar::AppearanceQAList}} {:
		/addvar key=appearanceQA "{{newline}}{{var::item}}"|
	:}|
	/addvar key=appearanceQA "{newline}}</Q&A>"|
:}|
//--------|

//Personality Q&A|
/var key=do No|
/var key=variableName "personalityQAList"|
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
	/setvar key=genSettings index=wi_book_key "Personality QA"|
	/setvar key=genSettings index=genIsList No|
	/setvar key=genSettings index=inputIsList Yes|
	/setvar key=genSettings index=genIsSentence Yes|
	/setvar key=genSettings index=needOutput Yes|
	/setvar key=genSettings index=outputIsList No|
	/setvar key=genSettings index=useContext No|
	/setvar key=extra []|
	/addvar key=extra "{{newline}}{{getvar::parsedArchetype}}"|
	/ife (parsedAlignment != 'None') {:
		/addvar key=extra "{{newline}}{{getvar::parsedAlignment}}{{newline}}"|
	:}|
	/addvar key=extra "- Intelligence Level: {{getvar::intelligenceLevel}}"|
	/ife (cognitiveAbilities != 'None') {:
		/addvar key=extra "- Cognitive Abilities: {{getvar::cognitiveAbilities}}{{newline}}"|
	:}|
	/addvar key=extra "- Social Behavior: {{getvar::socialBehavior}}"|
	/ife (socialSkills != 'None') {:
		/addvar key=extra "- Social Skills and Integration Into Society: {{getvar::socialSkills}}{{newline}}"|
	:}|
	/addvar key=extra "{{newline}}{{getvar::parsedAspiration}}"|
	/setvar key=genSettings index=extraContext {{getvar::extra}}|
	/flushvar extra|
	/setvar key=genSettings index=contextKey []|
	/wait {{getvar::wait}}|
	
	
	/ife (qestions == '') {: 
		/findentry field=comment file="CMC Questions" "Personality: Q"|
		/let key=wi_uid {{pipe}}|
		/getentryfield field=content file="CMC Questions" {{var::wi_uid}}|
		/let key=unfilteredQuestions {{pipe}}|
		/split find="\n" {{var::unfilteredQuestions}}|
		/var key=unfilteredQuestions {{pipe}}|
	
	
		/setvar key=qestions []|
		/foreach {{var::unfilteredQuestions}} {:
			/ife (( user != 'Yes') and ('--User--' not in item)) or ( user == 'Yes') {:
				/buttons labels=["Yes", "No"] <div>Do you want to have this question?</div><div>{{var::item}}</div>|
				/let key=exp {{pipe}}|
				/ife ( exp == ''){:
					/echo Aborting |
					/abort
				:}|
				/elseif ( exp == 'Yes') {:
					/addvar key=qestions {{var::item}}|
				:}|
			:}| 
		:}|
	:}|
	/let key=stop Yes|
	/whilee (stop != 'Yes') {:
		/buttons labels=["Yes", "No"] Do you want to add another question?|
		/var key=stop {{pipe}}|
		/ife ( stop == '') {:
			/echo Aborting |
			/abort
		:}|
		/ife ( stop == 'Yes') {:
			/input What is the question you want {{getvar::firstName}} to answer?|
			/let key=q {{pipe}}|
			/ife ( q == '') {:
				/echo Aborting |
				/abort
			:}|
			/addvar key=qestions {{var::q}}|
		:}|
	:}|
	
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
		/foreach {{getvar::qestions}} {:
			/setvar key=question {{var::item}}|
			/:"CMC Logic.GenerateWithPrompt"|
			/addvar key={{var::variableName}} Q: {{getvar::question}}{{newline}}A: {{getvar::output}}|
			/flushvar output|
			/flushvar guidance|
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
/else {:
	/addvar key=dataBaseNames {{var::variableName}}|
:}|
//--------|


/ife (personalityQAList != '') {:
	/setvar key=personalityQA "{newline}}{newline}}<Q&A>{{newline}}"
	/join glue="{{newline}}{{newline}}" {{getvar::personalityQAList}}|
	/addvar key=personalityQA {{pipe}}|
	/addvar key=personalityQA "{newline}}</Q&A>"|
:}|

//Sexuality QA|


/ife (sexualityQAList != '') {:
	/setvar key=sexualityQA "{newline}}{newline}}<Q&A>{{newline}}"
	/join glue="{{newline}}{{newline}}" {{getvar::sexualityQAList}}|
	/addvar key=sexualityQA {{pipe}}|
	/addvar key=sexualityQA "{newline}}</Q&A>"|
:}|
//--------|

//Story Plan|

//--------|

//Previously|

//--------|

//Notes|
/var key=do No|
/var key=variableName "notes"|
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
	/setvar key=genSettings index=wi_book "CMC Rules"|
	/setvar key=genSettings index=combineLorebookEntries No|
	/setvar key=genSettings index=genIsSentence No|
	/setvar key=genSettings index=inputIsList No|
	/setvar key=genSettings index=genIsList Yes|
	/setvar key=genSettings index=outputIsList No|
	/setvar key=genSettings index=needOutput No|
	/setvar key=genSettings index=useContext No|
	/wait {{getvar::wait}}|
	
	
	/setvar key={{var::variableName}} []|
	
	/setvar key=genSettings index=wi_book_key "Narration Formatting Rule"|
	/setvar key=it "Narration Formatting Rule"|
	/setvar key=genSettings index=buttonPrompt "Select one — determines how the LLM structures output"|
	/:"CMC Logic.GenerateWithSelector"|
	/addvar key={{var::variableName}} {{getvar::output}}|
	
	/setvar key=genSettings index=wi_book_key "Narrative Tone Rule"|
	/setvar key=it "Narrative Tone Rule"|
	/setvar key=genSettings index=buttonPrompt "Select one — how expressive or reserved the model writes"|
	/:"CMC Logic.GenerateWithSelector"|
	/addvar key={{var::variableName}} {{getvar::output}}|
	
	/setvar key=genSettings index=wi_book_key "Perspective Rule"|
	/setvar key=it "Perspective Rule"|
	/setvar key=genSettings index=buttonPrompt "Select one — POV handling"|
	/:"CMC Logic.GenerateWithSelector"|
	/addvar key={{var::variableName}} {{getvar::output}}|
	
	/setvar key=genSettings index=wi_book_key ["Output Style Behavior"]|
	/setvar key=it "Output Style Behavior"|
	/setvar key=genSettings index=buttonPrompt "Select one or more — controls structure and generation behavior"|
	/:"CMC Logic.GenerateWithSelector"|
	/foreach {{getvar::output}} {:
		/addvar key={{var::variableName}} {{var::item}}|
	:}|
	
	/addvar key=dataBaseNames {{var::variableName}}|
	/flushvar output|
	/flushvar genOrder|
	/flushvar genContent|
	/flushvar it|
	/flushvar genSettings|
:}|
/else {:
	/addvar key=dataBaseNames {{var::variableName}}|
:}|
//--------|

//Synonyms|

//--------|

//Extra Characters|

//--------|




/*
/:"CMC Logic.JEDParse"|

/:"CMC Logic.Save DataBase"|

/setvar key=stepDone Yes|
/qr-list CMC Main|
/getat index=1 {{pipe}}|
/var qrlabel {{pipe}}|
/qr-get set="CMC Main" label={{var::qrlabel}}|
/getat index="message" {{pipe}}|
/qr-update set="CMC Main" label={{var::qrlabel}} newlabel="Start Exporting" {{pipe}}|
*|