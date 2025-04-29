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
//Create Temporary Variables|
/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/Functions/TempVariables.md|
/setvar key=tempVars {{pipe}}|
//|-----|

/qr-list CMC Main|
/let key=qrListContent {{pipe}}|

//New Char|
/ife ('New Character' not in qrList) {:
	/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/Visible%20QR%20Buttons/New%20Char.md|
	/re-replace find="/--Replace--/g" replace="{{getvar::tempVars}}" {{pipe}}|
	/qr-create set="CMC Main" label="New Character" title="Will make a new character and let you set the Gender, type(Human, Anthro etc..)" {{pipe}}|
	/qr-update set="CMC Main" label="New Character" title="Make a character from the beginning."|
:}|
//|-----|

//Create Character Generation|
/ife ( ('Character Generation' not in qrList) and ('Start Generating' not in qrList) and ('Restart/Continue with a' not in qrList)) {:
	/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/Visible%20QR%20Buttons/Character%20Generation.md|
	/re-replace find="/--Replace--/g" replace="{{getvar::tempVars}}" {{pipe}}|
	/qr-create set="CMC Main" label="Character Generation" {{pipe}}|
	/qr-update set="CMC Main" label="Character Generation" title="Continues/Restart the last Generation or Starts the next Generation."|
	/qr-chat-set-on CMC Main|
:}|
//|-----|



/qr-set-create CMC Logic|

//Get Char info|
/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/Functions/Get%20Character%20information.md|
/re-replace find="/--Replace--/g" replace="{{getvar::tempVars}}" {{pipe}}|
/qr-create set="CMC Logic" label="Get Char info" {{pipe}}|
//|-----|

//Is Real|
/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/Functions/Is%20Real.md|
/re-replace find="/--Replace--/g" replace="{{getvar::tempVars}}" {{pipe}}|
/qr-create set="CMC Logic" label="Is Real" {{pipe}}|
//|-----|

//Text Parce|
/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/Functions/Text%20Parce.md|
/re-replace find="/--Replace--/g" replace="{{getvar::tempVars}}" {{pipe}}|
/qr-create set="CMC Logic" label="Text Parce" {{pipe}}|
//|-----|

//Save Gen|
/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/Functions/SaveGen.md|
/re-replace find="/--Replace--/g" replace="{{getvar::tempVars}}" {{pipe}}|
/qr-create set="CMC Logic" label="SaveGen" {{pipe}}|
//|-----|

//Combine List Lorebooks|
/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/Functions/Combine%20List%20Lorebooks.md|
/re-replace find="/--Replace--/g" replace="{{getvar::tempVars}}" {{pipe}}|
/qr-create set="CMC Logic" label="Combine List Lorebooks" {{pipe}}|
//|-----|

//Generate with Prompt|
/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/Functions/Generate%20with%20Prompt.md|
/re-replace find="/--Replace--/g" replace="{{getvar::tempVars}}" {{pipe}}|
/qr-create set="CMC Logic" label="Generator" {{pipe}}|
//|-----|

//Generate with Selector|
/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/Functions/Selector.md|
/re-replace find="/--Replace--/g" replace="{{getvar::tempVars}}" {{pipe}}|
/qr-create set="CMC Logic" label="Selector" {{pipe}}|
//|-----|

//Generate|
/qr-set-create CMC Generate|

//Generate World Info|
/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/Generate/Generate%20Basic%20World%20Info.md|
/re-replace find="/--Replace--/g" replace="{{getvar::tempVars}}" {{pipe}}|
/qr-create set="CMC Generate" label="Generate World Info" {{pipe}}|
//|-----|

//Generate Basic Character Information|
/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/Generate/Generate%20Basic%20Character%20Information.md|
/re-replace find="/--Replace--/g" replace="{{getvar::tempVars}}" {{pipe}}|
/qr-create set="CMC Generate" label="Generate Basic Character Information" {{pipe}}|
//|-----|

/qr-chat-set-on visible=true "CMC Main"|