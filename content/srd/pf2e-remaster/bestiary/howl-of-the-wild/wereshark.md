---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Wereshark"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/amphibious
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/werecreature
  - pf2e/creature/trait/large
statblock: inline
name: "Wereshark"
level: 4
source: "Howl of the Wild"
aon_id: "creature-3324"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3324"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Wereshark"
level: "Creature 4"
size: "Large"
trait_01: "Amphibious"
trait_02: "Beast"
trait_03: "Human"
trait_04: "Humanoid"
trait_05: "Werecreature"
modifier: 10
perception:
  - name: "Perception"
    desc: "Perception +10; blood scent, scent (imprecise) 100 feet"
languages: "Common; shark empathy"
skills:
  - name: "Skills"
    desc: "Athletics +12, Stealth +9, Survival +8"
abilityMods: [4, 3, 4, -1, 2, -1]
abilities_top:
  - name: "Blood Scent"
    desc: "The wereshark can smell blood in the water from up to 1 mile away."
  - name: "Shark Empathy"
    desc: "(primal) A wereshark can communicate with sharks."
  - name: "Items"
    desc: "studded leather, Trident"
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +12; __Ref__: +11; __Will__: +8"
hp: 75
health:
  - name: "HP"
    desc: "75; __Weaknesses__ silver 5"
abilities_mid:
  - name: "Reactive Strike"
    desc: "⬲"
speed: "25 feet, swim 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +14 __Damage__ 1d12+7 piercing plus curse of the wereshark"
  - name: "Melee"
    desc: "⬻ trident +14 __Damage__ 1d8+7 piercing plus fish fork"
  - name: "Ranged"
    desc: "⬻ trident +13 (thrown 20 feet) __Damage__ 1d8+7 piercing"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ (Concentrate, Polymorph, Primal) Medium human with fist +14 for 1d4+7 bludgeoning, or Large shark with jaws +14 for 1d12+7 piercing, no land Speed, and swim Speed 40 feet. The wereshark doesn't have the amphibious trait in human or shark form and has the aquatic trait in shark form."
  - name: "Curse of the Wereshark"
    desc: "(Curse, Primal) Saving Throw DC 18 Fortitude"
  - name: "Fish Fork"
    desc: "⬻"
  - name: "Requirements"
    desc: "The wereshark critically hit with a trident Strike on their most recent action this turn"
  - name: "Effect"
    desc: "The wereshark digs their trident deep within their target, skewering it before taking a massive bite. The target of the Strike becomes grabbed (Escape DC 18) and takes 1d4 persistent bleed damage, and the wereshark attempts a jaws Strike against it. The wereshark can't use their trident while they have a creature grabbed with it, but they can pull the trident free with a single action that has the manipulate trait."
  - name: "Moon Frenzy"
    desc: "(Polymorph, Primal)"
sourcebook: "_Howl of the Wild_, page 197."
```

```encounter-table
name: Wereshark
creatures:
  - 1: Wereshark
```
