---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Gambling Companion"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/tengu
  - pf2e/creature/trait/medium
statblock: inline
name: "Gambling Companion"
level: 3
source: "NPC Core"
aon_id: "creature-3670"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3670"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Gambling Companion"
level: "Creature 3"
size: "Medium"
trait_01: "Humanoid"
trait_02: "Tengu"
modifier: 12
perception:
  - name: "Perception"
    desc: "Perception +12; (14 to Sense Motive) low-light vision"
languages: "Common, Tengu; plus three others"
skills:
  - name: "Skills"
    desc: "Deception +11, Diplomacy +11, Games Lore +16, Society +9, Thievery +9"
abilityMods: [0, 3, 0, 2, 1, 4]
abilities_top:
  - name: "Social Specialist"
    desc: "For social encounters involving gaming or gambling, the gambling companion is a 5th-level challenge."
  - name: "Items"
    desc: "cards, Dagger (3), dice"
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +6; __Ref__: +12; __Will__: +9"
hp: 46
health:
  - name: "HP"
    desc: "46"
abilities_mid:
  - name: "Gamer's Guidance"
    desc: "(fortune) When the gambling companion successfully Aids a skill check related to games or gambling, the ally rolls twice and takes the higher result instead of gaining the usual bonus."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ beak +10 (Finesse) __Damage__ 1d6+2 piercing"
  - name: "Melee"
    desc: "⬻ dagger +10 (Agile, Finesse, versatile S) __Damage__ 1d4+2 piercing"
  - name: "Ranged"
    desc: "⬻ dagger +10 (Agile, thrown 10 feet, versatile S) __Damage__ 1d4+2 piercing"
abilities_bot:
  - name: "Distracting Trick"
    desc: "⬺"
  - name: "Requirements"
    desc: "The gambling companion is wielding cards or dice"
  - name: "Effect"
    desc: "The gambling companion performs a quick trick with the cards or dice to Feint, then makes a beak Strike against the same target. If the Feint succeeds, the Strike deals an additional 1d6 precision damage."
sourcebook: "_NPC Core_, page 212."
```

```encounter-table
name: Gambling Companion
creatures:
  - 1: Gambling Companion
```
