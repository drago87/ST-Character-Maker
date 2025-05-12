/qr-list CMC Main|
/getat index=1 {{pipe}}|
/let qrlabel {{pipe}}|
/qr-get set="CMC Main" label={{var::qrlabel}}|
/getat index="message" {{pipe}}|
/qr-update set="CMC Main" label={{var::qrlabel}} newlabel="Continue Generating Character Personality" {{pipe}}|

/:"CMC Logic.Get Char info"|

/setvar key=dataBaseNames []|
/flushvar genSettings|

/setvar key=stepVar Step4|

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

//Archetype|
/var key=do No|
/var key=variableName "archetype"|
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
	/setvar key=genSettings index=wi_book_key "Archetype"|
	/setvar key=genSettings index=genIsList No|
	/setvar key=genSettings index=inputIsTaskList No|
	/setvar key=genSettings index=genIsSentence Yes|
	/setvar key=genSettings index=needOutput Yes|
	/setvar key=genSettings index=useContext Yes|
	/setvar key=genSettings index=contextKey []|
	/wait {{getvar::wait}}|
	
	/setvar key=settingModifier {Modifier}|
	/setvar key=settingArchetype {Archetype}|
	/setvar key=settingAddition {Addition}|
	
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
/else {:
	/addvar key=dataBaseNames {{var::variableName}}|
:}|
//--------|


//Archetype Details|
/var key=do No|
/var key=variableName "archetypeDetails"|
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
	/setvar key=genSettings index=wi_book_key "Archetype Details"|
	/setvar key=genSettings index=genIsList No|
	/setvar key=genSettings index=inputIsTaskList No|
	/setvar key=genSettings index=genIsSentence Yes|
	/setvar key=genSettings index=needOutput Yes|
	/setvar key=genSettings index=useContext Yes|
	/setvar key=extra []|
	/addvar key=extra Archetype: {{getvar::archetype}}|
	/setvar key=genSettings index=extraContext {{getvar::extra}}|
	/flushvar extra|
	/setvar key=genSettings index=contextKey []|
	/wait {{getvar::wait}}|
	
	/setvar key=settingModifier {Modifier}|
	/setvar key=settingArchetype {Archetype}|
	/setvar key=settingAddition {Addition}|
	
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
	/flushvar settingModifier|
	/flushvar settingArchetype|
	/flushvar settingAddition|
:}|
/else {:
	/addvar key=dataBaseNames {{var::variableName}}|
:}|
//--------|


//Reasoning|

//--------|


/buttons labels=["Yes", "No"] Do you want to select and generate an Alignment and its details?|
/var selected_btn {{pipe}}|
/ife ( selected_btn == ''){:
	/echo Aborting |
	/abort
:}|
/elseif ( selected_btn == 'Yes') {:
	//Alignment|
	
	//--------|
	
	
	//Alignment Details|
	
	//--------|
	
	
	//Ideals|
	
	//--------|
:}|
/else {:
	/setvar key=alignment Nope|
	/setvar key=alignmentDetails Nope|
	/setvar key=alignmentIdeals Nope|
:}|

/ife ( alignment != 'Nope') {:
	/findentry field=comment file="CMC Templates" "Alignment Template"|
	/getentryfield field=content file="CMC Templates" {{pipe}}|
	/setvar key=parsedAlignment {{pipe}}|
:}|
/else {:
	/setvar key=parsedAlignment None|
:}|


//Personality Tags|

//--------|


//Cognitive Abilities|

//--------|


//Social Skills and Integration Into Society|

//--------|


//Main Aspiration|

//--------|


//Aspiration Details|

//--------|


//Aspiration Goals|

//--------|


/findentry field=comment file="CMC Templates" "Aspiration Template"|
/getentryfield field=content file="CMC Templates" {{pipe}}|
/setvar key=parsedAspiration {{pipe}}|



//Unique Trait|

//--------|


//Trait Effect|

//--------|

/setvar key=parsedTraits []|
/foreach {{uniqueTrait}} {:
	/let key=trait {{var::item}}|
	/getvar key=traitEffect index={{var::index}}|
	/let key=effect {{pipe}}|
	/findentry field=comment file="CMC Templates" "Unique Trait Template"|
	/getentryfield field=content file="CMC Templates" {{pipe}}|
	/re-replace find="/--UniqueTrait--/g" replace="{{var::item}}" {{pipe}}|
	/re-replace find="/--Effect--/g" replace="{{var::effect}}" {{pipe}}|
	/addvar key=parsedTraits {{pipe}}|
:}|
/join glue="{{newline}}{{newline}}" {{getvar::parsedTraits}}|
/setvar key=parsedTraits {{pipe}}||

//Personality Q&A|

//--------|

/:"CMC Logic.JEDParse"|

/:"CMC Logic.Save DataBase"|

/setvar key=stepDone Yes|
/qr-list CMC Main|
/getat index=1 {{pipe}}|
/var qrlabel {{pipe}}|
/qr-get set="CMC Main" label={{var::qrlabel}}|
/getat index="message" {{pipe}}|
/qr-update set="CMC Main" label={{var::qrlabel}} newlabel="Start Generating Personality" {{pipe}}|