```json
{
	"schema_type": "archetype",

	"instruction": "Provide a clear definition and metadata for the requested archetype.",
	"input": "What is a '<archetype_name>' character?",

	"placeholder_conventions": {
		"purpose": "Provide consistent grounding for archetype definitions without hardcoding names.",
		"allowed_placeholders": ["<archetype_name>", "<Example>", "<Synonym>"],
		"usage_guidelines": "Use placeholders early in examples, then natural language afterwards."
	},

	"output": {
		"archetype": "<archetype_name>",
		"definition": "<Concise and precise description of the archetype highlighting morphology, behavior, and cognitive traits>",

		"traits": {
			"morphology": "<Physical structure, proportions, and distinguishing features>",
			"behavioral_profile": "<Typical behavior patterns, movement, and interaction style>",
			"communication": "<Typical communication style, speech, or non-verbal signaling>",
			"cognitive_level": "<Level of intelligence or reasoning ability relative to humans or a spectrum of levels>",
			"notes": "<Optional additional info on variations or edge cases>"
		},

		"categories": ["<Category1>", "<Category2>"] ,
		"associated_schemas": ["anatomy_sizes", "clothing_categories", "actions"],
		"variations": [
			{
				"name": "<Variant Name>",
				"notes": "<How this variant differs from the base archetype>"
			}
		],

		"examples": [
			"<Example 1>",
			"<Example 2>",
			"<Example 3>"
		],

		"synonyms": [
			"<Synonym 1>",
			"<Synonym 2>"
		],

		"not_includes": [
			"<What this archetype explicitly excludes>"
		],

		"notes": "<Optional clarifications, edge cases, or common misconceptions>"
	}
}
```