---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Marp"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/small
statblock: inline
name: "Marp"
level: 4
source: "Howl of the Wild"
aon_id: "creature-3301"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3301"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Marp"
level: "Creature 4"
size: "Small"
trait_01: "Beast"
modifier: 12
perception:
  - name: "Perception"
    desc: "Perception +12; darkvision, goldsense (imprecise) 60 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Fey|Fey]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +12, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +10, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +13, [[srd/pf2e/compendium/rules-elements/skills/thievery|Thievery]] +12"
abilityMods: [4, 4, 2, -2, 2, 5]
abilities_top:
  - name: "Goldsense"
    desc: "Marps can sense any accumulation of gold within range. They also can precisely measure the purity of gold by touch."
ac: 20
armorclass:
  - name: "AC"
    desc: "20; __Fort__: +10; __Ref__: +14; __Will__: +10"
hp: 48
health:
  - name: "HP"
    desc: "48"
abilities_mid:
  - name: "Panicked Withdrawal"
    desc: "⬲"
  - name: "Trigger"
    desc: "The marp takes damage from a melee Strike"
  - name: "Effect"
    desc: "The marp drops any items held in their hands, then [[srd/pf2e/compendium/rules-elements/actions/player-core#Climb|ClimbS]] or Strides up to 15 feet."
speed: "25 feet, climb 15 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +12 __Damage__ 2d6+6 piercing __Gold?__ ⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/linguistic|Linguistic]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]]) The marp asks for gold from all creatures in a 30-foot emanation. Each target must attempt a DC 22 Will save or retrieve and drop gold valuables as a free action."
abilities_bot:
  - name: "Critical Success"
    desc: "The target can refuse the request, though they can also choose to willingly hand over any amount of gold. If they do so, they gain a +1 status bonus to the next saving throw they attempt within 1 minute, and they're temporarily immune to Scampering Theft for 1 minute."
  - name: "Success"
    desc: "The target can refuse the request."
  - name: "Failure"
    desc: "The target must drop coins, gold jewelry, or other objects worth 20 gp."
  - name: "Critical Failure"
    desc: "As failure, but 40 gp"
  - name: "Scampering Theft"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/manipulate|Manipulate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/move|Move]]) The marp runs and attempts to snatch a purse, pendant, or other such object. The marp Strides up to their Speed, and they can move through enemy spaces during this movement. They then attempt to steal valuables from the target, who must attempt a DC 22 Reflex save."
  - name: "Success"
    desc: "The marp fails to steal anything from the target."
  - name: "Failure"
    desc: "The marp steals one object from the target's possession that is made of or contains gold. They can't steal objects held by or permanently attached to the creature. If the object contains lead, the marp drops it at the target's feet. After stealing the object (or dropping it), the marp then Strides up to their Speed."
sourcebook: "_Howl of the Wild_, page 174."
```

```encounter-table
name: Marp
creatures:
  - 1: Marp
```
