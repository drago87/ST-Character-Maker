/wi-list-books all=true|
/let key=lorebookList {{pipe}}|

/db-list source=chat field=name |
/let key=databaseList {{pipe}}|

/ife ( 'CMC Clothes' not in lorebookList) {:
	/fetch 
	/ife ( 'CMC Clothes' in databaseList){:
		/db-add source=chat name="CMC Clothes.json" {{getvar::type}}|
		/db-disable source=chat CMC Clothes.json|
	:}|
	/else {:
		/db-update source=chat name="CMC Clothes.json" {{getvar::type}}|
		/db-disable source=chat CMC Clothes.json|
	:}|
:}|

/ife ( 'CMC Appearance' not in lorebookList) {:
	/ife ( 'CMC Appearance' in databaseList){:
		/db-add source=chat name="CMC Appearance.json" {{getvar::type}}|
		/db-disable source=chat CMC Appearance.json|
	:}|
	/else {:
		/db-update source=chat name="CMC Appearance.json" {{getvar::type}}|
		/db-disable source=chat CMC Appearance.json|
	:}|
:}|

/ife ( 'CMC Variablers' not in lorebookList) {:

:}|

/ife ( 'CMC Personality' not in lorebookList) {:

:}|

/ife ( 'CMC Generation Prompts' not in lorebookList) {:

:}|

/ife ( 'CMC Information' not in lorebookList) {:

:}|