---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Desert Giant"
tags:
  - pf2e/creature/level/9
  - pf2e/creature/trait/giant
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/large
statblock: inline
name: "Desert Giant"
level: 9
source: "Monster Core 2"
aon_id: "creature-4409"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4409"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Desert Giant"
level: "Creature 9"
size: "Large"
trait_01: "Giant"
trait_02: "Humanoid"
modifier: 19
perception:
  - name: "Perception"
    desc: "Perception +19"
languages: "Common, Jotun"
skills:
  - name: "Skills"
    desc: "Acrobatics +21, Desert Lore +18, Intimidation +15, Survival +19"
abilityMods: [6, 6, 5, 3, 4, 0]
abilities_top:
  - name: "Items"
    desc: "Doubling Rings, Leather Armor, Scimitar, _+1 striking scimitar_"
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +18; __Ref__: +21; __Will__: +15"
hp: 185
health:
  - name: "HP"
    desc: "185"
speed: "40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _scimitar_ +21 (Forceful, magical, reach 10 feet, sweep) __Damage__ 2d6+12 slashing"
  - name: "Ranged"
    desc: "⬻ rock +19 (Brutal, range increment 120 feet) __Damage__ 2d8+12 bludgeoning"
abilities_bot:
  - name: "Sand Spin"
    desc: "⬻"
  - name: "Requirements"
    desc: "The desert giant is standing in sandy terrain"
  - name: "Effect"
    desc: "The desert giant spins around and stirs up loose sand in a 10-foot emanation. Until the beginning of the giant's next turn, creatures in the area are concealed, and other creatures are concealed to them."
  - name: "Sandwalking"
    desc: "Desert giants have adapted to the loose sands of the desert and can move across them with ease. Desert giants ignore non-magical difficult terrain and uneven ground caused by sand."
  - name: "Scimitar Blitz"
    desc: "⬺ The desert giant Strides up to their Speed, Striking once with each of their scimitars at any point during the movement. Oasis Protectors Keenly aware of their native environs' fragile ecosystem, desert giants fiercely protect their favorite watering holes and ancestral oases from newcomers who might despoil the local flora or chase away scarce fauna. Anyone who convinces them they mean no harm is welcomed, and there are tales of them aiding those hurt by the harshness of the desert."
sourcebook: "_Monster Core 2_, page 162."
```

```encounter-table
name: Desert Giant
creatures:
  - 1: Desert Giant
```
