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
/setvar key=stepVar Step0|
/qr-list CMC Main|
/getat index=1 {{pipe}}|
/let qrlabel {{pipe}}|
/qr-get set="CMC Main" label={{var::qrlabel}}|
/getat index="message" {{pipe}}|
/qr-update set="CMC Main" label={{var::qrlabel}} newlabel="Continue Generating Basic Information" {{pipe}}|

/qr-list CMC Logic|
/var key=qrList {{pipe}} |
/setvar key=dataBaseNames []|
/var selected_btn {{noop}}|
/ife ( gender != '' ) {:
	/buttons labels=["Yes", "No"] Do you want to change the gender?|
	/var selected_btn {{pipe}}|
:}|
/ife ( (gender == '') or ( selected_btn == 'Yes')) {:
	/buttons labels=["Female", "Male"] What gender is the character you are making? |
	/setvar key=gender {{pipe}}|
	/ife ( gender == '') {:
		/echo Aborting |
		/abort
	:}|
:}|
/addvar key=dataBaseNames gender|


/var selected_btn {{noop}}|
/ife ( futanari != '' ) {:
	/buttons labels=["Yes", "No"] Do you want to change the futanari choice?|
	/var selected_btn {{pipe}}|
:}|
/ife ( (futanari == '') or ( selected_btn == 'Yes')) {:
	/buttons labels=["Yes", "No"] Is the character you are making a futanari? |
	/setvar key=futunari {{pipe}}|
	/ife ( gender == '') {:
		/echo Aborting |
		/abort
	:}|
:}|
/addvar key=dataBaseNames futanari|

/var selected_btn {{noop}}|
/ife ( characterArchetype != '' ) {:
	/buttons labels=["Yes", "No"] Do you want to change the type of character?|
	/var selected_btn {{pipe}}|
	/ife ( selected_btn == '') {:
		/echo Aborting|
		/abort|
	:}|
:}|
/ife ( (characterArchetype == '') or ( selected_btn == 'Yes')) {:
	/setvar key=characterArchetype "Help me Decide"|
	/findentry field=comment file="CMC Information" Type Guide|
	/getentryfield file="CMC Information" {{pipe}}| 
	/var typeGuide {{pipe}}|
	/whilee ( characterArchetype == 'Help me Decide') {:
		/buttons labels=["Help me Decide", "Human", "Anthropomorphic\n(Anthropomorphic is a character that combines both human and animal traits, often featuring an animal body with human-like posture, facial expressions, speech, and behavior.)", "Demi-Human\n(Demi-Human is races that mostly looks like humans like Dwarfs, Elves etc...)", "Tauric\n(Tauric are hybrid species with a humanoid upper body and an animal-like lower body, such as centaurs, lamias, and mermaids.)", "Beastkin\n(Beastkin is a character with animal features like ears and tail but otherwise human appearance.)", "Animalistic\n(Animalistic refers to standard animals, fantasy creatures, or monsters that behave and appear primarily as non-human beings, typically walking on all fours and lacking human speech or reasoning.)", "Pokémon", "Digimon", "Android\n(Android is a robot that looks and acts like a Human.)"] What type of character are you making? |
		/re-replace find="/(\n\(\|\()[\s\S]*$/g" replace="" {{pipe}}|
		/setvar key=characterArchetype {{pipe}}|
		/ife ( characterArchetype == ''){:
			/echo Aborting|
			/abort
		:}|
		/ife ( characterArchetype == 'Help me Decide' ){:
			/input rows=8 What race do you want the character to be?|
			/let key=inp {{pipe}}|
			/genraw as=char Respond to the question: What type of character is a {{var::inp}}?
The reply should be in this format:
'<div>{{getvar::inp}} is a x</div>'
x is one of the following "Human", "Anthropomorphic", "Demi-Human", "Tauric", "Beastkin ", "Animalistic", "Pokémon", "Digimon", "Android"
INFORMATION: 
{{var::typeGuide}}
INSTRUCTION: Only respond in the given format.|

			/setvar key=characterArchetype {{pipe}}|
			/popup okButton=Continue result=true {{getvar::characterArchetype}}|
			/setvar key=characterArchetype {{pipe}}|
			/ife ( characterArchetype == '' ){:
				/echo Aborting |
				/abort
			:}|
			/elseif ( characterArchetype == '1' ){:
				/setvar key=characterArchetype "Help me Decide"|
			:}|
		:}|
	:}|
	/re-replace find="/\(.*$/g" replace="" {{getvar::characterArchetype}}|
	/setvar key=characterArchetype {{pipe}}|
:}|
/addvar key=dataBaseNames characterArchetype|


