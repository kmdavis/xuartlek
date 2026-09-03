---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Kholo Outrider"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/kholo
  - pf2e/creature/trait/medium
  - pf2e/creature/trait/gnoll
statblock: inline
name: "Kholo Outrider"
level: 7
source: "NPC Core"
aon_id: "creature-3653"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3653"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Kholo Outrider"
level: "Creature 7"
size: "Medium"
trait_01: "Humanoid"
trait_02: "Kholo"
trait_03: "Gnoll"
modifier: 18
perception:
  - name: "Perception"
    desc: "Perception +18; low-light vision"
languages: "Common, Kholo"
skills:
  - name: "Skills"
    desc: "Acrobatics +13, Athletics +18, Intimidation +13, Stealth +15, Survival +18"
abilityMods: [4, 3, 2, 1, 3, 0]
abilities_top:
  - name: "Items"
    desc: "_+1 composite shortbow_ (20 arrows), _+1 hatchet_ (2), Hide Armor"
ac: 25
armorclass:
  - name: "AC"
    desc: "25; __Fort__: +14; __Ref__: +18; __Will__: +13"
hp: 120
health:
  - name: "HP"
    desc: "120"
abilities_mid:
  - name: "Reactive Strike"
    desc: "⬲"
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _hatchet_ +19 (Agile, Magical, Sweep) __Damage__ 1d6+7 slashing"
  - name: "Melee"
    desc: "⬻ jaws +18 __Damage__ 1d6+7 piercing"
  - name: "Ranged"
    desc: "⬻ _hatchet_ +17 (Agile, Magical, Sweep, thrown 10 feet) __Damage__ 1d6+7 slashing"
  - name: "Ranged"
    desc: "⬻ _composite shortbow_ +17 (deadly d10, Magical, Propulsive, range increment 60 feet, reload 0) __Damage__ 1d6+5 piercing"
abilities_bot:
  - name: "Bloody Flurry"
    desc: "⬺ The kholo outrider Strikes, Steps, then Strikes again. If the kholo outrider hits the same enemy with both Strikes, that enemy takes an additional 1d6 persistent bleed damage."
  - name: "Rugged Travel"
    desc: "A kholo ignores the first square of difficult terrain they move into each time they Step or Stride."
  - name: "Solo Hunter"
    desc: "A kholo outrider deals 1d6 extra damage while adjacent to at least 2 enemies and no allies."
sourcebook: "_NPC Core_, page 197."
```

```encounter-table
name: Kholo Outrider
creatures:
  - 1: Kholo Outrider
```
