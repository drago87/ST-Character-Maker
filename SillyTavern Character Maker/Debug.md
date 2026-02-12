/qr-list CMC Logic|
/setvar key=qr-list {{pipe}} |
/ife (debug != 'Yes' ){:
  /setvar key=debug Yes|
  /echo Debug Enabled||
  /find {{getvar::qr-list}} {:
	  /test left={{var::item}} right="Debug" rule=in
  :}|
  /qr-update set="CMC Main" label={{pipe}} newlabel="Debug Is On"|
:}|
/else {:
  /setvar key=debug No|
  /echo Debug Disabled||
   /find {{getvar::qr-list}} {:
	  /test left={{var::item}} right="Debug" rule=in
  :}|
  /qr-update set="CMC Main" label={{pipe}} newlabel="Debug Is Off"|
:}|
