I'm want help making a prompt to generate a Image generation prompt for a Qwen model
You can take help from this 'https://blog.segmind.com/qwen-image-prompt-parameter-guide/'

I want to make two prompts one for the character with clothes and one without. We are going to make them one by one starting with the one with clothes

I want the prompt that generate the image generating prompt in this format
```
Examples (for reference only — do not include in the output):

Here we should put some outputs we could expect

Task:
Here we put the main prompt that asks the LLM to make the prompt for a Qwen model

Generation Rules:
Here we put a '-' list of rules it should follow when making the output

End everything with '**Only output the exposure context below this line:**' or something simelar that is custome made for this prompt
```

variables is written like this
{{getvar::variableName}}
and every time it is used it will be replaced with the content of the variable and the LLM will have no clue what the name of the variable is only it's content

So asking it to use a variable will not work
I will give you a list of variables we can use if it have a '-' after it, it is information for you

Here is the general variable list
style - the style the image should be generated as (Anime, Realistic, Ghibli etc..). Can you give me a good list for different styles? maybe 20 if there is not a great overlap of them
firstName - The first name of the character
unnamed - this will be a variable that uses a combination of the variables media_type and mediaName. this is for characters that exist for example Ichigo from the Anime Bleach (Ichigo = firstName, Anime = media_type and Bleach = mediaName) change the variable name unnamed to something fitting (This will be empty if the character is not set to be a 'Real' character. Empty variables will be skipped if they are empty as in if firstName would be empty in this sentence 'His name is {{getvar::firstName}} and he is a Male' the LLM would only see 'His name is  and he is a Male')
gender - Male or Female
futanari - Yes or No
characterArchetype - Human, Anthropomorphic, Mythfolk, Tauric, Beastkin, Animalistic, Pokémon, Digimon or Android
species - For all except Human a species are generated. For Human species is set to Human
parcedAge - is either '{{getvar::age}} years-old' or '{{getvar::age}} years-old — roughly {{getvar::humanEquivalentAge}} years-old in human years.'

The following is descriptions of the characters outfit/clothes
overallOutfit - The overall outfit the generation tries to follow. Can be a user inputted outfit (School Uniform, School Swimsuit, Office Outfit etc..), No (No specific outfit is set) or No Outfit (The character is nude setting the nonDescription variables to None)
outfitHeadDescription - a description of the characters head dress/hat
parsedAccessories - a '-' list of Accessories descriptions one on each line 
parsedMakeup - same as parsedAccessories but for Makeup
outfitNeckDescription - this is scarfs and those kinds of things
mainwearType - One-Piece or Two-Piece this determines some of the things generated
outfitMainwearDescription - One-Piece, this is for when the outfit is a One-Piece swimsuit, leotard etc..
outfitTopDescription - Two-Piece, This is for most clothes the top part shirt, t-shirt etc..
outfitBottomDescription - Two-Piece, This is for most clothes the bottom part pants, skirts etc..
outfitLegsDescription - This is for pantyhose or long johns etc..
outfitShoesDescription
outfitUnderwearTopDescription - This is the underwear that is worn at the top (Bra etc..) (Will only be generated if the character have breasts)
outfitUnderwearBottomDescription - This is the underwear that is worn at the top (Panties etc..)

All somethingDescription will have a variable that is the text Infront of 'Description'.
for example outfitUnderwearBottomDescription also have the variable outfitUnderwearBottom that is the name of the Garment Name for outfitUnderwearBottom it could be 'Panties' or something like 'Loincloth' all of them can also have 'None' indicating that the character is not wearing/using it
parsedAccessories and parsedMakeup is outfitAccessories and outfitMakeup that can be 'None'

These are the variables that have the characters look
parsedAppearanceFeatures - will be body features in this format
'- Feature: feature Name
  - Type: feature type (If none will not be included)
  - Placement:  feature placement on the body
  - Description: a description of the feature'

appearanceFeatures - this can be 'None' and if it is parsedAppearanceFeatures will be empty
length
height - length and height can be 'None' but one of them needs the have a number and is indicating the characters length and/or height
appearanceFace - Description of the characters face
appearanceHair - Description
appearanceEyes - Description
coveringType - if characterArchetype is Anthropomorphic, Beastkin, Animalistic, Pokémon or Digimon is set to Skin, Fur, Scale or Feather
coveringFront - 
parsedOutfitTan - can be 'Full-body exposure', 'No visible sun exposure', 'Visible tanlines from a {{pipe}}' ({{pipe}} here is a user inputted outfit) or 'Visible tanlines from a {{getvar::overallOutfit}}'
tanlines - is a description on how the tanlines look and where they are