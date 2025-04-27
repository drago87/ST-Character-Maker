/qr-set-create CMC Main|
//New Char|
/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/Visible%20QR%20Buttons/New%20Chat.md|
/qr-create set="CMC Main" label="New Character" title="Will make a new character and let you set the Gender, type(Human, Anthro etc..)" {{pipe}}|
//|-----|


/qr-set-create CMC Logic|
//Create Temporary Variables|
/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/Functions/TempVariables.md|
/qr-create set="CMC Logic" label="TempVariables" {{pipe}}|
//|-----|

//Get Char info|
/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/Functions/Get%20Character%20information.md|
/qr-create set="CMC Logic" label="Get Char info" {{pipe}}|
//|-----|

//Is Real|
/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/Functions/Is%20Real.md|
/qr-create set="CMC Logic" label="Is Real" {{pipe}}|
//|-----|

//Text Parce|
/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/Functions/Text%20Parce.md|
/qr-create set="CMC Logic" label="Text Parce" {{pipe}}|
//|-----|

//Save Gen|
/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/Functions/SaveGen.md|
/qr-create set="CMC Logic" label="SaveGen" {{pipe}}|
//|-----|

//Combine List Lorebooks|
/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/Functions/Combine%20List%20Lorebooks.md|
/qr-create set="CMC Logic" label="Combine List Lorebooks" {{pipe}}|
//|-----|

//Generate with Prompt|
/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/Functions/Generate%20with%20Prompt.md|
/qr-create set="CMC Logic" label="Generator" {{pipe}}|
//|-----|

//Generate with Selector|
/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/Functions/Selector.md|
/qr-create set="CMC Logic" label="Selector" {{pipe}}|
//|-----|

//Generate|
/qr-set-create CMC Generate|

//Generate World Info|
/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/Generate/Generate%20Basic%20World%20Info.md|
/qr-create set="CMC Logic" label="Generate World Info" {{pipe}}|
//|-----|

//Generate Basic Character Information|
/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/Generate/Generate%20Basic%20Character%20Information.md|
/qr-create set="CMC Logic" label="Generate Basic Character Information" {{pipe}}|
//|-----|

/qr-chat-set-on visible=true "CMC Main"