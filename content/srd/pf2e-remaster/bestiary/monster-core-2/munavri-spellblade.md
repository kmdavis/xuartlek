---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Munavri Spellblade"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/munavri
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/medium
statblock: inline
name: "Munavri Spellblade"
level: 2
source: "Monster Core 2"
aon_id: "creature-4483"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4483"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Munavri Spellblade"
level: "Creature 2"
size: "Medium"
trait_01: "Humanoid"
trait_02: "Munavri"
trait_03: "Rare"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7; darkvision, light blindness"
languages: "Munavri, Sakvroth; telepathy 30 feet (munavris only)"
skills:
  - name: "Skills"
    desc: "Athletics +8, Deception +7, Occultism +6, Stealth +4"
abilityMods: [4, 0, 2, 0, 1, 3]
abilities_top:
  - name: "Items"
    desc: "Bastard Sword, Breastplate"
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +8; __Ref__: +6; __Will__: +7"
hp: 30
health:
  - name: "HP"
    desc: "30; __Resistances__ mental 2"
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ bastard sword +8 (two-hand d12) __Damage__ 1d8+4 slashing"
abilities_bot:
  - name: "Addling Strike"
    desc: "⬻"
  - name: "Frequency"
    desc: "once per turn"
  - name: "Requirements"
    desc: "The munavri's most recent action was to Cast a Spell"
  - name: "Effect"
    desc: "The munavri Strikes. This Strike gains the occult trait and deals an additional 1d4 mental damage."
  - name: "Intuit Object"
    desc: "⬺ (Concentrate, fortune, occult)"
  - name: "Frequency"
    desc: "once per day"
  - name: "Effect"
    desc: "By concentrating their psychic energy on a held object, the munavri intuits its use and understands how to effectively wield it. If they focus on a weapon, they can roll twice and take the better result for the next Strike they make with it before the end of their next turn. If they focus on a tool, they can roll twice and take the better result for the next skill check they attempt with that tool within the next minute."
spellcasting:
  - name: "Occult Spontaneous Spells"
    desc: "DC 17, attack +9 - __Cantrips (1st)__ Daze, Message, Shield, Telekinetic Projectile - __1st__ Mindlink, Phantom Pain, Soothe"
sourcebook: "_Monster Core 2_, page 229."
```

```encounter-table
name: Munavri Spellblade
creatures:
  - 1: Munavri Spellblade
```
