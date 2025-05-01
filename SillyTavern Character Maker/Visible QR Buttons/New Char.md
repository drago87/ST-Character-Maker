--VarReplace--
/messages 0|
/let firstMess {{pipe}}|
/ife ( 'Installation Instructions' not in firstMess) {:
	/buttons labels=["Yes", "No"] <div>Doing this will delete all progress.</div><div>Do you want to continue?</div>|
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
:}|

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
/ife ( type != '' ) {:
	/buttons labels=["Yes", "No"] Do you want to change the type of character?|
	/var selected_btn {{pipe}}|
:}|
/ife ( (type == '') or ( selected_btn == 'Yes')) {:
	/setvar key=type "Help me Decide"|
	/findentry field=comment file="CMC Variables" Type Guide|
	/getentryfield file="CMC Variables" {{pipe}}| 
	/var typeGuide {{pipe}}|
	/whilee ( type == 'Help me Decide') {:
		/buttons labels=["Help me Decide", "Human", "Anthropomorphic\n(Anthropomorphic is a animal that have a human form.)", "Demi-Human\n(Demi-Human is races that mostly looks like humans like Dwarfs, Elves etc...)", "Furry\n(Furry is animal like humans that mostly looks like humans but have certain animal parts.)", "Feral\n(Feral is standard animals, fantasy animals or monsters.)", "Pokémon", "Digimon", "Android\n(Android is a robot that looks and acts like a Human.)"] What type of character are you making? |
		/re-replace find="/(\n\(\|\()[\s\S]*$/g" replace="" {{pipe}}|
		/setvar key=type {{pipe}}|
		/ife ( type == ''){:
			/echo Aborting|
			/abort
		:}|
		/ife ( type == 'Help me Decide' ){:
			/input rows=8 What race do you want the character to be?|
			/let key=inp {{pipe}}|
			/genraw as=char Respond to the question: What type of character is a {{var::inp}}?
The reply should be in this format:
'<div>{{getvar::inp}} is a x</div>'
x is one of the following "Human", "Anthropomorphic", "Demi-Human", "Furry", "Feral", "Pokémon", "Digimon", "Android"
INFORMATION: 
Human is a standard human.
Andromorphic is a animal that have a human form.
Demi-Human is races that mostly looks like humans like Dwarfs, Elves etc...
Furry is animal like humans that mostly looks like humans but have certain animal parts.
Feral is standard animals, fantasy animals or monsters.
Pokémon is the creatures from the Pokémon games and anime.
Digimon is the creatures from the Digimon games and anime.
Android is a robot that looks and acts like a Human.
INSTRUCTION: Only respond in the given format.|

			/setvar key=type {{pipe}}|
			/popup okButton=Continue result=true {{getvar::type}}|
			/setvar key=type {{pipe}}|
			/ife ( type == '' ){:
				/echo Aborting |
				/abort
			:}|
			/elseif ( type == '1' ){:
				/setvar key=type "Help me Decide"|
			:}|
		:}|
	:}|
	/re-replace find="/\(.*$/g" replace="" {{getvar::type}}|
	/setvar key=type {{pipe}}|
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
/ife (((character_type == 'None') or ( selected_btn == 'Yes')) and (( type == 'Anthropomorphic') or ( type == 'Furry')  or ( type == 'Feral'))) {:
	/buttons labels=["Pokémon", "Digimon", "Normal"] Select the type you want?|
	/setvar key=character_type {{pipe}}|
	/ife ( character_type == '') {:
		/echo Aborting|
		/abort
	:}|
:}|

/var selected_btn {{noop}}|
/ife ( type != '' ) {:
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
	/setvar key=normal_form {{getvar::type}}|
:}|


/:"CMC Logic.Is Real"|

/db-list source=chat field=name |
/let key=a {{pipe}}|

/setvar key=dataBaseNames []|
/addvar key=dataBaseNames normal_form|
/addvar key=dataBaseNames type|
/addvar key=dataBaseNames speciesType|
/addvar key=dataBaseNames gender|
/addvar key=dataBaseNames character_type|

--JEDParse--
/findentry field=comment file="CMC Variables" Character Template|
/getentryfield file="CMC Variables" {{pipe}}|
/:JEDParse input={{pipe}}|
/setvar key=t {{pipe}}|
/:"CMC Logic.Parse"|
/message-edit message=0 {{pipe}}|
/flushvar t|

/:"CMC Logic.Save DataBase"|

/setvar key=stepDone Yes|
/qr-list CMC Main|
/getat index=1 {{pipe}}|
/var qrlabel {{pipe}}|
/qr-get set="CMC Main" label={{var::qrlabel}}|
/getat index="message" {{pipe}}|
/qr-update set="CMC Main" label={{var::qrlabel}} newlabel="Start Generating World Info" {{pipe}}|