---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Ghostly Mob"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/ghost
  - pf2e/creature/trait/incorporeal
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Ghostly Mob"
level: 8
source: "Monster Core 2"
aon_id: "creature-4407"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4407"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Ghostly Mob"
level: "Creature 8"
size: "Gargantuan"
trait_01: "Ghost"
trait_02: "Incorporeal"
trait_03: "Troop"
trait_04: "Uncommon"
trait_05: "Undead"
trait_06: "Unholy"
modifier: 16
perception:
  - name: "Perception"
    desc: "Perception +16; darkvision"
languages: "Common, Necril"
skills:
  - name: "Skills"
    desc: "Acrobatics +16, Dwelling Lore +16, Stealth +18"
abilityMods: [-5, 4, 3, 0, 4, 4]
abilities_top:
  - name: "Site Bound"
    desc: "A ghostly mob can stray no farther than 240 feet from where its members were killed."
ac: 25
armorclass:
  - name: "AC"
    desc: "25; __Fort__: +15; __Ref__: +14; __Will__: +18"
hp: 105
health:
  - name: "HP"
    desc: "105 (4 segments, rejuvenation, void healing); __Immunities__ bleed, death effects, disease, paralyzed, poison, precision, unconscious; __Resistances__ all damage 10 (except force, _ghost touch_, spirit, or vitality; double resistance vs. non-magical); __Weaknesses__ area damage 8, splash damage 8"
abilities_mid:
  - name: "Rejuvenation"
    desc: "(divine) When a ghostly mob is destroyed, it reforms after 2d4 days within the location it's bound to, fully healed. A ghostly mob can be permanently destroyed only if someone sets right whatever prevents the troop from resting."
  - name: "Troop Defenses"
    desc: ""
speed: "fly 25 feet; troop movement"
abilities_bot:
  - name: "Clutching Hands"
    desc: "Frequency__ once per round__"
  - name: "Effect"
    desc: "The troop attacks enemies in a 5-foot emanation, with a DC 23 basic Reflex save. The damage depends on the number of actions. ⬻ 1d6+3 void damage ⬺ 3d6+6 void damage ⬽ 4d6+9 void damage"
  - name: "Frightful Chorus"
    desc: "⬺ (Auditory, divine, emotion, fear, mental) The ghostly mob howls in anguish, sharing the pain of their death with any living creature that can hear them. This painful wailing forces each living creature in a 30-foot emanation to attempt a DC 26 Will save or become frightened 2 (frightened 3 on a critical failure). Regardless of the save result, the creature is then temporarily immune to the troop's Frightful Chorus for 1 minute. Echoes Of Tragedy The specific tragedy that created a ghostly mob might alter its abilities. For example, a ghostly mob spawned from a fire might have Burning Grasp rather than Clutching Hands, which deals fire damage instead of void damage. A ghostly mob created in an earthquake might have Earthshaking Chorus rather than Frightful Chorus, which causes living victims to be slowed for 1 round rather than frightened."
sourcebook: "_Monster Core 2_, page 161."
```

```encounter-table
name: Ghostly Mob
creatures:
  - 1: Ghostly Mob
```
