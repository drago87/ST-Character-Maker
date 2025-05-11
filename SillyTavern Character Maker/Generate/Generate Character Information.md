/setvar key=stepDone No|
/setvar key=stepVar Step3|
/qr-list CMC Main|
/getat index=1 {{pipe}}|
/let qrlabel {{pipe}}|
/qr-get set="CMC Main" label={{var::qrlabel}}|
/getat index="message" {{pipe}}|
/qr-update set="CMC Main" label={{var::qrlabel}} newlabel="Continue Generating Character Information" {{pipe}}|

/:"CMC Logic.Get Char info"|

/setvar key=dataBaseNames []|

//Character Overview|

//Race/Species|
/ife () {:
	/let key=do Yes|
	/let key=variableName ""|
	/ife ( {{var::variableName}} != '') {:
		/buttons labels=["Yes", "No"] Do you want to redo {{var::variableName}}|
		/var key=do {{pipe}}|
	:}|
	/ife ( do == 'Yes' ) {:
		/setvar key=genSettings index=wi_book ""|
		/setvar key=genSettings index=wi_book_key ""|
		/setvar key=genSettings index=genIsList No|
		/setvar key=genSettings index=genIsSentence No|
		/setvar key=genSettings index=needOutput Yes|
		/setvar key=genSettings index=useContext No|
		/setvar key=genSettings index=contextKey []|
		
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
		/flushvar genOrder|
		/flushvar genContent|
		/flushvar genSettings|
	:}|
:}|
/else {:
	
:}|
//-----------|

//Nationality|
/var key=do Yes|
/var key=variableName "nationality"|
/ife ( {{var::variableName}} != '') {:
	/buttons labels=["Yes", "No"] Do you want to redo {{var::variableName}}|
	/var key=do {{pipe}}|
:}|
/ife ( do == 'Yes' ) {:
	/setvar key=genSettings index=wi_book_key "Nationalities"|
	/setvar key=genSettings index=genIsList Yes|//Yes or No|
	/setvar key=genSettings index=genIsSentence No|//Yes or No|
	/setvar key=genSettings index=needOutput Yes|//Yes or No|
	/setvar key=genSettings index=useContext Yes|
	/setvar key=genSettings index=contextKey []|
	
	
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
	/flushvar genOrder|
	/flushvar genContent|
	/flushvar genSettings|
:}|
//-----------|
/*
//Ethnicity|
/var key=do Yes|
/var key=variableName "ethnicity"|
/ife ( {{var::variableName}} != '') {:
	/buttons labels=["Yes", "No"] Do you want to redo {{var::variableName}}|
	/var key=do {{pipe}}|
:}|
/ife ( do == 'Yes' ) {:
	/var key=wi_book_key "Ethnicities"|
	/var key=genIsList Yes|//Yes or No|
	/var key=outputIsList No|//Yes or No|
	/var key=genIsSentence No|//Yes or No|
	/var key=needOutput Yes|//Yes or No|
	/var key=contextKey "Character"|
	
	
	/ife (outputIsList == 'Yes') {:
		/setvar as=array key={{var::variableName}} []|
	:}|
	/else {:
		/setvar as=string key={{var::variableName}} {{noop}}|
	:}|
	//[[Generate with Prompt]]|
	/:"CMC Logic.GenerateWithPrompt"|
	
	/setvar key={{var::variableName}} {{getvar::output}}|
	/addvar key=dataBaseNames {{var::variableName}}|
:}|
//-----------|


/ife ( real != 'Yes') {:
	//First Name|
	/var key=do Yes|
	/var key=variableName "firstName"|
	/ife ( {{var::variableName}} != '') {:
		/buttons labels=["Yes", "No"] Do you want to redo {{var::variableName}}|
		/var key=do {{pipe}}|
	:}|
	/ife ( do == 'Yes' ) {:
		/var key=wi_book_key "First Name"|
		/var key=genIsList Yes|//Yes or No|
		/var key=outputIsList No|//Yes or No|
		/var key=genIsSentence No|//Yes or No|
		/var key=needOutput Yes|//Yes or No|
		/var key=contextKey "Character"|
		
		/ife (outputIsList == 'Yes') {:
			/setvar as=array key={{var::variableName}} []|
		:}|
		/else {:
			/setvar as=string key={{var::variableName}} {{noop}}|
		:}|
		//[[Generate with Prompt]]|
		/:"CMC Logic.GenerateWithPrompt"|
		
		/setvar key={{var::variableName}} {{getvar::output}}|
		/addvar key=dataBaseNames {{var::variableName}}|
	:}|
	//-----------|
	
	
	
	//Last Name|
	/var key=do Yes|
	/var key=variableName "lastName"|
	/ife ( {{var::variableName}} != '') {:
		/buttons labels=["Yes", "No"] Do you want to redo {{var::variableName}}|
		/var key=do {{pipe}}|
	:}|
	/ife ( do == 'Yes' ) {:
		/var key=wi_book_key "Last Name"|
		/var key=genIsList Yes|//Yes or No|
		/var key=genIsSentence No|//Yes or No|
		/var key=outputIsList No|//Yes or No|
		/var key=needOutput Yes|//Yes or No|
		/var key=contextKey "Character"|
		
		/ife (outputIsList == 'Yes') {:
			/setvar as=array key={{var::variableName}} []|
		:}|
		/else {:
			/setvar as=string key={{var::variableName}} {{noop}}|
		:}|
		//[[Generate with Prompt]]|
		/:"CMC Logic.GenerateWithPrompt"|
		
		/setvar key={{var::variableName}} {{getvar::output}}|
		/addvar key=dataBaseNames {{var::variableName}}|
	:}|
	//-----------|
:}|

//Nickname|
/var key=do Yes|
/var key=variableName "nickName"|
/ife ( {{var::variableName}} != '') {:
	/buttons labels=["Yes", "No"] Do you want to redo {{var::variableName}}|
	/var key=do {{pipe}}|
:}|
/ife ( do == 'Yes' ) {:
	/var key=wi_book_key "Nickname"|
	/var key=genIsList Yes|//Yes or No|
	/var key=outputIsList No|//Yes or No|
	/var key=genIsSentence No|//Yes or No|
	/var key=needOutput Yes|//Yes or No|
	/var key=contextKey "Character"|
	
	
	/ife (outputIsList == 'Yes') {:
		/setvar as=array key={{var::variableName}} []|
	:}|
	/else {:
		/setvar as=string key={{var::variableName}} {{noop}}|
	:}|
	//[[Generate with Prompt]]|
	/:"CMC Logic.GenerateWithPrompt"|
	
	/setvar key={{var::variableName}} {{getvar::output}}|
	/addvar key=dataBaseNames {{var::variableName}}|
:}|
//-----------|

//Age|

//-----------|

//Race Age|

//-----------|

/:"CMC Logic.JEDParse"|

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
/forcesave|
/renamechat {{getvar::filename}}|
/flushvar filename|
*|