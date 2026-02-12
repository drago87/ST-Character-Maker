/qr-list CMC Menu|
/let key=menylist {{pipe}}|
/ife ('CMC Menu2' in menylist) {:
	/qr-delete set="CMC Menu" label="CMC Menu"|
	/wait 100|
	/qr-update set="CMC Menu" label="CMC Menu2" newlabel="CMC Menu"|
:}|