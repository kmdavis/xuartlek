---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Zebub"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/devil
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/small
statblock: inline
name: "Zebub"
level: 3
source: "Monster Core 2"
aon_id: "creature-4325"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4325"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Zebub"
level: "Creature 3"
size: "Small"
trait_01: "Devil"
trait_02: "Fiend"
trait_03: "Unholy"
modifier: 12
perception:
  - name: "Perception"
    desc: "Perception +12; greater darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/languages#Empyrean|Empyrean]]; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +10, [[srd/pf2e/compendium/rules-elements/skills/arcana|Arcana]] +7, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +8, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +9, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +10"
abilityMods: [1, 4, 1, 0, 3, 1]
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +8; __Ref__: +10; __Will__: +8 +1 status to all saves vs. magic"
hp: 45
health:
  - name: "HP"
    desc: "45; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]]; __Resistances__ physical 5 (except [[srd/pf2e/compendium/equipment/materials/silver-object-high-grade|silver]]), [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]] 5­­; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/holy|holy]] 5"
speed: "15 feet, fly 50 feet"
attacks:
  - name: "Melee"
    desc: "⬻ mandibles +12 ([[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|unholy]]) __Damage__ 1d10+5 piercing plus Cocytan filth"
abilities_bot:
  - name: "Cocytan Filth"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/disease|Disease]], [[srd/pf2e/compendium/rules-elements/traits/gm-core/virulent|virulent]])"
  - name: "Saving Throw"
    desc: "DC 18 Fortitude"
  - name: "Onset"
    desc: "1d4 days"
  - name: "Stage 1"
    desc: "[[srd/pf2e/compendium/rules-elements/conditions#Enfeebled|enfeebled]] 1 (1 day)"
  - name: "Stage 2"
    desc: "enfeebled 2 (1 day)"
  - name: "Stage 3"
    desc: "enfeebled 3 (1 day)"
  - name: "Diabolic Eye"
    desc: "⬽ ([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]]) The zebub records everything they see, and though they don't remember all observations, they can pass them along to another creature. The zebub replays 10 minutes of witnessed events to a touched willing creature, which receives the memories in a flash of information. By remaining in contact, the zebub can spend additional 3-action activities to replay more information. After relaying their visions to another, the zebub can't ever recall those events again."
  - name: "Sneak Attack"
    desc: "The zebub's Strikes deal an additional 1d6 precision damage to [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] creatures."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 17 - __Cantrips (2nd)__ [[srd/pf2e/compendium/spells/cantrips/message|Message]] - __2nd__ [[srd/pf2e/compendium/spells/rank-2/invisibility|Invisibility]] (at will; self only), [[srd/pf2e/compendium/spells/rank-1/summon-animal|Summon Animal]] (swarm creatures only) - __4th__ [[srd/pf2e/compendium/spells/rank-4/translocate|Translocate]] (at will) - __5th__ [[srd/pf2e/compendium/spells/rank-4/translocate|Translocate]]"
  - name: "Rituals"
    desc: "DC 17 - __1st__ [[srd/pf2e/compendium/spells/rituals/diabolic-pact|Diabolic Pact]]"
sourcebook: "_Monster Core 2_, page 98."
```

```encounter-table
name: Zebub
creatures:
  - 1: Zebub
```
