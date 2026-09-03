---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Zombie Hulk"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/zombie
  - pf2e/creature/trait/huge
statblock: inline
name: "Zombie Hulk"
level: 6
source: "Monster Core"
aon_id: "creature-3252"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3252"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Zombie Hulk"
level: "Creature 6"
size: "Huge"
trait_01: "Mindless"
trait_02: "Undead"
trait_03: "Unholy"
trait_04: "Zombie"
modifier: 8
perception:
  - name: "Perception"
    desc: "Perception +8; darkvision"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +18"
abilityMods: [7, -1, 4, -5, 0, -2]
abilities_top:
  - name: "Slow"
    desc: "A zombie is permanently [[srd/pf2e/compendium/rules-elements/conditions#Slowed|slowed 1]] and can't use reactions."
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +16; __Ref__: +9; __Will__: +12"
hp: 160
health:
  - name: "HP"
    desc: "160 (void healing); __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/traits/player-core/death|death]] effects, [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]]; __Weaknesses__ slashing 10, vitality 10"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ hunk of meat +17 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 2d10+9 bludgeoning"
  - name: "Ranged"
    desc: "⬻ corpse +17 (Brutal, range increment 30 feet) __Damage__ 2d6+9 bludgeoning"
abilities_bot:
  - name: "Corpse Throwing"
    desc: "A zombie hulk can throw Medium or smaller corpses at foes. They can also throw Medium or smaller zombies for this purpose, who take just as much damage as the target they hit. A zombie that survives being thrown falls [[srd/pf2e/compendium/rules-elements/conditions#Prone|prone]]."
  - name: "Wide Swing"
    desc: "⬻ The zombie hulk makes two hunk of meat Strikes against different targets within its reach."
sourcebook: "_Monster Core_, page 357."
```

```encounter-table
name: Zombie Hulk
creatures:
  - 1: Zombie Hulk
```
