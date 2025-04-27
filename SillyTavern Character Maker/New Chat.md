//Empty the Database to propare for the new character|
/db-list source=chat field=name |
/var key=databaseList {{pipe}}|
/foreach {{var::databaseList}} {:
	/db-delete source=chat {{var::item}}|
:}|
/qr-list CMC Logic|
/var key=qr-list {{pipe}} |

/buttons labels=["Female", "Male", "Futanari"] What gender is the character you are making? |
/setvar key=gender {{pipe}}|
/ife ( gender == ''){:
	/:"CMC Logic.Flushvar"| /echo Aborting |	/abort
:}|


/setvar key=type "Help me Decide"|
/findentry field=comment file="CMC Logic" Type Guide|
/getentryfield file="CMC Logic" {{pipe}}| 
/setvar key=typeExplanation {{pipe}}|
/setvar key=temp []|
/addvar key=temp "Help me Decide"|
/addvar key=temp "Human"|
/addvar key=temp "Anthro{{newline}}(Test)"|
/whilee ( type == 'Help me Decide') {:
	/buttons labels=["Help me Decide", "Human", "Anthro{{newline}}(Test)", "Demi-Human", "Furry", "Feral", "Pokémon", "Digimon", "Machine"] What type of character are you making? |
	/re-replace find="/\(.*$/g" replace="" {{pipe}}|
	/setvar key=type {{pipe}}|
	/ife ( type == ''){:
		/echo Aborting | /ife ( quickRoll == 'Yes' ) {:
			/setvar key=debug {{getvar::tempDebug}}| :}|
		/:"CMC Logic.Flushvar"|
	:}|
	/ife ( type == 'Help me Decide' ){:
		/input rows=8 What race do you want the character to be?|
		/setvar key=inp {{pipe}}|
		/genraw as=char Respond to the question: What type of character is a {{getvar::inp}}?
The reply should be in this format:
'<div>{{getvar::inp}} is a x</div>'
x is one of the following "Human", "Anthro", "Demi-Human", "Furry", "Feral", "Pokémon(Normal)", "Digimon(Normal)", "Machine"
INFORMATION: {{getvar::typeExplanation}}
INSTRUCTION: Only respond in the given format.|

		/setvar key=type {{pipe}}|
		/buttons labels=["Continue"]{{getvar::type}}|
		/setvar key=type {{pipe}}|
		/ife ( type == '' ){:
			/echo Aborting | /ife ( quickRoll == 'Yes' ) {: /setvar key=debug {{getvar::tempDebug}}| :}| /:"CMC Logic.Flushvar"|
		:}|
		/elseif ( type == 'Continue' ){:
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
/ife ( type != 'Human'){:
	/buttons labels={{getvar::speciesType}} What type of species should the character be? This will guide later generations. |
	/re-replace find="/\(.*$/g" replace="" {{pipe}}|
	/var key=s {{pipe}}|
	/ife ( s == ''){:
		/echo Aborting | /ife ( quickRoll == 'Yes' ) {:
		/setvar key=debug {{getvar::tempDebug}}|
	:}|
	/:"CMC Logic.Flushvar"|
	/elseif ( s == 'Other'){:
		/input rows=8 Write what kind of speciesType the character should be.|
		/var key=s {{pipe}}|
		/ife ( s == ''){:
			/echo Aborting | /ife ( quickRoll == 'Yes' ) {: /setvar key=debug {{getvar::tempDebug}}| :}| /:"CMC Logic.Flushvar"|
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

/findentry field=comment file="CMC Logic" Character Template|
/getentryfield file="CMC Logic" {{pipe}}|
/var key=message {{pipe}}|

/message-edit message=0 {{var::message}}|

//[[Generate Basic World Info]]|
/:"CMC Logic.Generate Basic World Info"|