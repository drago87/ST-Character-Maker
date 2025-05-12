/db-list source=chat field=name |
/let key=databaseList {{pipe}}|
/ife ( 'lastName' in databaseList){:
	/db-get source=chat lastName| /setvar key=firstName {{pipe}}|
:}|
/ife ( 'lastName' in databaseList){:
	/db-get source=chat lastName| /setvar key=lastName {{pipe}}|
:}|
/ife ( 'alias' in databaseList){:
	/db-get source=chat alias| /setvar key=alias {{pipe}}|
:}|
/ife ( 'age' in databaseList){:
	/db-get source=chat age| /setvar key=age {{pipe}}|
:}|
/ife ( 'humanEquivalentAge' in databaseList){:
	/db-get source=chat humanEquivalentAge| /setvar key=humanEquivalentAge {{pipe}}|
:}|
/ife ( 'species' in databaseList){:
	/db-get source=chat species| /setvar key=species {{pipe}}|
:}|
/ife ( 'normal_form' in databaseList){:
	/db-get source=chat normal_form| /setvar key=normal_form {{pipe}}|
:}|
/ife ( 'speciesType' in databaseList){:
	/db-get source=chat speciesType| /setvar key=speciesType {{pipe}}|
:}|
/ife ( 'character_type' in databaseList){:
	/db-get source=chat character_type| /setvar key=character_type {{pipe}}|
:}|
/ife ( 'real' in databaseList){:
	/db-get source=chat real| /setvar key=real {{pipe}}|
:}|
/ife ( 'media_type' in databaseList){:
	/db-get source=chat media_type| /setvar key=media_type {{pipe}}|
:}|
/ife ( 'media_name' in databaseList){:
	/db-get source=chat media_name| /setvar key=media_name {{pipe}}|
:}|
/ife ( 'lifeStage' in databaseList){:
	/db-get source=chat lifeStage| /setvar key=lifeStage {{pipe}}|
:}|

//Parse character Age|
/setvar key=parcedAge {{noop}}|
/ife ( ((humanEquivalentAge != 'None') and (humanEquivalentAge != '')) and ( age != humanEquivalentAge) ) {:
	/setvar key=parcedAge {{getvar::age}} years-old — roughly {{getvar::humanEquivalentAge}} years-old in human years.|
:}|
/elseif (age != '') {:
	/setvar key=parcedAge {{getvar::age}} years-old|
:}|
//-----------|


//Parse character Species|
/setvar key=parsedSpecies {{noop}}|
/ife ((character_type == 'None') or ( character_type ==  normal_form)) {:
	/setvar key=character_type {{noop}}|
:}|
/ife ( normal_form == species ) {:
    /setvar key=parsedSpecies {{getvar::species}}|
:}|
/else {:
	/ife ( character_type != '') {:
		/setvar key=parsedSpecies "{{getvar::normal_form}} {{getvar::character_type}} {{getvar::species}}"|
	:}|
	/else {:
		/setvar key=parsedSpecies "{{getvar::normal_form}} {{getvar::species}}"|
	:}|
:}|
//-----------|

//Parse Real Character info|
/ife ( real == 'Yes') {:
	/setvar key=realInfoParced "{{newline}}- Origin: {{getvar::media_type}} – {{getvar::media_name}}"|
	/setvar key=realParced "{{char}} is a character from the {{getvar::media_type}} _{{getvar::media_name}}._"|
:}|
//-----------|

//Parse Nationality and Ethnicity|
/ife ( nationality == 'None' ) {:
	/setvar key=nationality {{noop}}|
:}|
/ife ( ethnicity == 'None' ) {:
	/setvar key=ethnicity {{noop}}|
:}|

/ife ( (nationality != '') and ( ethnicity != '')) {:
	/setvar key=parsedOrigin "- Origin: {{getvar::ethnicity}} from {{getvar::nationality}}"|
:}|
/elseif ( (nationality != '') and ( ethnicity != '')) {:
	/setvar key=parsedOrigin "- Origin: "From {{getvar::nationality}}"|
:}|
/else {:
	/setvar key=parsedOrigin {{noop}}|
:}|
//-----------|


/ife ( lastName == '' ) {:
	/setvar key=lastName None|
:}|
/ife ( ni == '' ) {:
	/setvar key=lastName None|
:}|