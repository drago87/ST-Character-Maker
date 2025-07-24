/wi-list-books all=true|
/let key=lorebookList {{pipe}}|

/db-list source=chat field=name |
/let key=databaseList {{pipe}}|



/ife ( 'CMC Generation Prompts' not in lorebookList) {:
	/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/LoreBooks/{{getvar::model}}/CMC%20Generation%20Prompts.json|
	/let key=f {{pipe}}|
	/ife ( 'CMC Generation Prompts.json' not in databaseList){:
		/db-add source=chat name="CMC Generation Prompts.json" {{var::f}}|
		/db-disable source=chat CMC Generation Prompts.json|
	:}|
	/else {:
		/db-update source=chat name="CMC Generation Prompts.json" {{var::f}}|
		/db-disable source=chat CMC Generation Prompts.json|
	:}|
:}|

/ife ( 'CMC Information' not in lorebookList) {:
	/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/LoreBooks/{{getvar::model}}/CMC%20Information.json|
	/let key=f {{pipe}}|
	/ife ( 'CMC Generation Prompts.json' not in databaseList){:
		/db-add source=chat name="CMC Information.json" {{var::f}}|
		/db-disable source=chat CMC Information.json|
	:}|
	/else {:
		/db-update source=chat name="CMC Information.json" {{var::f}}|
		/db-disable source=chat CMC Information.json|
	:}|
:}|

/ife ( 'CMC Questions' not in lorebookList) {:
	/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/LoreBooks/{{getvar::model}}/CMC%20Questions.json|
	/let key=f {{pipe}}|
	/ife ( 'CMC Questions.json' not in databaseList){:
		/db-add source=chat name="CMC Questions.json" {{var::f}}|
		/db-disable source=chat CMC Questions.json|
	:}|
	/else {:
		/db-update source=chat name="CMC Questions.json" {{var::f}}|
		/db-disable source=chat CMC Questions.json|
	:}|
:}|

/ife ( 'CMC Rules' not in lorebookList) {:
	/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/LoreBooks/{{getvar::model}}/CMC%20Rules.json|
	/let key=f {{pipe}}|
	/ife ( 'CMC Rules.json' not in databaseList){:
		/db-add source=chat name="CMC Rules.json" {{var::f}}|
		/db-disable source=chat CMC Rules.json|
	:}|
	/else {:
		/db-update source=chat name="CMC Rules.json" {{var::f}}|
		/db-disable source=chat CMC Rules.json|
	:}|
:}|

/ife ( 'CMC Templates' not in lorebookList) {:
	/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/LoreBooks/{{getvar::model}}/CMC%20Templates.json|
	/let key=f {{pipe}}|
	/ife ( 'CMC Templates.json' not in databaseList){:
		/db-add source=chat name="CMC Templates.json" {{var::f}}|
		/db-disable source=chat CMC Templates.json|
	:}|
	/else {:
		/db-update source=chat name="CMC Templates.json" {{var::f}}|
		/db-disable source=chat CMC Templates.json|
	:}|
:}|

/ife ( 'CMC Variables' not in lorebookList) {:
	/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/LoreBooks/{{getvar::model}}/CMC%20Variables.json|
	/let key=f {{pipe}}|
	/ife ( 'CMC Variables.json' not in databaseList){:
		/db-add source=chat name="CMC Variables.json" {{var::f}}|
		/db-disable source=chat CMC Variables.json|
	:}|
	/else {:
		/db-update source=chat name="CMC Variables.json" {{var::f}}|
		/db-disable source=chat CMC Variables.json|
	:}|
:}|

/popup Download all .json files (Should be 6 of them) from SillyTavern Data Bank (It will open when you press ok) and import them into the lorebook/World Info.|
/db|