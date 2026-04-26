# Body Decision Schema

This contract captures the output of the stage that chooses the body construction.

It sits between:

- retrieval
- body blueprint

Do not skip this stage.

## Purpose

The `body decision` object records:

- which analysis proof mode was chosen when relevant
- whether the slide has terminal bridge role before recommendation
- which references were shortlisted
- which reference was chosen as primary
- whether a secondary reference is being borrowed
- which visual devices were selected
- which grammar selection was selected
- which layout variant inside that grammar was selected
- why those choices beat the nearby alternatives

## Required Fields

- `slide_number`
- `key_message`
- `content_classes`
- `decision_types`
- `data_shapes`
- `analysis_proof_mode`
- `analysis_terminal_role`
- `retrieved_reference_candidates`
- `retrieved_visual_device_candidates`
- `primary_reference`
- `secondary_references`
- `chosen_visual_devices`
- `grammar_selection`
- `why_chosen`
- `reject_reasons`

## Intent

This object should be strong enough that another reviewer can answer:

- Why was this body chosen?
- Why were the other nearby references not chosen?
- Is this choice actually supported by the training refs?

## Canonical JSON Schema

Use:

- [body-decision.schema.json](contracts/body-decision.schema.json)

Examples:

- [body-decision-examples.md](body-decision-examples.md)
