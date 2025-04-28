/wi-list-books all=true|
/let key=lorebookList {{pipe}}|

/db-list source=chat field=name |
/let key=databaseList {{pipe}}|

/ife ( 'CMC Clothes' not in lorebookList) {:
	/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/LoreBooks/CMC%20Clothes.json|
	/let key=f {{pipe}}|
	/ife ( 'CMC Clothes' not in databaseList){:
		/db-add source=chat name="CMC Clothes.json" {{var::f}}|
		/db-disable source=chat CMC Clothes.json|
	:}|
	/else {:
		/db-update source=chat name="CMC Clothes.json" {{var::f}}|
		/db-disable source=chat CMC Clothes.json|
	:}|
:}|

/ife ( 'CMC Appearance' not in lorebookList) {:
	/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/LoreBooks/CMC%20Appearance.json|
	/let key=f {{pipe}}|
	/ife ( 'CMC Appearance' not in databaseList){:
		/db-add source=chat name="CMC Appearance.json" {{var::f}}|
		/db-disable source=chat CMC Appearance.json|
	:}|
	/else {:
		/db-update source=chat name="CMC Appearance.json" {{var::f}}|
		/db-disable source=chat CMC Appearance.json|
	:}|
:}|

/ife ( 'CMC Variablers' not in lorebookList) {:
	/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/LoreBooks/CMC%20Variablers.json|
	/let key=f {{pipe}}|
	/ife ( 'CMC Variablers' not in databaseList){:
		/db-add source=chat name="CMC Variablers.json" {{var::f}}|
		/db-disable source=chat CMC Variablers.json|
	:}|
	/else {:
		/db-update source=chat name="CMC Variablers.json" {{var::f}}|
		/db-disable source=chat CMC Variablers.json|
	:}|
:}|

/ife ( 'CMC Personality' not in lorebookList) {:
	/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/LoreBooks/CMC%20Personality.json|
	/let key=f {{pipe}}|
	/ife ( 'CMC Personality' not in databaseList){:
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
	/ife ( 'CMC Generation Prompts' not in databaseList){:
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
	/ife ( 'CMC Generation Prompts' not in databaseList){:
		/db-add source=chat name="CMC Generation Prompts.json" {{var::f}}|
		/db-disable source=chat CMC Generation Prompts.json|
	:}|
	/else {:
		/db-update source=chat name="CMC Generation Prompts.json" {{var::f}}|
		/db-disable source=chat CMC Generation Prompts.json|
	:}|
:}|

/popup Download all .json files (Should be 6 of them)  from SillyTavern Data Bank (It will open when you press ok) and import them into the lorebook/World Info.|
/db|