/qr-set-list|

/buttons labels=["Manually", "Automatically"] Do you want to Manually or Automatically download the World Info/Lore Book?|
/setvar key=selected_btn {{pipe}}|

/ife ( selected_btn == 'Manually') {:
	/popup WIP<div>You need to manually download these files and import them to the World Info</div>
<div><a href="https://github.com/drago87/ST-Character-Maker/blob/main/Lorebooks/Character%20Maker%20Combined%20NSFW%20GenRaw.json">Character Maker Combined NSFW GenRaw</a></div>
<div><a href="https://github.com/drago87/ST-Character-Maker/blob/main/Lorebooks/Character%20Maker%20Combined%20NSFW%20Variables.json">Character Maker Combined NSFW Variables</a></div>
<div><a href="https://github.com/drago87/ST-Character-Maker/blob/main/Lorebooks/Character%20Maker%20Combined%20NSFW.json">Character Maker Combined NSFW</a></div>

:}|
/elseif ( selected_btn == 'Automatically') {:
	/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/Install/Install%20WI.md|
	/qr-create set="CMC Temp" label="Install Wi" {{pipe}}|
	//[[Install WI]]|
	/:"CMC Temp.Install WI"|
	/qr-delete set="CMC Temp" label="Install Wi"
:}|

/setvar key=qr-list {{pipe}}|
/ife (('CMC Main' not in qr-list) and ('CMC Logic' not in qr-list)) {:
	/buttons labels=["Manually", "Automatically"] Do you want to Manually or Automatically download the QR scripts?|
	/setvar key=selected_btn {{pipe}}|
	
	/ife ( selected_btn == 'Manually') {:
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