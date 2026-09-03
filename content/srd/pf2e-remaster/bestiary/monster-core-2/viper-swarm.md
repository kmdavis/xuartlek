---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Viper Swarm"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/swarm
  - pf2e/creature/trait/large
statblock: inline
name: "Viper Swarm"
level: 4
source: "Monster Core 2"
aon_id: "creature-4555"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4555"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Viper Swarm"
level: "Creature 4"
size: "Large"
trait_01: "Animal"
trait_02: "Swarm"
modifier: 12
perception:
  - name: "Perception"
    desc: "Perception +12; low-light vision, scent (imprecise) 60 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +13, Stealth +11"
abilityMods: [1, 5, 3, -4, 2, -3]
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +11; __Ref__: +13; __Will__: +10"
hp: 50
health:
  - name: "HP"
    desc: "50; __Immunities__ precision, swarm mind; __Resistances__ bludgeoning 5, piercing 5, slashing 3; __Weaknesses__ area damage 5, splash damage 5"
speed: "30 feet, climb 30 feet, swim 30 feet"
abilities_bot:
  - name: "Venom Spritz"
    desc: "⬺ The vipers spray venom from their fangs in a defensive display. Each creature in a 10-foot cone is exposed to viper swarm venom but gains a +2 circumstance bonus to its initial saving throw against the poison."
  - name: "Venomous Fangs"
    desc: "⬻ Each enemy in the swarm's space takes 2d8 piercing damage (DC 21 basic Reflex save). A creature that fails their save is also exposed to viper swarm venom."
  - name: "Viper Swarm Venom"
    desc: "(Poison)"
  - name: "Saving Throw"
    desc: "DC 21 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "1d4 poison damage (1 round)"
  - name: "Stage 2"
    desc: "1d6 poison damage and clumsy 1 (1 round)"
  - name: "Stage 3"
    desc: "2d4 poison damage, clumsy 2, and enfeebled 1 (1 round) Slithering Packs Despite their solitary natures, snakes come together in swarms for purposes of hibernation or mating. However, a few species have learned to stick together and coordinate their hunting efforts, leading to slithering packs of predatory snakes."
sourcebook: "_Monster Core 2_, page 294."
```

```encounter-table
name: Viper Swarm
creatures:
  - 1: Viper Swarm
```
