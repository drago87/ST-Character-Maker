/:"CMC Logic.TempVariables"|
/:"CMC Logic.Get Char info"|

//Functions|
/:"CMC Functions.Text Parce"|

//Character Overview|

//Nationality|
/var key=do Yes|
/var key=variableName "nationality"|
/ife ( {{var::variableName}} != '') {:
	/buttons labels=["Yes", "No"] Do you want to redo redo {{var::variableName}}|
	/var key=do {{pipe}}|
:}|
/ife ( do == 'Yes ) {:
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
	/:"CMC Logic.Generator"|
	
	/setvar key={{var::variableName}} {{var::output}}|
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
/ife ( do == 'Yes ) {:
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
	/:"CMC Logic.Generator"|
	
	/setvar key={{var::variableName}} {{var::output}}|
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
	/ife ( do == 'Yes ) {:
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
		/:"CMC Logic.Generator"|
		
		/setvar key={{var::variableName}} {{var::output}}|
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
	/ife ( do == 'Yes ) {:
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
		/:"CMC Logic.Generator"|
		
		/setvar key={{var::variableName}} {{var::output}}|
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
/ife ( do == 'Yes ) {:
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
	/:"CMC Logic.Generator"|
	
	/setvar key={{var::variableName}} {{var::output}}|
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