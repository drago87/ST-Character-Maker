```json
{
  "instruction": "Provide creature metadata with full schema.",
  "input": "Define the creature category '<creature_category_name>' with its major variants.",
  "output": {
    "id": "<creature_category_id>",
    "name": "<creature_category_name>",
    "category": ["Creature", "Fantasy", "<additional_tags>"],
    "description": "<high-level description of the creature category>",
    
    "common_traits": {
      "intelligence_level": "<animalistic / sapient / highly intelligent>",
      "social_structure": "<solitary / pack-based / hierarchical / variable>",
      "habitat": ["<common habitats>"],
      "diet": "<carnivore / herbivore / omnivore / magical>",
      "lifespan": "<typical lifespan or range>",
      "size_range": "<relative size compared to humans or other creatures>",
      "movement": "<primary locomotion methods>",
      "notes": "<general biological or behavioral notes>"
    },

    "variants": [
      {
        "id": "<variant_id>",
        "name": "<variant_display_name>",
        "type": "<variant_type_or_subspecies>",
        "description": "<what distinguishes this variant>",
        
        "physical_structure": {
          "body_plan": "<quadrupedal / bipedal / serpentine / hybrid>",
          "limbs": {
            "forelimbs": "<description>",
            "hind_limbs": "<description>",
            "wings": "<none / present / description>",
            "tail": "<description>"
          },
          "skin_covering": "<scales / fur / feathers / hide / other>",
          "head_features": ["<horns>", "<crest>", "<frills>", "<other>"],
          "notes": "<structural or anatomical notes>"
        },

        "anatomy_and_biology": {
          "respiration": "<lungs / gills / magical>",
          "reproduction": "<sexual / asexual / egg-laying / live birth>",
          "sexual_dimorphism": "<differences between sexes if applicable>",
          "genital_structure": "<generalized description or rule>",
          "waste_excretion": "<description if relevant>",
          "notes": "<important biological rules or exceptions>"
        },

        "abilities": {
          "natural_weapons": ["<claws>", "<teeth>", "<tail>", "<breath>"],
          "special_abilities": ["<magic>", "<elemental traits>", "<other>"],
          "mobility_capabilities": ["<flight>", "<burrowing>", "<swimming>"],
          "notes": "<limitations or special conditions>"
        },

        "behavior": {
          "temperament": "<docile / aggressive / territorial / curious>",
          "interaction_with_others": "<hostile / neutral / friendly / variable>",
          "communication": ["<vocalizations>", "<body language>", "<magic>"],
          "notes": "<behavioral quirks>"
        },

        "cultural_or_variant_notes": {
          "naming_conventions": "<how individuals are commonly named>",
          "subvariants": ["<elemental>", "<metallic>", "<regional>", "<other>"],
          "mythological_role": "<how this variant is perceived in lore>",
          "notes": "<optional lore or worldbuilding details>"
        }
      }
    ],

    "taxonomy_notes": "<how variants relate to each other>",
    "usage_notes": "<how this creature category should be interpreted by an LLM>",
    "notes": "<any additional clarifications>"
  }
}
```