/qr-list CMC Main|
/getat index=1 {{pipe}}|
/let qrlabel {{pipe}}|
/qr-get set="CMC Main" label={{var::qrlabel}}|
/getat index="message" {{pipe}}|
/qr-update set="CMC Main" label={{var::qrlabel}} newlabel="Continue making First Message" {{pipe}}|

/:"CMC Logic.Get Char info"|

/setvar key=dataBaseNames []|
/flushvar genSettings|

/setvar key=stepVar Step10|
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
	/setvar key=genSettings index=useContext No|
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

/messages names=off 1|
/let key=mess {{pipe}}|
/ife (mess == '') {:
	/sendas name={{char}} {{getvar::firstMessage}}
:}|
/else {:
	/message-edit message=0 await=true {{getvar::firstMessage}}|
:}|

/:"CMC Logic.Save DataBase"|

/setvar key=stepDone Yes|
/qr-update set="CMC Main" label="Character Export" hidden=false title="Exports the character to the DataBase and saves it as a .json file that can be imported to ST as a character (Without a image)"|
/forcesave|