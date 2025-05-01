/setvar key=stepDone No|
/setvar key=stepVar Step3|
/qr-list CMC Main|
/getat index=1 {{pipe}}|
/let qrlabel {{pipe}}|
/qr-get set="CMC Main" label={{var::qrlabel}}|
/getat index="message" {{pipe}}|
/qr-update set="CMC Main" label={{var::qrlabel}} newlabel="Continue Generating Character Information" {{pipe}}|

--VarReplace--

/:"CMC Logic.Get Char info"|

/setvar key=dataBaseNames []|

//Generation Functions|
--GenPrompt--

--GenSelector--
/----|

//Character Overview|

//Nationality|
/var key=do Yes|
/var key=variableName "nationality"|
/ife ( {{var::variableName}} != '') {:
	/buttons labels=["Yes", "No"] Do you want to redo redo {{var::variableName}}|
	/var key=do {{pipe}}|
:}|
/ife ( do == 'Yes' ) {:
	/var key=genKey "Nationalities"|
	/var key=genIsList Yes|//Yes or No|
	/var key=outputIsList No|//Yes or No|
	/var key=genIsSentence No|//Yes or No|
	/var key=needOutput Yes|//Yes or No|
	/var key=contextKey "Character"|
	
	
	/ife (outputIsList == 'Yes') {:
		/var as=array key={{var::variableName}} []|
	:}|
	/else {:
		/var as=string key={{var::variableName}} {{noop}}|
	:}|
	//[[Generate with Prompt]]|
	/:GenerateWithPrompt wi_book= genKey= genIsList= genIsSentence= needOutput=  contextKey={{noop}}|
	
	/setvar key={{var::variableName}} {{var::output}}|
	/addvar key=dataBaseNames {{var::variableName}}|
	/var key=context {{noop}}|
	/var key=examples {{noop}}|
	/var key=task {{pipe}}|
	/var key=instruct {{pipe}}|
	/var key=content {{pipe}}|
:}|
//-----------|

//Ethnicity|
/var key=do Yes|
/var key=variableName "ethnicity"|
/ife ( {{var::variableName}} != '') {:
	/buttons labels=["Yes", "No"] Do you want to redo redo {{var::variableName}}|
	/var key=do {{pipe}}|
:}|
/ife ( do == 'Yes' ) {:
	/var key=genKey "Ethnicities"|
	/var key=genIsList Yes|//Yes or No|
	/var key=outputIsList No|//Yes or No|
	/var key=genIsSentence No|//Yes or No|
	/var key=needOutput Yes|//Yes or No|
	/var key=contextKey "Character"|
	
	
	/ife (outputIsList == 'Yes') {:
		/var as=array key={{var::variableName}} []|
	:}|
	/else {:
		/var as=string key={{var::variableName}} {{noop}}|
	:}|
	//[[Generate with Prompt]]|
	/:GenerateWithPrompt wi_book= genKey= genIsList= genIsSentence= needOutput=  contextKey={{noop}}|
	
	/setvar key={{var::variableName}} {{var::output}}|
	/addvar key=dataBaseNames {{var::variableName}}|
	/var key=context {{noop}}|
	/var key=examples {{noop}}|
	/var key=task {{pipe}}|
	/var key=instruct {{pipe}}|
	/var key=content {{pipe}}|
:}|
//-----------|


