/qr-list CMC Temp|
/let key=qrList {{pipe}}|

/ife ('Character maker install script' in qrList) {:
	/qr-delete set="CMC Temp" label="Character maker install script"|
	/qr-chat-set-on CMC Temp|
:}|
/qr-set-list all|
/var key=qrList {{pipe}}|

/ife ('CMC Main' not in qrList) {:
	/buttons labels=["Manually", "Automatically"] Do you want to Manually or Automatically download the QR scripts?|
	/setvar key=selected_btn {{pipe}}|

	/ife ( selected_btn == '') {:
		/echo Aborting |
		/break|
	:}|
	/elseif ( selected_btn == 'Manually') {:
		/popup WIP<div>You need to manually download these files and import them to Extensions → Quick Reply</div>
<div><a href="https://github.com/drago87/ST-Character-Maker/blob/main/Quick%20Reply%20Buttons/Character%20Maker%20V4.json">CMC Logic</a></div>
<div>Optional Downloads</div><div><a href="https://github.com/drago87/ST-Character-Maker/blob/main/Quick%20Reply%20Buttons/Autorun.json">CMC Autorun</a></div>|
	:}|
	/elseif ( selected_btn == 'Automatically') {:
		/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/Install/Install%20QR.md|
		/qr-create set="CMC Temp" label="Install QR" {{pipe}}|
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
		/break|
	:}|
	/elseif ( selected_btn == 'Manually') {:
		/popup <div>You need to manually download these files and import them to the World Info</div>
	<div><a href="https://github.com/drago87/ST-Character-Maker/blob/Fetch-Files/SillyTavern%20Character%20Maker/LoreBooks/CMC%20Appearance.json">CMC Appearance</a></div>
	<div><a href="https://github.com/drago87/ST-Character-Maker/blob/Fetch-Files/SillyTavern%20Character%20Maker/LoreBooks/CMC%20Clothes.json">CMC Clothes</a></div>
	<div><a href="https://github.com/drago87/ST-Character-Maker/blob/Fetch-Files/SillyTavern%20Character%20Maker/LoreBooks/CMC%20Generation%20Prompts.json">CMC Generation Prompts</a></div>
	<div><a href="https://github.com/drago87/ST-Character-Maker/blob/Fetch-Files/SillyTavern%20Character%20Maker/LoreBooks/CMC%20Information.json">CMC Information</a></div>
	<div><a href="https://github.com/drago87/ST-Character-Maker/blob/Fetch-Files/SillyTavern%20Character%20Maker/LoreBooks/CMC%20Personality.json">CMC Personality</a></div>
	<div><a href="https://github.com/drago87/ST-Character-Maker/blob/Fetch-Files/SillyTavern%20Character%20Maker/LoreBooks/CMC%20Variablers.json">CMC Variablers</a></div>|
	
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
		/break|
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