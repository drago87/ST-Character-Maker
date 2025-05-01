/let getEntry {: entry= hairS= 
	/let x {{var::hairS}}|
	/let y {{var::entry}}|
	/findentry field=comment file="CMC Appearance" {{var::y}}|
	/getentryfield field=content file="CMC Appearance" {{pipe}}|
	/split find="/\n/" {{pipe}}|
	/let key=a {{pipe}}|
	/wait 1|
	/find index=true {{var::a}} {:
		/test left={{var::item}} rule=in right={{var::x}}|
	:}|
	/getat index={{pipe}} {{var::a}}|
	/split find="/{{var::x}}:/g" {{pipe}}|
	/var key=a {{pipe}}|
	/wait 1|
	/getat index=1 {{var::a}}|
	/return {{pipe}}|
:}||

/:getEntry hairS="Buzz Cut" entry="Hair texture"|
/setvar key=a {{pipe}}|