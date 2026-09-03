---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Urdefhan Warrior"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/urdefhan
  - pf2e/creature/trait/medium
statblock: inline
name: "Urdefhan Warrior"
level: 3
source: "Monster Core 2"
aon_id: "creature-4599"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4599"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Urdefhan Warrior"
level: "Creature 3"
size: "Medium"
trait_01: "Humanoid"
trait_02: "Urdefhan"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9; greater darkvision"
languages: "Aklo, Daemonic, Sakvroth"
skills:
  - name: "Skills"
    desc: "Athletics +10, Intimidation +9, Religion +7, Survival +7"
abilityMods: [3, 1, 2, 0, 2, 2]
abilities_top:
  - name: "Items"
    desc: "Composite Longbow (20 arrows), Rhoka Sword, studded leather"
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +9; __Ref__: +8; __Will__: +9"
hp: 55
health:
  - name: "HP"
    desc: "55 (void healing); __Immunities__ death effects, disease, fear; __Weaknesses__ vitality 5"
abilities_mid:
  - name: "Necrotic Decay"
    desc: "(divine, void) When an urdefhan dies, their translucent flesh quickly rots away and sublimates into a foul-smelling gas that fills a 5-foot emanation around the body. This gas deals 3d6 void damage to creatures in this area as their flesh curdles and rots (DC 17 basic Fortitude save)."
  - name: "Reactive Strike"
    desc: "⬲"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ rhoka sword +12 (deadly d8, two-hand d10) __Damage__ 1d8+6 slashing"
  - name: "Melee"
    desc: "⬻ jaws +12 __Damage__ 1d6+6 piercing plus Wicked Bite"
  - name: "Ranged"
    desc: "⬻ composite longbow +10 (deadly d10, propulsive, range increment 100 feet, volley 30 feet) __Damage__ 1d8+4 piercing"
abilities_bot:
  - name: "Ravenous Attack"
    desc: "⬺ The urdefhan makes one rhoka sword Strike and one jaws Strike against a single creature. Their multiple attack penalty doesn't increase until after both attacks."
  - name: "Wicked Bite"
    desc: "⬻"
  - name: "Requirements"
    desc: "The urdefhan damaged a creature with a jaws Strike on their last action"
  - name: "Effect"
    desc: "The urdefhan maintains contact, turning the creature's flesh translucent around the site of the injury. The target must succeed at a DC 20 Fortitude save or be affected by drain blood or drain vitality (the urdefhan's choice). If the jaws Strike was a critical hit, the creature is affected by both effects, using the same save result for both."
  - name: "Drain Blood"
    desc: "The urdefhan drinks some of the creature's blood. On a failed save, the creature is drained 1 and the urdefhan regains 5 HP (or, on a critical failure, it's drained 2 and the urdefhan regains 10 HP)."
  - name: "Drain Vitality"
    desc: "The urdefhan draws out some of the creature's vital essence. The creature becomes enfeebled 1 for 1 hour on a failed save (or enfeebled 2 for 1 hour on a critical failure)."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 17 - __1st__ Enfeeble, Gentle Landing (at will; self only) - __2nd__ Darkness"
sourcebook: "_Monster Core 2_, page 336."
```

```encounter-table
name: Urdefhan Warrior
creatures:
  - 1: Urdefhan Warrior
```
