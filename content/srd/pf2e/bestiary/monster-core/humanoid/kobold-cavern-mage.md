---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Kobold Cavern Mage"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/kobold
  - pf2e/creature/trait/small
statblock: inline
name: "Kobold Cavern Mage"
level: 2
source: "Monster Core"
aon_id: "creature-3074"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3074"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Kobold Cavern Mage"
level: "Creature 2"
size: "Small"
trait_01: "Humanoid"
trait_02: "Kobold"
modifier: 5
perception:
  - name: "Perception"
    desc: "Perception +5; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Fey|Fey]], [[srd/pf2e/compendium/rules-elements/languages#Petran|Petran]], [[srd/pf2e/compendium/rules-elements/languages#Sakvroth|Sakvroth]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +6, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +8, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +8, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +8, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +5, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +6"
abilityMods: [2, 2, -1, 0, 1, 4]
abilities_top:
  - name: "Items"
    desc: "light hammer"
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +5; __Ref__: +6; __Will__: +7"
hp: 20
health:
  - name: "HP"
    desc: "20"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ light hammer +6 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]]) __Damage__ 1d6+2 bludgeoning"
  - name: "Melee"
    desc: "⬻ claw +6 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]]) __Damage__ 1d6+2 slashing"
  - name: "Ranged"
    desc: "⬻ light hammer +6 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 20 feet]]) __Damage__ 1d6+2 bludgeoning"
abilities_bot:
  - name: "Inspiring Display"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/linguistic|Linguistic]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]])"
  - name: "Requirements"
    desc: "The cavern mage's previous action was to Cast a Spell"
  - name: "Effect"
    desc: "The cavern mage uses their magical display to inspire another kobold within 30 feet. That kobold gains 4 temporary Hit Points that last until the start of the cavern mage's next turn."
  - name: "Scamper"
    desc: "⬻"
  - name: "Requirements"
    desc: "The cavern mage is adjacent to at least one enemy"
  - name: "Effect"
    desc: "The cavern mage Strides up to their Speed plus 5 feet and gains a +2 circumstance bonus to AC against reactions triggered by this movement. They must end this movement in a space that's not adjacent to any enemy."
spellcasting:
  - name: "Primal Spontaneous Spells"
    desc: "DC 18 - __Cantrips (1st)__ [[srd/pf2e/compendium/spells/cantrips/caustic-blast|Caustic Blast]], [[srd/pf2e/compendium/spells/cantrips/detect-magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/figment|Figment]], [[srd/pf2e/compendium/spells/cantrips/know-the-way|Know the Way]], [[srd/pf2e/compendium/spells/cantrips/tangle-vine|Tangle Vine]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/fleet-step|Fleet Step]], [[srd/pf2e/compendium/spells/rank-1/heal|Heal]], [[srd/pf2e/compendium/spells/rank-1/pummeling-rubble|Pummeling Rubble]], [[srd/pf2e/compendium/spells/rank-1/runic-weapon|Runic Weapon]] (4 slots)"
sourcebook: "_Monster Core_, page 211."
```

```encounter-table
name: Kobold Cavern Mage
creatures:
  - 1: Kobold Cavern Mage
```
