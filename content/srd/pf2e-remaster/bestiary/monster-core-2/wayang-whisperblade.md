---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Wayang Whisperblade"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/shadow
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/wayang
  - pf2e/creature/trait/small
statblock: inline
name: "Wayang Whisperblade"
level: 1
source: "Monster Core 2"
aon_id: "creature-4615"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4615"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Wayang Whisperblade"
level: "Creature 1"
size: "Small"
trait_01: "Humanoid"
trait_02: "Shadow"
trait_03: "Uncommon"
trait_04: "Wayang"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9; darkvision"
languages: "Common, Shadowtongue, Wayang"
skills:
  - name: "Skills"
    desc: "Acrobatics +7, Deception +4, Netherworld Lore +6, Occultism +6, Performance +6, Stealth +7, Thievery +7"
abilityMods: [0, 4, 1, 3, 0, 1]
abilities_top:
  - name: "Items"
    desc: "Kukri (2), Leather Armor"
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +6; __Ref__: +9; __Will__: +5 +1 to all saves vs. darkness or shadow"
hp: 19
health:
  - name: "HP"
    desc: "19"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ kukri +8 (Agile, finesse, trip) __Damage__ 1d6 slashing"
abilities_bot:
  - name: "Shadowplay"
    desc: "⬻ (Illusion, occult, shadow)"
  - name: "Requirements"
    desc: "The wayang's last action was a melee Strike that damaged their opponent"
  - name: "Effect"
    desc: "The wayang attempts to Tumble Through the opponent's space, with a +2 circumstance bonus to the Acrobatics check. If they succeed, the wayang leaves a shadowy afterimage in their original space, which provides flanking against the opponent until the beginning of the wayang's next turn (usually making them off-guard to the wayang's melee attacks)."
  - name: "Sneak Attack"
    desc: "The wayang deals an additional 1d6 precision damage to off-guard creatures."
sourcebook: "_Monster Core 2_, page 353."
```

```encounter-table
name: Wayang Whisperblade
creatures:
  - 1: Wayang Whisperblade
```
