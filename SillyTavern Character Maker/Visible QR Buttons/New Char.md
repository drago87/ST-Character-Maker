/let key=selected_btn {{noop}}|
/let key=databaseList {{noop}}|
/let key=qrList {{noop}}|
/let key=typeGuide {{noop}}|


/messages 0|
/let firstMess {{pipe}}|
/ife ( ('Installation Instructions' not in firstMess) and (continue != 'Yes')) {:
	/buttons labels=["Yes", "No"] <div>Doing this will delete all progress. And all Chat Attachments.</div><div>Do you want to continue?</div>|
	/var selected_btn {{pipe}}|
	/ife (( selected_btn == '') or ( selected_btn == 'No')) {:
		/echo Aborting|
		/abort|
	:}|
	//Empty the Database to prepare for the new character|
	/db-list source=chat field=name |
	/var key=databaseList {{pipe}}|
	/foreach {{var::databaseList}} {:
		/db-delete source=chat {{var::item}}|
	:}|
	
	/listvar scope=local return=object |
	/let  key=flvars {{pipe}}|
	/foreach {{var::flvars}} {:
		/getat index=key {{var::item}}|
		/flushvar {{pipe}}|
	:}|
	
:}|

/setvar key=continue Yes|
/setvar key=wait 100|
/setvar key=stepDone No|
/setvar key=stepVar Step1|
/qr-list CMC Main|
/getat index=1 {{pipe}}|
/let qrlabel {{pipe}}|
/qr-get set="CMC Main" label={{var::qrlabel}}|
/getat index="message" {{pipe}}|
/qr-update set="CMC Main" label={{var::qrlabel}} newlabel="Continue Generating Basic Information" {{pipe}}|

/qr-list CMC Logic|
/var key=qrList {{pipe}} |

/var selected_btn {{noop}}|
/ife ( gender != '' ) {:
	/buttons labels=["Yes", "No"] Do you want to change the gender?|
	/var selected_btn {{pipe}}|
:}|
/ife ( (gender == '') or ( selected_btn == 'Yes')) {:
	/buttons labels=["Female", "Male", "Futanari"] What gender is the character you are making? |
	/setvar key=gender {{pipe}}|
	/ife ( gender == '') {:
		/echo Aborting |
		/abort
	:}|
:}|
/var selected_btn {{noop}}|
/ife ( normal_form != '' ) {:
	/buttons labels=["Yes", "No"] Do you want to change the type of character?|
	/var selected_btn {{pipe}}|
	/ife ( selected_btn == '') {:
		/echo Aborting|
		/abort|
	:}|
:}|
/ife ( (normal_form == '') or ( selected_btn == 'Yes')) {:
	/setvar key=normal_form "Help me Decide"|
	/findentry field=comment file="CMC Information" Type Guide|
	/getentryfield file="CMC Information" {{pipe}}| 
	/var typeGuide {{pipe}}|
	/whilee ( normal_form == 'Help me Decide') {:
		/buttons labels=["Help me Decide", "Human", "Anthropomorphic\n(Anthropomorphic is a character that combines both human and animal traits, often featuring an animal body with human-like posture, facial expressions, speech, and behavior.)", "Demi-Human\n(Demi-Human is races that mostly looks like humans like Dwarfs, Elves etc...)", "Kemonomimi\n(Kemonomimi is a character with animal features like ears and tail but otherwise human appearance.)", "Animalistic\n(Animalistic refers to standard animals, fantasy creatures, or monsters that behave and appear primarily as non-human beings, typically walking on all fours and lacking human speech or reasoning.)", "Pokémon", "Digimon", "Android\n(Android is a robot that looks and acts like a Human.)"] What type of character are you making? |
		/re-replace find="/(\n\(\|\()[\s\S]*$/g" replace="" {{pipe}}|
		/setvar key=normal_form {{pipe}}|
		/ife ( normal_form == ''){:
			/echo Aborting|
			/abort
		:}|
		/ife ( normal_form == 'Help me Decide' ){:
			/input rows=8 What race do you want the character to be?|
			/let key=inp {{pipe}}|
			/genraw as=char Respond to the question: What type of character is a {{var::inp}}?
The reply should be in this format:
'<div>{{getvar::inp}} is a x</div>'
x is one of the following "Human", "Anthropomorphic", "Demi-Human", "Furry", "Animalistic", "Pokémon", "Digimon", "Android"
INFORMATION: 
{{var::typeGuide}}
INSTRUCTION: Only respond in the given format.|

			/setvar key=normal_form {{pipe}}|
			/popup okButton=Continue result=true {{getvar::normal_form}}|
			/setvar key=normal_form {{pipe}}|
			/ife ( normal_form == '' ){:
				/echo Aborting |
				/abort
			:}|
			/elseif ( normal_form == '1' ){:
				/setvar key=normal_form "Help me Decide"|
			:}|
		:}|
	:}|
	/re-replace find="/\(.*$/g" replace="" {{getvar::normal_form}}|
	/setvar key=normal_form {{pipe}}|
:}|


