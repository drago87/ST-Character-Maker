/ife (gen != 'Yes') {:
	/db-list source=chat field=name |
	/let key=databaseList {{pipe}}|
	
	/foreach {{var::databaseList}} {:
		/db-get source=chat {{var::item}}| 
		/setvar key={{var::item}} {{pipe}}|
	:}|
:}|
/ife ( lastName == '' ) {:
	/setvar key=lastName {{noop}}|
	/setvar key=name {{getvar::firstName}}|
:}|
/elseif ((firstName != '') and (lastName != '') ) {:
	/setvar key=name {{getvar::firstName}} {{getvar::lastName}}|
:}|
/ife ( alias == '' ) {:
	/setvar key=alias {{noop}}|
:}|

//Parse character Age|
/setvar key=parcedAge {{noop}}|

/ife ((humanEquivalentAge == age) and (age != '')) {:
	/setvar key=parcedAge {{getvar::age}} years-old|
:}|
/elseif ((humanEquivalentAge != '') and (humanEquivalentAge != 'None') and (humanEquivalentAge != age)) {:
	/setvar key=parcedAge {{getvar::age}} years-old — roughly {{getvar::humanEquivalentAge}} years-old in human years.|
:}|
/else (age != '') {:
	/setvar key=parcedAge {{getvar::age}} years-old|
:}|
//-----------|

/ife (parsedAnimalType == 'None') {:
	/setvar key=parsedAnimalType {{noop}}|
:}|


//Parse character Species|
/setvar key=parsedSpecies {{noop}}|
/ife ((characterType == 'None') or ( characterType ==  characterArchetype)) {:
	/setvar key=characterType {{noop}}|
:}|
/ife ( characterArchetype == species ) {:
    /setvar key=parsedSpecies {{getvar::species}}|
:}|
/else {:
	/setvar key=parsedSpecies "{{getvar::characterArchetype}} {{getvar::species}}"|
:}|
//-----------|

//Parse Real Character info|
/ife ( real == 'Yes') {:
	/setvar key=realInfoParced "{{newline}}- Origin: {{getvar::media_type}} – {{getvar::media_name}}"|
	/setvar key=realParced "{{getvar::firstName}} is a character from the {{getvar::media_type}} _{{getvar::media_name}}_."|
	/setvar key=realParcedContext "{{getvar::name}} is a character from the {{getvar::media_type}} _{{getvar::media_name}}_. Use your knowledge about {{getvar::name}} and the {{getvar::media_type}} _{{getvar::media_name}}_ when doing the assigned **TASK**"|
:}|
//-----------|

//Parse Nationality and Ethnicity|
/ife ( nationality == 'None' ) {:
	/setvar key=nationality {{noop}}|
:}|
/ife ( ethnicity == 'None' ) {:
	/setvar key=ethnicity {{noop}}|
:}|
/ife ( parsedOrigin == 'None' ) {:
	/setvar key=parsedOrigin {{noop}}|
:}|