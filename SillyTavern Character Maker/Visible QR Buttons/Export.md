/input Who do you want the name of the author of the character to be?|
/setvar key=author {{pipe}}|
/let key=done Regenerate|
/findentry field=comment file="CMC Generation Prompts" "Export Prompt"|
/getentryfield field=content file="CMC Generation Prompts" {{pipe}}|
/let key=prompt {{pipe}}|
/let key=output {{noop}}|
/whilee (done == 'Regenerate') {:
	/echo Generationg Brief Character Overview|
	/genraw {{var::prompt}}|
	/var key=output {{pipe}}|
	/buttons labels=["Yes", "Regenerate"] <div>Are you happy with the Character Overview?</div><div>{{var::output}}</div>|
	/var key=done {{pipe}}|
	/ife ( done == ''){:
		/echo Aborting |
		/abort
	:}|
:}|
/re-replace find="/\n/g" replace="\r\n" {{var::output}}|
/re-replace find="/\"/g" replace="\\\"" {{pipe}}|
/var key=output {{pipe}}|
/re-replace find="/\n/g" replace="\r\n" {{getvar::fullCharacterSheet}}|
/re-replace find="/\"/g" replace="\\\"" {{pipe}}|
/let key=fullCharacterSheetFixed {{pipe}}|
/re-replace find="/\n/g" replace="\r\n" {{getvar::firstMessage}}|
/re-replace find="/\"/g" replace="\\\"" {{pipe}}|
/let key=firstMessageFixed {{pipe}}|
/findentry field=comment file="CMC Templates" "Character Card Template"|
/getentryfield field=content file="CMC Templates" {{pipe}}|
/re-replace find="/--CharName--/g" replace="{{getvar::firstName}}" {{pipe}}|
/re-replace find="/--Summary--/g" replace="" {{pipe}}|
/re-replace find="/--Scenario--/g" replace="" {{pipe}}|
/re-replace find="/--Example_Dial--/g" replace="" {{pipe}}|
/re-replace find="/--Main_Prompt--/g" replace="" {{pipe}}|
/re-replace find="/--Post_Hist--/g" replace="" {{pipe}}|
/re-replace find="/--Alt_Greet1--/g" replace="" {{pipe}}|
/re-replace find="/--Char_Notes--/g" replace="" {{pipe}}|
/re-replace find="/--Group_Greeting1--/g" replace="" {{pipe}}|
/re-replace find="/--Tag1--/g" replace="" {{pipe}}|
/re-replace find="/--Created_By--/g" replace="{{getvar::author}}" {{pipe}}|
/re-replace find="/--Creator_Notes--/g" replace="{{var::output}}" {{pipe}}|

/re-replace find="/--Description--/g" replace="{{var::fullCharacterSheetFixed}}" {{pipe}}|
/re-replace find="/--First_Mess--/g" replace="{{var::firstMessageFixed}}" {{pipe}}|
/re-replace find="/--User--/g" replace="{\{user}}" {{pipe}}|
/db-add source=chat name="{{getvar::firstName}}.json" {{pipe}}|
/db-disable source=chat "{{getvar::firstName}}.json"|

/popup Download {{getvar::firstName}}.json from the SillyTavern Data Bank (It will open when you press ok) and import it as a character to be able to change the image.|
/db|