/var selected_btn {{noop}}|
/ife ( characterType != '' ) {:
	/buttons labels=["Yes", "No"] Do you want to change the character type?|
	/var selected_btn {{pipe}}|
	/ife ( selected_btn == '') {:
		/echo Aborting|
		/abort
	:}|
:}|
/ife ( (selected_btn == 'Yes') or (characterType == '')) {:
	/setvar key=characterType None|
:}|
/ife (((characterType == 'None') or ( selected_btn == 'Yes')) and (( characterArchetype == 'Anthropomorphic') or ( characterArchetype == 'Beastkin'))) {:
	/buttons labels=["Pokémon", "Digimon", "Animalistic"] Select the type you want?|
	/setvar key=characterType {{pipe}}|
	/ife ( characterType == '') {:
		/echo Aborting|
		/abort
	:}|
:}|
/addvar key=dataBaseNames characterType|


/ife ( (characterArchetype != 'Human') and (characterArchetype != 'Demi-Human') and (characterArchetype != 'Android')) {:
	/var selected_btn {{noop}}|
	/ife ( animalBase != '' ) {:
		/buttons labels=["Yes", "No"] Do you want to change the animal base?|
		/var selected_btn {{pipe}}|
		/ife ( selected_btn == '') {:
			/echo Aborting|
			/abort
		:}|
	:}|
	/ife ( ( selected_btn == 'Yes') or ( animalBase == '')) {:
		/buttons labels=["Mammal", "Reptile", "Bird", "Fish", "Amphibian", "Invertebrate", "Fantasy"] What type of species should the character be? This will guide later generations. |
		/re-replace find="/\(.*$/g" replace="" {{pipe}}|
		/setvar key=animalBase {{pipe}}|
		/ife ( animalBase == '') {:
			/echo Aborting|
			/abort
		:}|
	:}|
:}|
/elseif (characterArchetype == 'Human') {:
	/setvar key=animalBase Humanoid|
:}|
/elseif (characterArchetype == 'Android') {:
	/setvar key=animalBase Synthetic|
:}|
/else {:
	/setvar key=animalBase None|
:}|
/addvar key=dataBaseNames animalBase|

/ife ( (characterArchetype != 'Human') and (characterArchetype != 'Demi-Human') and (characterArchetype != 'Android')) {:
	/buttons labels=["Yes", "No"] Do you want the character to use the animal base as-is, or pick a more specific category like Canine, Feline, or Reptilian when generating the species later?|
	/var selected_btn {{pipe}}|
	/ife ( selected_btn == '') {:
		/echo Aborting|
		/abort
	:}|
	/elseif ( selected_btn == 'No') {:
		/setvar key=speciesGroup {{getvar::animalBase}}|
	:}|
	/else {:
		/let key=find {{getvar::speciesGroup}}: List|
		/findentry field=comment file="CMC Variables" {{var::find}}|
		/getentryfield field=content file="CMC Variables" {{pipe}}|
		/split find="/\n/" {{pipe}} |
		/setvar key=speciesGroup {{pipe}}|
		/buttons labels={{getvar::speciesGroup}} Select the Species Group you want to use for later when generating the Species.|
		/setvar key=speciesGroup {{pipe}}|
		/ife ( temp == '') {:
			/echo Aborting|
			/abort
		:}|
		/re-replace find="/\(.*$/g" replace="" {{getvar::temp}}|
		/setvar key=speciesGroup {{pipe}}|
	:}|
:}|
/else {:
	/setvar key=speciesGroup None|
:}|
/ife ( (characterArchetype == 'Human') and (characterArchetype == 'Demi-Human') and (characterArchetype == 'Android')) {:
	/setvar key=parsedAnimalType None|
:}|
/ife (((characterArchetype == Anthropomorphic) or (characterArchetype == Anthropomorphic)) and ((characterType == 'Pokémon') or (characterType == 'Digimon') or (characterType == 'Animalistic'))) {:
	/setvar key=parsedAnimalType {{getvar::characterType}}|
:}|
/elseif (animalBase != speciesGroup) {:
	/setvar key=parsedAnimalType {{getvar::speciesGroup}}|
:}|
/else {:
	/setvar key=parsedAnimalType {{getvar::animalBase}}|
:}|

