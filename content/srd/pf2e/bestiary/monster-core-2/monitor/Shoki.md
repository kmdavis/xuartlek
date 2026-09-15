---
noteType: pf2eMonster
aliases: "Shoki"
tags:
  - pf2e/creature/level/9
  - pf2e/creature/trait/monitor
  - pf2e/creature/trait/psychopomp
  - pf2e/creature/trait/medium
statblock: inline
name: "Shoki"
level: 9
source: "Monster Core 2"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4524"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Shoki"
level: "Creature 9"
size: "Medium"
trait_01: "Monitor"
trait_02: "Psychopomp"
modifier: 21
perception:
  - name: "Perception"
    desc: "+21; darkvision, lifesense 60 feet"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Chthonian|Chthonian]], [[srd/pf2e/compendium/rules-elements/Languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/Languages#Empyrean|Empyrean]], Requian; [[srd/pf2e/compendium/spells/rank-5/Truespeech|_truespeech_]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Lore|Boneyard Lore]] +19, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +20, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +20, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +20, [[srd/pf2e/compendium/rules-elements/skills/Occultism|Occultism]] +16, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +19, [[srd/pf2e/compendium/rules-elements/skills/Society|Society]] +16, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +14"
abilityMods: [4, 1, 4, 3, 6, 5]
abilities_top:
  - name: "Items"
    desc: "countless [[srd/pf2e/compendium/equipment/adventuring-gear/Religious Symbol|religious symbols]], Staff"
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +19; __Ref__: +14; __Will__: +21 +1 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magic]]"
hp: 150
health:
  - name: "HP"
    desc: "150; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Death|death]] effects, [[srd/pf2e/compendium/rules-elements/traits/player-core/Disease|disease]]; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|poison]] 10, [[srd/pf2e/compendium/rules-elements/traits/player-core/Void|void]] 10"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ staff +19 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Two-Hand|two-hand d8]]) __Damage__ 2d4+6 bludgeoning plus shepherd's touch"
abilities_bot:
  - name: "Infuse Staff"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]]) A shoki's staff becomes a _+1 [[srd/pf2e/compendium/equipment/runes/Striking|striking]] staff_ and is treated as if it were adamantine while the shoki wields it. A shoki's staff has Hardness 14 and HP 56 (BT 28) while possessed by the shoki and Hardness 5 and HP 20 (BT 10) while out of the shoki's possession. A shoki whose staff is taken or destroyed can infuse a new one with an hour of work."
  - name: "Soul Lock"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Incapacitation|Incapacitation]])"
  - name: "Requirements"
    desc: "The shoki doesn't have a soul locked within their staff"
  - name: "Effect"
    desc: "The shoki attempts to capture the soul of a creature on the brink of death: an [[srd/pf2e/compendium/rules-elements/traits/player-core/Undead|undead]] creature, a creature with the [[srd/pf2e/compendium/rules-elements/Conditions#Dying|dying]] condition, or a creature that died within the last minute. The target must attempt a DC 32 Will save with the following results."
  - name: "Critical Success"
    desc: "The creature is unaffected and becomes temporarily immune to Soul Lock."
  - name: "Success"
    desc: "The shoki's staff tugs at the creature's soul but doesn't trap it. If the creature is living, it becomes [[srd/pf2e/compendium/rules-elements/Conditions#Doomed|doomed 1]] (or increases its doomed condition by 1). If the creature is a corporeal undead, it becomes [[srd/pf2e/compendium/rules-elements/Conditions#Enfeebled|enfeebled 2]]. If the creature is an [[srd/pf2e/compendium/rules-elements/traits/gm-core/Incorporeal|incorporeal]] undead, it becomes [[srd/pf2e/compendium/rules-elements/Conditions#Stupefied|stupefied 2]]. The creature then becomes temporarily immune to Soul Lock for 24 hours."
  - name: "Failure"
    desc: "The shoki captures the creature's soul in its staff. If the creature is living, it dies. If the creature is a corporeal undead, its body becomes an inanimate corpse. While the soul is locked in the staff, the target can't be returned to life or undeath or rejuvenate through any means, save for powerful magic, such a [[srd/pf2e/compendium/spells/rituals/Wish|_wish_]] ritual. If the shoki's staff is destroyed or the shoki wills it, the soul is released. A shoki's staff can only hold one soul at a time."
  - name: "Shepherd's Touch"
    desc: "A psychopomp's Strikes affect [[srd/pf2e/compendium/rules-elements/traits/gm-core/Incorporeal|incorporeal]] creatures with the effects of a [[srd/pf2e/compendium/equipment/runes/Ghost Touch|_ghost touch_]] property rune and deal 2d6 void damage to living creatures and 2d6 vitality damage to [[srd/pf2e/compendium/rules-elements/traits/player-core/Undead|undead]]. Tools Of The Trade Shokis utilize numerous tools to aid them in their work, including religious symbols, magic, soul-trapping staves, and false empathy—though shokis spout impassioned speeches and play upon mortal emotions, they hold no compassion for the dead."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 28, attack +20 - __Cantrips (5th)__ [[srd/pf2e/compendium/spells/cantrips/Detect Magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/Frostbite|Frostbite]], [[srd/pf2e/compendium/spells/cantrips/Read Aura|Read Aura]], [[srd/pf2e/compendium/spells/cantrips/Stabilize|Stabilize]], [[srd/pf2e/compendium/spells/cantrips/Vitality Lash|Vitality Lash]] - __2nd__ [[srd/pf2e/compendium/spells/rank-2/Calm|Calm]], [[srd/pf2e/compendium/spells/rank-2/Invisibility|Invisibility]] (at will; self only) - __4th__ [[srd/pf2e/compendium/spells/rank-3/Holy Light|Holy Light]] (×3), [[srd/pf2e/compendium/spells/rank-4/Read Omens|Read Omens]] - __5th__ [[srd/pf2e/compendium/spells/rank-1/Heal|Heal]] (×3), [[srd/pf2e/compendium/spells/rank-5/Mind Probe|Mind Probe]] - __6th__ [[srd/pf2e/compendium/spells/rank-6/Spirit Blast|Spirit Blast]] - __7th__ [[srd/pf2e/compendium/spells/rank-7/Interplanar Teleport|Interplanar Teleport]] (self and locked soul only; to the [[srd/pf2e/compendium/gm/Planes#Boneyard|Boneyard]] only) - __Constant (5th)__ [[srd/pf2e/compendium/spells/rank-5/Truespeech|Truespeech]]"
sourcebook: "_Monster Core 2_, page 264."
```

```encounter-table
name: Shoki
creatures:
  - 1: Shoki
```
