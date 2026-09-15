---
noteType: pf2eMonster
aliases: "Nosoi"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/monitor
  - pf2e/creature/trait/psychopomp
  - pf2e/creature/trait/tiny
statblock: inline
name: "Nosoi"
level: 1
source: "Monster Core"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3147"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Nosoi"
level: "Creature 1"
size: "Tiny"
trait_01: "Monitor"
trait_02: "Psychopomp"
modifier: 6
perception:
  - name: "Perception"
    desc: "+6; darkvision, lifesense 60 feet"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Chthonian|Chthonian]], [[srd/pf2e/compendium/rules-elements/Languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/Languages#Empyrean|Empyrean]], Requian"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +6, Boneyard Lore +8, Library Lore +8, [[srd/pf2e/compendium/rules-elements/skills/Performance|Performance]] +6, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +6, [[srd/pf2e/compendium/rules-elements/skills/Society|Society]] +2, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +6"
abilityMods: [-1, 3, 1, 1, 1, 3]
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +4; __Ref__: +8; __Will__: +6"
hp: 18
health:
  - name: "HP"
    desc: "18; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Death|death]] effects, [[srd/pf2e/compendium/rules-elements/traits/player-core/Disease|disease]]; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|poison]] 3, [[srd/pf2e/compendium/rules-elements/traits/player-core/Void|void]] 3"
speed: "15 feet, fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ beak +6 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 0 feet]]) __Damage__ 1d4–1 piercing plus 1d6 shepherd's touch"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Polymorph|Polymorph]]) The nosoi takes the appearance of a raven or songbird. This doesn't change its Speed or its attack and damage modifiers with its Strikes."
  - name: "Haunting Melody"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Incapacitation|Incapacitation]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|Mental]]) The nosoi croons an entrancing song. Each living or [[srd/pf2e/compendium/rules-elements/traits/player-core/Undead|undead]] creature within a 60-foot emanation must attempt a DC 18 Will save. The effect lasts until the end of the nosoi's next turn, but the nosoi can Sustain it. A creature that succeeds at its save is temporarily immune for 24 hours. Despite being a [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]] effect, this ability affects [[srd/pf2e/compendium/rules-elements/traits/player-core/Mindless|mindless]] undead. Psychopomps are immune to this ability."
  - name: "Failure"
    desc: "The creature is [[srd/pf2e/compendium/rules-elements/Conditions#Fascinated|fascinated]] with the nosoi."
  - name: "Critical Failure"
    desc: "The creature is fascinated with the nosoi and must spend each of its actions on its turn to move closer to the nosoi as expediently as possible while avoiding obvious dangers. If a fascinated creature is adjacent to the nosoi, it stays still and doesn't act. If the creature is attacked, the fascination ends."
  - name: "Shepherd's Touch"
    desc: "A nosoi's Strikes have the benefit of a [[srd/pf2e/compendium/equipment/runes/Ghost Touch|_ghost touch_]] property rune and deal an additional 1d6 void damage to living creatures or 1d6 vitality damage to undead."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 16 - __2nd__ [[srd/pf2e/compendium/spells/rank-2/Invisibility|Invisibility]] (at will; self only), [[srd/pf2e/compendium/spells/rank-2/Noise Blast|Noise Blast]] - __4th__ [[srd/pf2e/compendium/spells/rank-4/Read Omens|Read Omens]], [[srd/pf2e/compendium/spells/rank-4/Talking Corpse|Talking Corpse]]"
sourcebook: "_Monster Core_, page 274."
```

```encounter-table
name: Nosoi
creatures:
  - 1: Nosoi
```
