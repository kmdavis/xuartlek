---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Army Ant Swarm"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/swarm
  - pf2e/creature/trait/large
statblock: inline
name: "Army Ant Swarm"
level: 5
source: "Monster Core"
aon_id: "creature-2825"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2825"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Army Ant Swarm"
level: "Creature 5"
size: "Large"
trait_01: "Animal"
trait_02: "Swarm"
modifier: 11
perception:
  - name: "Perception"
    desc: "Perception +11; darkvision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +7"
abilityMods: [-2, 4, 4, -5, 2, -4]
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +13; __Ref__: +11; __Will__: +9"
hp: 55
health:
  - name: "HP"
    desc: "55; __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]], precision, [[srd/pf2e/compendium/rules-elements/conditions#Prone|prone]], [[srd/pf2e/compendium/rules-elements/conditions#Restrained|restrained]], swarm mind; __Resistances__ bludgeoning 2, piercing 5, slashing 5; __Weaknesses__ area damage 5, [[srd/pf2e/compendium/rules-elements/traits/gm-core/splash|splash]] damage 5"
abilities_mid:
  - name: "Cling"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature leaves the swarm's space"
  - name: "Effect"
    desc: "The swarm takes 1d6 damage as ants cling to the creature and continue biting, dealing 3d6 persistent piercing damage. High winds or immersion in water reduces the DC of the flat check to end this persistent damage to 5. Any area damage dealt to the creature destroys these clinging ants."
speed: "30 feet, climb 30 feet"
abilities_bot:
  - name: "Swarming Bites"
    desc: "⬻ Each enemy in the swarm's space takes 3d6 piercing damage (DC 21 basic Fortitude save). A creature that fails its save against Swarming Bites becomes [[srd/pf2e/compendium/rules-elements/conditions#Clumsy|clumsy 1]] for 1 round. If the creature attempts a [[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|concentrate]] or [[srd/pf2e/compendium/rules-elements/traits/player-core/manipulate|manipulate]] action while affected, it must succeed at a DC 5 flat check or the action is lost; roll the check after spending the action, but before any effects are applied."
sourcebook: "_Monster Core_, page 21."
```

```encounter-table
name: Army Ant Swarm
creatures:
  - 1: Army Ant Swarm
```
