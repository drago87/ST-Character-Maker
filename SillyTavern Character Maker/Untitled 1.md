/setvar key=00 {{noop}}|
/whilee (i++ < 10) {:
/getvar key="00 Genraw"|
/genraw {{pipe}}|
/addvar key=00 {{pipe}}{{newline}}---{{newline}}|
:}|