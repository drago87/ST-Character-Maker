## **TASK:**
Based on the character sheet below, generate a **display Name** and a **Tagline** for the character. These will be shown publicly in searchable character lists or summaries.

## **CHARACTER SHEET:**
```
{{getvar::taglineSheet}}
```

## **OUTPUT FORMAT:**
```
Name:

Tagline:
```

## **INSTRUCTIONS:**
1. **Name:** Create a short, catchy display name (e.g., "{{getvar::firstName}} the Lost Princess" or "Curious Stablehand {{getvar::firstName}}").
   - May use a nickname or role descriptor.
   - Must be 3–6 words long.
   - Must include {{getvar::firstName}} in some form (e.g., "Shy {{getvar::firstName}}", "{{getvar::firstName}} the Caretaker").
   - Capitalize all main words.

2. **Tagline:** Write a short sentence (max 25 words) describing the vibe or premise of the character.
   - Loosely explain the character’s situation, tone, or the scenario.
   - May reference species traits, the character’s vibe, the world context, or a hint at the story hook.
   - Do not use quotation marks, markdown, or bold text.

3. Output format must be **exactly** as shown below:
```
Name: [Your generated name]

Tagline: [Your generated tagline]
```

4. Do **not** copy full sentences from the scenario or backstory — reinterpret tone and key concepts into a fresh summary.
5. Do **not** add commentary, headers, or markdown formatting.
{{getvar::guidance}}