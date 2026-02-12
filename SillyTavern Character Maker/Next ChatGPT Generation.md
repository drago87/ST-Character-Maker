/ife ((labiaMinoraOutsideColor == '') or (skip == 'Update')) {:
			/findentry field=comment file="CMC Variables" "Labia Minora Outside Color"|
			/let key=wi_uid {{pipe}}|
			/getentryfield field=content file="CMC Variables" {{var::wi_uid}}|
			/let key=list {{pipe}}|
			/split find="---" {{var::list}}|
			/var key=list {{pipe}}|
			/buttons labels={{var::list}} What is the color of {{getvar::firstName}}'s Labia Minora's Outside?|
			/setvar key=labiaMinoraOutsideColor {{pipe}}|
			/ife (labiaMinoraOutsideColor == '') {:
		        /echo Aborting |
		        /abort
		    :}|
		    /elseif (labiaMinoraOutsideColor == 'Own Color') {:
			    /input Type the color your want {{getvar::firstName}}'s Labia Minora's Outside Color to be.|
			    /setvar key=labiaMinoraOutsideColor {{pipe}}|
				/ife (labiaMinoraOutsideColor == '') {:
			        /echo Aborting |
			        /abort
			    :}|
		    :}|
		:}|


		/ife (labiaMinoraOutsideColor != 'Skip') {:
			/addvar key=extra "- Labia Minora's Outside Color: {{getvar::labiaMinoraOutsideColor}}"|
		:}|