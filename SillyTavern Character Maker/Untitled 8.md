/fetch https://files.catbox.moe/4en3sz.json|
/let key=f {{pipe}}|
/ife ( 'Personas' not in databaseList){:
	/db-add source=chat name="Personas.json" {{var::f}}|
	/db-disable source=chat Personas.json|
:}|
/else {:
	/db-update source=chat name="Personas.json" {{var::f}}|
	/db-disable source=chat Personas.json|
:}|
/databank|