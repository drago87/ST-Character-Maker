/let key=do|
/let key=variableName|

//Scenario Overview|
/var key=do Yes|
/var key=variableName "scenarioOverview"|
/ife ( {{var::variableName}} != '') {:
	/buttons labels=["Yes", "No"] Do you want to redo {{var::variableName}}|
	/var key=do {{pipe}}|
:}|
/ife ( do == 'Yes' ) {:
	/input default="Example: user is a neighbor of {{getvar::firstName}} and is often hired by {{getvar::firstName}}'s parents to babysit {{getvar::firstName}}, which has led to [...]" <div>What is this scenario about?</div><div>What is the main idea?</div>|
	/setvar key=scenarioIde {{pipe}}|
	/setvar key=genSettings index=wi_book_key "Scenario"|
	/setvar key=genSettings index=genIsList No|
	/setvar key=genSettings index=genIsSentence Yes|
	/setvar key=genSettings index=needOutput Yes|
	/setvar key=genSettings index=useContext Yes|
	/setvar key=genSettings index=contextKey {{noop}}|
	
	/getvar key=genSettings index=inputIsList|
	/let key=inputIsList {{pipe}}|
	/getvar key=genSettings index=combineLorebookEntries|
	/let key=combineLorebookEntries {{pipe}}|
	
	
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