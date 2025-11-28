/buttons labels=["Change Model", "Add New Model", "Update QR Scripts", "Download Model Lorebooks", "Download newest version of Lorebooks"] What do you want to do?|
/let key=selection {{pipe}}|

/ife (selection == 'Change Model') {:
	/findentry field=comment file="CMC Variables" "Models"|
	/let key=wi_uid {{pipe}}|
	/getentryfield field=content file="CMC Variables" {{var::wi_uid}}|
	/let key=selectModels {{pipe}}|
	/buttons multiple=true labels={{var::selectModels}} Select the model prompts you want use for generation.|
	/setglobalvar key=model {{pipe}}|
	/ife (model == '') {:
		/echo Aborting |
		/abort
	:}|
:}|


/ife (selection == 'Add New Model') {:
	/buttons labels={{getglobalvar::models}} What model do you want to base the new model on?|
	/let key=selectedModel {{pipe}}|
	/ife (selectedModel == '') {:
		/echo Aborting |
		/abort
	:}|
	/input What is the name of the new model?|
	/let modelName {{pipe}}|
	/db-list source=chat field=name |
	/let key=databaseList {{pipe}}|
	
	/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/LoreBooks/{{var::selectedModel}}/CMC%20Generation%20Prompts%20{{var::selectedModel}}.json|
	/let key=f {{pipe}}|
	/ife ( 'CMC Generation Prompts {{var::modelName}}.json' not in databaseList){:
		/db-add source=chat name="CMC Generation Prompts {{var::modelName}}.json" {{var::f}}|
		/db-disable source=chat CMC Generation Prompts {{var::modelName}}.json|
	:}|
	/else {:
		/db-update source=chat name="CMC Generation Prompts {{var::modelName}}.json" {{var::f}}|
		/db-disable source=chat CMC Generation Prompts {{var::modelName}}.json|
	:}|
	
	/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/LoreBooks/{{var::selectedModel}}/CMC%20Information%20{{var::selectedModel}}.json|
	/var key=f {{pipe}}|
	/ife ( 'CMC Generation Prompts {{var::modelName}}.json' not in databaseList){:
		/db-add source=chat name="CMC Information {{var::modelName}}.json" {{var::f}}|
		/db-disable source=chat CMC Information {{var::modelName}}.json|
	:}|
	/else {:
		/db-update source=chat name="CMC Information {{var::modelName}}.json" {{var::f}}|
		/db-disable source=chat CMC Information {{var::modelName}}.json|
	:}|
	/addglobalvar key=models {{var::modelName}}|
	/join glue="{{newline}}---{{newline}}" {{getglobalvar::models}}|
	/let key=gluedModels {{pipe}}|
	/findentry field=comment file="CMC Variables" "Models"|
	/let key=wi_uid {{pipe}}|
	/setentryfield field=content file="CMC Variables" uid={{var::wi_uid}} {{var::gluedModels}}|
	/popup Don't forget to download the .json files from the databank. It will open automaticly.|
	/db
:}|

/elseif (selection == 'Update QR Scripts') {:
	/qr-set-delete CMC Generate|
	/qr-set-delete CMC Logic|
	/qr-chat-set-off CMC Main|
	/qr-set-delete CMC Main|
	//qr-set-delete CMC Menu|
	/qr-set-delete CMC Automate| 
	
	/wait 1000|
	/qr-set-create CMC Temp|
	/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/Install/Install%20QR.md|
	
	/qr-create set="CMC Temp" label="Install QR" {{pipe}}|
	
	/:"CMC Temp.Install QR"|
	
	/wait 1000|
	/qr-set-delete CMC Temp |
	/qr-delete set="CMC Menu" label="CMC Menu"|
	/qr-update set="CMC Menu" label="CMC Menu2" "CMC Menu"|
	/wait 10000|
	/forcesave|
	/wait 1000|
	/reload-page|
:}|

/ife (selection == 'Download Model Lorebooks') {:
	/buttons labels=["dans-personalityengine-v1.1.0-12b-q6_k", "EsotericSage-12B.i1-Q6_K"] Select the Model you want to download the Lorebooks for.|

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
	/var key=f {{pipe}}|
	/ife ( 'CMC Information {{var::selectedModel}}.json' not in databaseList){:
		/db-add source=chat name="CMC Information {{var::selectedModel}}.json" {{var::f}}|
		/db-disable source=chat CMC Information {{var::selectedModel}}.json|
	:}|
	/else {:
		/db-update source=chat name="CMC Information {{var::selectedModel}}.json" {{var::f}}|
		/db-disable source=chat CMC Information {{var::selectedModel}}.json|
	:}|
	/popup Don't forget to download the .json files from the databank. It will open automaticly.|
	/db
:}|

