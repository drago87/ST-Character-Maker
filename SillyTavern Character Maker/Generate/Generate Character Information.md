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
//----|

//Character Overview|

//Nationality|
/var key=do Yes|
/var key=variableName "nationality"|
/ife ( {{var::variableName}} != '') {:
	/buttons labels=["Yes", "No"] Do you want to redo {{var::variableName}}|
	/var key=do {{pipe}}|
:}|
/ife ( do == 'Yes' ) {:
	/var key=wi_book_key "Nationalities"|
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
	/:GenerateWithPrompt wi_book_key_f="{{var::wi_book_key}}" genIsList_f="{{var::genIsList}}" genIsSentence_f="{{var::genIsSentence}}" needOutput_f="{{var::needOutput}}" contextKey_f="{{var::contextKey}}"|
	
	/setvar key={{var::variableName}} {{getvar::output}}|
	/addvar key=dataBaseNames {{var::variableName}}|
:}|
//-----------|

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
	/:GenerateWithPrompt wi_book_key_f="{{var::wi_book_key}}" genIsList_f="{{var::genIsList}}" genIsSentence_f="{{var::genIsSentence}}" needOutput_f="{{var::needOutput}}" contextKey_f="{{var::contextKey}}"|
	
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
		/:GenerateWithPrompt wi_book_key_f="{{var::wi_book_key}}" genIsList_f="{{var::genIsList}}" genIsSentence_f="{{var::genIsSentence}}" needOutput_f="{{var::needOutput}}" contextKey_f="{{var::contextKey}}"|
		
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
		/:GenerateWithPrompt wi_book_key_f="{{var::wi_book_key}}" genIsList_f="{{var::genIsList}}" genIsSentence_f="{{var::genIsSentence}}" needOutput_f="{{var::needOutput}}" contextKey_f="{{var::contextKey}}"|
		
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
	/:GenerateWithPrompt wi_book_key_f="{{var::wi_book_key}}" genIsList_f="{{var::genIsList}}" genIsSentence_f="{{var::genIsSentence}}" needOutput_f="{{var::needOutput}}" contextKey_f="{{var::contextKey}}"|
	
	/setvar key={{var::variableName}} {{getvar::output}}|
	/addvar key=dataBaseNames {{var::variableName}}|
:}|
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