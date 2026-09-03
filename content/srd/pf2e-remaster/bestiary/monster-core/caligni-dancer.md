---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Caligni Dancer"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/caligni
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/small
statblock: inline
name: "Caligni Dancer"
level: 1
source: "Monster Core"
aon_id: "creature-2862"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2862"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Caligni Dancer"
level: "Creature 1"
size: "Small"
trait_01: "Caligni"
trait_02: "Humanoid"
modifier: 6
perception:
  - name: "Perception"
    desc: "Perception +6; greater darkvision, light blindness"
languages: "Caligni"
skills:
  - name: "Skills"
    desc: "Acrobatics +7, Diplomacy +8, Performance +6, Stealth +7, Thievery +7"
abilityMods: [0, 4, 2, -1, 1, 3]
abilities_top:
  - name: "Items"
    desc: "baton (functions as light mace), Dagger"
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +7; __Ref__: +9; __Will__: +4"
hp: 18
health:
  - name: "HP"
    desc: "18 (final dance)"
abilities_mid:
  - name: "Distracting Frolic"
    desc: "⬲ (fortune, manipulate)"
  - name: "Trigger"
    desc: "An ally within 10 feet of the dancer rolls a saving throw against a mental or illusion effect"
  - name: "Effect"
    desc: "The target ally can roll the save twice and take the better result."
  - name: "Final Dance"
    desc: "(occult, shadow, visual) When the dancer dies, their body dissolves into a swirling mass of darkness and light. All creatures in a 10-foot emanation must succeed at a DC 17 Will save or be dazzled for 1d4 rounds. The dancer's possessions are left in a pile where they died."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ baton +9 (Agile, Finesse, Shove) __Damage__ 1d4 bludgeoning"
  - name: "Melee"
    desc: "⬻ dagger +9 (Agile, Finesse, versatile S) __Damage__ 1d4 piercing"
  - name: "Ranged"
    desc: "⬻ dagger +9 (Agile, thrown 10 feet, versatile S) __Damage__ 1d4 piercing"
abilities_bot:
  - name: "Dancer's Curse"
    desc: "⬻ (Curse, Mental, Occult) The caligni dancer touches a foe and curses it. If the target fails a DC 18 Will save, it gains clumsy 1 and stupefied 1. The target is then temporarily immune for 24 hours. These conditions persist until the curse is removed. The victim can attempt a new DC 18 Will save once per hour to end the curse."
  - name: "Sneak Attack"
    desc: "The caligni dancer deals 1d6 extra precision damage to off-guard creatures."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 16 - __Cantrips (1st)__ Courageous Anthem - __1st__ Counter Performance (visual only)"
sourcebook: "_Monster Core_, page 48."
```

```encounter-table
name: Caligni Dancer
creatures:
  - 1: Caligni Dancer
```
