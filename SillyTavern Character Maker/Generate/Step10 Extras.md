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
    /ife (do == 'Yes') {:
	    /flushvar {{getvar::variableName}}|
    :}|
:}|
/ife ( do == 'Yes' ) {:
	/setvar key=genSettings {}|
	/setvar key=genSettings index=wi_book "CMC Rules"|
	
	/setvar key=genSettings index=combineLorebookEntries No|
	/setvar key=genSettings index=genIsSentence No|
	/setvar key=genSettings index=inputIsList No|
	/setvar key=genSettings index=genIsList Yes|
	/setvar key=genSettings index=outputIsList No|
	/setvar key=genSettings index=needOutput No|
	/setvar key=genSettings index=useContext No|
	/wait {{getvar::wait}}|
	
	
	/getvar key=genSettings index=wi_book_key|
	/let key=wi_book_key {{pipe}}|
	/getvar key=genSettings index=inputIsList|
	/let key=inputIsList {{pipe}}|
	/getvar key=genSettings index=combineLorebookEntries|
	/let key=combineLorebookEntries {{pipe}}|
	/len {{getvar::behaviorNotes}}|
	/var key=len {{pipe}}|
	
	/ife ( len == 0) {:
		/setvar key={{var::variableName}} []|
		/setvar key=genSettings index=wi_book_key "Emotional Responsiveness"|
		/setvar key=genSettings index=buttonPrompt "Select the Emotional Responsiveness you want {{getvar::firstName}} to follow."|
		/setvar key=it Behavior Rules|
		/:"CMC Logic.GenerateWithSelector"|
		/addvar key={{var::variableName}} "**Emotional Responsiveness:** {{getvar::output}}"|
	:}|
	/len {{getvar::behaviorNotes}}|
	/var key=len {{pipe}}|
	/ife ( len == 1) {:
		/setvar key=genSettings index=wi_book_key "Conflict Handling"|
		/setvar key=genSettings index=buttonPrompt "Select the Conflict Handling you want {{getvar::firstName}} to follow."|
		/setvar key=it Behavior Rules|
		/:"CMC Logic.GenerateWithSelector"|
		/addvar key={{var::variableName}} "**Conflict Handling:** {{getvar::output}}"|
	:}|
	/len {{getvar::behaviorNotes}}|
	/var key=len {{pipe}}|
	/ife ( len == 2) {:
		/setvar key=genSettings index=wi_book_key "Social Openness"|
		/setvar key=genSettings index=buttonPrompt "Select the Social Openness you want {{getvar::firstName}} to follow."|
		/setvar key=it Behavior Rules|
		/:"CMC Logic.GenerateWithSelector"|
		/addvar key={{var::variableName}} "**Social Openness:** {{getvar::output}}"|
	:}|
	/len {{getvar::behaviorNotes}}|
	/var key=len {{pipe}}|
	/ife ( len == 3) {:
		/setvar key=genSettings index=wi_book_key "Empathy Attunement"|
		/setvar key=genSettings index=buttonPrompt "Select the Empathy & Attunement you want {{getvar::firstName}} to follow."|
		/setvar key=it Behavior Rules|
		/:"CMC Logic.GenerateWithSelector"|
		/addvar key={{var::variableName}} "**Empathy & Attunement:** {{getvar::output}}"|
	:}|
	/len {{getvar::behaviorNotes}}|
	/var key=len {{pipe}}|
	/ife ( len == 4) {:
		/setvar key=genSettings index=wi_book_key "Verbal Style Communication"|
		/setvar key=genSettings index=buttonPrompt "Select the Verbal Style / Communication you want {{getvar::firstName}} to follow."|
		/setvar key=it Behavior Rules|
		/:"CMC Logic.GenerateWithSelector"|
		/addvar key={{var::variableName}} "**Verbal Style / Communication:** {{getvar::output}}"|
	:}|
	/len {{getvar::behaviorNotes}}|
	/var key=len {{pipe}}|
	/ife ( len == 5) {:
		/setvar key=genSettings index=wi_book_key "Physical Expressiveness"|
		/setvar key=genSettings index=buttonPrompt "Select the Physical Expressiveness you want {{getvar::firstName}} to follow."|
		/setvar key=it Behavior Rules|
		/:"CMC Logic.GenerateWithSelector"|
		/addvar key={{var::variableName}} "**Physical Expressiveness:** {{getvar::output}}"|
	:}|
	/len {{getvar::behaviorNotes}}|
	/var key=len {{pipe}}|
	/ife ( len >= 6) {:
	/var key=do No|
		/buttons labels=["Yes", "No"] Do you want to generate or add more behavior Rules?|
		/var key=do {{pipe}}|
		/ife (do == '') {:
			/echo Aborting |
			/abort
		:}|
		/ife (do == 'Yes') {:
			/setvar key=genSettings {}|
			/setvar key=genSettings index=wi_book "CMC Generation Prompts"|
			/setvar key=genSettings index=genIsSentence Yes|
			/setvar key=genSettings index=outputIsList Yes|
			/setvar key=genSettings index=needOutput No|
			/setvar key=genSettings index=useContext Yes|
			/setvar key=extra []|
			/addvar key=extra "- Main Personality Trait: {{getvar::personalityMainTrait}}"|
			/addvar key=extra "- Personality Tags: {{getvar::personalityFoundTags}}, {{getvar::personalityTags}}"|
			/setvar key=genSettings index=extraContext {{getvar::extra}}|
			/setvar key=extra []|
			/:"CMC Logic.Get Basic Type Context"|
			/ife (extra != '') {:
				/setvar key=genSettings index=contextKey {{getvar::extra}}|
			:}|
			/flushvar extra|
			/setvar key=genSettings index=wi_book_key "Behavior Notes"|
			/setvar key=genSettings index=buttonPrompt "Is this a good behavior rule you want {{getvar::firstName}} to follow?"|
			/setvar key=it Behavior Rules|
			/:"CMC Logic.GenerateWithPrompt"|
			/foreach {{getvar::output}} {:
				/addvar key={{var::variableName}} "{{var::output}}"|
			:}|
		:}|
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

/setvar key=parsedBehaviorNotes {{noop}}|
/ife (behaviorNotes != '') {:
	/foreach {{getvar::behaviorNotes}} {:
		/ife ( index > 0) {:
			/addvar key=parsedBehaviorNotes "{{newline}}"|
		:}|
		/addvar key=parsedBehaviorNotes "- {{var::item}}"|
	:}|
:}|
/else {:
	/setvar key=parsedBehaviorNotes None|
:}
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
    /ife (do == 'Yes') {:
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
	
	
	/ife ((inputIsList== 'Yes') or (outputIsList == 'Yes')) {:
		/setvar as=array key={{var::variableName}} []|
	:}|
	/else {:
		/setvar as=string key={{var::variableName}} {{noop}}|
	:}|
	//[[Generate with Prompt]]|
	/ife (inputIsList == 'Yes') {:
		/foreach {{getvar::speechQuestions}} {:
			/setvar key=speechPromptClaim {{var::item}}|
			/:"CMC Logic.GenerateWithPrompt"|
			/ife ((output != '') and (output != 'None')) {:
				/re-replace find="/^\"/g" replace="" {{getvar::output}}|
				/re-replace find="/\"$/g" replace="" {{pipe}}|
				/addvar key={{var::variableName}} "\"{{pipe}}\""|
			:}|
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
	/flushvar speechQuestions|
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


//Appearance QA|
/var key=do No|
/var key=variableName "appearanceQAList"|
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
    /ife (do == 'Yes') {:
	    /flushvar {{getvar::variableName}}|
    :}|
:}|
/ife ( do == 'Yes' ) {:
	/setvar key=genSettings {}|
	/setvar key=genSettings index=wi_book_key "Appearance QA"|
	/setvar key=genSettings index=genIsList No|
	/setvar key=genSettings index=inputIsList Yes|
	/setvar key=genSettings index=genIsSentence Yes|
	/setvar key=genSettings index=needOutput Yes|
	/setvar key=genSettings index=outputIsList No|
	/setvar key=genSettings index=useContext No|
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
	
	/addvar key=extra "{{newline}}**Appearance**{{newline}}- Facial Features: {{getvar::appearanceFace}}"|
	/addvar key=extra "- Eye Description: {{getvar::appearanceEyes}}"|
	/addvar key=extra "- Hair Style: {{getvar::appearanceHair}}"|
	/addvar key=extra "- Body Shape: {{getvar::appearanceBody}}"|
	/ife (appearanceFeatures != 'None') {:
		/addvar key=extra "- Distinctive Features: {{getvar::appearanceFeatures}}"|
	:}|
	/ife (appearanceBreasts != 'None') {:
		/addvar key=extra "- Breast Description: {{getvar::appearanceBreasts}}"|
	:}|
	
	/ife (appearanceNipples != 'None') {:
		/addvar key=extra "- Nipple Description: {{getvar::appearanceNipples}}"|
	:}|
	/ife (appearanceGenitals != 'None') {:
		/addvar key=extra "- Genital Description: {{getvar::appearanceGenitals}}"|
	:}|
	/elseif (appearancePussy != 'None') {:
		/addvar key=extra "- Genital Description: {{getvar::appearancePussy}}"|
	:}|
	/elseif (appearanceCock != 'None') {:
		/addvar key=extra "- Genital Description: {{getvar::appearanceCock}}"|
	:}|
	/addvar key=extra "- Anus Appearance: {{getvar::appearanceAnus}}"|
	/ife (parsedAppearanceTraits != 'None') {:
		/addvar key=extra "- Appearance Traits information: {{getvar::parsedAppearanceTraits}}"|
	:}|
	/setvar key=genSettings index=extraContext {{getvar::extra}}|
	/flushvar extra|
	/setvar key=genSettings index=contextKey []|
	/wait {{getvar::wait}}|
	/ife ((appearanceQuestions is list) and (appearanceQuestions != '')) {:
		/buttons labels=["Yes", "No"] <div>Appearance Questions</div><div>Do you want to redo the static apperance questions?</div>|
		/var key=selected_btn {{pipe}}|
		/ife ( selected_btn == ''){:
			/echo Aborting |
			/abort
		:}|
		/elseif ( selected_btn == 'Yes'){:
			/flushvar appearanceQuestions|
		:}|
	:}|
	/else {:
		/setvar key=appearanceQuestions []|
	:}|
	
	/ife (appearanceQuestions == '') {: 
		/findentry field=comment file="CMC Questions" "Appearance: Q"|
		/let key=wi_uid {{pipe}}|
		/getentryfield field=content file="CMC Questions" {{var::wi_uid}}|
		/let key=unfilteredQuestions {{pipe}}|
		
		/split find="{{newline}}" {{var::unfilteredQuestions}}|
		/var key=unfilteredQuestions {{pipe}}|
		/let key=pop {{noop}}|
		/foreach {{var::unfilteredQuestions}} {:
			/var key=pop {{var::pop}}<div>{{var::item}}</div>| 
		:}|
		/popup wide=true okButton="Continue" <div>Here is the questions you have to choose from during generation. {taget} is going to get randomised each time you redo the generation.<div></div>You will also be able to add your own.</div>{{var::pop}}|
		/let key=filteredQuestions []|
		/foreach {{var::unfilteredQuestions}} {:
			/ife (( user != 'Yes') and ('--User--' not in item)) or ( user == 'Yes') {:
				/var key=filteredQuestions index={{var::index}} {{var::item}}|
			:}| 
		:}|
		/buttons labels={{var::filteredQuestions}} multiple=true Choose questions or prompts that will help define how {{getvar::firstName}} thinks about {{getvar::reflexivePronoun}}.|
		/setvar key=appearanceQuestions {{pipe}}|
		/ife (appearanceQuestions == '') {:
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
			/input default="What do you think about your " 
<div>What question or opinion do you want {{getvar::firstName}} to respond to about {{getvar::possAdjPronoun}} body or looks?</div>
<div style="text-align: center;">
  <p>Your input will be used to complete a question like one of these:</p>
  <div>
    <div>How do you feel about your appearance?</div>
    <div>Is there something you like or dislike about how you look?</div>
    <div>What do you think people notice first about you?</div>
    <div>Have you ever been complimented on something specific?</div>
    <div>If someone teased you about your looks, how would you react?</div>
  </div>
</div>|
			/let key=q {{pipe}}|
			/ife ( q == '') {:
				/echo Aborting |
				/abort
			:}|
			/addvar key=appearanceQuestions {{var::q}}|
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
		/foreach {{getvar::appearanceQuestions}} {:
			/setvar key=question {{var::item}}|
			/:"CMC Logic.GenerateWithPrompt"|
			/ife ((output != '') and (output != 'None')) {:
				/re-replace find="/^\"/g" replace="" {{getvar::output}}|
				/re-replace find="/\"$/g" replace="" {{pipe}}|
				/addvar key={{var::variableName}} "Q: \"{{getvar::question}}\"{{newline}}A: \"{{pipe}}\""|
			:}|
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

/ife (appearanceQAList != '') {:
	/setvar key=appearanceQA {{noop}}|
	/foreach {{getvar::appearanceQAList}} {:
		/addvar key=appearanceQA "{{newline}}{{var::item}}"|
	:}|
:}|
/addvar key=dataBaseNames appearanceQA|
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
    /ife (do == 'Yes') {:
	    /flushvar {{getvar::variableName}}|
    :}|
:}|
/ife ( do == 'Yes' ) {:
	/setvar key=genSettings {}|
	/setvar key=genSettings index=wi_book_key "Personality QA"|
	/setvar key=genSettings index=genIsList No|
	/setvar key=genSettings index=inputIsList Yes|
	/setvar key=genSettings index=genIsSentence Yes|
	/setvar key=genSettings index=needOutput Yes|
	/setvar key=genSettings index=outputIsList No|
	/setvar key=genSettings index=useContext No|
	/setvar key=extra []|
	/addvar key=extra "- Main Personality Trait: {{getvar::personalityMainTrait}}"| 
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
	/setvar key=genSettings index=extraContext {{getvar::extra}}|
	/flushvar extra|
	/setvar key=genSettings index=contextKey []|
	/wait {{getvar::wait}}|
	/ife ((personalityQuestions is list) and (personalityQuestions != '')) {:
		/buttons labels=["Yes", "No"] <div>Personality Questions</div><div>Do you want to redo the static personality questions?</div>|
		/var key=selected_btn {{pipe}}|
		/ife ( selected_btn == ''){:
			/echo Aborting |
			/abort
		:}|
		/elseif ( selected_btn == 'Yes'){:
			/flushvar personalityQuestions|
		:}|
	:}|
	/else {:
		/setvar key=personalityQuestions []|
	:}|
	
	/ife (personalityQuestions == '') {: 
		/findentry field=comment file="CMC Questions" "Personality: Q"|
		/let key=wi_uid {{pipe}}|
		/getentryfield field=content file="CMC Questions" {{var::wi_uid}}|
		/let key=unfilteredQuestions {{pipe}}|
		
		/split find="{{newline}}" {{var::unfilteredQuestions}}|
		/var key=unfilteredQuestions {{pipe}}|
		/let key=pop {{noop}}|
		/foreach {{var::unfilteredQuestions}} {:
			/var key=pop {{var::pop}}<div>{{var::item}}</div>| 
		:}|
		/popup wide=true okButton="Continue" <div>Here is the questions you have to choose from during generation. {taget} is going to get randomised each time you redo the generation.<div></div>You will also be able to add your own.</div>{{var::pop}}|
		/let key=filteredQuestions []|
		/foreach {{var::unfilteredQuestions}} {:
			/ife (( user != 'Yes') and ('--User--' not in item)) or ( user == 'Yes') {:
				/var key=filteredQuestions index={{var::index}} {{var::item}}|
			:}| 
		:}|
		/buttons labels={{var::filteredQuestions}} multiple=true Choose questions or prompts that will help define how {{getvar::firstName}} thinks about {{getvar::reflexivePronoun}}.|
		/setvar key=personalityQuestions {{pipe}}|
		/ife (personalityQuestions == '') {:
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
			/input default="What do you do " 
<div>What kind of personality question or situation do you want {{getvar::firstName}} to respond to?</div>
<div style="text-align: center;">
  <p>Your input will be used to complete a question like one of these:</p>
  <div>
    <div>What do you do when you're under pressure?</div>
    <div>How do you feel about people who challenge you?</div>
    <div>Do you think people actually understand you?</div>
    <div>Is there a part of your personality you try to hide?</div>
    <div>How do you act when you're alone versus in a group?</div>
  </div>
</div>|
			/let key=q {{pipe}}|
			/ife ( q == '') {:
				/echo Aborting |
				/abort
			:}|
			/addvar key=personalityQuestions {{var::q}}|
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
		/foreach {{getvar::personalityQuestions}} {:
			/setvar key=question {{var::item}}|
			/:"CMC Logic.GenerateWithPrompt"|
			/ife ((output != '') and (output != 'None')) {:
				/re-replace find="/^\"/g" replace="" {{getvar::output}}|
				/re-replace find="/\"$/g" replace="" {{pipe}}|
				/addvar key={{var::variableName}} "Q: \"{{getvar::question}}\"{{newline}}A: \"{{pipe}}\""|
			:}|
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
	/setvar key=personalityQA {{noop}}|
	/join glue="{{newline}}{{newline}}" {{getvar::personalityQAList}}|
	/addvar key=personalityQA {{pipe}}|
:}|
/addvar key=dataBaseNames personalityQA|

//Sexuality QA|
/var key=do No|
/var key=variableName "sexualityQAList"|
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
    /ife (do == 'Yes') {:
	    /flushvar {{getvar::variableName}}|
    :}|
:}|
/ife ( do == 'Yes' ) {:
	/setvar key=genSettings {}|
	/setvar key=genSettings index=wi_book_key "Sexuality QA"|
	/setvar key=genSettings index=genIsList No|
	/setvar key=genSettings index=inputIsList Yes|
	/setvar key=genSettings index=genIsSentence Yes|
	/setvar key=genSettings index=needOutput Yes|
	/setvar key=genSettings index=outputIsList No|
	/setvar key=genSettings index=useContext No|
	/setvar key=extra []|
	/addvar key=extra "- Main Personality Trait: {{getvar::personalityMainTrait}}"| 
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
	/addvar key=extra "{{newline}}{{getvar::parsedSexualOrientation}}"|
	/addvar key=extra "{{getvar::parsedSexualRole}}"|
	/addvar key=extra "- Libido: {{getvar::sexualLibido}}"|
	/ife (parsedSexualKinks != 'None') {:
		/addvar key=extra "{{getvar::parsedSexualKinks}}"|
	:}|
	/ife (parsedSexualItems != 'None') {:
		/addvar key=extra "{{getvar::parsedSexualItems}}"|
	:}|
	/ife (parsedSexualAblilities != 'None') {:
		/addvar key=extra "{{getvar::parsedSexualAblilities}}"|
	:}|
	/setvar key=genSettings index=extraContext {{getvar::extra}}|
	/flushvar extra|
	/setvar key=genSettings index=contextKey []|
	/wait {{getvar::wait}}|
	/ife ((sexualityQuestions is list) and (sexualityQuestions != '')) {:
		/buttons labels=["Yes", "No"] <div>Personality Questions</div><div>Do you want to redo the static sexuality questions?</div>|
		/var key=selected_btn {{pipe}}|
		/ife ( selected_btn == ''){:
			/echo Aborting |
			/abort
		:}|
		/elseif ( selected_btn == 'Yes'){:
			/flushvar sexualityQuestions|
		:}|
	:}|
	/else {:
		/setvar key=sexualityQuestions []|
	:}|
	
	/ife (sexualityQuestions == '') {: 
		/findentry field=comment file="CMC Questions" "Sexuality: Q"|
		/let key=wi_uid {{pipe}}|
		/getentryfield field=content file="CMC Questions" {{var::wi_uid}}|
		/let key=unfilteredQuestions {{pipe}}|
		
		/split find="{{newline}}" {{var::unfilteredQuestions}}|
		/var key=unfilteredQuestions {{pipe}}|
		/let key=pop {{noop}}|
		/foreach {{var::unfilteredQuestions}} {:
			/var key=pop {{var::pop}}<div>{{var::item}}</div>| 
		:}|
		/popup wide=true okButton="Continue" <div>Here is the questions you have to choose from during generation. {taget} is going to get randomised each time you redo the generation.<div></div>You will also be able to add your own.</div>{{var::pop}}|
		/let key=filteredQuestions []|
		/foreach {{var::unfilteredQuestions}} {:
			/ife (( user != 'Yes') and ('--User--' not in item)) or ( user == 'Yes') {:
				/var key=filteredQuestions index={{var::index}} {{var::item}}|
			:}| 
		:}|
		/buttons labels={{var::filteredQuestions}} multiple=true Choose questions or prompts that will help define how {{getvar::firstName}} thinks about sex and NSFW stuff.|
		/setvar key=sexualityQuestions {{pipe}}|
		/ife (sexualityQuestions == '') {:
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
			/input default="Would you try " 
<div>What intimate or NSFW question do you want {{getvar::firstName}} to answer or react to?</div>
<div style="text-align: center;">
  <p>Your input will be used to complete a question like one of these:</p>
  <div>
    <div>What do you really think about sex?</div>
    <div>Do you like being in control — or taken over?</div>
    <div>What turns you on, even if you don’t like admitting it?</div>
    <div>Would you ever flirt first — even with --User--?</div>
    <div>Have you ever felt ashamed or proud after sex?</div>
  </div>
</div>
|
			/let key=q {{pipe}}|
			/ife ( q == '') {:
				/echo Aborting |
				/abort
			:}|
			/addvar key=sexualityQuestions {{var::q}}|
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
		/foreach {{getvar::sexualityQuestions}} {:
			/setvar key=question {{var::item}}|
			/setvar key=genSettings index=buttonPrompt "<div>Is this a good Answer by {{getvar::firstName}} for the question:</div><div>{{getvar::question}}</div>"|
			/:"CMC Logic.GenerateWithPrompt"|
			/ife ((output != '') and (output != 'None')) {:
				/re-replace find="/^\"/g" replace="" {{getvar::output}}|
				/re-replace find="/\"$/g" replace="" {{pipe}}|
				/addvar key={{var::variableName}} "Q: \"{{getvar::question}}\"{{newline}}A: \"{{pipe}}\""|
			:}|
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

/ife (sexualityQAList != '') {:
	/setvar key=sexualityQA {{noop}}|
	/join glue="{{newline}}{{newline}}" {{getvar::sexualityQAList}}|
	/addvar key=sexualityQA {{pipe}}|
:}|
/addvar key=dataBaseNames sexualityQA|
//--------|

//Previously|
/var key=do No|
/var key=variableName "previously"|
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
    /ife (do == 'Yes') {:
	    /flushvar {{getvar::variableName}}|
    :}|
:}|
/ife ( do == 'Yes' ) {:
	/setvar key=genSettings {}|
	/setvar key=genSettings index=wi_book_key "Previously"|
	/setvar key=genSettings index=genIsList No|
	/setvar key=genSettings index=inputIsList No|
	/setvar key=genSettings index=genIsSentence Yes|
	/setvar key=genSettings index=needOutput Yes|
	/setvar key=genSettings index=outputIsList No|
	/setvar key=genSettings index=useContext Yes|
	/setvar key=extra []|
	/:"CMC Logic.Get Basic Type Context"|
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

//Story Plan|
/var key=selected_btn {{noop}}|
/ife ((parsedStoryPlan == '') and ((storyPlanMilestones == '') or (storyPlanMilestones == ''))) {:
	/buttons labels=["Yes", "No"] Do you want to make a premade story plan?|
	/var key=selected_btn {{pipe}}|
	/ife (selected_btn == '') {:
        /echo Aborting |
        /abort
    :}|
:}|
/ife ((selected_btn != 'No') or (storyPlanMilestones != '') or (storyPlanMilestones != '')) {:
	/var key=do No|
	/var key=variableName "storyPlanMilestones"|
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
    /ife (do == 'Yes') {:
	    /flushvar {{getvar::variableName}}|
    :}|
	:}|
	/ife ( do == 'Yes' ) {:
		/setvar key=genSettings {}|
		/setvar key=genSettings index=wi_book_key "Story Plan Milestones"|
		/setvar key=genSettings index=genIsList No|
		/setvar key=genSettings index=inputIsList No|
		/setvar key=genSettings index=genIsSentence Yes|
		/setvar key=genSettings index=needOutput Yes|
		/setvar key=genSettings index=outputIsList No|
		/setvar key=genSettings index=useContext Yes|
		/setvar key=extra []|
		/addvar key=extra "- Residence: {{getvar::residence}}"|
		/addvar key=extra "- Occupation: {{getvar::parsedOccupation}}"|
		/addvar key=extra "- Backstory: {{getvar::backstory}}"|
		/addvar key=extra "- Previously: {{getvar::previously}}"|
		/setvar key=genSettings index=extraContext {{getvar::extra}}|
		/setvar key=extra []|
		/:"CMC Logic.Get Basic Type Context"|
		/ife (extra != '') {:
			/setvar key=genSettings index=contextKey {{getvar::extra}}|
		:}|
		/flushvar extra|
		/wait {{getvar::wait}}|
		
		
		/getvar key=genSettings index=inputIsList|
		/let key=inputIsList {{pipe}}|
		/getvar key=genSettings index=inputIsList|
		/let key=outputIsList {{pipe}}|
		
		/ife (amount == '') {:
			/buttons labels=["Two", "Three", "Four", "Five"] Select the number of milestone you want.|
			/setvar key=amount {{pipe}}|
			/ife (amount == '') {:
				/echo Aborting |
		        /abort
			:}|
		:}|
		
		
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
		/flushvar amount|
	:}|
	/else {:
		/addvar key=dataBaseNames {{var::variableName}}|
	:}|
	
	
	/split find="{{newline}}" {{getvar::storyPlanMilestones}}|
	/setvar key=storyPlanMilestonesList {{pipe}}|
	
	
	/var key=do No|
	/var key=variableName "storyPlanDetails"|
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
	    /ife (do == 'Yes') {:
		    /flushvar {{getvar::variableName}}|
	    :}|
	:}|
	/ife ( do == 'Yes' ) {:
		/setvar key=genSettings {}|
		/setvar key=genSettings index=wi_book_key "Story Plan Details"|
		/setvar key=genSettings index=genIsList No|
		/setvar key=genSettings index=inputIsList Yes|
		/setvar key=genSettings index=genIsSentence Yes|
		/setvar key=genSettings index=needOutput Yes|
		/setvar key=genSettings index=outputIsList No|
		/setvar key=genSettings index=useContext Yes|
		/setvar key=extra []|
		/addvar key=extra "- Residence: {{getvar::residence}}"|
		/addvar key=extra "- Occupation: {{getvar::parsedOccupation}}"|
		/addvar key=extra "- Backstory: {{getvar::backstory}}"|
		/addvar key=extra "- Previously: {{getvar::previously}}"|
		/setvar key=genSettings index=extraContext {{getvar::extra}}|
		/setvar key=extra []|
		/:"CMC Logic.Get Basic Type Context"|
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
			/setvar key=tempOutputList []|
			/foreach {{getvar::storyPlanMilestonesList}} {:
				/setvar key=storyMilestone {{var::item}}|
				/:"CMC Logic.GenerateWithPrompt"|
				/addvar key=tempOutputList {{getvar::output}}|
				/flushvar output|
				/flushvar guidance|
			:}|
			/foreach {{getvar::tempOutputList}} {:
				/addvar key={{var::variableName}} {{var::item}}|
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
	
:}|
/else {:
	/setvar key=storyPlanMilestones Nope|
	/addvar key=dataBaseNames storyPlanMilestones|
	/setvar key=storyPlanDetails Nope|
	/addvar key=dataBaseNames storyPlanDetails|
:}|

/ife (((storyPlanMilestones != '') and (storyPlanMilestones != 'Nope')) and ((storyPlanMilestonesList is list))) {:
	/setvar key=parsedStoryPlan {{noop}}|
	/foreach {{getvar::storyPlanMilestonesList}} {:
		/ife (index > 0) {:
			/addvar key=parsedStoryPlan "{{newline}}"|
		:}|
		/add {{var::index}} 1|
		/let key=i {{pipe}}|
		/ife (index == 0) {:
			/getvar key=storyPlanDetails index={{var::index}}|
			/addvar key=parsedStoryPlan "- Start: {{var::item}}{{newline}}  - Details: {{pipe}}"|
		:}|
		/elseif (index > 0) {:
			/getvar key=storyPlanDetails index={{var::index}}|
			/addvar key=parsedStoryPlan "- Milestone {{var::i}}: {{var::item}}{{newline}}  - Details: {{pipe}}"|
		:}|
	:}|
:}|
/else {:
	/setvar key=parsedStoryPlan Nope|
	/addvar key=dataBaseNames parsedStoryPlan|
:}|
/addvar key=dataBaseNames parsedStoryPlan|
//--------|


//Notes|
/var key=do No|
/var key=variableName "notes"|
/ife (({{var::variableName}} == '') or ({{var::variableName}} is list)) {:
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
    /ife (do == 'Yes') {:
	    /flushvar {{getvar::variableName}}|
    :}|
:}|
/ife ( do == 'Yes' ) {:
	/setvar key=genSettings {}|
	/setvar key=genSettings index=wi_book "CMC Rules"|
	/setvar key=genSettings index=combineLorebookEntries No|
	/setvar key=genSettings index=genIsSentence No|
	/setvar key=genSettings index=inputIsList No|
	/setvar key=genSettings index=genIsList Yes|
	/setvar key=genSettings index=outputIsList No|
	/setvar key=genSettings index=needOutput No|
	/setvar key=genSettings index=useContext No|
	/wait {{getvar::wait}}|
	
	/len {{getvar::notes}}|
	/var key=len {{pipe}}|
	
	/ife ( len == 0) {:
		/setvar key={{var::variableName}} []|
		
		/setvar key=genSettings index=wi_book_key "Narration Formatting Rule"|
		/setvar key=it "Narration Formatting Rule"|
		/setvar key=genSettings index=buttonPrompt "Select one — determines how the LLM structures output"|
		/:"CMC Logic.GenerateWithSelector"|
		/addvar key={{var::variableName}} {{getvar::output}}|
	:}|
	/len {{getvar::notes}}|
	/var key=len {{pipe}}|
	/ife ( len == 1) {:
		/setvar key=genSettings index=wi_book_key "Narrative Tone Rule"|
		/setvar key=it "Narrative Tone Rule"|
		/setvar key=genSettings index=buttonPrompt "Select one — how expressive or reserved the model writes"|
		/:"CMC Logic.GenerateWithSelector"|
		/addvar key={{var::variableName}} {{getvar::output}}|
	:}|
	/len {{getvar::notes}}|
	/var key=len {{pipe}}|
	/ife ( len == 2) {:
		/setvar key=genSettings index=wi_book_key "Perspective Rule"|
		/setvar key=it "Perspective Rule"|
		/setvar key=genSettings index=buttonPrompt "Select one — PoV handling"|
		/:"CMC Logic.GenerateWithSelector"|
		/addvar key={{var::variableName}} {{getvar::output}}|
	:}|
	/len {{getvar::notes}}|
	/var key=len {{pipe}}|
	/ife ( len == 3) {:
		/setvar key=genSettings index=wi_book_key ["Output Style Behavior"]|
		/setvar key=it "Output Style Behavior"|
		/setvar key=genSettings index=buttonPrompt "Select one or more — controls structure and generation behavior"|
		/:"CMC Logic.GenerateWithSelector"|
		/foreach {{getvar::output}} {:
			/addvar key={{var::variableName}} {{var::item}}|
		:}|
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

/ife (((notes != '') and (notes != 'None')) and (notes is list)) {:
	/setvar key=parsedNotes {{noop}}|
	/foreach {{getvar::notes}} {:
		/ife (index > 0) {:
			/addvar key=parsedNotes {{newline}}|
		:}|
		/addvar key=parsedNotes - {{var::item}}|
	:}|
:}|
/else {:
	/setvar key=parsedNotes None|
:}|
/addvar key=dataBaseNames parsedNotes|
//--------|

//Synonyms|

/var key=do No|
/var key=variableName "synonyms"|
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
    /ife (do == 'Yes') {:
	    /flushvar {{getvar::variableName}}|
    :}|
:}|
/ife ( do == 'Yes' ) {:
	/setvar key=genSettings {}|
	/setvar key=genSettings index=wi_book_key "Synonyms"|
	/setvar key=genSettings index=genIsList Yes|
	/setvar key=genSettings index=inputIsList No|
	/setvar key=genSettings index=genIsSentence No|
	/setvar key=genSettings index=needOutput Yes|
	/setvar key=genSettings index=outputIsList Yes|
	/setvar key=genSettings index=useContext Yes|
	/setvar key=extra []|
	/addvar key=extra "- Appearance: {{getvar::appearanceBody}}, {{getvar::appearanceFeatures}}"|
	/addvar key=extra "- Species Group: {{getvar::speciesGroup}}"|
	/setvar key=genSettings index=extraContext {{getvar::extra}}|
	/setvar key=extra []|
	/:"CMC Logic.Get Basic Type Context"|
	/ife (extra != '') {:
		/setvar key=genSettings index=contextKey {{getvar::extra}}|
	:}|
	/flushvar extra|
	/wait {{getvar::wait}}|
	
	/getvar key=genSettings index=inputIsList|
	/let key=inputIsList {{pipe}}|
	/getvar key=genSettings index=inputIsList|
	/let key=outputIsList {{pipe}}|
	
	/setvar key=logicBasedInstruction {{noop}}|
	/setvar key=x 7|
	
	/ife ((characterArchetype == 'Human') or (characterArchetype == 'Android')) {:
		/incvar x|
		/ife ( logicBasedInstruction != '') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. Use grounded, physical or role-based descriptors only (e.g., the teen, the shy girl, the brunette)."|
		
	:}|
	/elseif ((characterArchetype != 'Human') and (characterArchetype != 'Android')) {:
		/incvar x|
		/ife ( logicBasedInstruction != '') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. You may include fantasy or species-based metaphors (e.g., “furred wanderer,” “clawed misfit,” “slime-bodied girl”) as long as they reflect the character’s anatomy or species identity."|
		
	:}|
	/flushvar x|
	
	
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

/ife (((synonyms != '') and (synonyms != 'None')) and (synonyms is list) ) {:
	/setvar key=parsedSynonyms {{noop}}|
	/foreach {{getvar::synonyms}} {:
		/ife (index > 0) {:
			/addvar key=parsedSynonyms {{newline}}|
		:}|
		/addvar key=parsedSynonyms - {{var::item}}|
	:}|
:}|
/else {:
	/setvar key=parsedSynonyms None|
:}|
/addvar key=dataBaseNames parsedSynonyms|
//--------|

//Extra Characters|
/ife (extracha == '') {:
	/buttons labels=["Yes", "No"] Do you want to add any extra characters?|
	/setvar key=extracha {{pipe}}|
    /ife (extracha == '') {:
        /echo Aborting |
        /abort
    :}|
:}| 
/ife (extracha == 'Yes') {:
	/var key=do No|
	/var key=variableName "extraCharacters"|
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
	    /ife (do == 'Yes') {:
		    /flushvar {{getvar::variableName}}|
	    :}|
	:}|
	/ife ( do == 'Yes' ) {:
		/setvar key=genSettings {}|
		/setvar key=genSettings index=wi_book_key "Extra Characters"|
		/setvar key=genSettings index=genIsList No|
		/setvar key=genSettings index=inputIsList No|
		/setvar key=genSettings index=genIsSentence Yes|
		/setvar key=genSettings index=needOutput Yes|
		/setvar key=genSettings index=outputIsList Yes|
		/setvar key=genSettings index=useContext Yes|
		/setvar key=extra []|
		/addvar key=extra "- Nationality: {{getvar::nationality}}"|
		/addvar key=extra "- Ethnicity: {{getvar::ethnicity}}"|
		/addvar key=extra "- Main Personality Trait: {{getvar::personalityMainTrait}}"| 
		/addvar key=extra "- Personality Tags: {{getvar::personalityFoundTags}}, {{getvar::personalityTags}}"|
		/addvar key=extra "- Backstory: {{getvar::backstory}}"|
		/addvar key=extra "- Scenario Overview: {{getvar::scenarioOverview}}"|
		/addvar key=extra "- Residence: {{getvar::residence}}"|
		/addvar key=extra "- Connections: {{getvar::connections}}"|
		/setvar key=genSettings index=extraContext {{getvar::extra}}|
		/setvar key=extra []|
		/:"CMC Logic.Get Basic Type Context"|
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
:}|
/else {:
	/setvar key=extraCharacters None|
	/addvar key=dataBaseNames extraCharacters|
:}|

/ife (((extraCharacters != '') and (extraCharacters != 'None')) and (extraCharacters is list)) {:
	/setvar key=parsedExtraCharacters {{noop}}|
	/foreach {{getvar::extraCharacters}} {:
		/ife (index > 0) {:
			/addvar key=parsedExtraCharacters {{newline}}|
		:}|
		/addvar key=parsedExtraCharacters - {{var::item}}|
	:}|
:}|
/else {:
	/setvar key=parsedExtraCharacters None|
:}|
/addvar key=dataBaseNames parsedExtraCharacters|

//--------|

//WRITING INSTRUCTIONS|

/var key=do No|
/var key=variableName "writingInstruct"|
/ife (({{var::variableName}} == '') and ({{var::variableName}} is list)) {:
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
    /ife (do == 'Yes') {:
	    /flushvar {{getvar::variableName}}|
    :}|
:}|
/ife ( do == 'Yes' ) {:
	/setvar key=genSettings {}|
	/setvar key=genSettings index=wi_book "CMC Rules"|
	/setvar key=genSettings index=combineLorebookEntries No|
	/setvar key=genSettings index=genIsSentence No|
	/setvar key=genSettings index=inputIsList No|
	/setvar key=genSettings index=genIsList Yes|
	/setvar key=genSettings index=outputIsList No|
	/setvar key=genSettings index=needOutput No|
	/setvar key=genSettings index=useContext No|
	/wait {{getvar::wait}}|
	
	
	/getvar key=genSettings index=wi_book_key|
	/let key=wi_book_key {{pipe}}|
	/getvar key=genSettings index=inputIsList|
	/let key=inputIsList {{pipe}}|
	/getvar key=genSettings index=combineLorebookEntries|
	/let key=combineLorebookEntries {{pipe}}|
	/len {{getvar::writingInstruct}}|
	/var key=len {{pipe}}|
	
	/ife ( len == 0) {:
		/setvar key={{var::variableName}} []|
		/setvar key=genSettings index=wi_book_key "Formatting Style"|
		/getvar key=genSettings index=wi_book_key|
		/setvar key=it {{pipe}}|
		/:"CMC Logic.GenerateWithSelector"|
		/addvar key={{var::variableName}} "**Formatting Style:** {{getvar::output}}"|
	:}|
	/len {{getvar::writingInstruct}}|
	/var key=len {{pipe}}|
	/ife ( len == 1) {:
		/setvar key=genSettings index=wi_book_key "Explicitness Level"|
		/getvar key=genSettings index=wi_book_key|
		/setvar key=it {{pipe}}|
		/:"CMC Logic.GenerateWithSelector"|
		/addvar key={{var::variableName}} "**Explicitness Level:** {{getvar::output}}"|
	:}|
	/len {{getvar::writingInstruct}}|
	/var key=len {{pipe}}|
	/ife ( len == 2) {:
		/setvar key=genSettings index=wi_book_key "User Input Style"|
		/getvar key=genSettings index=wi_book_key|
		/setvar key=it {{pipe}}|
		/:"CMC Logic.GenerateWithSelector"|
		/addvar key={{var::variableName}} "**User Input Style:** {{getvar::output}}"|
	:}|
	/len {{getvar::writingInstruct}}|
	/var key=len {{pipe}}|
	/ife ( len == 3) {:
		/setvar key=genSettings index=wi_book_key "Response Length"|
		/getvar key=genSettings index=wi_book_key|
		/setvar key=it {{pipe}}|
		/:"CMC Logic.GenerateWithSelector"|
		/addvar key={{var::variableName}} "**Response Length:** {{getvar::output}}"|
	:}|
	/len {{getvar::writingInstruct}}|
	/var key=len {{pipe}}|
	/ife ( len == 4) {:
		/setvar key=genSettings index=wi_book_key "Consent Reaction Tone"|
		/getvar key=genSettings index=wi_book_key|
		/setvar key=it {{pipe}}|
		/:"CMC Logic.GenerateWithSelector"|
		/addvar key={{var::variableName}} "**Consent & Reaction Tone:** {{getvar::output}}"|
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





/:"CMC Logic.JEDParse"|

/:"CMC Logic.Save DataBase"|

/setvar key=stepDone Yes|
/qr-list CMC Main|
/getat index=1 {{pipe}}|
/var qrlabel {{pipe}}|
/qr-get set="CMC Main" label={{var::qrlabel}}|
/getat index="message" {{pipe}}|
/qr-update set="CMC Main" label={{var::qrlabel}} newlabel="Generate First Message" {{pipe}}|