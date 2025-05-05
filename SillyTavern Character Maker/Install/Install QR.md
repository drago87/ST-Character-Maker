/qr-set-list all|
/let key=qrList {{pipe}}|

/ife ('CMC Main' in qrList) {:
	/buttons labels=["Yes", "No"] want to update CMC Main scripts?|
	/let selected_btn {{pipe}}|
	/ife ( selected_btn == Yes) {:
		/qr-chat-set-off CMC Main|
		/qr-set-create CMC Main|
	:}|
:}|
/else {:
	/qr-set-create CMC Main|
:}|


//Create JEDParse|
/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/Replace/JED%20Parse.md|
/setvar key=jedParse {{pipe}}|
//-----|

//Create TextParse|
/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/Replace/Text%20Parse.md|
/setvar key=textParse {{pipe}}|
//-----|

//-----|
/qr-list CMC Main|
/let key=qrListContent {{pipe}}|

//New Char|
/ife ('New Character' not in qrListContent) {:
	/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/Visible%20QR%20Buttons/New%20Char.md|
	
	/re-replace find="/--JEDParse--/g" replace="{{getvar::jedParse}}" {{pipe}}|
	/re-replace find="/--TextParse--/g" replace="{{getvar::textParse}}" {{pipe}}|
	/qr-create set="CMC Main" label="New Character" title="Will make a new character and let you set the Gender, type(Human, Anthro etc..)" {{pipe}}|
	/qr-update set="CMC Main" label="New Character" title="Make a character from the beginning."|
:}|
//|-----|
/wait 100|
/qr-list CMC Main|
/getat index=1 {{pipe}}|
/let key=qrlabel {{pipe}}|
/let key=temp {{noop}}|
/ife ( qrlabel != '') {:
	/qr-get set="CMC Main" label={{var::qrlabel}}|
	/getat index="message" {{pipe}}|
	/var key=temp {{pipe}}|
:}|


//Create Character Generation|
/ife ('{{var::temp}}' not in qrList) {:
	/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/Visible%20QR%20Buttons/Character%20Generation.md|
	
	/re-replace find="/--JEDParse--/g" replace="{{getvar::jedParse}}" {{pipe}}|
	/re-replace find="/--TextParse--/g" replace="{{getvar::textParse}}" {{pipe}}|
	/qr-create set="CMC Main" label="Character Generation" {{pipe}}|
	/qr-update set="CMC Main" label="Character Generation" title="Continues/Restart the last Generation or Starts the next Generation."|
	/qr-chat-set-on CMC Main|
:}|
//|-----|


/qr-list CMC Logic|
/var key=qrListContent {{pipe}}|

/ife ('CMC Logic' in qrList) {:
	/buttons labels=["Yes", "No"] want to update CMC Logic scripts?|
	/let selected_btn {{pipe}}|
	/ife ( selected_btn == Yes) {:
		/qr-chat-set-off CMC Logic|
		/qr-set-create CMC Logic|
	:}|
:}|
/else {:
	/qr-set-create CMC Logic|
:}|

//Combine Lorbook|
/ife ( 'Combine Lorbook' not in qrListContent) {:
	/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/Replace/Combine%20List%20Lorebooks.md|
	
	/qr-create set="CMC Logic" label="Combine Lorbook" {{pipe}}|
:}|
//-----|


//Create SaveGen|
/ife ( 'SaveGen' not in qrListContent) {:
	/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/Replace/SaveGen.md|
	/qr-create set="CMC Logic" label="SaveGen" {{pipe}}|
:}|
//-----|


//Create GenerateWithPrompt|
/ife ( 'GenerateWithPrompt' not in qrListContent) {:
	/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/Replace/Generate%20with%20Prompt.md|
	/qr-create set="CMC Logic" label="GenerateWithPrompt" {{pipe}}|
:}|
//-----|

//Create GenerateWithSelector|
/ife ( 'GenerateWithSelector' not in qrListContent) {:
	/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/Replace/Selector.md|
	
	/qr-create set="CMC Logic" label="GenerateWithSelector" {{pipe}}|
:}|
//-----|

/ife ( 'Get Char info' not in qrListContent) {:
	//Get Char info|
	/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/Functions/Get%20Character%20information.md|
	
	/re-replace find="/--JEDParse--/g" replace="{{getvar::jedParse}}" {{pipe}}|
	/re-replace find="/--TextParse--/g" replace="{{getvar::textParse}}" {{pipe}}|
	
	
	/qr-create set="CMC Logic" label="Get Char info" {{pipe}}|
	//|-----|
:}|

/ife ( 'Is Real' not in qrListContent) {:
	//Is Real|
	/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/Functions/Is%20Real.md|
	
	/re-replace find="/--JEDParse--/g" replace="{{getvar::jedParse}}" {{pipe}}|
	/re-replace find="/--TextParse--/g" replace="{{getvar::textParse}}" {{pipe}}|
	
	
	/qr-create set="CMC Logic" label="Is Real" {{pipe}}|
	//|-----|
:}|

/ife ( 'Parse' not in qrListContent) {:
	//Parse|
	/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/Functions/Parse.md|
	/qr-create set="CMC Logic" label="Parse" {{pipe}}|
	//|-----|
:}|

/ife ( 'Save DataBase' not in qrListContent) {:
	//Save DataBase|
	/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/Functions/Save%20DataBase.md|
	/qr-create set="CMC Logic" label="Save DataBase" {{pipe}}|
	//|-----|
:}|

//Generate|
/ife ('CMC Generate' in qrList) {:
	/buttons labels=["Yes", "No"] want to update CMC Generate scripts?|
	/let selected_btn {{pipe}}|
	/ife ( selected_btn == Yes) {:
		/qr-chat-set-off CMC Generate|
		/qr-set-create CMC Generate|
	:}|
:}|
/else {:
	/qr-set-create CMC Generate|
:}|

/ife ( 'Generate World Info' not in qrListContent) {:
	//Generate World Info|
	/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/Generate/Generate%20Basic%20World%20Info.md|
	
	/re-replace find="/--JEDParse--/g" replace="{{getvar::jedParse}}" {{pipe}}|
	/re-replace find="/--TextParse--/g" replace="{{getvar::textParse}}" {{pipe}}|
	/qr-create set="CMC Generate" label="Generate World Info" {{pipe}}|
	//|-----|
:}|

/ife ( 'Generate Character Information' not in qrListContent) {:
	//Generate Character Information|
	/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/Generate/Generate%20Character%20Information.md|
	
	/re-replace find="/--JEDParse--/g" replace="{{getvar::jedParse}}" {{pipe}}|
	/re-replace find="/--TextParse--/g" replace="{{getvar::textParse}}" {{pipe}}|
	/qr-create set="CMC Generate" label="Generate Character Information" {{pipe}}|
	//|-----|
:}|

/qr-chat-set-on visible=true "CMC Main"|
/flushvar jedParse|
/flushvar textParse|