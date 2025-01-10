# ST-QR-buttons Beta for new LALib version

<h1 align='center'>Quick Reply Buttons</h1>


Quck Reply buttons made for [Character Maker QR](https://chub.ai/characters/Drago87/character-maker-sillytavern-quick-reply-driven-0eb2c2852a4f)


<h1 align='center'>Lorebooks</h1>

<h2 align='center'>Character Maker Combined NSFW</h2>

[🔗](https://github.com/drago87/ST-Character-Maker/blob/main/Lorebooks/Character%20Maker%20Combined%20NSFW.json)
The lorebook that all information and templates the [Character Maker QR]([https://chub.ai/characters/Drago87/character-maker-lore-v4-c2bdf3ee5aad](https://chub.ai/characters/Drago87/character-maker-sillytavern-quick-reply-driven-0eb2c2852a4f)) needs to functions.
Sort it after UID ↗ to make it esier to navigate.

[🔗](https://github.com/drago87/ST-Character-Maker/blob/main/Lorebooks/Character%20Maker%20Combined%20NSFW%20GenRaw.json)
A lorebook that controlls all generations in the QR buttons
Sort it after UID ↗ to make it esier to navigate.


<h2 align='center'>TabbyAPI Loader Setting</h2>

[🔗](https://github.com/drago87/ST-Character-Maker/blob/main/Lorebooks/Character%20Maker%20Combined%20NSFW.json)
Is a Lorebook with the Local LLM models i have tested and what setting i have used for them. (Optional)

<h1 align='center'>Other Needed stuff</h1>

[🔗](https://github.com/drago87/ST-Character-Maker/blob/main/Lorebooks/Work%20In%20Progress/Character%20Maker%20Combined%20NSFW.json) The Loorebook for the new V6 Card

[🔗](https://github.com/drago87/ST-Character-Maker/blob/main/Lorebooks/Character%20Maker%20Combined%20NSFW%20GenRaw.json) The Loorebook driving the generation.

[🔗](https://github.com/drago87/ST-Character-Maker/blob/main/Quick%20Reply%20Buttons/Character%20Maker.json) The visible quick reply buttons for the V6 card (This file needs to be enabled in Global Quick Reply Sets)
 
[🔗](https://chub.ai/characters/Drago87/character-maker-sillytavern-quick-reply-driven-0eb2c2852a4f) The invisible quick reply buttons for the V6 card (This only need to be imported)
 
![image](https://github.com/user-attachments/assets/601ab79c-2b59-40f0-873a-62a6bc629b84)

[🔗](https://github.com/drago87/ST-Character-Maker/tree/main/Quick%20Reply%20Buttons/Work%20In%20Progress%20Plain%20Text) Same as above but in plain text for easier readabillity

<h2 align='center'>________________________________</h2>

<h4 align='center'><div>Version history</div></h4>

<h4 align='center'><div>V6.1.3 - Beta</div></h4>
Added a explanation on variables that can be used during generation

Added new Generation option. Extra character that will be exported as a Lorebook entry.

<h4 align='center'><div>Update</div></h4>

[Variables Lorebook](https://github.com/drago87/ST-Character-Maker/blob/main/Lorebooks/Character%20Maker%20Combined%20NSFW%20Variables.json)

[Character Maker v4](https://github.com/drago87/ST-Character-Maker/blob/main/Quick%20Reply%20Buttons/Character%20Maker%20V4.json)

[Character Maker QR](https://github.com/drago87/ST-Character-Maker/blob/main/Quick%20Reply%20Buttons/Character%20Maker.json)

[GenRaw Lorebook](https://github.com/drago87/ST-Character-Maker/blob/main/Lorebooks/Character%20Maker%20Combined%20NSFW%20GenRaw.json)

<h4 align='center'><div>V6.1.2 - Beta</div></h4>
Added a quick generate option

<h4 align='center'><div>Update</div></h4>

[Character Maker v4](https://github.com/drago87/ST-Character-Maker/blob/main/Quick%20Reply%20Buttons/Character%20Maker%20V4.json)

<h4 align='center'><div>V6.1.1 - Beta</div></h4>
Fixed Automation QR

Fixed Export QR making sure that each have the right triggers and contain the information needed for the LLM to know it is for the character.

Changed most outputs so that it points more to the character preventing the LLM from being as confused.

<h4 align='center'><div>V6.1.0 - Beta</div></h4>
Added a QR button to export part of the character to a Lorebook
Added a QR button to export the rest of the character to a character sheet json file.

Added a prompt builder guide to the scenario.

Changed common words to word exchange. eg what the character says instead of a word.
Rewritten most of the Appearance Info generation prompts.

The Appearance Info will now ask for what type of measurements you want to use(cm, m, ft., in., g, kg, oz, lbs)

Now it will only show the QR buttons when the Character Generator  character is selected. (Only the ones that are associated with the card will be hidden)

Added tag for type (Antro, Beastkin etc..) Missed adding it after i remade the initial generation on new chat.

Added choice for NSFW/SFW generation(Tell me if i missed something)
Changed
Time period -> Takes place during
World Type -> Reality Level

Made the system message that explains changes done when copying to the character sheet clearer.

Will now try to find information about nickname, age, species(if not set to human) and occupation

Added a printout for the characters gender (No ide how i had missed it so far.)

Will now rename the chat to YYYY-MM-DD Time FirstName LastName when Basic Information is done.

Fixed a problem where if the last message was hidden it would be overwritten instead of swiped when using the QR swipe.

Lets you generate the siblings to put into Lorebook. Will make new messages for each sibling to help with export.

Have split Enemy and Rival to make it more readable and added a None button for it.

Known and Latent kinks output have been changed to make one message for each kink to enable better exportation to lorebook.

Extras output have been split into three outputs one for Character Description, one for speech examples and one for tags

get info changed to save the id of the last user message.

flushvar change to not remove the id of the last user message.

<h4 align='center'><div>Update</div></h4>

[Character Maker v4](https://github.com/drago87/ST-Character-Maker/blob/main/Quick%20Reply%20Buttons/Character%20Maker%20V4.json)

[GenRaw Lorebook](https://github.com/drago87/ST-Character-Maker/blob/main/Lorebooks/Character%20Maker%20Combined%20NSFW%20GenRaw.json)

<h4 align='center'><div>V6.0.8 - Beta</div></h4>
Updated the github with a Guide

[Installation Guide](https://github.com/drago87/ST-Character-Maker/wiki)

<h4 align='center'><div>V6.0.7 - Beta</div></h4>
Changed when pressing the 'Change Guidance' button it will keep the old guidance and let you edit it.

Added a choice to sexual knowledge and variables for that in the lorebook

When making a new character sets the persona to 'user' if it exists. If not it will make a temporary empty persona named 'user'.

Fixed some genraw that used fnames instead of fname

Added a way to have no dialect.

Added a way to select what outfit you want to use for the scenario.

Updated Character Rules

Added a choice for for Known and Latent kinks that can be changed from a new [Lorebook](https://github.com/drago87/ST-Character-Maker/blob/main/Lorebooks/Character%20Maker%20Combined%20NSFW%20Variables.json) (Needed) this makes it easier to guide the generations to what you want.

Fixed missing | in known and latent kinks preventing old information to be purged.

Added missed guidance for personality

Fixed posting positive traits under negative traits loosing the negative traits altogether.

Renamed Butt to Buttocks
Added skin_color to generations (Had forgotten to add it to system in genraw)
Added skin color and tanning to more generations.

Fixed typo in genraw

Fixed problems when using Debug mode during 'Basic Information' generation.

Added Friend to user generation.

Fixed spelling mistakes.

<h4 align='center'><div>Update</div></h4>

[Character Maker v4](https://github.com/drago87/ST-Character-Maker/blob/main/Quick%20Reply%20Buttons/Character%20Maker%20V4.json)

[GenRaw Lorebook](https://github.com/drago87/ST-Character-Maker/blob/main/Lorebooks/Character%20Maker%20Combined%20NSFW%20GenRaw.json)

[Character Maker Lorebook](https://github.com/drago87/ST-Character-Maker/blob/main/Lorebooks/Character%20Maker%20Combined%20NSFW.json)

<h4 align='center'><div>V6.0.7 - Beta</div></h4>
Changed when pressing the 'Change Guidance' button it will keep the old guidance and let you edit it.

Added a choice to sexual knowledge and variables for that in the lorebook

When making a new character sets the persona to 'user' if it exists. If not it will make a temporary empty persona named 'user'.

Fixed some genraw that used fnames instead of fname

Added a way to have no dialect.

Added a way to select what outfit you want to use for the scenario.

Updated Character Rules

Added a choice for for Known and Latent kinks that can be changed from a new [Lorebook](https://github.com/drago87/ST-Character-Maker/blob/main/Lorebooks/Character%20Maker%20Combined%20NSFW%20Variables.json) (Needed) this makes it easier to guide the generations to what you want.

Fixed missing | in known and latent kinks preventing old information to be purged.

Added missed guidance for personality

Fixed posting positive traits under negative traits loosing the negative traits altogether.

Renamed Butt to Buttocks
Added skin_color to generations (Had forgotten to add it to system in genraw)
Added skin color and tanning to more generations.

Fixed typo in genraw

Fixed problems when using Debug mode during 'Basic Information' generation.

Added Friend to user generation.

Fixed spelling mistakes.

<h4 align='center'><div>Update</div></h4>

[Character Maker v4](https://github.com/drago87/ST-Character-Maker/blob/main/Quick%20Reply%20Buttons/Character%20Maker%20V4.json)

[GenRaw Lorebook](https://github.com/drago87/ST-Character-Maker/blob/main/Lorebooks/Character%20Maker%20Combined%20NSFW%20GenRaw.json)

[Character Maker Lorebook](https://github.com/drago87/ST-Character-Maker/blob/main/Lorebooks/Character%20Maker%20Combined%20NSFW.json)

<h4 align='center'><div>V6.0.5 - Beta</div></h4>
When editing a reply i have change the cancel to redo the reply instead of stopping the generation altogether. (Only in 'Basic Information' for now. Will update the others as i go)
Fixed error in Genres
Fixed Full Name input

<h4 align='center'><div>Update</div></h4>

[Character Maker v4](https://github.com/drago87/ST-Character-Maker/blob/main/Quick%20Reply%20Buttons/Character%20Maker%20V4.json)

<h4 align='center'><div>V6.0.4 - Beta</div></h4>
Added more functionality to the debug mode.
It will ask if you want to enable debug mode when making a new character.
If debug mode is enabled it will let you see and edit what is passed to each /genraw.
When copying rules you will be able to see and edit them in debug mode.
When making a scenario debug mode lets you see and edit the prompt that is sent to the continue function.

<h4 align='center'><div>Update</div></h4>

[Character Maker v4](https://github.com/drago87/ST-Character-Maker/blob/main/Quick%20Reply%20Buttons/Character%20Maker%20V4.json)

<h4 align='center'><div>V6.0.3 - Beta</div></h4>
Added Guidance to missing generations
Refined prompt for daily activities when making 'Contextual Information' by using a /genraw to ask the LLM if the characters occupation is deemed work or school.
Added Full Name to the 'Basic Information'
Changed Output format for the outfit to better indicate nudity.
Added Why char like the kink to known kinks.
Fixed genraw for user age.
Added how the positive and negative traits manifests in the character.
Fixed not emptying outputList
Fixed Quirks not generating
Fixed Infinite loop for Negative Traits
Fixed Error when making female breasts.
Fixed using same variable for different things breaking when generating user data.
Fixed Tags to be uppercase.
Fixed age choice for teacher and student when generating user data.

Updated Choice
03. Generate Personality Traits And Quirks
04. Character's Relation to user
05. Generate Relationship Information
06. Generate Known Kinks
07. Generate Latent Kinks
08. Generate Outfit and Gear (Can Generate Multiple)
09. Generate Background Info
10. Generate Interaction Style
11. Generate Contextual Information
12. Generate Additional Notes
13. Generate Spells and Abilities
15. Generate Extras

To the new LALib version

<h4 align='center'><div>Update</div></h4>

[GenRaw Lorebook](https://github.com/drago87/ST-Character-Maker/blob/main/Lorebooks/Character%20Maker%20Combined%20NSFW%20GenRaw.json)

[Character Maker Lorebook](https://github.com/drago87/ST-Character-Maker/blob/main/Lorebooks/Character%20Maker%20Combined%20NSFW.json)

[Character Maker v4](https://github.com/drago87/ST-Character-Maker/blob/main/Quick%20Reply%20Buttons/Character%20Maker%20V4.json)

[Character Maker QR](https://github.com/drago87/ST-Character-Maker/blob/main/Quick%20Reply%20Buttons/Character%20Maker.json)

<h4 align='center'><div>V6.0.2 - Beta</div></h4>
Fixed wrong check in Basic Information.

<h4 align='center'><div>Update</div></h4>

[Character Maker v4](https://github.com/drago87/ST-Character-Maker/blob/main/Quick%20Reply%20Buttons/Character%20Maker%20V4.json)

<h4 align='center'><div>V6.0.1 - Beta<h4 align='center'><div>
Rewrote the Tags and Transform.
Removed  ethnicity from non-humans.
Fixed Check for type of character.
Fixed problem when making a character that can transform.
Fixed wrong variable name error.
Fixed ethnicity in information
Fixed missed :}| in last_name breaking rerolling
Fixed sub_species not saving giving a warning.

<h4 align='center'><div>Update</div></h4>

[Character Maker v4](https://github.com/drago87/ST-Character-Maker/blob/main/Quick%20Reply%20Buttons/Character%20Maker%20V4.json)

[Character Maker QR](https://github.com/drago87/ST-Character-Maker/blob/main/Quick%20Reply%20Buttons/Character%20Maker.json)
 
<h4 align='center'><div>V6.0.0 - Beta</div></h4>
These are the ones that have been updated to the new LALib version:
'
New Chat and Set Character Gender and Type
Character Generator Swipe
Generate Character Choice
Debug On/Off
'
Generate Character Choice that are updated are:
'
01. Generate Basic Information (form)
02. Generate Appearance Info (Can Generate Multiple)
14. Copy Character Rules
16. Generate Scenario
'
And all required QR buttons for the above.
The rest should still work but will give warnings.

Updated for new [LALib](https://github.com/LenAnderson/SillyTavern-LALib) version make sure to update.
Added check to make sure LALib is installed and enabled.
Added Skin Color for species without covering.
Added printout for Realistic characters (Characters from shows/anime's/books etc..) only showing when selecting it on new character.
Added spoken language (single or multiple)
Added nationality and ethnicity to the generation. (option to ignore it)
Added exclusion and guidance to most if not all dialogue options to help get the result you want.
Added generation for user's Relation to the generated character.
Moved the order of generation.
Added guidance for 'Additional Notes' (Letting you prevent specific things from generating or pushing the generation towards specific things)
Moved general exclusion from "Get Char Info" to Lorebook.
Fixed minor typos and stuff

<h4 align='center'><div>Update</div></h4>

[GenRaw Lorebook](https://github.com/drago87/ST-Character-Maker/blob/main/Lorebooks/Character%20Maker%20Combined%20NSFW%20GenRaw.json)

[Character Maker Lorebook](https://github.com/drago87/ST-Character-Maker/blob/main/Lorebooks/Character%20Maker%20Combined%20NSFW.json)

[Character Maker v4](https://github.com/drago87/ST-Character-Maker/blob/main/Quick%20Reply%20Buttons/Character%20Maker%20V4.json)

[Character Maker QR](https://github.com/drago87/ST-Character-Maker/blob/main/Quick%20Reply%20Buttons/Character%20Maker.json)
