---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Skin Shifter"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Skin Shifter"
level: 8
source: "NPC Core"
aon_id: "creature-3584"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3584"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Skin Shifter"
level: "Creature 8"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 16
perception:
  - name: "Perception"
    desc: "Perception +16; (18 in animal form)"
languages: "Common, Wildsong"
skills:
  - name: "Skills"
    desc: "Acrobatics +12, Athletics +14, Diplomacy +13, Intimidation +11, Nature +18, Stealth +12, Survival +18"
abilityMods: [4, 2, 3, 0, 4, 1]
abilities_top:
  - name: "Animal Empathy"
    desc: "The skin shifter can ask questions of, receive answers from, and use the Diplomacy skill with animals."
  - name: "Items"
    desc: "Hide Armor, _+1 striking longbow_ (20 arrows), Spiked Gauntlet"
ac: 25
armorclass:
  - name: "AC"
    desc: "25; __Fort__: +15; __Ref__: +14; __Will__: +16"
hp: 140
health:
  - name: "HP"
    desc: "140"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ spiked gauntlet +18 (Agile, Free-Hand) __Damage__ 1d4+10 piercing"
  - name: "Ranged"
    desc: "⬻ _longbow_ +17 (deadly d10, Magical, range increment 100 feet, reload 0, volley 30 feet) __Damage__ 2d8+6 piercing"
abilities_bot:
  - name: "Gift of the Wild Spirits"
    desc: "⬻ (Primal)"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The skin shifter casts their choice of a 4th-rank _aerial form_, _animal form_, _dinosaur form_, or _pest form_ spell. They must transform into an animal of a kind they've seen within the last 24 hours. They can't gain temporary HP again from a spell cast with Gift of the Wild Spirits for 10 minutes. Their Strikes for forms other than _pest form_ have reach 10 feet, a +20 attack modifier, and a +13 damage bonus (or a +9 damage bonus for aerial form). Most other changes to their statistics are listed above. While polymorphed, the skin shifter can still use Gift of the Wild Spirits, though they're still prevented from casting other spells as normal."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 26 - __Cantrips (4th)__ Gouging Claw, Know the Way"
sourcebook: "_NPC Core_, page 134."
```

```encounter-table
name: Skin Shifter
creatures:
  - 1: Skin Shifter
```
