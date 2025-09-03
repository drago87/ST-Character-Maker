unambiguous

/let key=selectedModel {{pipe}}|
/db-list source=chat field=name |
	/let key=databaseList {{pipe}}|
	
	/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/LoreBooks/{{var::selectedModel}}/CMC%20Generation%20Prompts%20{{var::selectedModel}}.json|
	/let key=f {{pipe}}|
	/ife ( 'CMC Generation Prompts {{var::selectedModel}}.json' not in databaseList){:
		/db-add source=chat name="CMC Generation Prompts {{var::selectedModel}}.json" {{var::f}}|
		/db-disable source=chat CMC Generation Prompts {{var::selectedModel}}.json|
	:}|
	/else {:
		/db-update source=chat name="CMC Generation Prompts {{var::selectedModel}}.json" {{var::f}}|
		/db-disable source=chat CMC Generation Prompts {{var::selectedModel}}.json|
	:}|
	
	/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/LoreBooks/{{var::selectedModel}}/CMC%20Information%20{{var::selectedModel}}.json|
	/let key=f {{pipe}}|
	/ife ( 'CMC Generation Prompts {{var::selectedModel}}.json' not in databaseList){:
		/db-add source=chat name="CMC Information {{var::selectedModel}}.json" {{var::f}}|
		/db-disable source=chat CMC Information {{var::selectedModel}}.json|
	:}|
	/else {:
		/db-update source=chat name="CMC Information {{var::selectedModel}}.json" {{var::f}}|
		/db-disable source=chat CMC Information {{var::selectedModel}}.json|
	:}|