/buttons labels=["Yes", "No"] Do you want the character to have Privates that differs from it's species type?|
/var selected_btn {{pipe}}|
/ife ( selected_btn == '') {:
	/echo Aborting|
	/abort
:}|
/elseif ( selected_btn == 'Yes') {:
	/buttons labels=["Mammal", "Reptile", "Bird", "Fish", "Amphibian", "Invertebrate", "Fantasy"] What type of species should the characters Privates be? This will guide later generations.|
	/let key=t {{pipe}}|
	/ife (t == '') {:
		/echo Aborting |
		/abort
	:}|
	/let key=find {{var::t}}: List|
	/findentry field=comment file="CMC Variables" {{var::find}}|
	/getentryfield field=content file="CMC Variables" {{pipe}}|
	/split find="/\n/" {{pipe}} |
	/setvar key=temp1 {{pipe}}|
	/setvar key=temp {{getvar::temp1}}|
	/addvar key=temp Use Base Type|
	/buttons labels={{getvar::temp}} Select the Species Group you want to use for later when generating the Privates.|
	/setvar key=temp {{pipe}}|
	/ife ( temp == '') {:
		/echo Aborting|
		/abort
	:}|
	/re-replace find="/\(.*$/g" replace="" {{getvar::temp}}|
	/setvar key=temp {{pipe}}|
	/ife ( temp == 'Use Base Type') {:
		/setvar key=temp {{getvar::animalBase}}|
	:}|
	/ife (futanari == 'Yes') {:
		/buttons labels=["Yes", "No"] Do you want to use the same type of Privates for the Male and Female parts?|
		/var selected_btn {{pipe}}|
		/ife ( selected_btn == '') {:
			/echo Aborting|
			/abort
		:}|
		/elseif ( selected_btn == 'Yes') {:
			/setvar key=privatesFemale {{getvar::temp}}|
			/setvar key=privatesMale {{getvar::temp}}|
		:}|
		/else {:
			/buttons labels=["Male", "Female"] Do you want to apply the selected type to the Female or Male part?|
			/var selected_btn {{pipe}}|
			/ife ( selected_btn == '') {:
				/echo Aborting|
				/abort
			:}|
			/else {:
				/setvar key=privates{{var::selected_btn}} {{getvar::temp}}|
			:}|
			/setvar key=temp {{getvar::temp1}}|
			/addvar key=temp Use Base Type|
			/buttons labels={{getvar::temp}} Select the Species Group you want to use for later when generating the Privates.|
			/setvar key=temp {{pipe}}|
			/ife ( temp == '') {:
				/echo Aborting|
				/abort
			:}|
			/re-replace find="/\(.*$/g" replace="" {{getvar::temp}}|
			/setvar key=temp {{pipe}}|
			/ife ( temp == 'Use Base Type') {:
				/setvar key=temp {{getvar::animalBase}}|
			:}|
			/ife ( privatesFemale == '') {:
				/setvar key=privatesFemale {{getvar::temp}}|
			:}|
			/elseif ( privatesFemale == '') {:
				/setvar key=privatesMale {{getvar::temp}}|
			:}|
		:}|
	:}|
	/elseif (gender == 'Male') {:
		/setvar key=privatesFemale None|
		/setvar key=privatesMale {{getvar::temp}}|
	:}|
	/else {:
		/setvar key=privatesFemale {{getvar::temp}}|
		/setvar key=privatesMale None|
	:}|
:}|
/elseif (futanari == 'Yes') {:
	/setvar key=privatesFemale {{getvar::animalBase}}|
	/setvar key=privatesMale {{getvar::animalBase}}|
:}|
/elseif (gender == 'Male') {:
	/setvar key=privatesFemale None|
	/setvar key=privatesMale {{getvar::animalBase}}|
:}|
/else {:
	/setvar key=privatesFemale {{getvar::animalBase}}|
	/setvar key=privatesMale None|
:}|
/flushvar temp|
/flushvar temp1|
/addvar key=dataBaseNames privatesFemale|
/addvar key=dataBaseNames privatesMale|



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
/addvar key=dataBaseNames user|
/addvar key=dataBaseNames chatGroup|


/db-list source=chat field=name |
/let key=a {{pipe}}|


/findentry field=comment file="CMC Templates" Character Template|
/getentryfield file="CMC Templates" {{pipe}}|
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