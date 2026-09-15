---
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
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3596"
socialImage: og-image.png
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
    desc: "+32"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Draconic|Draconic]]; up to 6 additional languages"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Lore|Academia Lore]] +30, [[srd/pf2e/compendium/rules-elements/skills/Arcana|Arcana]] +36, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +30, [[srd/pf2e/compendium/rules-elements/skills/Nature|Nature]] +33, [[srd/pf2e/compendium/rules-elements/skills/Occultism|Occultism]] +33, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +33"
abilityMods: [4, 4, 4, 8, 1, -1]
abilities_top:
  - name: "Items"
    desc: "somewhat disheveled [[srd/pf2e/compendium/equipment/worn-items/Accolade Robe|_accolade robe_]], [[srd/pf2e/compendium/equipment/adventuring-gear/Spellbook (Blank)|spellbook]], _+2 [[srd/pf2e/compendium/equipment/runes/Striking|greater striking]] [[srd/pf2e/compendium/equipment/staves/Staff of Fire|major staff of fire]]_"
ac: 39
armorclass:
  - name: "AC"
    desc: "39; __Fort__: +27; __Ref__: +27; __Will__: +32"
hp: 290
health:
  - name: "HP"
    desc: "290; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Acid|acid]] 10, [[srd/pf2e/compendium/rules-elements/traits/player-core/Cold|cold]] 10, [[srd/pf2e/compendium/rules-elements/traits/player-core/Electricity|electricity]] 10, [[srd/pf2e/compendium/rules-elements/traits/player-core/Fire|fire]] 10, [[srd/pf2e/compendium/rules-elements/traits/player-core/Force|force]] 10, [[srd/pf2e/compendium/rules-elements/traits/player-core/Sonic|sonic]] 10, [[srd/pf2e/compendium/rules-elements/traits/player-core/Vitality|vitality]] 10, [[srd/pf2e/compendium/rules-elements/traits/player-core/Void|void]] 10"
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
    desc: "A masterpiece of complex spellwork instantly takes shape, casting [[srd/pf2e/compendium/spells/rank-4/Fire Shield|_fire shield_]], [[srd/pf2e/compendium/spells/rank-6/Mislead|_mislead_]], and [[srd/pf2e/compendium/spells/rank-4/Mountain Resilience|_mountain resilience_]] on the eldritch emeritus, each as an 8th-rank arcane spell."
speed: "25 feet, teleport 50 feet"
attacks:
  - name: "Melee"
    desc: "⬻ staff +31 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Two-Hand|two-hand d8]]) __Damage__ 3d4+14 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +30 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unarmed|Unarmed]]) __Damage__ 1d4+14 bludgeoning"
  - name: "Ranged"
    desc: "⬻ arcane beam +31 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Arcane|Arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Fire|Fire]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]]) __Damage__ 6d6+10 fire"
abilities_bot:
  - name: "Didactic Arcanism"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Arcane|Arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]])"
  - name: "Requirement"
    desc: "The eldritch emeritus has seen a creature Cast a Spell of 7th rank or lower during the previous round, that spell takes between one and three actions to cast, and that spell is on the arcane spell list"
  - name: "Effect"
    desc: "The eldritch emeritus mastered that spell 30 years ago, and is happy to show how a real master does it. The emeritus Casts the same Spell but heightened to 8th rank. Didactic Arcanism uses the same number of actions as the original spell took to cast."
  - name: "Steady Spellcasting"
    desc: "If a reaction would [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Actions#Disrupting Actions|disrupt]] the eldritch emeritus's spellcasting action, the eldritch emeritus attempts a DC 15 flat check. On a success, the action isn't disrupted."
spellcasting:
  - name: "Arcane Prepared Spells"
    desc: "DC 38, attack +30 - __Cantrips (9th)__ [[srd/pf2e/compendium/spells/cantrips/Detect Magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/Light|Light]], [[srd/pf2e/compendium/spells/cantrips/Prestidigitation|Prestidigitation]], [[srd/pf2e/compendium/spells/cantrips/Sigil|Sigil]], [[srd/pf2e/compendium/spells/cantrips/Telekinetic Hand|Telekinetic Hand]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/Fleet Step|Fleet Step]] (x2), [[srd/pf2e/compendium/spells/rank-1/Sure Strike|Sure Strike]] - __2nd__ [[srd/pf2e/compendium/spells/rank-2/Gecko Grip|Gecko Grip]], [[srd/pf2e/compendium/spells/rank-2/Translate|Translate]], [[srd/pf2e/compendium/spells/rank-2/Water Walk|Water Walk]] - __3rd__ [[srd/pf2e/compendium/spells/rank-3/Earthbind|Earthbind]], [[srd/pf2e/compendium/spells/rank-3/Haste|Haste]], [[srd/pf2e/compendium/spells/rank-3/Locate|Locate]] - __4th__ [[srd/pf2e/compendium/spells/rank-4/Creation|Creation]], [[srd/pf2e/compendium/spells/rank-2/Dispel Magic|Dispel Magic]], [[srd/pf2e/compendium/spells/rank-4/Fly|Fly]] - __5th__ [[srd/pf2e/compendium/spells/rank-5/Banishment|Banishment]], [[srd/pf2e/compendium/spells/rank-5/Howling Blizzard|Howling Blizzard]], [[srd/pf2e/compendium/spells/rank-5/Slither|Slither]] - __6th__ [[srd/pf2e/compendium/spells/rank-6/Disintegrate|Disintegrate]], [[srd/pf2e/compendium/spells/rank-6/Teleport|Teleport]], [[srd/pf2e/compendium/spells/rank-6/Wall of Force|Wall of Force]] - __7th__ [[srd/pf2e/compendium/spells/rank-6/Chain Lightning|Chain Lightning]] (×2), [[srd/pf2e/compendium/spells/rank-7/Project Image|Project Image]] - __8th__ [[srd/pf2e/compendium/spells/rank-8/Earthquake|Earthquake]], [[srd/pf2e/compendium/spells/rank-8/Quandary|Quandary]] (×2) - __9th__ [[srd/pf2e/compendium/spells/rank-9/Detonate Magic|Detonate Magic]], [[srd/pf2e/compendium/spells/rank-9/Falling Stars|Falling Stars]] - __Constant (9th)__ [[srd/pf2e/compendium/spells/rank-7/Energy Aegis|Energy Aegis]]"
sourcebook: "_NPC Core_, page 143."
```

```encounter-table
name: Eldritch Emeritus
creatures:
  - 1: Eldritch Emeritus
```
