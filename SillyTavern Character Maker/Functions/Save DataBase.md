/db-list source=chat field=name |
/let key=a {{pipe}}|
/foreach {{getvar::dataBaseNames}} {:
	/ife ( ('{{var::item}}' not in a) and ({{var::item}} != '')) {:
		/getvar key={{var::item}}|
		/db-add source=chat name={{var::item}} {{pipe}}|
		/db-disable source=chat {{var::item}}|
	:}|
	/elseif ({{var::item}} != '') {:
		/getvar key={{var::item}}|
		/db-update source=chat name={{var::item}} {{pipe}}|
		/db-disable source=chat {{var::item}}|
	:}|
:}|

/flushvar dataBaseNames|