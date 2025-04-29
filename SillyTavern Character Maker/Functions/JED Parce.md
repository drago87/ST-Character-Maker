/let JEDParce {: input=
	/let x {{var::input}}|
	/ife (timePeriod != '') {:
		/re-replace find="/--TimePeriod--/g" replace="{{getvar::timePeriod}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/ife (season != '') {:
		/re-replace find="/--Season--/g" replace="{{getvar::season}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/ife (worldDetails != '') {:
		/re-replace find="/--WorldDetails--/g" replace="{{getvar::worldDetails}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/re-replace find="/{{user}}\|--User--/g" replace="{\{user}}" {{var::x}}|
	/var x {{pipe}}|
	/ife (extraCharacters != '') {:
		/re-replace find="/--ExtraCharacters--/g" replace=", {{getvar::extraCharacters}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/ife (lore != '') {:
		/re-replace find="/--Lore--/g" replace="{{getvar::lore}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/ife (scenarioOverview != '') {:
		/re-replace find="/--ScenarioOverview--/g" replace="{{getvar::scenarioOverview}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/ife (characterOverview != '') {:
		/re-replace find="/--CharacterOverview--/g" replace="{{getvar::characterOverview}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/ife ((export == 'Yes') and (firstName != '')) {:
		/re-replace find="/{{getvar::firstName}}\|{{char}}\|--FirstName--/g" replace="{\{char}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/elseif (firstName != '') {:
		/re-replace find="/{{getvar::firstName}}\|{{char}}\|--FirstName--/g" replace="{{getvar::firstName}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/ife (lastName != '') {:
		/re-replace find="/--LastName--/g" replace="{{getvar::lastName}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/ife (nickName != '') {:
		/re-replace find="/--NickName--/g" replace="{{getvar::nickName}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/ife (parcedSpecies != '') {:
		/re-replace find="/--Species--/g" replace="{{getvar::parcedSpecies}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/ife (gender != '') {:
		/re-replace find="/--Gender--/g" replace="{{getvar::gender}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/ife (height != '') {:
		/re-replace find="/--Height--/g" replace="{{getvar::height}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/ife (age != '') {:
		/re-replace find="/--Age--/g" replace="{{getvar::age}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/ife (hair != '') {:
		/re-replace find="/--Hair--/g" replace="{{getvar::hair}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/ife (eyes != '') {:
		/re-replace find="/--Eyes--/g" replace="{{getvar::eyes}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/ife (body != '') {:
		/re-replace find="/--Body--/g" replace="{{getvar::body}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/ife (face != '') {:
		/re-replace find="/--Face--/g" replace="{{getvar::face}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/ife (features != '') {:
		/re-replace find="/--Features--/g" replace="{{getvar::features}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/ife (privates != '') {:
		/re-replace find="/--Privates--/g" replace="{{getvar::privates}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/ife (apperanceTraits != '') {:
		/re-replace find="/--ApperanceTraits--/g" replace="{{getvar::apperanceTraits}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/ife (outfitHead != '') {:
		/re-replace find="/--OutfitHead--/g" replace="{{getvar::outfitHead}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/ife (outfitAccessories != '') {:
		/re-replace find="/--OutfitAccessories--/g" replace="{{getvar::outfitAccessories}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/ife (outfitMakeup != '') {:
		/re-replace find="/--OutfitMakeup--/g" replace="{{getvar::outfitMakeup}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/ife (outfitNeck != '') {:
		/re-replace find="/--OutfitNeck--/g" replace="{{getvar::outfitNeck}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/ife (outfitTop != '') {:
		/re-replace find="/--OutfitTop--/g" replace="{{getvar::outfitTop}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/ife (outfitBottom != '') {:
		/re-replace find="/--OutfitBottom--/g" replace="{{getvar::outfitBottom}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/ife (outfitLegs != '') {:
		/re-replace find="/--OutfitLegs--/g" replace="{{getvar::outfitLegs}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/ife (outfitShoes != '') {:
		/re-replace find="/--OutfitShoes--/g" replace="{{getvar::outfitShoes}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/ife (outfitUnderwear != '') {:
		/re-replace find="/--OutfitUnderwear--/g" replace="{{getvar::outfitUnderwear}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/ife (appearanceQAList != '') {:
		/re-replace find="/--AppearanceQAList--/g" replace="{{getvar::appearanceQAList}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/ife (backstory != '') {:
		/re-replace find="/--Backstory--/g" replace="{{getvar::backstory}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/ife (residence != '') {:
		/re-replace find="/--Residence--/g" replace="{{getvar::residence}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/ife (connections != '') {:
		/re-replace find="/--Connections--/g" replace="{{getvar::connections}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/ife (secret != '') {:
		/re-replace find="/--Secret--/g" replace="{{getvar::secret}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/ife (itemList != '') {:
		/re-replace find="/--ItemList--/g" replace="{{getvar::itemList}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/ife (abilities != '') {:
		/re-replace find="/--Abilities--/g" replace="{{getvar::abilities}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/ife (archetype != '') {:
		/re-replace find="/--Archetype--/g" replace="{{getvar::archetype}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/ife (alignment != '') {:
		/re-replace find="/--Alignment--/g" replace="{{getvar::alignment}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/ife (personalityTags != '') {:
		/re-replace find="/--PersonalityTags--/g" replace="{{getvar::personalityTags}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/ife (cognitiveAbilities != '') {:
		/re-replace find="/--CognitiveAbilities--/g" replace="{{getvar::cognitiveAbilities}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/ife (socialSkills != '') {:
		/re-replace find="/--SocialSkills--/g" replace="{{getvar::socialSkills}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/ife (mainAspiration != '') {:
		/re-replace find="/--MainAspiration--/g" replace="{{getvar::mainAspiration}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/ife (uniqueTraits != '') {:
		/re-replace find="/--UniqueTraits--/g" replace="{{getvar::uniqueTraits}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/ife (personalityQA != '') {:
		/re-replace find="/--PersonalityQA--/g" replace="{{getvar::personalityQA}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/ife (behaviorNotes != '') {:
		/re-replace find="/--BehaviorNotes--/g" replace="{{getvar::behaviorNotes}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/ife (sexualOrientation != '') {:
		/re-replace find="/--SexualOrientation--/g" replace="{{getvar::sexualOrientation}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/ife (sexualRole != '') {:
		/re-replace find="/--SexualRole--/g" replace="{{getvar::sexualRole}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/ife (sexualityQA != '') {:
		/re-replace find="/--SexualityQA--/g" replace="{{getvar::sexualityQA}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/ife (sexualNotes != '') {:
		/re-replace find="/--SexualNotes--/g" replace="{{getvar::sexualNotes}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/ife (speachStyle != '') {:
		/re-replace find="/--SpeachStyle--/g" replace="{{getvar::speachStyle}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/ife (speachQuirks != '') {:
		/re-replace find="/--SpeachQuirks--/g" replace="{{getvar::speachQuirks}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/ife (speachTics != '') {:
		/re-replace find="/--SpeachTics--/g" replace="{{getvar::speachTics}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/ife (speachExamples != '') {:
		/re-replace find="/--SpeachExamples--/g" replace="{{getvar::speachExamples}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/ife (synonyms != '') {:
		/re-replace find="/--Synonyms--/g" replace="{{getvar::synonyms}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/ife (storyPlan != '') {:
		/re-replace find="/--StoryPlan--/g" replace="{{getvar::storyPlan}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/ife (previously != '') {:
		/re-replace find="/--Previously--/g" replace="{{getvar::previously}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/ife (notes != '') {:
		/re-replace find="/--Notes--/g" replace="{{getvar::notes}}" {{var::x}}|
		/var x {{pipe}}|
	:}|
	/return {{var::x}}|
:}||