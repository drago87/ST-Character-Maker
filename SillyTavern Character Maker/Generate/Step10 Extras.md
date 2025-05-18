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


//Behavior Notes|



/ife (behaviorNotesList != '') {:
	/setvar key=behaviorNotes "{newline}}{newline}}- - -

## [BEHAVIOR_NOTES]
[IMPORTANT NOTE FOR AI: This section governs how --FirstName-- behaves moment to moment. In all interactions—especially intimate or emotionally charged scenes—adhere closely to the personality, social behavior, sexual role, and emotional boundaries established in this profile. Do not deviate from {{char}}’s defined orientation, role, or behavioral patterns unless a clear, in-character transformation is justified.]"|
	/foreach {{getvar::behaviorNotesList}} {:
		/addvar key=behaviorNotes "{{newline}}- {{var::item}}"|
	:}|
:}|
//--------|

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
	/setvar key=genSettings index=inputIsTaskList No|
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
		/getentryfield field=content file="CMC Information" {{var::wi_uid}}|
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
		:}|
		/flushvar {{var::variableName}}Item|
	:}|
	/else {:
		/:"CMC Logic.GenerateWithPrompt"|
		/setvar key={{var::variableName}} {{getvar::output}}|
	:}|
	/addvar key=dataBaseNames {{var::variableName}}|
	/flushvar output|
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