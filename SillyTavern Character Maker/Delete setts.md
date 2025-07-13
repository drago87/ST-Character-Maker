/qr-set-delete CMC Generate|
/qr-set-delete CMC Logic|
/qr-chat-set-off CMC Main|
/qr-set-delete CMC Main |

/wait 1000|
/qr-set-create CMC Temp|
/fetch https://raw.githubusercontent.com/drago87/ST-Character-Maker/refs/heads/Fetch-Files/SillyTavern%20Character%20Maker/Install/Install%20QR.md|

/qr-create set="CMC Temp" label="Install QR" {{pipe}}|

/:"CMC Temp.Install QR"|

/wait 1000|
/qr-set-delete CMC Temp |
/wait 10000|
/reload-page|