---
noteType: pf2eMonster
aliases: "Wraith"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/incorporeal
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/wraith
  - pf2e/creature/trait/medium
statblock: inline
name: "Wraith"
level: 6
source: "Monster Core"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3243"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Wraith"
level: "Creature 6"
size: "Medium"
trait_01: "Incorporeal"
trait_02: "Undead"
trait_03: "Unholy"
trait_04: "Wraith"
modifier: 14
perception:
  - name: "Perception"
    desc: "+14; darkvision, lifesense 60 feet"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Necril|Necril]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +12, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +13, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +15, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +16"
abilityMods: [-5, 4, 0, 2, 2, 5]
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +8; __Ref__: +14; __Will__: +14"
hp: 80
health:
  - name: "HP"
    desc: "80 (void healing); __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/traits/player-core/Death|death]] effects, [[srd/pf2e/compendium/rules-elements/traits/player-core/Disease|disease]], [[srd/pf2e/compendium/rules-elements/Conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|poison]], precision, [[srd/pf2e/compendium/rules-elements/Conditions#Unconscious|unconscious]]; __Resistances__ all damage 5 (except [[srd/pf2e/compendium/rules-elements/traits/player-core/Force|force]], [[srd/pf2e/compendium/equipment/runes/Ghost Touch|ghost touch]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Spirit|spirit]], or [[srd/pf2e/compendium/rules-elements/traits/player-core/Vitality|vitality]]; double resistance vs. non-[[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magical]])"
abilities_mid:
  - name: "Sunlight Powerlessness"
    desc: "While in sunlight, a wraith is [[srd/pf2e/compendium/rules-elements/Conditions#Blinded|blinded]] and [[srd/pf2e/compendium/rules-elements/Conditions#Slowed|slowed 2]]."
speed: "fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ wraith touch +17 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Void|Void]]) __Damage__ 3d8 void"
abilities_bot:
  - name: "Grip of Fear"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Fear|Fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|Mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|Nonlethal]]) The wraith reaches into an adjacent creature's chest, gripping their heart. The target takes 6d6 mental damage with a DC 24 basic Will save. On a critical failure, the creature is also [[srd/pf2e/compendium/rules-elements/Conditions#Paralyzed|paralyzed]] until the start of the wraith's next turn."
  - name: "Robes of Welcome"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Void|Void]])"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The wraith wraps its robes around an adjacent living creature, exposing it to void's embrace. If any creature is cursed by the wraith's void's embrace, the wraith can't impose void's embrace on another creature."
  - name: "Void's Embrace"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Curse|Curse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Death|Death]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Void|Void]]) If the victim succeeds at a saving throw against this curse while in sunlight, the curse ends. While you have this curse, you bypass the resistance of the wraith that cursed you"
  - name: "Saving Throw"
    desc: "DC 24 Will"
  - name: "Stage 1"
    desc: "the victim is [[srd/pf2e/compendium/rules-elements/Conditions#Dazzled|dazzled]] in any light (1 hour)"
  - name: "Stage 2"
    desc: "the victim gains lifesense 30 feet but is [[srd/pf2e/compendium/rules-elements/Conditions#Blinded|blinded]] in any light (1 hour)"
  - name: "Stage 3"
    desc: "as stage 2, but the creature also has void healing (1 hour)"
  - name: "Stage 4"
    desc: "the victim becomes [[srd/pf2e/compendium/rules-elements/Conditions#Unconscious|unconscious]] and can't awaken (1 day)"
  - name: "Stage 5"
    desc: "the creature dies and becomes a wraith, its body crumbling to ash"
sourcebook: "_Monster Core_, page 351."
```

```encounter-table
name: Wraith
creatures:
  - 1: Wraith
```
