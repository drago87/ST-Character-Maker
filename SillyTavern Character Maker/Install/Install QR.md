/qr-set-create CMC Main|
//New Char|
/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/main/Quick%20Reply%20Buttons/Work%20In%20Progress%20Plain%20Text/Debug.txt|
/qr-create set="CMC Main" label="New Chat and Set Character Gender and Type" title="Will make a new character and let you set the Gender, type(Human, Anthro etc..)" {{pipe}}|

//Character Generator Swipe|
/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/main/Quick%20Reply%20Buttons/Work%20In%20Progress%20Plain%20Text/Debug.txt|
/qr-create set="CMC Main" label="Character Generator Swipe" {{pipe}} title="Swipes the last message after loading needed information. (Use this instead of the built in swipe)"|

//Generate Character Choice|
/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/main/Quick%20Reply%20Buttons/Work%20In%20Progress%20Plain%20Text/Debug.txt|
/qr-create set="CMC Main" label="Generate Character Choice" {{pipe}} title="Select what to generate next"|

//Debug|
/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/main/Quick%20Reply%20Buttons/Work%20In%20Progress%20Plain%20Text/Debug.txt|
/qr-create set="CMC Main" label="Debug Is Off" {{pipe}} title="Enables or Disables the Debug mode"|

//Export character Card|
/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/main/Quick%20Reply%20Buttons/Work%20In%20Progress%20Plain%20Text/Debug.txt|
/qr-create set="CMC Main" label="Export character Card" {{pipe}} title="Exports the Character to a Character Sheet that needs to be downloaded from the Data Bank. More info at the end of the generation"|


/qr-set-create CMC Logic|
//Flushvar|
/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/main/Quick%20Reply%20Buttons/Work%20In%20Progress%20Plain%20Text/Debug.txt|
/qr-create set="CMC Logic" label="Flushvar" {{pipe}}|

//Get Char info|
/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/main/Quick%20Reply%20Buttons/Work%20In%20Progress%20Plain%20Text/Debug.txt|
/qr-create set="CMC Logic" label="Get Char info" {{pipe}}|

/qr-chat-set visible=true "CMC Main"