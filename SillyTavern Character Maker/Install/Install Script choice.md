/let key=models ["dans-personalityengine-v1.1.0-12b-q6_k", "EsotericSage-12B.i1-Q6_K"]|
/buttons multiple=true labels={{var::models}} Select the models you want to download the model lorebook prompts for.|
/setglobalvar key=models {{pipe}}|
/ife (models == '') {:
	/echo Aborting |
	/abort
:}|

/setvar key=choicePrompt 
Prompts are tested with this model.|

/ife ('dans-personalityengine-v1.1.0-12b-q6_k' in models) {:
	/addvar key=choicePrompt <div><a href="https://huggingface.co/bartowski/Dans-PersonalityEngine-V1.1.0-12b-GGUF/blob/main/Dans-PersonalityEngine-V1.1.0-12b-Q6_K.gguf">Dans-PersonalityEngine-V1.1.0-12b-Q6_K.gguf</a></div>|
:}|
/ife ('EsotericSage-12B.i1-Q6_K' in models) {:
	/addvar key=choicePrompt <div><a href="https://huggingface.co/mradermacher/EsotericSage-12B-i1-GGUF/blob/main/EsotericSage-12B.i1-Q6_K.gguf">EsotericSage-12B.i1-Q6_K.gguf</a></div>|
:}|

/popup {{getvar::choicePrompt}}|

/db-list source=character field=name |
/let key=databaseList {{pipe}}|

/*
/ife ('model' not in databaseList) {:
	/db-add source=character name=model {{getglobalvar::model}}|
	/db-disable source=character model|
:}|
/else {:
	/db-update source=character name=model {{getglobalvar::model}}|
	/db-disable source=character model|
:}|
*|

/qr-list CMC Temp|
/let key=qrList {{pipe}}|

/ife ('Character maker install script' in qrList) {:
	/qr-delete set="CMC Temp" label="Character maker install script"|
	/qr-update set="CMC Temp" label="Install Script" title="A script that will walk you through the setup."|
	/qr-chat-set-on CMC Temp|
:}|
/qr-set-list all|
/var key=qrList {{pipe}}|

/ife ('CMC Main' not in qrList) {:
	/buttons labels=["Manually", "Automatically"] Do you want to Manually or Automatically download the QR scripts?|
	/setvar key=selected_btn {{pipe}}|

	/ife ( selected_btn == '') {:
		/echo Aborting |
		/abort|
	:}|
	/elseif ( selected_btn == 'Manually') {:
		/popup <div>You need to manually download these files and import them to Extensions → Quick Reply</div>
<div><a href="https://github.com/drago87/ST-Character-Maker/blob/Fetch-Files/SillyTavern%20Character%20Maker/QR%20Sets/CMC%20Generate.json">CMC Generate</a></div><div><a href="https://github.com/drago87/ST-Character-Maker/blob/Fetch-Files/SillyTavern%20Character%20Maker/QR%20Sets/CMC%20Logic.json">CMC Logic</a></div><div><a href="https://github.com/drago87/ST-Character-Maker/blob/Fetch-Files/SillyTavern%20Character%20Maker/QR%20Sets/CMC%20Main.json">CMC Main</a></div><div><a href="https://github.com/drago87/ST-Character-Maker/blob/Fetch-Files/SillyTavern%20Character%20Maker/QR%20Sets/CMC%20Automate.json">CMC Automate (optional but recommended)</a></div>|
	:}|
	/elseif ( selected_btn == 'Automatically') {:
		/qr-list CMC Temp|
		/let x {{pipe}}|
		/ife ('Install QR' not in x) {:
			/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/Install/Install%20QR.md|
			/qr-create set="CMC Temp" label="Install QR" {{pipe}}|
		:}|
		//[[Install QR]]|
		/:"CMC Temp.Install QR"|
		/qr-delete set="CMC Temp" label="Install QR"|
	:}|
:}|

/ife ( selected_btn != '') {:
	/buttons labels=["Manually", "Semi Automatically"] Do you want to Manually or Semi Automatically download the World Info/Lore Book?|
	/let key=selected_btn {{pipe}}|
	
	/ife ( selected_btn == '') {:
		/echo Aborting |
		/abort|
	:}|
	/elseif ( selected_btn == 'Manually') {:
		/setvar key=popupLinks "Model Specific Lorebooks"|
		/foreach {{getglobalvar::models}} {:
			/addvar key=popupLinks "<div><a href="https://github.com/drago87/ST-Character-Maker/blob/Fetch-Files/SillyTavern%20Character%20Maker/LoreBooks/{{var::item}}/CMC%20Generation%20Prompts%20{{var::item}}.json">CMC Generation Prompts {{var::item}}</a></div>|
			/addvar key=popupLinks "<div><a href="https://github.com/drago87/ST-Character-Maker/blob/Fetch-Files/SillyTavern%20Character%20Maker/LoreBooks/{{var::item}}/CMC%20Information%20{{var::item}}.json">CMC Information {{var::item}}</a></div>|
			/addvar key=popupLinks "<div>---</div>"|
	
		:}|
		/popup <div>You need to manually download these files and import them to the World Info</div>
		{{getvar::popupLinks}}
		<div>General Lorebooks</div>
	<div><a href="https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/LoreBooks/General/CMC%20Questions.json">CMC Questions</a></div>
	<div><a href="https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/LoreBooks/General/CMC%20Rules.json">CMC Rules</a></div>
	<div><a href="https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/LoreBooks/General/CMC%20Templates.json">CMC Templates</a></div>
	<div><a href="https://github.com/drago87/ST-Character-Maker/blob/Fetch-Files/SillyTavern%20Character%20Maker/LoreBooks/General/CMC%20%20Static%20Variablers.json">CMC Static Variablers</a></div>
	<div><a href="https://github.com/drago87/ST-Character-Maker/blob/Fetch-Files/SillyTavern%20Character%20Maker/LoreBooks/General/CMC%20Variables.json">CMC Variablers</a></div>
	<div><a href="https://github.com/drago87/ST-Character-Maker/blob/Fetch-Files/SillyTavern%20Character%20Maker/LoreBooks/General/CMC%20Anatomy.json">CMC Anatomy (Optional, WIP)</a></div>|
	
	:}|
	/elseif ( selected_btn == 'Semi Automatically') {:
		/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/Install/Install%20WI.md|
		/qr-create set="CMC Temp" label="Install WI" {{pipe}}|
		//[[Install WI]]|
		/:"CMC Temp.Install WI"|
		/qr-delete set="CMC Temp" label="Install WI"
	:}|
	
	/ife ( selected_btn == '') {:
		/echo Aborting |
		/abort|
	:}|
	/else {:
		/qr-set-list all|
		/var qrList {{pipe}}|
		/ife ( 'CMC Temp' in qrList ) {:
			/qr-chat-set-off CMC Temp|
			/qr-set-delete CMC Temp|
		:}|
	:}|
:}|

/flushvar selected_btn|
/flushvar popupLinks|