/var selected_btn {{noop}}|
/ife ( character_type != '' ) {:
	/buttons labels=["Yes", "No"] Do you want to change the character type?|
	/var selected_btn {{pipe}}|
	/ife ( selected_btn == '') {:
		/echo Aborting|
		/abort
	:}|
:}|
/ife ( (selected_btn == 'Yes') or (character_type == '')) {:
	/setvar key=character_type None|
:}|
/ife (((character_type == 'None') or ( selected_btn == 'Yes')) and (( type == 'Anthropomorphic') or ( type == 'Kemonomimi')  or ( type == 'Animalistic'))) {:
	/buttons labels=["Pokémon", "Digimon", "Animalistic"] Select the type you want?|
	/setvar key=character_type {{pipe}}|
	/ife ( character_type == '') {:
		/echo Aborting|
		/abort
	:}|
:}|

/var selected_btn {{noop}}|
/ife ( speciesType != '' ) {:
	/buttons labels=["Yes", "No"] Do you want to change the species type?|
	/var selected_btn {{pipe}}|
	/ife ( selected_btn == '') {:
		/echo Aborting|
		/abort
	:}|
:}|
/ife ( (selected_btn == 'Yes') or (speciesType == '')) {:
	/setvar key=speciesType None|
:}|
/ife ( (type != 'Human') and ( selected_btn == 'Yes') or ( speciesType == 'None')) {:
	/buttons labels=["Canine", "Equine", "Feline", "Reptilian", "Aviary", "Leporidae(Rabbit)", "Other"]What type of species should the character be? This will guide later generations. |
	/re-replace find="/\(.*$/g" replace="" {{pipe}}|
	/setvar key=speciesType {{pipe}}|
	/ife ( speciesType == '') {:
		/echo Aborting|
		/abort
	:}|
	/elseif ( speciesType == 'Other') {:
		/input rows=8 Write what kind of speciesType the character should be.|
		/setvar key=speciesType {{pipe}}|
		/ife ( speciesType == ''){:
			/echo Aborting |
			/abort
		:}|
	:}|
:}|


/:"CMC Logic.Is Real"|

/buttons labels=["Yes", "No"] Is the character going to be part of a Chat Group?|
/var selected_btn {{pipe}}|
/ife ( selected_btn == '') {:
	/echo Aborting|
	/abort
:}|
/elseif ( selected_btn == 'Yes') {:
	/setvar key=chatGroup Yes|
	/buttons labels=["Yes", "No"] Is the user going to be part of the Chat Group?|
	/var selected_btn {{pipe}}|
	/ife ( selected_btn == '') {:
		/echo Aborting|
		/abort
	:}|
	/elseif ( selected_btn == 'Yes') {:
		/setvar key=user Yes|
	:}|
	/else {:
		/setvar key=user No|
	:}|
:}|
/else {:
	/setvar key=user Yes|
	/setvar key=chatGroup No|
:}|

/db-list source=chat field=name |
/let key=a {{pipe}}|

/setvar key=dataBaseNames []|
/addvar key=dataBaseNames normal_form|
/addvar key=dataBaseNames speciesType|
/addvar key=dataBaseNames gender|
/addvar key=dataBaseNames character_type|
/addvar key=dataBaseNames user|
/addvar key=dataBaseNames chatGroup|


/findentry field=comment file="CMC Variables" Character Template|
/getentryfield file="CMC Variables" {{pipe}}|
/message-edit message=0 await=true {{pipe}}|
/:"CMC Logic.JEDParse"|

/:"CMC Logic.Save DataBase"|

/setvar key=stepDone Yes|
/qr-list CMC Main|
/getat index=1 {{pipe}}|
/var qrlabel {{pipe}}|
/qr-get set="CMC Main" label={{var::qrlabel}}|
/getat index="message" {{pipe}}|
/qr-update set="CMC Main" label={{var::qrlabel}} newlabel="Start Generating World Info" {{pipe}}|

/flushvar continue|