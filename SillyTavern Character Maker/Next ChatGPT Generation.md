/whilee (i++ < 15) {:
/setvar key=it Exhibitionism|
			/findentry field=comment file="CMC Information" "Kink Role Prompt"|
			/getentryfield field=content file="CMC Information" {{pipe}}|
			/genraw {{pipe}}|
			/let key=kinkTemp {{pipe}}|
			/setvar key=kinkExp {{noop}}|
			/split {{var::kinkTemp}}|
			/foreach {{pipe}} {:
				/addvar key=kinkExp <div>{{var::item}}</div>|
			:}|
/ife (i < 10) {:
/setvar key=000{{var::i}} {{getvar::kinkExp}}|
:}|
/else
/setvar key=00{{var::i}} {{getvar::kinkExp}}|
:}|

:}|
/echo timeout=0 awaitDismissal=true Test|
/whilee (i++ < 15) {:

/ife (i < 10) {:
/flushvar 000{{var::i}}|
:}|
/else
/flushvar 00{{var::i}}|
:}|

:}|
/flushvar it|