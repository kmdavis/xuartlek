---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Adult Adamantine Dragon"
tags:
  - pf2e/creature/level/13
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/primal
  - pf2e/creature/trait/huge
statblock: inline
name: "Adult Adamantine Dragon"
level: 13
source: "Monster Core"
aon_id: "creature-2933"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2933"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Adult Adamantine Dragon"
level: "Creature 13"
size: "Huge"
trait_01: "Dragon"
trait_02: "Primal"
modifier: 23
perception:
  - name: "Perception"
    desc: "Perception +23; darkvision, scent (imprecise) 60 feet, tremorsense (imprecise) 90 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/languages#Fey|Fey]], [[srd/pf2e/compendium/rules-elements/languages#Petran|Petran]], [[srd/pf2e/compendium/rules-elements/languages#Sakvroth|Sakvroth]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +22, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +27, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +24, Mining Lore +24, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +23, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +25"
abilityMods: [8, 3, 6, 3, 4, 5]
ac: 33
armorclass:
  - name: "AC"
    desc: "33; __Fort__: +25; __Ref__: +20; __Will__: +23 +2 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|primal]]"
hp: 220
health:
  - name: "HP"
    desc: "220; __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/conditions#Petrified|petrified]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]; __Resistances__ physical 15 (except adamantine)"
abilities_mid:
  - name: "Abandon Armor"
    desc: "Once the adamantine dragon is reduced to fewer than half their Hit Points, their resistance is reduced by 10 and they gain a +10 circumstance bonus to their Speeds."
  - name: "Frightful Presence"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]]) 90 feet, DC 30"
  - name: "Resilient Form"
    desc: "⬲"
  - name: "Trigger"
    desc: "The dragon is critically hit with a weapon or unarmed attack"
  - name: "Effect"
    desc: "The dragon's tough scales ward off deadly attacks. The dragon attempts a DC 17 flat check. On a success, the triggering attack becomes a normal hit."
speed: "30 feet, burrow 40 feet, fly 150 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +27 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 3d12+14 piercing plus Improved Grab"
  - name: "Melee"
    desc: "⬻ claw +27 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 3d8+14 slashing plus Knockdown"
  - name: "Melee"
    desc: "⬻ tail +25 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 20 feet]]) __Damage__ 3d10+14 bludgeoning"
  - name: "Ranged"
    desc: "⬻ rock +25 (Brutal, range increment 120 feet) __Damage__ 3d8+14 bludgeoning"
abilities_bot:
  - name: "Adamantine Body"
    desc: "The dragon's unarmed melee Strikes are adamantine."
  - name: "Avalanche Breath"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]]) The dragon belches a mass of boulders that deals 11d8 bludgeoning damage in a 40-foot cone (DC 33 basic Reflex save). They can't use Avalanche Breath again for 1d4 rounds."
  - name: "Burrowing Pounce"
    desc: "⬽"
  - name: "Requirements"
    desc: "The dragon is burrowed"
  - name: "Effect"
    desc: "The dragon [[srd/pf2e/compendium/rules-elements/actions/player-core#Burrow|Burrows]], then [[srd/pf2e/compendium/rules-elements/actions/player-core#Leap|Leaps]] out of the ground, landing at a point within 25 feet. The dragon makes a melee Strike against a creature within reach when they land. If the Strike is a critical hit, the target is knocked [[srd/pf2e/compendium/rules-elements/conditions#Prone|prone]]."
  - name: "Draconic Frenzy"
    desc: "⬺ The dragon makes two claw Strikes and one tail Strike in any order."
  - name: "Draconic Momentum"
    desc: "The dragon recharges their Avalanche Breath whenever they score a critical hit with a Strike."
  - name: "Rock Tunneler"
    desc: "The dragon can burrow through solid stone at a Speed of 20 feet. They can leave a tunnel if they desire, and they usually don't."
  - name: "Swallow Whole"
    desc: "⬻ Large, 3d12+7 bludgeoning, Rupture 29"
  - name: "Throw Rock"
    desc: "⬻"
sourcebook: "_Monster Core_, page 109."
```

```encounter-table
name: Adult Adamantine Dragon
creatures:
  - 1: Adult Adamantine Dragon
```
