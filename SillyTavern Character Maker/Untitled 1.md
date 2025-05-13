/find index=true {{var::genState}} {:
	/test left={{getvar::item}} rule=eq right="Random"|
:}|
/slice start=0 end={{pipe}} {{var::genState}}|

/find index=true {{getvar::a}} {:
	/test left={{var::item}} rule=eq right="Test2"|
:}|
/splice start={{pipe}} delete=1 {{getvar::a}}|
/setvar key=a0 {{pipe}}|
/wait 100|
/unshift {{getvar::a0}} Test2|
/setvar key=a0 {{pipe}}|