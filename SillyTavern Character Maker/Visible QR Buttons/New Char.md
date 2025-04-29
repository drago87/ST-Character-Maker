--Replace--
/messages 0|
/let firstMess {{pipe}}|
/ife ( 'Installation Instructions' in firstMess) {:
	/buttons labels=["Yes", "No"] <div>Doing this will delete all progress.</div><div>Do you want to continue?</div>|
	/var selected_btn {{pipe}}|
	/ife ( selected_btn == '') {:
		/echo Aborting|
		/abort|
	:}|
:}|

/setvar key=stepDone 'No'|
/setvar key=stepVar Step1|

//Empty the Database to prepare for the new character|
/db-list source=chat field=name |
/var key=databaseList {{pipe}}|
/foreach {{var::databaseList}} {:
	/db-delete source=chat {{var::item}}|
:}|
/qr-list CMC Logic|
/var key=qrList {{pipe}} |

/buttons labels=["Female", "Male", "Futanari"] What gender is the character you are making? |
/setvar key=gender {{pipe}}|
/ife ( gender == '') {:
	/echo Aborting |
	/abort
:}|


/setvar key=type "Help me Decide"|
/findentry field=comment file="CMC Logic" Type Guide|
/getentryfield file="CMC Variables" {{pipe}}| 
/whilee ( type == 'Help me Decide') {:
	/buttons labels=["Help me Decide", "Human", "Anthro\n(Anthro is a animal that have a human form.)", "Demi-Human\n(Demi-Human is races that mostly looks like humans like Dwarfs, Elves etc...)", "Furry\n(Furry is animal like humans that mostly looks like humans but have certain animal parts.)", "Feral\n(Feral is standard animals, fantasy animals or monsters.)", "Pokémon", "Digimon", "Android/n(Android is a robot that looks and acts like a Human.)"] What type of character are you making? |
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
x is one of the following "Human", "Anthro", "Demi-Human", "Furry", "Feral", "Pokémon", "Digimon", "Android"
INFORMATION: 
Human is a standard human.
Anthro is a animal that have a human form.
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
/setvar key=type {{pipe}}

/setvar key=character_type none|
/ife (( type == 'Anthro') or ( type == 'Furry')  or ( type == 'Feral')) {:
	/buttons labels=["Pokémon", "Digimon", "Normal"] Select the type you want?|
	/setvar key=character_type {{pipe}}|
:}|

/setvar key=speciesType ["Canine", "Equine", "Feline", "Reptilian", "Aviary", "Leporidae(Rabbit)", "Other"]|
/setvar key=type None|
/ife ( type != 'Human') {:
	/buttons labels={{getvar::speciesType}} What type of species should the character be? This will guide later generations. |
	/re-replace find="/\(.*$/g" replace="" {{pipe}}|
	/let key=s {{pipe}}|
	/ife ( s == '') {:
		/echo Aborting|
		/abort
	:}|
	/elseif ( s == 'Other') {:
		/input rows=8 Write what kind of speciesType the character should be.|
		/var key=s {{pipe}}|
		/ife ( s == ''){:
			/echo Aborting |
			/abort
		:}|
	:}|
	/setvar key=type {{var::s}}|
:}|

/setvar key=normal_form {{getvar::type}}|

/:"CMC Logic.Is real"|

/db-list source=chat field=name |
/var key=a {{pipe}}|

/ife ( 'normal_form' not in a){:
	/db-add source=chat name=normal_form {{getvar::normal_form}}|
	/db-disable source=chat normal_form|
:}|
/else {:
	/db-update source=chat name=normal_form {{getvar::normal_form}}|
	/db-disable source=chat normal_form|
:}|
/ife ( 'type' not in a){:
	/db-add source=chat name=type {{getvar::type}}|
	/db-disable source=chat type|
:}|
/else {:
	/db-update source=chat name=type {{getvar::type}}|
	/db-disable source=chat type|
:}|
/ife ( 'gender' not in a){:
	/db-add source=chat name=gender {{getvar::gender}}|
	/db-disable source=chat gender|
:}|
/else {:
	/db-update source=chat name=gender {{getvar::gender}}|
	/db-disable source=chat gender|
:}|
/ife ( 'character_type' not in a){:
	/db-add source=chat name=character_type {{getvar::character_type}}|
	/db-disable source=chat character_type|
:}|
/else {:
	/db-update source=chat name=character_type {{getvar::character_type}}|
	/db-disable source=chat character_type|
:}|

/findentry field=comment file="CMC Variables" Character Template|
/getentryfield file="CMC Variables" {{pipe}}|
/var key=message {{pipe}}|

/message-edit message=0 {{var::message}}|
/qr-update set="CMC Main" id=1 newlabel="Start Generating World Info"|