# Input Contract

Collect or infer:

- `content_source`: PDF path, doc text, notes, transcript, or raw content
- `slide_limit`: target count for main slides
- `language_mode`: `Thai`, `English`, `Thai-first with English business terms`, or `Match source`
- `audience`: judges, executives, clients, internal team
- `strictness`: `close`, `balanced`, `allow synthesis`
- `detail_density`: `low`, `medium`, `high`, `adaptive`
- `shell_mode`: default `fixed`
- `theme`: optional; use when the user explicitly wants a color or visual theme for the deck
- `style_base`: optional; use only if the user explicitly wants to anchor to a specific reference deck or style family
- `section_spine_mode`: optional; default `case-competition-default`

Defaults:

- `strictness = close`
- `detail_density = adaptive`
- `shell_mode = fixed`
- `language_mode = Match source`
- `section_spine_mode = case-competition-default`

Interpretation rules:

- `strictness` controls how freely you rewrite the story from the source.
- `detail_density` controls how dense the body should feel, not the shell.
- `shell_mode = fixed` means headline/detail line/bottom flow must stay in one family across the deck.
- `theme` should guide body color mood and surface treatment, but must not break shell consistency or role-based color logic.
- in this skill, the default bottom flow family is a slim footer with a thin top rule, centered section labels, one short active marker above the current section, and a far-right brand mark.
- `section_spine_mode = case-competition-default` means the deck should first be mapped into the default narrative section order before slide-level planning begins.
