```json
{
	"instruction": "Provide item metadata with full schema.",
	"input": "What is <item_name>?",
	"output": {
		"id": "<item_id>",
		"name": "<item_name>",
		"synonyms": ["<synonyms>"],
		"category": ["<category_from_list>"],
		"type": "<type_of_item_or_subcategory>",
		"short_description": "<describe_shortly_what_the_item_looks_like>",
	"indepth_description": "<describe_indepth_what_the_item_looks_like>",
		"intended_use": "<why_and_where_it_is_used>",
		"operation": "<how_to_use_or_apply_item>",
		"materials": "<common_materials>",
		"safety_notes": "<safety_or_warnings>",
		"variants": [
			{
				"name": "<optional_variants_or_sizes>",
				...,
				"notes": "<optional_additional_notes>"
			}
		],
		"metadata": {
			"size": "<size_information>",
			"weight": "<weight_information>",
			"color_options": ["<available_colors>"],
			"compatibility": ["<compatibility_notes_or_restrictions>"]
		},
		"notes": "<optional_additional_notes>"
	}
}
```