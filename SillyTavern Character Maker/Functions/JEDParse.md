/ife (timePeriod != '') {:
	/messages names=off 0|
	/re-replace find="/--TimePeriod--/g" replace="{{getvar::timePeriod}}" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/ife (seasons != '') {:
	/messages names=off 0|
	/re-replace find="/--Season--/g" replace="{{getvar::seasons}}" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/elseif ( seasons == 'None') {:
	/messages names=off 0|
	/re-replace find="/--Season--/g" replace="" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/ife (worldDetails != '') {:
	/messages names=off 0|
	/re-replace find="/--WorldDetails--/g" replace="{{getvar::worldDetails}}" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/ife (extraCharacters != '') {:
	/messages names=off 0|
	/re-replace find="/--ExtraCharacters--/g" replace=", {{getvar::extraCharacters}}" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/ife ((lore != '') and ( lore != 'None')) {:
	/messages names=off 0|
	/re-replace find="/--Lore--/g" replace="## LORE{{newline}}{{getvar::lore}}{{newline}}{{newline}}" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/elseif ( lore == 'None') {:
	/messages names=off 0|
	/re-replace find="/--Lore--/g" replace="" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/ife (scenarioOverview != '') {:
	/messages names=off 0|
	/re-replace find="/--ScenarioOverview--/g" replace="{{getvar::scenarioOverview}}" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/ife (characterOverview != '') {:
	/messages names=off 0|
	/re-replace find="/--CharacterOverview--/g" replace="{{getvar::characterOverview}}" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/ife ( (lastName != '') and (lastName != 'None')) {:
	/messages names=off 0|
	/re-replace find="/--LastName--/g" replace="{{getvar::lastName}}" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/elseif (lastName == 'None') {:
	/messages names=off 0|
	/re-replace find="/--LastName--/g" replace="" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/ife ( (alias != '') and (alias != 'None')){:
	/messages names=off 0|
	/re-replace find="/--Alias1--/g" replace=", Alias" {{pipe}}|
	/re-replace find="/--Alias--/g" replace=", {{getvar::alias}}" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/elseif (alias == 'None' ) {:
	/messages names=off 0|
	/re-replace find="/--Alias1--/g" replace="" {{pipe}}|
	/re-replace find="/--Alias--/g" replace="" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/ife (parsedSpecies != '') {:
	/messages names=off 0|
	/re-replace find="/--Species--/g" replace="{{getvar::parsedSpecies}}" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/ife (gender != '') {:
	/messages names=off 0|
	/re-replace find="/--Gender--/g" replace="{{getvar::gender}}" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/ife ((futanari != '') and (futanari == 'Yes')) {:
	/messages names=off 0|
	/re-replace find="/--Futanari--/g" replace=" Futanari" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/else {:
	/messages names=off 0|
	/re-replace find="/--Futanari--/g" replace="" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/ife ((length != '') and (length != 'None')) {:
	/messages names=off 0|
	/re-replace find="/--Length--/g" replace="{{getvar::length}}{{newline}}" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/elseif (length == 'None') {:
	/messages names=off 0|
	/re-replace find="/--Length--/g" replace="" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/ife (height != '') {:
	/messages names=off 0|
	/re-replace find="/--Height--/g" replace="{{getvar::height}}" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/ife (age != '') {:
	/messages names=off 0|
	/re-replace find="/--Age--/g" replace="{{getvar::age}}" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/ife (hair != '') {:
	/messages names=off 0|
	/re-replace find="/--Hair--/g" replace="{{getvar::hair}}" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/ife (eyes != '') {:
	/messages names=off 0|
	/re-replace find="/--Eyes--/g" replace="{{getvar::eyes}}" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/ife (face != '') {:
	/messages names=off 0|
	/re-replace find="/--Face--/g" replace="{{getvar::face}}" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/ife (body != '') {:
	/messages names=off 0|
	/re-replace find="/--Body--/g" replace="{{getvar::body}}" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/ife (nipples != '') {:
	/messages names=off 0|
	/re-replace find="/--Nipples--/g" replace="{{newline}} - Nipple Descriptors: {{getvar::nipples}}" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/elseif (export == 'Yes' ) {:
	/messages names=off 0|
	/re-replace find="/--Nipples--/g" replace="" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/ife ( (breast != '') and (breast != 'None')) {:
	/messages names=off 0|
	/re-replace find="/--Breasts--/g" replace="{{newline}} - Breast Descriptors: {{getvar::breast}}" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/elseif (breast == 'None' ) {:
	/messages names=off 0|
	/re-replace find="/--Breasts--/g" replace="" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/ife ((appearanceGenitals != '') and (appearanceGenitals != '') and (futanari == 'yes')) {:
	/messages names=off 0|
	/re-replace find="/--Genitals--/g" replace="{{newline}} - Genitals: {{getvar::appearanceGenitals}}" {{pipe}}|
	/re-replace find="/--Pussy--/g" replace="" {{pipe}}|
	/re-replace find="/--Cock--/g" replace="" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/elseif (appearancePussy != '') {:
	/messages names=off 0|
	/re-replace find="/--Pussy--/g" replace="{{newline}} - Pussy: {{getvar::appearancePussy}}" {{pipe}}|
	/re-replace find="/--Cock--/g" replace="" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/elseif (appearanceCock != '') {:
	/messages names=off 0|
	/re-replace find="/--Cock--/g" replace="{{newline}} - Cock: {{getvar::appearanceCock}}" {{pipe}}|
	/re-replace find="/--Pussy--/g" replace="" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/ife (appearanceAnus != '') {:
	/messages names=off 0|
	/re-replace find="/--Anus--/g" replace="{{getvar::appearanceAnus}}" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/ife (appearanceFeatures != '') {:
	/messages names=off 0|
	/re-replace find="/--Features--/g" replace="{{getvar::appearanceFeatures}}" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/ife (apperanceTraits != '') {:
	/messages names=off 0|
	/re-replace find="/--ApperanceTraits--/g" replace="{{getvar::apperanceTraits}}" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/ife (outfitHead != '') {:
	/messages names=off 0|
	/re-replace find="/--OutfitHead--/g" replace="{{getvar::outfitHead}}" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/ife (outfitAccessories != '') {:
	/messages names=off 0|
	/re-replace find="/--OutfitAccessories--/g" replace="{{getvar::outfitAccessories}}" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/ife (outfitMakeup != '') {:
	/messages names=off 0|
	/re-replace find="/--OutfitMakeup--/g" replace="{{getvar::outfitMakeup}}" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/ife (outfitNeck != '') {:
	/messages names=off 0|
	/re-replace find="/--OutfitNeck--/g" replace="{{getvar::outfitNeck}}" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/ife (outfitTop != '') {:
	/messages names=off 0|
	/re-replace find="/--OutfitTop--/g" replace="{{getvar::outfitTop}}" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/ife (outfitBottom != '') {:
	/messages names=off 0|
	/re-replace find="/--OutfitBottom--/g" replace="{{getvar::outfitBottom}}" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/ife (outfitLegs != '') {:
	/messages names=off 0|
	/re-replace find="/--OutfitLegs--/g" replace="{{getvar::outfitLegs}}" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/ife (outfitShoes != '') {:
	/messages names=off 0|
	/re-replace find="/--OutfitShoes--/g" replace="{{getvar::outfitShoes}}" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/ife (outfitUnderwear != '') {:
	/messages names=off 0|
	/re-replace find="/--OutfitUnderwear--/g" replace="{{getvar::outfitUnderwear}}" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/ife (appearanceQAList != '') {:
	/messages names=off 0|
	/re-replace find="/--AppearanceQAList--/g" replace="{{getvar::appearanceQAList}}" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/ife (backstory != '') {:
	/messages names=off 0|
	/re-replace find="/--Backstory--/g" replace="{{getvar::backstory}}" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/ife (residence != '') {:
	/messages names=off 0|
	/re-replace find="/--Residence--/g" replace="{{getvar::residence}}" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/ife (connections != '') {:
	/messages names=off 0|
	/re-replace find="/--Connections--/g" replace="{{getvar::connections}}" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/ife (secret != '') {:
	/messages names=off 0|
	/re-replace find="/--Secret--/g" replace="### SECRET{{newline}}{{getvar::secret}}" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/elseif (export == 'Yes' ) {:
	/messages names=off 0|
	/re-replace find="/--Secret--/g" replace="" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/ife (itemList != '') {:
	/messages names=off 0|
	/re-replace find="/--ItemList--/g" replace="### INVENTORY{{newline}}{{getvar::itemList}}" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/elseif (export == 'Yes' ) {:
	/messages names=off 0|
	/re-replace find="/--ItemList--/g" replace="" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/ife ( (abilities != '') and (abilities != 'None')) {:
	/messages names=off 0|
	/re-replace find="/--Abilities--/g" replace="### ABILITIES{{newline}}{{getvar::abilities}}" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/elseif (abilities == 'None') {:
	/messages names=off 0|
	/re-replace find="/--Abilities--/g" replace="" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/ife (archetype != '') {:
	/messages names=off 0|
	/re-replace find="/--Archetype--/g" replace="{{getvar::archetype}}" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/ife ( (parsedAlignment != '') and  (parsedAlignment != 'None')) {:
	/messages names=off 0|
	/re-replace find="/--Alignment--/g" replace="{{newline}}{{newline}}{{getvar::parsedAlignment}}" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/elseif (parsedAlignment == 'None' ) {:
	/messages names=off 0|
	/re-replace find="/--Alignment--/g" replace="" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/ife (personalityTags != '') {:
	/messages names=off 0|
	/re-replace find="/--PersonalityTags--/g" replace="- Personality Tags:{{getvar::personalityTags}}" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/ife ( intelligenceLevel != '') {:
	/messages names=off 0|
	/re-replace find="/--IntelligenceLevel--/g" replace="- Personality Tags:{{getvar::intelligenceLevel}}" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/ife ( (cognitiveAbilities != '') and (cognitiveAbilities != 'None') ) {:
	/messages names=off 0|
	/re-replace find="/--CognitiveAbilities--/g" replace="{{newline}}{{newline}}- Cognitive Abilities: {{getvar::cognitiveAbilities}}" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/elseif (cognitiveAbilities == 'None' ) {:
	/messages names=off 0|
	/re-replace find="/--CognitiveAbilities--/g" replace="" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/ife ( socialBehavior != '') {:
	/messages names=off 0|
	/re-replace find="/--SocialBehavior--/g" replace="- Personality Tags:{{getvar::socialBehavior}}" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/ife ( (socialSkills != '') and (socialSkills != 'None')) {:
	/messages names=off 0|
	/re-replace find="/--SocialSkills--/g" replace="{{newline}}{{newline}}- Social Skills and Integration Into Society:{{getvar::socialSkills}}" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/elseif (socialSkills == 'None' ) {:
	/messages names=off 0|
	/re-replace find="/--SocialSkills--/g" replace="" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/ife (parsedAspiration != '') {:
	/messages names=off 0|
	/re-replace find="/--MainAspiration--/g" replace="{{getvar::mainAspiration}}" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/ife (parsedTraits != '') {:
	/messages names=off 0|
	/re-replace find="/--UniqueTraits--/g" replace="{{getvar::parsedTraits}}" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/ife (personalityQA != '') {:
	/messages names=off 0|
	/re-replace find="/--PersonalityQA--/g" replace="{{getvar::personalityQA}}" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/ife (behaviorNotes != '') {:
	/messages names=off 0|
	/re-replace find="/--BehaviorNotes--/g" replace="{{getvar::behaviorNotes}}" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/ife (sexualOrientation != '') {:
	/messages names=off 0|
	/re-replace find="/--SexualOrientation--/g" replace="{{getvar::sexualOrientation}}" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/ife (sexualRole != '') {:
	/messages names=off 0|
	/re-replace find="/--SexualRole--/g" replace="{{getvar::sexualRole}}" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/ife (sexualityQA != '') {:
	/messages names=off 0|
	/re-replace find="/--SexualityQA--/g" replace="{{getvar::sexualityQA}}" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/ife (sexualNotes != '') {:
	/messages names=off 0|
	/re-replace find="/--SexualNotes--/g" replace="{{getvar::sexualNotes}}" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/ife (speachStyle != '') {:
	/messages names=off 0|
	/re-replace find="/--SpeachStyle--/g" replace="{{getvar::speachStyle}}" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/ife (speachQuirks != '') {:
	/messages names=off 0|
	/re-replace find="/--SpeachQuirks--/g" replace="{{getvar::speachQuirks}}" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/ife (speachTics != '') {:
	/messages names=off 0|
	/re-replace find="/--SpeachTics--/g" replace="{{getvar::speachTics}}" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/ife (speachExamples != '') {:
	/messages names=off 0|
	/re-replace find="/--SpeachExamples--/g" replace="{{getvar::speachExamples}}" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/ife (synonyms != '') {:
	/messages names=off 0|
	/re-replace find="/--Synonyms--/g" replace="{{getvar::synonyms}}" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/ife ( (storyPlan != '') and (storyPlan != 'None') ){:
	/messages names=off 0|
	/re-replace find="/--StoryPlan--/g" replace="## PREMADE STORY PLAN{{newline}}{{getvar::storyPlan}}" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/elseif (storyPlan == 'None' ) {:
	/messages names=off 0|
	/re-replace find="/--StoryPlan--/g" replace="" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/ife (previously != '') {:
	/messages names=off 0|
	/re-replace find="/--Previously--/g" replace="{{getvar::previously}}" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/ife (notes != '') {:
	/messages names=off 0|
	/re-replace find="/--Notes--/g" replace="{{getvar::notes}}" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/ife ((user != '') and (user == 'Yes')) {:
	/messages names=off 0|
	/re-replace find="/--User1--,\s/g" replace="--User--, " {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|
/elseif ((user != '') and (user != 'Yes')) {:
	/messages names=off 0|
	/re-replace find="/--User1--,\s/g" replace="" {{pipe}}|
	/message-edit message=0 await=true {{pipe}}|
:}|