/ife (selection == 'Download newest version of Lorebooks') {:
	/setvar key=counter 0|
	/db-list source=chat field=name |
	/let key=databaseList {{pipe}}|
	/let key=f {{noop}}|
	
	/foreach {{getglobalvar::models}} {:
		/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/LoreBooks/{{var::item}}/CMC%20Generation%20Prompts%20{{var::item}}.json|
		/var key=f {{pipe}}|
		/addvar key=counter 1|
		
		/ife ( 'CMC Generation Prompts {{var::item}}.json' not in databaseList){:
			/db-add source=chat name="CMC Generation Prompts {{var::item}}.json" {{var::f}}|
			/db-disable source=chat CMC Generation Prompts {{var::item}}.json|
		:}|
		/else {:
			/db-update source=chat name="CMC Generation Prompts {{var::item}}.json" {{var::f}}|
			/db-disable source=chat CMC Generation Prompts {{var::item}}.json|
		:}|
		
		/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/LoreBooks/{{var::item}}/CMC%20Information%20{{var::item}}.json|
		/var key=f {{pipe}}|
		/addvar key=counter 1|
		
		/ife ( 'CMC Generation Prompts {{var::item}}.json' not in databaseList){:
			/db-add source=chat name="CMC Information {{var::item}}.json" {{var::f}}|
			/db-disable source=chat CMC Information {{var::item}}.json|
		:}|
		/else {:
			/db-update source=chat name="CMC Information {{var::item}}.json" {{var::f}}|
			/db-disable source=chat CMC Information {{var::item}}.json|
		:}|
	:}|
	
	/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/LoreBooks/General/CMC%20Variables.json |
	/var key=f {{pipe}}|
	/addvar key=counter 1|
	
	/ife ( 'CMC Variables.json' not in databaseList){:
		/db-add source=chat name="CMC Variables.json" {{var::f}}|
		/db-disable source=chat CMC Variables.json|
	:}|
	/else {:
		/db-update source=chat name="CMC Variables.json" {{var::f}}|
		/db-disable source=chat CMC Variables.json|
	:}|
	
	/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/LoreBooks/General/CMC%20Questions.json |
	/var key=f {{pipe}}|
	/addvar key=counter 1|
	
	/ife ( 'CMC Questions.json' not in databaseList){:
		/db-add source=chat name="CMC Questions.json" {{var::f}}|
		/db-disable source=chat CMC Questions.json|
	:}|
	/else {:
		/db-update source=chat name="CMC Questions.json" {{var::f}}|
		/db-disable source=chat CMC Questions.json|
	:}|
	
	/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/LoreBooks/General/CMC%20Rules.json |
	/var key=f {{pipe}}|
	/addvar key=counter 1|
	
	/ife ( 'CMC Rules.json' not in databaseList){:
		/db-add source=chat name="CMC Rules.json" {{var::f}}|
		/db-disable source=chat CMC Rules.json|
	:}|
	/else {:
		/db-update source=chat name="CMC Rules.json" {{var::f}}|
		/db-disable source=chat CMC Rules.json|
	:}|
	
	/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/LoreBooks/General/CMC%20Templates.json |
	/var key=f {{pipe}}|
	/addvar key=counter 1|
	
	/ife ( 'CMC Templates.json' not in databaseList){:
		/db-add source=chat name="CMC Templates.json" {{var::f}}|
		/db-disable source=chat CMC Templates.json|
	:}|
	/else {:
		/db-update source=chat name="CMC Templates.json" {{var::f}}|
		/db-disable source=chat CMC Templates.json|
	:}|
	
	/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/LoreBooks/General/CMC%20Static%20Variables.json |
	/var key=f {{pipe}}|
	/addvar key=counter 1|
	
	/ife ( 'CMC Static Variables.json' not in databaseList){:
		/db-add source=chat name="CMC Static Variables.json" {{var::f}}|
		/db-disable source=chat CMC Static Variables.json|
	:}|
	/else {:
		/db-update source=chat name="CMC Static Variables.json" {{var::f}}|
		/db-disable source=chat CMC Static Variables.json|
	:}|
	
	/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/LoreBooks/General/CMC%20Guides.json |
	/var key=f {{pipe}}|
	/addvar key=counter 1|
	
	/ife ( 'CMC Guides.json' not in databaseList){:
		/db-add source=chat name="CMC Guides.json" {{var::f}}|
		/db-disable source=chat CMC Guides.json|
	:}|
	/else {:
		/db-update source=chat name="CMC Guides.json" {{var::f}}|
		/db-disable source=chat CMC Guides.json|
	:}|
	
	/buttons labels=["Yes", "No"] Do you want to download the optional CMC Anatomy (WIP) lorebook?|
	/let key=button {{pipe}}|
	/ife (button == 'Yes') {:
		/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/LoreBooks/General/CMC%20Anatomy.json |
		/var key=f {{pipe}}|
		/addvar key=counter 1|
		
		/ife ( 'CMC Guides.json' not in databaseList){:
			/db-add source=chat name="CMC Anatomy.json" {{var::f}}|
			/db-disable source=chat CMC Anatomy.json|
		:}|
		/else {:
			/db-update source=chat name="CMC Anatomy.json" {{var::f}}|
			/db-disable source=chat CMC Anatomy.json|
		:}|
	:}|
	
	
	/popup Download all .json files starting with CMC (Should be {{getvar::counter}} of them) from SillyTavern Data Bank (It will open when you press ok) and import them into the lorebook/World Info.|
	/db|
	/flushvar counter|
	/echo extendedTimeout=0 timeout=0 awaitDismissal=true Press to Continue|
:}|