/buttons labels=["Change Model", "Add New Model", "Update QR Scripts", "Download WI"] What do you want to do?|
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
	/qr-set-delete CMC Menu|
	/qr-set-delete CMC Automate| 
	
	/wait 1000|
	/qr-set-create CMC Temp|
	/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/Install/Install%20QR.md|
	
	/qr-create set="CMC Temp" label="Install QR" {{pipe}}|
	
	/:"CMC Temp.Install QR"|
	
	/wait 1000|
	/qr-set-delete CMC Temp |
	/wait 10000|
	/reload-page|
:}|

/ife (selection == 'Download WI') {:
	/buttons labels=["dans-personalityengine-v1.1.0-12b-q6_k", "EsotericSage-12B.i1-Q6_K"] Select the Model you want to download the WI for.|

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