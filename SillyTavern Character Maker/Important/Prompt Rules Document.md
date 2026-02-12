Agreed on prompt template with explanations inside ()

```
Base Context (This line will be exchanged for the base context or removed if not needed)
ExtraInput (This line will be exchanged for extra inputs one per line or removed if not needed)

Type Context (Add this line if the LLM is going to generate something that is about characterArchetype. This line will be exchanged for infomration about the characterArchetype or removed if information is needed)

### **EXAMPLES (for your reference—do not include in the answer):**

#### **Example:**  
An example

#### **Example:**  
Another example


## **TASK:**  
The task the LLM should perform
{{getvar::guide}}

## **INSTRUCTIONS:**  
A numberd list of instrucktions
{{getvar::logicBasedInstruction}}
```

ExtraInput
```
Here you put extra input that is needed for the LLM to have the knowlage it needs to generate the desired output
```

logicBasedInstruction
```
Here you put a continuation of the numberd list for things that only need extra instrucktions if something is true. Will be removed if not needed
```

Here is what will be inserted if Base Context is needed
```
### **CONTEXT (for your reference—do not include in the answer):**
- Name: {{getvar::firstName}} {{getvar::lastName}}
- Nationality: {{getvar::nationality}} (Will be removed if not generated)
- Ethnicity: {{getvar::ethnicity}} (Will be removed if not generated)
- Life Stage: {{getvar::lifeStage}}
- Age: {{getvar::parcedAge}}
- Gender: {{getvar::gender}}
- Species: {{getvar::parsedSpecies}}
```

Type Context will change based on characterArchetype but will look something like this
```
### **Beastkin**
Beastkin are primarily human characters who display distinct animal traits—such as ears, tails, claws, fangs, or unusual markings.  
They maintain a fully human body shape, face, and posture, but their hybrid nature is revealed through inherited or altered features from a non-human species.

These traits are often the result of magical fusion, ancestry, mutation, or other supernatural origins that blend human and animal characteristics.

#### **Examples might include:**
- A boy with wolf ears and a bushy tail.
- A girl with tiger stripes, feline eyes, and retractable claws.
- A human with bat-like wings and sharp fangs.
```

ExtraInput can look like this
```
- Face: {{getvar::face}}
- Eyes: {{getvar::eyes}}
etc..
```

---

Here is a example on how the Prompt for the generation of the body could look

```
Base Context
ExtraInput
 
Type Context

### **EXAMPLES (for your reference—do not include in the answer):**
#### **Example (Human – Young Adult):**
Slender frame with a lightly toned build, balanced posture, and subtle muscle definition from regular activity.

#### **Example (Beastkin – Rabbit Girl):**
Light and athletic body with long legs and digitigrade feet. Movement is quick and agile, with a center of balance shifted slightly due to her tail.

#### **Example (Anthropomorphic – Feline Male):**
Lean and flexible frame with padded paws, fur-covered limbs, and a low, crouched stance suited for bursts of speed.

#### **Example (Tauric – Centaur):**
Humanoid upper torso blending into a powerful equine body below, built for endurance and speed. The four-legged base gives her a stable and grounded posture.

#### **Example (Animalistic – Dragon):**
Thick, scaled body with a grounded gait, strong limbs, and a naturally aggressive forward-leaning stance.

## **TASK:**
Describe {{getvar::firstName}}’s body based on their species, age, gender, and previously generated features.
{{getvar::guide}}

## **INSTRUCTIONS:**
1. Refer to Features: for tail placement, wing presence, limb types, or body texture.
2. Focus on overall **shape**, **proportions**, **locomotion style**, and **species-based structure** (e.g., upright vs. quadrupedal).
3. Do **not** describe breasts, genitals, or explicit anatomy — this section is neutral and anatomical.
4. Reference posture, fur coverage, scale patterns, or movement as it relates to their form.
5. Limit output to **1–2 clean, descriptive sentences**.
6. Avoid describing clothing, personality, or behavior.
```

ExtraInput
```
- Features: {{getvar::appearanceFeatures}}
```

---

Here is some extra information.

The goal of the Prompts is to generate something that will be inserted into a character sheet and later a LLM will use that character sheet to roleplay as the Character
So it is important that the prompt is easy for the LLM to understand what to generate and for the Instructions to make it generate information for the character sheet (In a way that is primarily clear for the LLM and its a bonus if it's easy for a human to read)

Here is some more information about parsedAge
If the the character is human or the characters actual age and mental age is the same age will look like this
- Age: x years-old
else it will look like this
- Age: x years-old — roughly y years-old in human years.
Where x and y is a number.

Here is some more information about parsedSpecies
If the character is a Human Species will look like this
- Species: Human

But if the character is a Anthropomorphic Dragon it will look like this
- Species: Anthropomorphic Dragon

For a Beastkin Cat
- Species: Beastkin Cat

