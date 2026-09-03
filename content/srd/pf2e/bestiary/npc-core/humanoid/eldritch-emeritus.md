---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Eldritch Emeritus"
tags:
  - pf2e/creature/level/17
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Eldritch Emeritus"
level: 17
source: "NPC Core"
aon_id: "creature-3596"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3596"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Eldritch Emeritus"
level: "Creature 17"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 32
perception:
  - name: "Perception"
    desc: "Perception +32"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Draconic|Draconic]]; up to 6 additional languages"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/lore|Academia Lore]] +30, [[srd/pf2e/compendium/rules-elements/skills/arcana|Arcana]] +36, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +30, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +33, [[srd/pf2e/compendium/rules-elements/skills/occultism|Occultism]] +33, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +33"
abilityMods: [4, 4, 4, 8, 1, -1]
abilities_top:
  - name: "Items"
    desc: "somewhat disheveled [[srd/pf2e/compendium/equipment/worn-items/accolade-robe-greater|_accolade robe_]], [[srd/pf2e/compendium/equipment/adventuring-gear/spellbook-blank|spellbook]], _+2 [[srd/pf2e/compendium/equipment/runes/striking-major|greater striking]] [[srd/pf2e/compendium/equipment/staves/staff-of-fire-major|major staff of fire]]_"
ac: 39
armorclass:
  - name: "AC"
    desc: "39; __Fort__: +27; __Ref__: +27; __Will__: +32"
hp: 290
health:
  - name: "HP"
    desc: "290; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/acid|acid]] 10, [[srd/pf2e/compendium/rules-elements/traits/player-core/cold|cold]] 10, [[srd/pf2e/compendium/rules-elements/traits/player-core/electricity|electricity]] 10, [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]] 10, [[srd/pf2e/compendium/rules-elements/traits/player-core/force|force]] 10, [[srd/pf2e/compendium/rules-elements/traits/player-core/sonic|sonic]] 10, [[srd/pf2e/compendium/rules-elements/traits/player-core/vitality|vitality]] 10, [[srd/pf2e/compendium/rules-elements/traits/player-core/void|void]] 10"
abilities_mid:
  - name: "Counterspell"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature casts a spell the eldritch emeritus has prepared."
  - name: "Effect"
    desc: "The emeritus expends a prepared spell to counter the triggering creature's casting of that same spell. The emeritus loses their spell slot as if they had cast the triggering spell. The emeritus then attempts to counteract the triggering spell."
  - name: "Third Contingent Sequencer"
    desc: "⬲"
  - name: "Frequency"
    desc: "once per day"
  - name: "Trigger"
    desc: "A creature attacks or uses a spell or ability that would affect the eldritch emeritus"
  - name: "Effect"
    desc: "A masterpiece of complex spellwork instantly takes shape, casting [[srd/pf2e/compendium/spells/rank-4/fire-shield|_fire shield_]], [[srd/pf2e/compendium/spells/rank-6/mislead|_mislead_]], and [[srd/pf2e/compendium/spells/rank-4/mountain-resilience|_mountain resilience_]] on the eldritch emeritus, each as an 8th-rank arcane spell."
speed: "25 feet, teleport 50 feet"
attacks:
  - name: "Melee"
    desc: "⬻ staff +31 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/two-hand|two-hand d8]]) __Damage__ 3d4+14 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +30 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+14 bludgeoning"
  - name: "Ranged"
    desc: "⬻ arcane beam +31 ([[srd/pf2e/compendium/rules-elements/traits/player-core/arcane|Arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|Fire]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]]) __Damage__ 6d6+10 fire"
abilities_bot:
  - name: "Didactic Arcanism"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/arcane|Arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]])"
  - name: "Requirement"
    desc: "The eldritch emeritus has seen a creature Cast a Spell of 7th rank or lower during the previous round, that spell takes between one and three actions to cast, and that spell is on the arcane spell list"
  - name: "Effect"
    desc: "The eldritch emeritus mastered that spell 30 years ago, and is happy to show how a real master does it. The emeritus Casts the same Spell but heightened to 8th rank. Didactic Arcanism uses the same number of actions as the original spell took to cast."
  - name: "Steady Spellcasting"
    desc: "If a reaction would [[srd/pf2e/books/player-core/chapter-8-playing-the-game/actions#Disrupting Actions|disrupt]] the eldritch emeritus's spellcasting action, the eldritch emeritus attempts a DC 15 flat check. On a success, the action isn't disrupted."
spellcasting:
  - name: "Arcane Prepared Spells"
    desc: "DC 38, attack +30 - __Cantrips (9th)__ [[srd/pf2e/compendium/spells/cantrips/detect-magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/light|Light]], [[srd/pf2e/compendium/spells/cantrips/prestidigitation|Prestidigitation]], [[srd/pf2e/compendium/spells/cantrips/sigil|Sigil]], [[srd/pf2e/compendium/spells/cantrips/telekinetic-hand|Telekinetic Hand]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/fleet-step|Fleet Step]] (x2), [[srd/pf2e/compendium/spells/rank-1/sure-strike|Sure Strike]] - __2nd__ [[srd/pf2e/compendium/spells/rank-2/gecko-grip|Gecko Grip]], [[srd/pf2e/compendium/spells/rank-2/translate|Translate]], [[srd/pf2e/compendium/spells/rank-2/water-walk|Water Walk]] - __3rd__ [[srd/pf2e/compendium/spells/rank-3/earthbind|Earthbind]], [[srd/pf2e/compendium/spells/rank-3/haste|Haste]], [[srd/pf2e/compendium/spells/rank-3/locate|Locate]] - __4th__ [[srd/pf2e/compendium/spells/rank-4/creation|Creation]], [[srd/pf2e/compendium/spells/rank-2/dispel-magic|Dispel Magic]], [[srd/pf2e/compendium/spells/rank-4/fly|Fly]] - __5th__ [[srd/pf2e/compendium/spells/rank-5/banishment|Banishment]], [[srd/pf2e/compendium/spells/rank-5/howling-blizzard|Howling Blizzard]], [[srd/pf2e/compendium/spells/rank-5/slither|Slither]] - __6th__ [[srd/pf2e/compendium/spells/rank-6/disintegrate|Disintegrate]], [[srd/pf2e/compendium/spells/rank-6/teleport|Teleport]], [[srd/pf2e/compendium/spells/rank-6/wall-of-force|Wall of Force]] - __7th__ [[srd/pf2e/compendium/spells/rank-6/chain-lightning|Chain Lightning]] (×2), [[srd/pf2e/compendium/spells/rank-7/project-image|Project Image]] - __8th__ [[srd/pf2e/compendium/spells/rank-8/earthquake|Earthquake]], [[srd/pf2e/compendium/spells/rank-8/quandary|Quandary]] (×2) - __9th__ [[srd/pf2e/compendium/spells/rank-9/detonate-magic|Detonate Magic]], [[srd/pf2e/compendium/spells/rank-9/falling-stars|Falling Stars]] - __Constant (9th)__ [[srd/pf2e/compendium/spells/rank-7/energy-aegis|Energy Aegis]]"
sourcebook: "_NPC Core_, page 143."
```

```encounter-table
name: Eldritch Emeritus
creatures:
  - 1: Eldritch Emeritus
```
