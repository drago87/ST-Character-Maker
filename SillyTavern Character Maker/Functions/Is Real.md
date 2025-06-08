/buttons labels=["Yes", "No"] Is the character you are making a "real" character from a game/anime/book etc..?|
/setvar key=real {{pipe}}|
/ife ( real == ''){:
	/echo Aborting|
	/abort|
:}|
/elseif ( real == 'Yes') {:
	/input rows=8 What is the first name of the character?|
	/setvar key=firstName {{pipe}}|
	/ife ( firstName == ''){:
		/echo Aborting|
		/abort|
	:}|
	/else {::}|

	/input rows=8 What is the last name of {{getvar::firstName}}?|
	/setvar key=lastName {{pipe}}|
	/ife ( lastName == ''){:
		/echo Aborting|
		/abort|
	:}|
	/else {::}|

	/input rows=8 What is the media of {{getvar::firstName}}?|
	/setvar key=media_type {{pipe}}|
	/ife ( media == ''){:
		/echo Aborting|
		/abort|
	:}|
	/else {::}|

	/input rows=8 What is the name of the {{getvar::media_type}} that {{getvar::firstName}} is in?|
	/setvar key=mediaName {{pipe}}|
	/ife ( mediaName == ''){:
		/echo Aborting|
		/abort|
	:}|
	/else {::}|
	
	
	/setvar key=parsedMedia "{{getvar::firstName}} is a character from the {{getvar::media_type}} _{{getvar::media_name}}_."|
	
	/addvar key=dataBaseNames real|
	/addvar key=dataBaseNames firstName|
	/addvar key=dataBaseNames lastName|
	/addvar key=dataBaseNames media_type|
	/addvar key=dataBaseNames media_name|
:}|
/else {:
	/addvar key=dataBaseNames real|
	/setvar key=media_type None|
	/addvar key=dataBaseNames media_type|
	/setvar key=media_name None|
	/addvar key=dataBaseNames media_name|
:}|
