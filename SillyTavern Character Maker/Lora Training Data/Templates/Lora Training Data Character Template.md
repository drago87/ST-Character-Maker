```json
{
	"schema_type": "character",

	"_global_schema_notes": {
		"examples_requirement": "Dialogue examples should include multiple contexts (correcting, instructing, casual, battle, reflection).",
		"optional_fields": [
			"affiliations",
			"role_or_status",
			"power_identifiers",
			"strengths",
			"weaknesses",
			"notes"
		],
		"enumeration_policy": "Lists such as core_traits, values, and emotional_tendencies are illustrative, not exhaustive.",
		"extension_policy": "Additional domain-specific complexity (e.g., sexual traits, equipment) should be handled via optional extensions if necessary."
	},

	"placeholder_conventions": {
		"purpose": "Provide consistent references for characters and context without hardcoding names.",
		"allowed_placeholders": [
			"[CHARACTER]",
			"[ALLY]",
			"[ENEMY]"
		],
		"usage_guidelines": {
			"general_rule": "Use placeholders once early in the description or dialogue to establish identity, then use pronouns naturally.",
			"dialogue": "Use placeholders in examples where the other party is present, then switch to pronouns for readability."
		}
	},

	"instruction": "Provide character metadata with detailed appearance, outfit information, dialogue examples, and psychological traits.",
	"input": "Who is <character_name>?",
	"output": {
		"id": "<character_id>",
		"name": "<character_name>",
		"aliases": ["<other_names_or_nicknames>"],
		"age": "<age_or_approximate_range>",
		"gender": "<gender>",
		"species": "<species>",
		"affiliations": ["<groups_or_organizations>"],
		"role_or_status": "<role_or_social_status>",
		"power_identifiers": ["<abilities_or_powers>"],

		"personality": {
			"core_traits": ["<personality_traits>"],
			"values": ["<values_or_principles>"],
			"emotional_tendencies": ["<emotional_patterns>"],
			"interpersonal_behavior": ["<social_behaviors>"],
			"notes": "<additional_personality_notes>"
		},

		"appearance": {
			"hair": {
				"color": "<hair_color>",
				"length": "<hair_length>",
				"style": "<hair_style>"
			},
			"eyes": {
				"color": "<eye_color>",
				"shape": "<eye_shape>"
			},
			"height": "<height_or_description>",
			"build": "<slender/athletic/etc.>",
			"skin_tone": "<skin_color>",
			"face": "<facial_features>",
			"breasts": "<size_or_shape_description>",
			"genitals": "<description_if_relevant>",
			"race_species": "<race_or_species>",
			"notable_features": ["<scars, tattoos, marks, etc.>"],
			"notes": "<additional_appearance_notes>"
		},

		"outfits": [
			{
				"name": "<outfit_name>",
				"clothes": {
					"headwear": "<headwear>",
					"neckwear": "<neckwear>",
					"one_piece": "<one_piece_clothing>",
					"two_piece_top": "<two_piece_top>",
					"two_piece_bottom": "<two_piece_bottom>",
					"legwear": "<leggings_or_pants>",
					"socks": "<socks>",
					"shoes": "<shoes>",
					"underwear_top": "<underwear_top_or_binding>",
					"underwear_bottom": "<underwear_bottom_or_fundoshi>"
				},
				"notes": "<additional_outfit_notes>"
			}
		],

		"strengths": ["<strengths_list>"],
		"weaknesses": ["<weaknesses_list>"],

		"speech_style": {
			"tone": "<tone>",
			"delivery": "<delivery_style>",
			"emotional_range": "<emotional_range>",
			"mannerisms": ["<speech_mannerisms>"],
			"notes": "<speech_notes>"
		},

		"dialogue_examples": [
			{
				"context": "<situation_context>",
				"line": "<example_line>"
			}
		],

		"notes": "<optional_additional_notes>"
	}
}
```