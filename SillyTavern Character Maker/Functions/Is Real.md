/buttons labels=["Yes", "No"] Is the character you are making a "real" character from a game/anime/book etc..?|
/setvar key=real {{pipe}}|
/ife ( real == ''){:
	/echo Aborting|
	/abort|
:}|
/elseif ( real == 'Yes') {:
	/input rows=8 What is the first name of the character?|
	/setvar key=fname {{pipe}}|
	/ife ( fname == ''){:
		/echo Aborting|
		/abort|
	:}|
	/else {::}|

	/input rows=8 What is the last name of {{getvar::fname}}?|
	/setvar key=lname {{pipe}}|
	/ife ( lname == ''){:
		/echo Aborting|
		/abort|
	:}|
	/else {::}|

	/input rows=8 What is the media of {{getvar::fname}}?|
	/setvar key=media {{pipe}}|
	/ife ( media == ''){:
		/echo Aborting|
		/abort|
	:}|
	/else {::}|

	/input rows=8 What is the name of the {{getvar::media}} that {{getvar::fname}} is in?|
	/setvar key=mediaName {{pipe}}|
	/ife ( mediaName == ''){:
		/echo Aborting|
		/abort|
	:}|
	/else {::}|

	
	/db-list source=chat field=name |
	/setvar key=a {{pipe}}|
	/ife ( 'real' not in a){:
		/db-add source=chat name=real {{getvar::real}}| /db-disable source=chat real|
	:}|
	/else {:
		/db-update source=chat name=real {{getvar::real}}| /db-disable source=chat real|
	:}|
	/ife ( 'first_name' not in a){:
		/db-add source=chat name=first_name {{getvar::fname}}| /db-disable source=chat first_name|
	:}|
	/else {:
		/db-update source=chat name=first_name {{getvar::fname}}| /db-disable source=chat first_name|
	:}|
	/ife ( 'last_name' not in a){:
		/db-add source=chat name=last_name {{getvar::lname}}| /db-disable source=chat last_name|
	:}|
	/else {:
		/db-update source=chat name=last_name {{getvar::lname}}| /db-disable source=chat last_name|
	:}|
	/ife ( 'media_type' not in a){:
		/db-add source=chat name=media_type {{getvar::media}}| /db-disable source=chat media_type|
	:}|
	/else {:
		/db-update source=chat name=media_type {{getvar::media}}| /db-disable source=chat media_type|
	:}|
	/ife ( 'media_name' not in a){:
		/db-add source=chat name=media_name {{getvar::mediaName}}| /db-disable source=chat media_name|
	:}|
	/else {:
		/db-update source=chat name=media_name {{getvar::mediaName}}| /db-disable source=chat media_name|
	:}|
:}|
/else {:
	/db-list source=chat field=name |
	/setvar key=a {{pipe}}|

	/ife ( 'real' not in a){:
		/db-add source=chat name=real {{getvar::real}}|
		/db-disable source=chat real|
	:}|
	/else {:
		/db-update source=chat name=real {{getvar::real}}| /db-disable source=chat real|
	:}|
	/ife ( 'media_type' not in a){:
		/db-add source=chat name=media_type None|
		/db-disable source=chat media_type|
	:}|
	/else {:
		/db-update source=chat name=media_type None| /db-disable source=chat media_type|
	:}|
	/ife ( 'media_name' not in a){:
		/db-add source=chat name=media_name None|
		/db-disable source=chat media_name|
	:}|
	/else {:
		/db-update source=chat name=media_name None| /db-disable source=chat media_name|
	:}|
:}|
