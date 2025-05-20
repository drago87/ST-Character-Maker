/qr-list CMC Main|
/getat index=1 {{pipe}}|
/let qrlabel {{pipe}}|
/qr-get set="CMC Main" label={{var::qrlabel}}|
/getat index="message" {{pipe}}|
/qr-update set="CMC Main" label={{var::qrlabel}} newlabel="Continue Generating Outfit" {{pipe}}|

/:"CMC Logic.Get Char info"|

/setvar key=dataBaseNames []|
/flushvar genSettings|

/setvar key=stepVar Step4|

/setvar key=skip Update|
/ife ( stepDone == 'No') {:
	/buttons labels=["Skip", "Update"] Do you want to skip or update already generated content? You will get a question for each already done if you select Update.|
	/setvar key=skip {{pipe}}|
	/ife ( skip == ''){:
		/echo Aborting |
		/abort
	:}|
:}|

/setvar key=stepDone No|
/setvar key=outfitsDone No|
/let key=do {{noop}}|
/let key=variableName {{noop}}|
/let selected_btn {{noop}}|


/getvar key=outfits index="Main Outfit"|
/let key=outfitsCheck {{pipe}}|

/ife (outfitsCheck == '') {:
	/setvar key=outfits {}|
:}|
/else {:
	/buttons labels=["Yes", "No"] Do you want to add more outfits?|
	/setvar key=outfitsDone {{pipe}}|
:}|

/whilee (outfitsDone != 'No') {:

	//Outfit Head|
	
	//--------|
	
	//Outfit Accessories|
	
	//--------|
	
	//Outfit Makeup|
	
	//--------|
	
	//Outfit Neck|
	
	//--------|
	
	//Outfit Top|
	
	//--------|
	
	//Outfit Bottom|
	
	//--------|
	
	//Outfit Legs|
	
	//--------|
	
	//Outfit Shoes|
	
	//--------|
	
	//Outfit Underwear|
	
	//--------|
	
	/ifempty value={{getvar::outfits}} {{noop}}|
	/var key=outfitsCheck {{pipe}}|
	/ife (outfitsCheck == '') {:
		/setvar key=outfits index="Main Outfit" {{getvar::}}|
	:}|
	/else {:
		/input What would you like to call this outfit?|
		/let key=outfitName {{pipe}}|
		/setvar key=outfits index={{var::outfitName}} {{getvar::}}|
	:}|
	/buttons labels=["Yes", "No"] Do you want to add more outfits?|
	/setvar key=outfitsDone {{pipe}}|
:}|
/*
/:"CMC Logic.JEDParse"|

/:"CMC Logic.Save DataBase"|

/setvar key=stepDone Yes|
/qr-list CMC Main|
/getat index=1 {{pipe}}|
/var qrlabel {{pipe}}|
/qr-get set="CMC Main" label={{var::qrlabel}}|
/getat index="message" {{pipe}}|
/qr-update set="CMC Main" label={{var::qrlabel}} newlabel="Start Generating Mental Traits & Personality" {{pipe}}|
/forcesave|
*|