/ife ( real != 'Yes') {:
	//First Name|
	/var key=do Yes|
	/var key=variableName "firstName"|
	/ife ( {{var::variableName}} != '') {:
		/buttons labels=["Yes", "No"] Do you want to redo redo {{var::variableName}}|
		/var key=do {{pipe}}|
	:}|
	/ife ( do == 'Yes' ) {:
		/var key=genKey "First Name"|
		/var key=genIsList Yes|//Yes or No|
		/var key=outputIsList No|//Yes or No|
		/var key=genIsSentence No|//Yes or No|
		/var key=needOutput Yes|//Yes or No|
		/var key=contextKey "Character"|
		
		/ife (outputIsList == 'Yes') {:
			/var as=array key={{var::variableName}} []|
		:}|
		/else {:
			/var as=string key={{var::variableName}} {{noop}}|
		:}|
		//[[Generate with Prompt]]|
		/:GenerateWithPrompt wi_book= genKey= genIsList= genIsSentence= needOutput=  contextKey={{noop}}|
		
		/setvar key={{var::variableName}} {{var::output}}|
		/addvar key=dataBaseNames {{var::variableName}}|
		/var key=context {{noop}}|
		/var key=examples {{noop}}|
		/var key=task {{pipe}}|
		/var key=instruct {{pipe}}|
		/var key=content {{pipe}}|
	:}|
	//-----------|
	
	
	
	//Last Name|
	/var key=do Yes|
	/var key=variableName "lastName"|
	/ife ( {{var::variableName}} != '') {:
		/buttons labels=["Yes", "No"] Do you want to redo redo {{var::variableName}}|
		/var key=do {{pipe}}|
	:}|
	/ife ( do == 'Yes' ) {:
		/var key=genKey "Last Name"|
		/var key=genIsList Yes|//Yes or No|
		/var key=genIsSentence No|//Yes or No|
		/var key=outputIsList No|//Yes or No|
		/var key=needOutput Yes|//Yes or No|
		/var key=contextKey "Character"|
		
		/ife (outputIsList == 'Yes') {:
			/var as=array key={{var::variableName}} []|
		:}|
		/else {:
			/var as=string key={{var::variableName}} {{noop}}|
		:}|
		//[[Generate with Prompt]]|
		/:GenerateWithPrompt wi_book= genKey= genIsList= genIsSentence= needOutput=  contextKey={{noop}}|
		
		/setvar key={{var::variableName}} {{var::output}}|
		/addvar key=dataBaseNames {{var::variableName}}|
		/var key=context {{noop}}|
		/var key=examples {{noop}}|
		/var key=task {{pipe}}|
		/var key=instruct {{pipe}}|
		/var key=content {{pipe}}|
	:}|
	//-----------|
:}|

//Nickname|
/var key=do Yes|
/var key=variableName "nickName"|
/ife ( {{var::variableName}} != '') {:
	/buttons labels=["Yes", "No"] Do you want to redo redo {{var::variableName}}|
	/var key=do {{pipe}}|
:}|
/ife ( do == 'Yes' ) {:
	/var key=genKey "Nickname"|
	/var key=genIsList Yes|//Yes or No|
	/var key=outputIsList No|//Yes or No|
	/var key=genIsSentence No|//Yes or No|
	/var key=needOutput Yes|//Yes or No|
	/var key=contextKey "Character"|
	
	
	/ife (outputIsList == 'Yes') {:
		/var as=array key={{var::variableName}}|
	:}|
	/else {:
		/var as=string key={{var::variableName}} {{noop}}|
	:}|
	//[[Generate with Prompt]]|
	/:GenerateWithPrompt wi_book= genKey= genIsList= genIsSentence= needOutput=  contextKey={{noop}}|
	
	/setvar key={{var::variableName}} {{var::output}}|
	/addvar key=dataBaseNames {{var::variableName}}|
	/var key=context {{noop}}|
	/var key=examples {{noop}}|
	/var key=task {{pipe}}|
	/var key=instruct {{pipe}}|
	/var key=content {{pipe}}|
}:|
//-----------|

//Race|

//-----------|

//Age|

//-----------|

--JEDParse--
/findentry field=comment file="CMC Variables" Character Template|
/getentryfield file="CMC Variables" {{pipe}}|
/:JEDParse input={{pipe}}|
/setvar key=t {{pipe}}|
/:"CMC Logic.Parse"|
/message-edit message=0 {{pipe}}|
/flushvar t|

/:"CMC Logic.Save DataBase"|

/setvar key=stepDone Yes|
/qr-list CMC Main|
/getat index=1 {{pipe}}|
/var qrlabel {{pipe}}|
/qr-get set="CMC Main" label={{var::qrlabel}}|
/getat index="message" {{pipe}}|
/qr-update set="CMC Main" label={{var::qrlabel}} newlabel="Start Generating Personality" {{pipe}}|

/let key=filename {{datetimeformat YYYY-MM-DD HH h mm}}|
/re-replace find="/\s(?=\d{2}$)/g" replace="h " {{var::filename}}|
/setvar key=filename {{pipe}}|
/addvar key=filename " m {{getvar::firstName}} {{getvar::lastName}}"|
/forcesave
/renamechat {{getvar::filename}}|
/flushvar filename|