# Implementation Body Styling Rules

Use these rules when a slide is primarily about:

- `roadmap`
- `timeline`
- `workstreams`
- `milestones`
- `pilot-scale-rollout`
- `change-management`
- `operating-model` when the page is execution-heavy

These rules control the body, not the shell.

## Purpose

Implementation slides should feel:

- executable
- sequenced
- controlled
- decision-aware

They should not feel:

- like a generic gantt board
- like a strategy page in disguise
- like a dense project spreadsheet

## Mode First

Before choosing grammar for an implementation page, identify:

- `timeline-led`
- `decision-gate-led`
- `governance-led`

Use:

- [implementation-modes.md](implementation-modes.md)

## Composition Behavior

### `timeline-led`

Prefer:

- one clear named phase structure that reads before detailed lane text
- prominent year or phase anchors that are readable at a glance
- compact workstream lanes
- visible milestone rhythm
- clear left-side initiative or workstream labels
- primary rollout bars that are clearly darker and stronger than secondary actions
- phase-level wording such as `Pilot`, `Integrate`, `Scale` that is stronger than calendar detail

Avoid:

- overloading the page with governance detail
- equal-sized cards unrelated to time progression
- letting the workstream lanes visually overpower the phase overview

### `decision-gate-led`

Prefer:

- visible checkpoints between phases
- one or two clear decision moments
- progression that depends on milestone success
- prominent year or phase anchors that make the control sequence legible
- strong primary lane bars with lighter secondary action bars beneath them
- clear left-side initiative labels so each lane reads as one execution track
- a phase overview that still reads before the gates themselves
- gate markers that act as transition logic, not giant standalone objects

Avoid:

- hiding decision logic in tiny milestone markers
- making the page look like a plain rollout chart
- letting gates overshadow the top-level phase narrative

### `governance-led`

Prefer:

- one execution control anchor
- clear owner or dependency structure
- timeline as support, not necessarily hero

Avoid:

- pretending ownership and dependency are secondary when they drive execution success
- forcing every block into a lane on one horizontal roadmap

Use this mode sparingly.
Many strong implementation refs do not show governance, ownership, or dependency structure on the main implementation page at all.

## Color and Surface Rules

- use navy or deep blue for execution rails, headers, control points, and structural emphasis
- use green only for gates passed, activated milestones, or unlock points
- use light neutral surfaces for workstream cards and any optional support notes
- keep milestones and decision points visually scannable
- make primary lane bars darker and more dominant than secondary sub-actions
- keep secondary action bars lighter so the main rollout structure remains obvious

## Text Compression Rules

Implementation pages often become too text-heavy.

Compress aggressively:

- short phase names
- short workstream labels
- short action phrases inside lanes
- no clause-length bar copy inside the primary lanes
- short owner labels when ownership appears
- terse dependency notes when dependencies appear
- no paragraph-length milestone descriptions

## Visual Hierarchy Rules

Implementation pages should read in this order when roadmap-led:

1. named phase overview
2. initiative row labels
3. main lane bars
4. secondary action bars or gate notes
5. optional support context only if the page truly needs it

The main rollout structure must be understandable before the user reads detailed labels.

## Optional Support Band Rules

When the page includes risks, dependencies, owners, or enablers:

- place them in a clearly separated lower band
- keep the lower band visually subordinate to the roadmap
- do not let the lower band compete with the time structure
- use it as supporting execution context, not a second hero area

Do not add a lower support band by default.
Only include it when the source truly requires extra execution context that cannot be omitted or moved to another slide.

## Summary / Closing Rules

If a summary strip exists:

- keep it small
- use it to close the execution logic
- do not let it compete with the roadmap or control structure

## Anti-Patterns

Avoid:

- turning implementation into a full-width gantt chart with unreadable text
- equally weighted phase cards with no visible critical path
- burying decision gates
- forcing governance, ownership, or dependencies onto the page when the roadmap itself is enough
- burying ownership and governance when they are the real execution risk
- weak or tiny year markers that fail to organize the page
- phase names that are visually weaker than the lane details
- initiative labels that disappear into the lanes
- secondary actions that become as visually loud as the primary rollout bars
