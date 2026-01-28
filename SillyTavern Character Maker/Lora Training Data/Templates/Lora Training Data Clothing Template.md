```json
{
	"schema_type": "clothing",

	"placeholder_conventions": {
		"purpose": "Provide consistent references for clothing items without hardcoding names.",
		"allowed_placeholders": [
			"[CLOTHING_ITEM]",
			"[OUTFIT]",
			"[CHARACTER]"
		],
		"usage_guidelines": {
			"general_rule": "Use placeholders once early in the description to establish identity, then use descriptive references naturally.",
			"example_contexts": "Can be used when describing what a character is wearing or when assembling an outfit."
		}
	},

	"instruction": "Provide clothing metadata with full schema.",
	"input": "What is [CLOTHING_ITEM]?",
	"output": {
		"id": "<clothing_id>",
		"name": "<clothing_name>",
		"category": "head|neck|one_piece|two_piece_top|two_piece_bottom|legwear|socks|shoes|underwear_top|underwear_bottom",
		"short_description": "<describe_shortly_what_the_clothing_item_looks_like>",
		"indepth_description": "<describe_indepth_what_the_clothing_item_looks_like>",
		"usage_context": "<why_and_where_it_is_used>",
		"how_to_wear": "<how_it_is_put_on_or_adjusted>",
		"materials": "<common_materials>",
		"outfit_associations": [
			"<outfit_or_garment_it_is_commonly_part_of_or_used_with>"
		],
		"notes": "<optional_notes_or_variants>"
	}
}
```