---
noteType: pf2eMonster
aliases: "Young Adamantine Dragon"
tags:
  - pf2e/creature/level/9
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/primal
  - pf2e/creature/trait/large
statblock: inline
name: "Young Adamantine Dragon"
level: 9
source: "Monster Core"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2932"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Young Adamantine Dragon"
level: "Creature 9"
size: "Large"
trait_01: "Dragon"
trait_02: "Primal"
modifier: 17
perception:
  - name: "Perception"
    desc: "+17; darkvision, scent (imprecise) 60 feet, tremorsense (imprecise) 60 feet"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/Languages#Petran|Petran]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +17, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +21, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +18, Mining Lore +16, [[srd/pf2e/compendium/rules-elements/skills/Nature|Nature]] +17, [[srd/pf2e/compendium/rules-elements/skills/Survival|Survival]] +19"
abilityMods: [6, 2, 4, 1, 2, 3]
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +21; __Ref__: +15; __Will__: +17 +2 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/Primal|primal]]"
hp: 140
health:
  - name: "HP"
    desc: "140; __Immunities__ [[srd/pf2e/compendium/rules-elements/Conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/Conditions#Petrified|petrified]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Sleep|sleep]]; __Resistances__ physical 10 (except adamantine)"
abilities_mid:
  - name: "Abandon Armor"
    desc: "Once the adamantine dragon is reduced to fewer than half their Hit Points, their resistance is reduced by 10 and they gain a +10 circumstance bonus to their Speeds."
  - name: "Frightful Presence"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Fear|fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]]) 90 feet, DC 26"
  - name: "Resilient Form"
    desc: "⬲"
  - name: "Trigger"
    desc: "The dragon is critically hit with a weapon or unarmed attack"
  - name: "Effect"
    desc: "The dragon's tough scales ward off deadly attacks. The dragon attempts a DC 17 flat check. On a success, the triggering attack becomes a normal hit."
speed: "25 feet, burrow 30 feet, fly 90 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +21 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 10 feet]]) __Damage__ 2d12+9 piercing plus Grab"
  - name: "Melee"
    desc: "⬻ claw +21 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]]) __Damage__ 2d8+9 slashing plus Knockdown"
  - name: "Melee"
    desc: "⬻ tail +19 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 15 feet]]) __Damage__ 2d10+9 bludgeoning"
  - name: "Ranged"
    desc: "⬻ rock +19 (Brutal, range increment 90 feet) __Damage__ 2d8+9 bludgeoning"
abilities_bot:
  - name: "Adamantine Body"
    desc: "The dragon's unarmed melee Strikes are adamantine."
  - name: "Avalanche Breath"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Primal|Primal]]) The dragon belches a mass of boulders that deals 8d8 bludgeoning damage in a 30-foot cone (DC 28 basic Reflex save). They can't use Avalanche Breath again for 1d4 rounds."
  - name: "Burrowing Pounce"
    desc: "⬽"
  - name: "Requirements"
    desc: "The dragon is burrowed"
  - name: "Effect"
    desc: "The dragon [[srd/pf2e/compendium/rules-elements/actions/player-core#Burrow|Burrows]], then [[srd/pf2e/compendium/rules-elements/actions/player-core#Leap|Leaps]] out of the ground, landing at a point within 25 feet. The dragon makes a melee Strike against a creature within reach when they land. If the Strike is a critical hit, the target is knocked [[srd/pf2e/compendium/rules-elements/Conditions#Prone|prone]]."
  - name: "Draconic Frenzy"
    desc: "⬺ The dragon makes two claw Strikes and one tail Strike in any order."
  - name: "Draconic Momentum"
    desc: "The dragon recharges their Avalanche Breath whenever they score a critical hit with a Strike."
  - name: "Rock Tunneler"
    desc: "The dragon can burrow through solid stone at a Speed of 20 feet. They can leave a tunnel if they desire, and they usually don't."
  - name: "Swallow Whole"
    desc: "⬻ Medium, 2d12+4 bludgeoning, Rupture 22"
  - name: "Throw Rock"
    desc: "⬻"
sourcebook: "_Monster Core_, page 108."
```

```encounter-table
name: Young Adamantine Dragon
creatures:
  - 1: Young Adamantine Dragon
```
