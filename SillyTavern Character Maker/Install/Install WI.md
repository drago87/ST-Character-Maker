/wi-list-books all=true|
/let key=lorebookList {{pipe}}|

/db-list source=chat field=name |
/let key=databaseList {{pipe}}|

/foreach {{getglobalvar::models}} {:
	/ife ( 'CMC Generation Prompts {{var::item}}' not in lorebookList) {:
		/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/LoreBooks/{{var::item}}/CMC%20Generation%20Prompts%20{{var::item}}.json|
		/let key=f {{pipe}}|
		/ife ( 'CMC Generation Prompts {{var::item}}.json' not in databaseList){:
			/db-add source=chat name="CMC Generation Prompts {{var::item}}.json" {{var::f}}|
			/db-disable source=chat CMC Generation Prompts {{var::item}}.json|
		:}|
		/else {:
			/db-update source=chat name="CMC Generation Prompts {{var::item}}.json" {{var::f}}|
			/db-disable source=chat CMC Generation Prompts {{var::item}}.json|
		:}|
	:}|
	
	/ife ( 'CMC Information {{var::item}}' not in lorebookList) {:
		/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/LoreBooks/{{var::item}}/CMC%20Information%20{{var::item}}.json|
		/let key=f {{pipe}}|
		/ife ( 'CMC Generation Prompts {{var::item}}.json' not in databaseList){:
			/db-add source=chat name="CMC Information {{var::item}}.json" {{var::f}}|
			/db-disable source=chat CMC Information {{var::item}}.json|
		:}|
		/else {:
			/db-update source=chat name="CMC Information {{var::item}}.json" {{var::f}}|
			/db-disable source=chat CMC Information {{var::item}}.json|
		:}|
	:}|
:}|

/ife ( 'CMC Variables' not in lorebookList) {:
	/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/LoreBooks/{{var::item}}/CMC%20Variables.json|
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

/ife ( 'CMC Questions' not in lorebookList) {:
	/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/LoreBooks/General/CMC%20Questions.json|
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
	/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/LoreBooks/General/CMC%20Rules.json|
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
	/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/LoreBooks/General/CMC%20Templates.json|
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

/ife ( 'CMC Static Variables' not in lorebookList) {:
	/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/LoreBooks/General/CMC%20Static%20Variables.json|
	/let key=f {{pipe}}|
	/ife ( 'CMC Static Variables.json' not in databaseList){:
		/db-add source=chat name="CMC Static Variables.json" {{var::f}}|
		/db-disable source=chat CMC Static Variables.json|
	:}|
	/else {:
		/db-update source=chat name="CMC Static Variables.json" {{var::f}}|
		/db-disable source=chat CMC Static Variables.json|
	:}|
:}|

/ife ( 'CMC Guides' not in lorebookList) {:
	/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/LoreBooks/General/CMC%20Guides.json|
	/let key=f {{pipe}}|
	/ife ( 'CMC Guides.json' not in databaseList){:
		/db-add source=chat name="CMC Guides.json" {{var::f}}|
		/db-disable source=chat CMC Guides.json|
	:}|
	/else {:
		/db-update source=chat name="CMC Guides.json" {{var::f}}|
		/db-disable source=chat CMC Guides.json|
	:}|
:}|

/let key=counter 6|
/len {{getglobalvar::models}}|
/mul {{pipe}} 2|
/add {{pipe}} counter|
/var key=counter {{pipe}}|
/popup Download all .json files starting with CMC (Should be {{var::counter}} of them) from SillyTavern Data Bank (It will open when you press ok) and import them into the lorebook/World Info.|
/db|