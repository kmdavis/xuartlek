---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Gamekeeper"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Gamekeeper"
level: 6
source: "NPC Core"
aon_id: "creature-3475"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3475"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Gamekeeper"
level: "Creature 6"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 14
perception:
  - name: "Perception"
    desc: "Perception +14"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Athletics +13, Diplomacy +11, Hunting Lore +11, Intimidation +13, Nature +15, Survival +15"
abilityMods: [3, 4, 2, 0, 2, 1]
abilities_top:
  - name: "Items"
    desc: "animal treats, _+1 arbalest_ (40 bolts), Club"
ac: 23
armorclass:
  - name: "AC"
    desc: "23; __Fort__: +17; __Ref__: +13; __Will__: +12"
hp: 95
health:
  - name: "HP"
    desc: "95 __Sic 'Em!__ ⬲ (auditory, emotion, mental)"
abilities_mid:
  - name: "Trigger"
    desc: "An animal within 60 feet of the gamekeeper is killed"
  - name: "Effect"
    desc: "The gamekeeper stokes the ire of the wild. Until the end of the gamekeeper's next turn, they and all animals in a 60-foot emanation gain a +1 status bonus to attack rolls and a +2 status bonus to damage rolls."
  - name: "Keeper's Revenge"
    desc: "(curse, primal) When the gamekeeper dies, all creatures in a 60-foot emanation that have damaged the gamekeeper in the last minute must succeed a DC 24 Will saving throw or be cursed. All animals the cursed creature encounters have an initial attitude toward them that is one step worse. This curse can be removed only by an effect that specifically targets curses."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ club +15 __Damage__ 1d6+9 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +15 (Agile, Finesse, Nonlethal, Unarmed) __Damage__ 1d4+9 bludgeoning"
  - name: "Ranged"
    desc: "⬻ _arbalest_ +17 (backstabber 1, Magical, range increment 110 feet, reload 1) __Damage__ 1d10+6 piercing"
abilities_bot:
  - name: "Leader of the Pack"
    desc: "The gamekeeper depends on a small pack of dogs or other pack animals suitable for the environment to patrol their area. Creatures that are adjacent to a hostile animal are considered off-guard to the gamekeeper."
sourcebook: "_NPC Core_, page 56."
```

```encounter-table
name: Gamekeeper
creatures:
  - 1: Gamekeeper
```
