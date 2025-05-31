/wi-list-books all=true|
/let key=lorebookList {{pipe}}|

/db-list source=chat field=name |
/let key=databaseList {{pipe}}|

/ife ( 'CMC Clothes' not in lorebookList) {:
	/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/LoreBooks/CMC%20Clothes.json|
	/let key=f {{pipe}}|
	/ife ( 'CMC Clothes.json' not in databaseList){:
		/db-add source=chat name="CMC Clothes.json" {{var::f}}|
		/db-disable source=chat CMC Clothes.json|
	:}|
	/else {:
		/db-update source=chat name="CMC Clothes.json" {{var::f}}|
		/db-disable source=chat CMC Clothes.json|
	:}|
:}|

/ife ( 'CMC Variables' not in lorebookList) {:
	/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/LoreBooks/CMC%20Variables.json|
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

/ife ( 'CMC Personality' not in lorebookList) {:
	/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/LoreBooks/CMC%20Personality.json|
	/let key=f {{pipe}}|
	/ife ( 'CMC Personality.json' not in databaseList){:
		/db-add source=chat name="CMC Personality.json" {{var::f}}|
		/db-disable source=chat CMC Personality.json|
	:}|
	/else {:
		/db-update source=chat name="CMC Personality.json" {{var::f}}|
		/db-disable source=chat CMC Personality.json|
	:}|
:}|

/ife ( 'CMC Generation Prompts' not in lorebookList) {:
	/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/LoreBooks/CMC%20Generation%20Prompts.json|
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
	/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/LoreBooks/CMC%20Information.json|
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

/ife ( 'CMC Rules' not in lorebookList) {:
	/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/LoreBooks/CMC%20Information.json|
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

/popup Download all .json files (Should be 6 of them) from SillyTavern Data Bank (It will open when you press ok) and import them into the lorebook/World Info.|
/db|