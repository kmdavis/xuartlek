---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Veteran Noble"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Veteran Noble"
level: 6
source: "NPC Core"
aon_id: "creature-3422"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3422"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Veteran Noble"
level: "Creature 6"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 15
perception:
  - name: "Perception"
    desc: "Perception +15"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Athletics +13, Deception +12, Diplomacy +12, Heraldry Lore +14, Intimidation +14, Warfare Lore +14"
abilityMods: [3, 2, 0, 2, 3, 2]
abilities_top:
  - name: "Items"
    desc: "Dagger, Half Plate, _+1 longsword_, signet ring"
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +12; __Ref__: +14; __Will__: +16"
hp: 85
health:
  - name: "HP"
    desc: "85"
abilities_mid:
  - name: "Battle Scarred"
    desc: "The first time each day the veteran noble would be reduced to 0 HP, they remain at 1 HP and are enfeebled 2 for the rest of the day."
  - name: "Noble Pride"
    desc: "⬲ (auditory, emotion, mental)"
  - name: "Trigger"
    desc: "An opponent attempts to Demoralize the veteran noble or one of the noble's allies within 30 feet"
  - name: "Effect"
    desc: "The veteran noble attempts to Demoralize the triggering opponent before the opponent rolls. On a critical success, the triggering action is disrupted as well."
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _longsword_ +16 (Magical, versatile P) __Damage__ 1d8+11 slashing"
  - name: "Melee"
    desc: "⬻ dagger +15 (Agile, versatile S) __Damage__ 1d4+11 piercing"
  - name: "Melee"
    desc: "⬻ gauntlet +15 (Agile, Free-Hand) __Damage__ 1d4+11 bludgeoning"
  - name: "Ranged"
    desc: "⬻ dagger +15 (Agile, thrown 10 feet, versatile S) __Damage__ 1d4+11 piercing"
abilities_bot:
  - name: "Tactical Command"
    desc: "⬻ (Auditory, Concentrate, Linguistic, Mental)"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The veteran noble directs an ally. The ally can immediately use their reaction to Strike or to Stride without triggering reactions. The ally gains a +2 status bonus to their Strike if the veteran noble has dealt with that creature or an organization that creature belongs to before, as the veteran offers hard-earned tactical advice."
sourcebook: "_NPC Core_, page 15."
```

```encounter-table
name: Veteran Noble
creatures:
  - 1: Veteran Noble
```
