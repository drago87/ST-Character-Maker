/db-list source=chat field=name |
/let key=databaseList {{pipe}}|
/ife ( 'first_name' in databaseList){:
	/db-get source=chat first_name| /setvar key=firstName {{pipe}}|
:}|
/ife ( 'last_name' in databaseList){:
	/db-get source=chat last_name| /setvar key=lastName {{pipe}}|
:}|
/ife ( 'age' in databaseList){:
	/db-get source=chat age| /setvar key=age {{pipe}}|
:}|
/ife ( 'human_equivalent_age' in databaseList){:
	/db-get source=chat human_equivalent_age| /setvar key=human_equivalent_age {{pipe}}|
:}|
/ife ( 'species' in databaseList){:
	/db-get source=chat species| /setvar key=species {{pipe}}|
:}|
/ife ( 'normal_form' in databaseList){:
	/db-get source=chat normal_form| /setvar key=normal_form {{pipe}}|
:}|
/ife ( 'type' in databaseList){:
	/db-get source=chat type| /setvar key=type {{pipe}}|
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


/ife ( human_equivalent_age != 'none') {:
	/let key=parcedAge {{getvar::age}} — roughly {{getvar::human_equivalent_age}} in human years.|
:}|

/ife (character_type == 'none'){:
	/setvar key=character_type {{noop}}|
:}|
/ife ( normal_form == species ) {:
    /let key=parsedSpecies {{getvar::species}}|
:}|
/else {:
	/ife ( character_type != ''){:
		/let key=parsedSpecies "{{getvar::normal_form}} {{getvar::species}} {{getvar::character_type}}"|
	:}|
	/else {:
		/let key=parsedSpecies "{{getvar::normal_form}} {{getvar::species}}"|
	:}|
:}|

/ife ( real == 'Yes') {:
	/let key=realParced {{newline}}- Origin: {{getvar::media_type}} – {{getvar::media_name}}|
:}|