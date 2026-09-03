---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Carbuncle"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/tiny
statblock: inline
name: "Carbuncle"
level: 1
source: "Monster Core 2"
aon_id: "creature-4292"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4292"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Carbuncle"
level: "Creature 1"
size: "Tiny"
trait_01: "Beast"
trait_02: "Rare"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7; darkvision, treasure sense (imprecise) 500 feet"
languages: "carbuncle empathy 30 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +3, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +6"
abilityMods: [-3, 0, 3, -2, 3, 0]
abilities_top:
  - name: "Carbuncle Empathy"
    desc: "The carbuncle can telepathically send mild feelings and sensations to nearby creatures. It can't use this ability to communicate in language or hinder a target, but it might convey a feeling of dread or the scent of food cooking nearby."
  - name: "Treasure Sense"
    desc: "The carbuncle can sense the presence and location of any object or grouping of objects worth at least 50 gp in total within 500 feet of it. The carbuncle's sense only functions if the treasure is within in a container or physically obscured, such as when buried underground. Objects worn on a person or left out in open air don't trigger the carbuncle's sense."
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +8; __Ref__: +3; __Will__: +6"
hp: 20
health:
  - name: "HP"
    desc: "20"
abilities_mid:
  - name: "Easy to Influence"
    desc: "Any mental spell can affect a carbuncle, regardless of creature type limitations. Against a [[srd/pf2e/compendium/spells/rank-4/suggestion|_suggestion_]] spell, a carbuncle always gets an outcome one degree of success worse than it rolled on its saving throw."
  - name: "Fatal Faker"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/arcane|arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/teleportation|teleportation]])"
  - name: "Trigger"
    desc: "The carbuncle takes damage"
  - name: "Effect"
    desc: "The carbuncle feigns death by teleporting away and leaving a replica of its corpse behind, creating a colorful flash of light and a croaking sound. The real carbuncle transports to a clear space within 30 feet that it can see and leaves a hollow shell behind. The fake body appears solid until it is touched, at which point it crumbles to dust."
speed: "15 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +5 ([[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]]) __Damage__ 1d6 piercing"
abilities_bot:
  - name: "Specious Suggestion"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/incapacitation|incapacitation]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/subtle|subtle]])"
  - name: "Frequency"
    desc: "three times per day"
  - name: "Effect"
    desc: "The carbuncle concentrates on a creature it can see and tries to manipulate that creature, imploring them to perform harmless, pointless, and usually embarrassing actions. The target must attempt a DC 18 Will save. The target then becomes temporarily immune for 24 hours. This has the effects of [[srd/pf2e/compendium/spells/rank-4/suggestion|_suggestion_]] except that a critical success bolsters the target and grants them a +1 status bonus to Will saves for 1 hour, the duration on a failure is 1 round, and the duration on a critical failure is a 1 minute. The target can attempt a new save at the end of its turn each round to end the effect. Carbuncle Chatter “A lizard with an apple-sized gem sticking out of its forehead? Wishful thinking!” “Carbuncles are real! I almost caught one, but even though it could barely walk, its magic allowed it to escape my clutches.” “Their mind control powers could make them useful familiars, but if you ever catch one, it dies of fright.” “My advice is to stay away from these pests. They drink your hopes and aspirations through their horns, leaving you empty except for bad luck and bellyaches.” “Planning a carbuncle hunt? You’d better leave your self-respect at home and be ready to emerge with fewer friends than you had at the start!”"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 18 - __Cantrips (1st)__ [[srd/pf2e/compendium/spells/cantrips/daze|Daze]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/jump|Jump]] (at will) - __3rd__ [[srd/pf2e/compendium/spells/rank-3/levitate|Levitate]] (at will; self only)"
sourcebook: "_Monster Core 2_, page 68."
```

```encounter-table
name: Carbuncle
creatures:
  - 1: Carbuncle
```
