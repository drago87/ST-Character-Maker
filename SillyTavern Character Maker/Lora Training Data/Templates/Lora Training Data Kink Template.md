```json
{
	"instruction": "Provide kink metadata with full schema.",
	"input": "What is <kink_name>?",
	"output": {
		"id": "<kink_id>",
		"name": "<kink_name>",
		"synonyms": ["<synonyms>"],
		"category": ["Kink", "<category_from_list>"],
		"description": "<describe_what_the_kink_is>",
		"roles": {
			"giver": {
				"id": "kinkname_giver_role",(Always keep "_giver_role". Remove this parantese)
				"label": "Giver",
				"definition": "<enjoys_doing_or_applying>",
				"notes": "<optional_notes_or_context>
			},
			"receiver": {
				"id": "kinkname_reciver_role",(Always keep "_reciver_role". Remove this parantese)
				"label": "Receiver",
				"definition": "<enjoys_receiving_or_experiencing>",
				"notes": "<optional_notes_or_context>
			}
		},
		"consent_and_safety": {
			"explicit_consent_required": true|false,
			"negotiation_recommended": true|false,
			"risk_level": "<low | moderate | high>",
			"notes": "<optional_safety_context>"
		},
		"notes": "<optional_notes_or_context>"
		
	}
}

```