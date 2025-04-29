/qr-set-create CMC Temp|
/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/Install/Check%20LALib.md|
/qr-create set="CMC Temp" label="Character maker install script" {{pipe}}|
/qr-update set="CMC Temp" label="Character maker install script" title="A script that will walk you through the setup."|
/:"CMC Temp.Character maker install script"|






/*
/let x ["Test", "Test2"] |
/getat index=1 {{var::x}} |
/let key=y {{pipe}}|
/echo {{var::y}}

/let x ["Test", "Test2"] |
/len {{var::x}}|
/var key=x index={{pipe}} Test3|
/setvar key=a {{var::x}}

/setvar key={{var::variableName}} {{var::output}}|
/var key=context {{noop}}|
/var key=examples {{noop}}|
/var key=task {{pipe}}|
/var key=instruct {{pipe}}|
/var key=content {{pipe}}|

/qr-get set="Character Maker V4" id=38|
/let key=a {{pipe}}|
/getat index=id {{var::a}}|
/setvar key=1a {{pipe}}|
*|