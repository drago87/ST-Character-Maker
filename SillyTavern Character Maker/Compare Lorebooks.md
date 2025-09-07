/wi-list-entries CMC Generation Prompts dans-personalityengine-v1.1.0-12b-q6_k|
/map {{pipe}} {:
    /getat index=entries {{var::item}} |
    /map {{pipe}} {:
        /getat index=comment {{var::item}}
    :}
:} |
/setvar key=a {{pipe}}|
/getvar key=a index=0|
/setvar key=a {{pipe}}|

/wi-list-entries CMC Generation Prompts EsotericSage-12B.i1-Q6_K|
/map {{pipe}} {:
    /getat index=entries {{var::item}} |
    /map {{pipe}} {:
        /getat index=comment {{var::item}}
    :}
:} |
/setvar key=b {{pipe}}|
/getvar key=b index=0|
/setvar key=b {{pipe}}|

/setvar key=dnotine []|
/foreach {{getvar::a}} {:
	/ife ('{{var::item}}' not in b) {:
		/addvar key=dnotine {{var::item}}|
	:}|
:}|

/setvar key=enotind []|
/foreach {{getvar::b}} {:
	/ife ('{{var::item}}' not in a) {:
		/addvar key=enotind {{var::item}}|
	:}|
:}|