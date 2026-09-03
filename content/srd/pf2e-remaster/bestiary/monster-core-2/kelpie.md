---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Kelpie"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/amphibious
  - pf2e/creature/trait/fey
  - pf2e/creature/trait/large
statblock: inline
name: "Kelpie"
level: 4
source: "Monster Core 2"
aon_id: "creature-4458"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4458"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Kelpie"
level: "Creature 4"
size: "Large"
trait_01: "Amphibious"
trait_02: "Fey"
modifier: 11
perception:
  - name: "Perception"
    desc: "Perception +11; low-light vision"
languages: "Common, Fey, Thalassic"
skills:
  - name: "Skills"
    desc: "Athletics +11, Deception +14, Stealth +10"
abilityMods: [5, 2, 3, -1, 3, 4]
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +11; __Ref__: +12; __Will__: +14"
hp: 60
health:
  - name: "HP"
    desc: "60; __Resistances__ fire 5; __Weaknesses__ cold iron 5"
speed: "35 feet, swim 35 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +13 __Damage__ 2d6+7 bludgeoning plus Grab"
abilities_bot:
  - name: "Captivating Lure"
    desc: "⬺ (Concentrate, emotion, incapacitation, mental, primal) The kelpie instills an overwhelming attraction to itself within the mind of a single creature within 60 feet. The target perceives the kelpie as a desirable person (if the kelpie is in humanoid form) or a magnificent steed (if the kelpie is in equine form) and must attempt a DC 23 Will saving throw."
  - name: "Critical Success"
    desc: "The creature is unaffected and is temporarily immune to Captivating Lure for 24 hours."
  - name: "Success"
    desc: "The creature is stupefied 1 for 1 round and is then temporarily immune to Captivating Lure for 24 hours."
  - name: "Failure"
    desc: "The creature is fascinated, and it must spend each of its actions to move closer to the kelpie as expediently as possible while avoiding obvious dangers. If a captivated creature is adjacent to the kelpie, it either attempts to mount the kelpie (if the kelpie is in equine form) or stays still and doesn't act. If the creature is attacked by the kelpie, or if it can't breathe water and enters an area of water, the creature is freed from captivation at the end of the kelpie's turn."
  - name: "Critical Failure"
    desc: "As failure, but the target doesn't consider water a danger and will enter an area of water even if it can't swim or breathe water. If it is attacked by the kelpie or starts to drown, it can attempt a new save at the start of its next turn, but it isn't freed automatically."
  - name: "Change Shape"
    desc: "⬻ (Concentrate, polymorph, primal) The kelpie can take on the appearance of any Medium or Large animal of an equine nature (such as a horse, hippocampus, or pony), or any Small or Medium humanoid. This doesn't change its Speeds or its attack and damage modifiers with its Strikes. Kelpie Folktales Some fanciful stories about kelpies speak of them appearing in equine form wearing riding tack, complete with silver stirrups and bridle bit. These folktales claim that cutting the harness from a kelpie's body grants the bearer power over it or causes a kelpie to sicken and die. In truth, doing so has no ill effect on a kelpie, suggesting these stories are spread by kelpies themselves to further trick prey into making foolish mistakes."
sourcebook: "_Monster Core 2_, page 209."
```

```encounter-table
name: Kelpie
creatures:
  - 1: Kelpie
```
