---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Amphisbaena"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/medium
statblock: inline
name: "Amphisbaena"
level: 4
source: "Monster Core 2"
aon_id: "creature-4027"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4027"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Amphisbaena"
level: "Creature 4"
size: "Medium"
trait_01: "Animal"
modifier: 11
perception:
  - name: "Perception"
    desc: "Perception +11; tremorsense 60 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +10, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +13, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +12"
abilityMods: [5, 4, 2, -4, 0, -4]
ac: 20
armorclass:
  - name: "AC"
    desc: "20; __Fort__: +11; __Ref__: +14; __Will__: +8"
hp: 70
health:
  - name: "HP"
    desc: "70; __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Petrified|petrified]]"
speed: "25 feet, climb 25 feet, swim 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fangs +13 __Damage__ 2d6+5 piercing plus amphisbaena venom"
  - name: "Ranged"
    desc: "⬻ spit +12 (range increment 15 feet) __Damage__ 1d6 poison plus amphisbaena venom and blinding spittle"
abilities_bot:
  - name: "Amphisbaena Venom"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]])"
  - name: "Saving Throw"
    desc: "DC 18 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "1d6 poison damage and [[srd/pf2e/compendium/rules-elements/conditions#Enfeebled|enfeebled 1]] (1 round)"
  - name: "Stage 2"
    desc: "2d6 poison damage and enfeebled 2 and [[srd/pf2e/compendium/rules-elements/conditions#Slowed|slowed 1]] (1 round)"
  - name: "Stage 3"
    desc: "3d6 poison damage and [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]] for 1 round (1 round)"
  - name: "Blinding Spittle"
    desc: "A creature critically hit by an amphisbaena's spit Strike is [[srd/pf2e/compendium/rules-elements/conditions#Blinded|blinded]] for 1 round."
  - name: "Twin Bites"
    desc: "⬻ An amphisbaena makes a fangs Strike with each of its heads, each against a different target. Both Strikes count toward its multiple attack penalty, but the penalty doesn't increase until after it has made both attacks. Amphisbaena Variants While the two-headed snake is by far the most common amphisbaena, the term sometimes describes other creatures with heads on both ends of their bodies. Occasionally, stories circulate of a monstrous amphisbaena with the body of a lizard, clawed feet, or even feathered wings. These stories are typically chalked up to an overactive imagination or an abundance of drink, but they persist regardless."
sourcebook: "_Monster Core 2_, page 25."
```

```encounter-table
name: Amphisbaena
creatures:
  - 1: Amphisbaena
```
