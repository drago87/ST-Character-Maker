/ife ( debug != 'Yes'){:
	/echo Flushing variables|

	/listvar scope=local return=object | /setvar  key=flvars {{pipe}}|
	/foreach {{getvar::flvars}} {:
		/setvar key=it1 {{var::item}}|
		/setvar key=in1 {{var::index}}|
		/foreach {{getvar::it1}} {:
			/setvar key=it2 {{var::item}}|
			/setvar key=in2 {{var::index}}|
			/ife ( in2 == 'key'){:
				/ife ( (it2 != 'userid') and (it2 != 'have_read_install_instructions') and ( it2 != 'savedForSwipe')){:
					/flushvar {{getvar::it2}}|
				:}|
				/elseif ( (it2 == 'savedForSwipe') and ( savedForSwipe != '')) {:
					/echo timeout=0 extendedTimeout=0 awaitDismissal=true Deleted message saved to the variable 'savedForSwipe'|
				:}|
			:}|
		:}|
	:}|
	/flushvar flvars|
	/flushvar it1|
	/flushvar in1|
	/flushvar it2|
	/flushvar in2|
:}|
/else {: /echo Not Flushing variables Debug enabled |:}|
/flushglobalvar run|
/abort
