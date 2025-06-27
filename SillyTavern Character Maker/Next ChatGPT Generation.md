Here is the prompt to establish who --User-- is
First the user can select the gender of --User--
Male, Female, Gender Neutral or Anything
This will be saved to the variable userGender

Then depending on what gender is chosen
userGender == Female
userSubjPronoun =  she
userObjPronoun =  her
userPossAdjPronoun =  her
userPossPronoun =  hers
userReflexivePronoun =  herself
variable = --User-- is a {{getvar::userGender}}

userGender == Male
userSubjPronoun =  he
userObjPronoun =  him
userPossAdjPronoun =  his
userPossPronoun =  his
userReflexivePronoun =  himself
variable = --User-- is a {{getvar::userGender}}

userGender == Gender Neutral
userSubjPronoun =  they
userObjPronoun =  them
userPossAdjPronoun =  their
userPossPronoun =  theirs
userReflexivePronoun =  themself
variable = --User-- is gender neutral and should be described using neutral language and tone, avoiding gendered assumptions.

userGender == Anything
userSubjPronoun =  they
userObjPronoun =  them
userPossAdjPronoun =  their
userPossPronoun =  theirs
userReflexivePronoun =  themself
variable = ?

Select a suitable variable name for 'variable' and give the 'userGender == Anything' variable some content instead of ?

Here is the variable names for the pronouns for firstName
subjPronoun
objPronoun
possAdjPronoun
possPronoun
reflexivePronoun

Update the following prompt to include 'variable' and pronouns for --User-- and firstName

```
Base Context
- World Tone: {{getvar::worldTone}}
- World Type: {{getvar::worldType}}
- World Details: {{getvar::worldDetails}}
--User-- is a Narrator (if user == No)

### **EXAMPLES (for your reference—do not include in the answer):**

#### **Example (Narrative Voice – Storyteller):**  
--User-- is an older woman narrating Mika’s story, offering both admiration and caution.

#### **Example (Close Relationship – Sibling):**  
--User-- is Tomas’s younger sister, familiar with his flaws and protective instincts.

#### **Example (Neutral Observer – Neighbor):**  
--User-- is neighbor who often watches Yuna from a distance, unsure how to feel about her presence.

#### **Example (Conflict-Based – Rival):**  
--User-- is Yuna’s childhood rival, always comparing their choices with poorly hidden envy.

#### **Example (New Connection – Stranger):**  
--User-- is a stranger who met Arlo today and is already fascinated by his unusual energy.

## **TASK:**  
Describe who `--User--` is in relation to {{getvar::firstName}}. This can be someone they know well, barely at all, or are just meeting — but it must make sense within the character's world and lifestyle.  
{{getvar::guidance}}

## **INSTRUCTIONS:**  
1. Choose a believable role for --User--: family, friend, rival, colleague, neighbor, narrator, or stranger.  
2. Establish their **emotional tone** toward {{getvar::firstName}} — are they affectionate, cautious, admiring, jealous, amused, etc.?  
3. Mention the **type of connection** (e.g., met at work, grew up together, never spoke until now).  
4. Limit to **1–2 clean, character-focused sentences**.  
5. Do not write a monologue or scene — just a short description of who --User-- is.
```