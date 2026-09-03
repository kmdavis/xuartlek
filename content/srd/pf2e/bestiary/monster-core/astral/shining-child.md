---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Shining Child"
tags:
  - pf2e/creature/level/12
  - pf2e/creature/trait/astral
  - pf2e/creature/trait/medium
statblock: inline
name: "Shining Child"
level: 12
source: "Monster Core"
aon_id: "creature-3190"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3190"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Shining Child"
level: "Creature 12"
size: "Medium"
trait_01: "Astral"
modifier: 23
perception:
  - name: "Perception"
    desc: "Perception +23; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Aklo|Aklo]]; telepathy 120 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/arcana|Arcana]] +18, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +23, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +21, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +21, [[srd/pf2e/compendium/rules-elements/skills/occultism|Occultism]] +18"
abilityMods: [2, 5, 6, 2, 5, 7]
abilities_top:
  - name: "Radiance Dependence"
    desc: "The shining child is [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] while in areas of darkness."
ac: 33
armorclass:
  - name: "AC"
    desc: "33; __Fort__: +22; __Ref__: +19; __Will__: +19"
hp: 215
health:
  - name: "HP"
    desc: "215; __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Blinded|blinded]], [[srd/pf2e/compendium/rules-elements/conditions#Dazzled|dazzled]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]]"
abilities_mid:
  - name: "Blinding Aura"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/arcane|arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/incapacitation|incapacitation]], [[srd/pf2e/compendium/rules-elements/traits/player-core/light|light]]) 60 feet. The shining child sheds bright light. Any creature that starts its turn in the aura must succeed at a DC 29 Fortitude save. If it fails, it is [[srd/pf2e/compendium/rules-elements/conditions#Blinded|blinded]] for 1 minute, and if it critically fails, it's permanently blinded. A creature that succeeds at its save is temporarily immune to this effect for 24 hours."
  - name: "Overwhelming Light"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/light|light]])"
  - name: "Trigger"
    desc: "The shining child enters an area of magical [[srd/pf2e/compendium/rules-elements/traits/player-core/darkness|darkness]] or begins its turn in an area of magical darkness"
  - name: "Effect"
    desc: "The shining child attempts to counteract the magical darkness (counteract rank 7, counteract modifier +23)."
speed: "30 feet, fly 50 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +25 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]]) __Damage__ 3d4+5 bludgeoning plus 4d6 fire and 2d4 persistent fire"
  - name: "Melee"
    desc: "⬻ fire ray +25 ([[srd/pf2e/compendium/rules-elements/traits/player-core/arcane|Arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], range 100 feet) __Damage__ 3d10+3 fire, plus 2d10 vitality damage if the target is [[srd/pf2e/compendium/rules-elements/traits/player-core/undead|undead]]"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 33 - __Cantrips (6th)__ [[srd/pf2e/compendium/spells/cantrips/light|Light]] - __2nd__ [[srd/pf2e/compendium/spells/rank-1/illusory-object|Illusory Object]] (at will) - __4th__ [[srd/pf2e/compendium/spells/rank-4/translocate|Translocate]] (at will) - __5th__ [[srd/pf2e/compendium/spells/rank-5/false-vision|False Vision]], [[srd/pf2e/compendium/spells/rank-4/mirage|Mirage]], [[srd/pf2e/compendium/spells/rank-4/translocate|Translocate]] - __6th__ [[srd/pf2e/compendium/spells/rank-2/dispel-magic|Dispel Magic]], [[srd/pf2e/compendium/spells/rank-6/vibrant-pattern|Vibrant Pattern]], [[srd/pf2e/compendium/spells/rank-6/wall-of-force|Wall of Force]] - __7th__ [[srd/pf2e/compendium/spells/rank-7/sunburst|Sunburst]] (x2) Ancient Guardians The practice of conjuring and binding shining children to serve as guardians of important locations was a popular one in Thassilon. Even today, thousands of years after this empire's fall, adventurers can still encounter shining children in ancient ruins, guarding treasures and forgotten lore from the distant past."
sourcebook: "_Monster Core_, page 308."
```

```encounter-table
name: Shining Child
creatures:
  - 1: Shining Child
```
