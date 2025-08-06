/let key=models ["dans-personalityengine-v1.1.0-12b-q6_k", "EsotericSage-12B.i1-Q6_K"]|
/buttons labels={{var::models}} Select the model you want to download the model lorebook prompts for.|
/setglobalvar key=model {{pipe}}|
/ife (model == '') {:
	/echo Aborting |
	/abort
:}|
/elseif (model == 'dans-personalityengine-v1.1.0-12b-q6_k') {:
	/popup <div>Prompts are tested with this model.</div><div><a href="https://huggingface.co/bartowski/Dans-PersonalityEngine-V1.1.0-12b-GGUF/blob/main/Dans-PersonalityEngine-V1.1.0-12b-Q6_K.gguf">Dans-PersonalityEngine-V1.1.0-12b-Q6_K.gguf</a></div>|
:}|
/elseif (model == 'EsotericSage-12B.i1-Q6_K') {:
	/popup <div>Prompts are tested with this model.</div><div><a href="https://huggingface.co/mradermacher/EsotericSage-12B-i1-GGUF/blob/main/EsotericSage-12B.i1-Q6_K.gguf">EsotericSage-12B.i1-Q6_K.gguf</a></div>|
:}|

/db-list source=character field=name |
/let key=databaseList {{pipe}}|

/ife ('model' not in databaseList) {:
	/db-add source=character name=model {{getglobalvar::model}}|
	/db-disable source=character model|
:}|
/else {:
	/db-update source=character name=model {{getglobalvar::model}}|
	/db-disable source=character model|
:}|

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
<div><a href="https://github.com/drago87/ST-Character-Maker/blob/Fetch-Files/SillyTavern%20Character%20Maker/QR%20Sets/CMC%20Generate.json">CMC Generate</a></div><div><a href="https://github.com/drago87/ST-Character-Maker/blob/Fetch-Files/SillyTavern%20Character%20Maker/QR%20Sets/CMC%20Logic.json">CMC Logic</a></div><div><a href="https://github.com/drago87/ST-Character-Maker/blob/Fetch-Files/SillyTavern%20Character%20Maker/QR%20Sets/CMC%20Main.json">CMC Main</a></div>|
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
	/buttons labels=["Manually", "Semi Automatically"] Do you want to Manually or Automatically download the World Info/Lore Book?|
	/let key=selected_btn {{pipe}}|
	
	/ife ( selected_btn == '') {:
		/echo Aborting |
		/abort|
	:}|
	/elseif ( selected_btn == 'Manually') {:
		/popup <div>You need to manually download these files and import them to the World Info</div>
	<div><a href="https://github.com/drago87/ST-Character-Maker/blob/Fetch-Files/SillyTavern%20Character%20Maker/LoreBooks/{{getglobalvar::model}}/CMC%20Generation%20Prompts.json">CMC Generation Prompts</a></div>
	<div><a href="https://github.com/drago87/ST-Character-Maker/blob/Fetch-Files/SillyTavern%20Character%20Maker/LoreBooks/{{getglobalvar::model}}/CMC%20Information.json">CMC Information</a></div>
	<div><a href="https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/LoreBooks/{{getglobalvar::model}}/CMC%20Questions.json">CMC Questions</a></div>
	<div><a href="https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/LoreBooks/{{getglobalvar::model}}/CMC%20Rules.json">CMC Rules</a></div>
	<div><a href="https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/LoreBooks/{{getglobalvar::model}}/CMC%20Templates.json">CMC Templates</a></div>
	<div><a href="https://github.com/drago87/ST-Character-Maker/blob/Fetch-Files/SillyTavern%20Character%20Maker/LoreBooks/{{getglobalvar::model}}/CMC%20Variablers.json">CMC Variablers</a></div>|
	
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