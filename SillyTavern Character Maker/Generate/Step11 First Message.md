/qr-list CMC Main|
/getat index=1 {{pipe}}|
/let qrlabel {{pipe}}|
/qr-get set="CMC Main" label={{var::qrlabel}}|
/getat index="message" {{pipe}}|
/qr-update set="CMC Main" label={{var::qrlabel}} newlabel="Continue making First Message" {{pipe}}|

/:"CMC Logic.Get Char info"|

/setvar key=dataBaseNames []|
/flushvar genSettings|

/setvar key=stepVar Step11|
/setvar key=stepDone No|

/let key=do {{noop}}|
/let key=variableName {{noop}}|
/let selected_btn {{noop}}|
/let key=len {{noop}}|

/var key=do Yes|
/var key=variableName "firstMessage"|
/ife ({{var::variableName}} != '') {:
	/buttons labels=["Yes", "No"] Do you want to remake {{getvar::firstName}}'s First Message|
    /var key=do {{pipe}}|
    /ife (do == '') {:
        /echo Aborting |
        /abort
    :}|
:}|
/ife ( do == 'Yes' ) {:
	/setvar key=genSettings {}|
	/setvar key=genSettings index=wi_book_key "First Message"|
	/setvar key=genSettings index=genIsList No|
	/setvar key=genSettings index=inputIsList No|
	/setvar key=genSettings index=genIsSentence Yes|
	/setvar key=genSettings index=needOutput Yes|
	/setvar key=genSettings index=outputIsList No|
	/setvar key=genSettings index=useContext Yes|
	/setvar key=extra []|
	/addvar key=extra "{{getvar::parsedApperance}}"|
	/addvar key=extra "{{getvar::parsedSentientLevel"|
	/setvar key=genSettings index=extraContext {{getvar::extra}}|
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
	
	
	/setvar key=logicBasedInstruction {{noop}}|
	/setvar key=x 9|
	
	/incvar x|
	/ife ( logicBasedInstruction != '') {:
		/addvar key=logicBasedInstruction {{newline}}|
	:}|
	/getvar key=writingInstruct index=0|
	/re-replace find="/\*\*Formatting Style:\*\*\s/g" replace="" {{pipe}}|
	/addvar key=logicBasedInstruction "{{getvar::x}}. {{pipe}} Do **not** alter or reinterpret the formatting — apply it **exactly**."|
	/ife (('Fully Animalistic' in parsedSentientLevel) or ('Semi-Sapient' in parsedSentientLevel)) {:
		/incvar x|
		/ife ( logicBasedInstruction != '') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. Do **not** include a visual impression that involves posture, clothing, or emotional expression — use physical behaviors like stance, motion, or instinctual cues instead."|
		
		/incvar x|
		/ife ( logicBasedInstruction != '') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. Do **not** include dialogue or speech. Replace the final line with a physical reaction or animal sound (e.g., snort, tail flick, attentive glance)."|
		
	:}|
	/elseif ('Emotionally Aware' in parsedSentientLevel) {:
		/incvar x|
		/ife ( logicBasedInstruction != '') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		  /addvar key=logicBasedInstruction "{{getvar::x}}. Avoid explicit speech or internal thoughts, but you **may** show emotion through posture, proximity, vocal sounds, or learned routine behavior. Final line should still be a **non-verbal** cue."|
	:}|
	/else {:
		/incvar x|
		/ife ( logicBasedInstruction != '') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. Include a quick visual impression of {{getvar::firstName}} — posture, outfit, or energy."|
		
		/incvar x|
		/ife ( logicBasedInstruction != '') {:
			/addvar key=logicBasedInstruction {{newline}}|
		:}|
		/addvar key=logicBasedInstruction "{{getvar::x}}. End with a single in-character line of dialogue, in quotes. Keep it short and expressive — no more than 15 words unless otherwise specified."|
		
	:}|
	/flushvar x|
	
	/ife (('Fully Animalistic' in parsedSentientLevel) or ('Semi-Sapient' in parsedSentientLevel)) {:
		/setvar key=sceneChecklist "```{{newline}}Your scene must:{{newline}}- Describe where {{getvar::firstName}} is.{{newline}}- What {{getvar::subjPronoun}} is physically doing or reacting to.{{newline}}- What’s around {{getvar::objPronoun}} — include surroundings, weather, scent, or movement.{{newline}}- Use only instinctual behavior or physical signals — no dialogue, thoughts, or human-style emotion.{{newline}}{{newline}}```"|
	:}|
	
	/else {:
		/setvar key=sceneChecklist "```{{newline}}Your scene must:{{newline}}- Describe where {{getvar::firstName}} is.{{newline}}- What {{getvar::subjPronoun}} is doing or feeling.{{newline}}- What’s around {{getvar::objPronoun}} (setting, tone, mood).{{newline}}- How {{getvar::firstName}} looks — posture, expression, outfit, or notable traits.{{newline}}- End with a single in-character line of dialogue that reflects {{getvar::possAdjPronoun}} personality and tone.```"|
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
:}|
/else {:
	/addvar key=dataBaseNames {{var::variableName}}|
:}|

/messages names=off 1|
/let key=mess {{pipe}}|
/ife (mess == '') {:
	/sendas name={{char}} {{getvar::firstMessage}}
:}|
/else {:
	/message-edit message=1 await=true {{getvar::firstMessage}}|
:}|

/:"CMC Logic.Save DataBase"|

/setvar key=stepDone Yes|
/qr-list CMC Main|
/getat index=1 {{pipe}}|
/var qrlabel {{pipe}}|
/qr-get set="CMC Main" label={{var::qrlabel}}|
/getat index="message" {{pipe}}|
/qr-update set="CMC Main" label={{var::qrlabel}} newlabel="Start Generating Tagline" {{pipe}}|

/qr-update set="CMC Main" label="Character Export" hidden=false title="Exports the character to the DataBase and saves it as a .json file that can be imported to ST as a character (Without a image)"|
/forcesave|