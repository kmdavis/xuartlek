---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Hippopotamus"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/large
statblock: inline
name: "Hippopotamus"
level: 5
source: "Monster Core 2"
aon_id: "creature-4438"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4438"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Hippopotamus"
level: "Creature 5"
size: "Large"
trait_01: "Animal"
modifier: 11
perception:
  - name: "Perception"
    desc: "Perception +11; low-light vision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +13, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +11, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +11"
abilityMods: [6, 2, 6, -4, 4, -2]
abilities_top:
  - name: "Deep Breath"
    desc: "The hippopotamus can hold its breath for 5 minutes."
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +15; __Ref__: +9; __Will__: +11"
hp: 85
health:
  - name: "HP"
    desc: "85"
speed: "25 feet, swim 20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +15 ([[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly d10]]) __Damage__ 2d8+8 piercing"
  - name: "Melee"
    desc: "⬻ foot +15 __Damage__ 1d10+8 bludgeoning"
abilities_bot:
  - name: "Aquatic Ambush"
    desc: "⬻ 30 feet"
  - name: "Capsize"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/attack|Attack]]) The hippopotamus tries to capsize an adjacent aquatic vessel of its size or smaller. The hippopotamus must succeed at an [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] check with a DC of 25 (reduced by 5 for each size smaller the vessel is than the hippo) or the pilot's [[srd/pf2e/compendium/rules-elements/skills/lore|Sailing Lore]] DC, whichever is higher."
  - name: "Trample"
    desc: "⬽ Medium or smaller, foot, DC 22"
sourcebook: "_Monster Core 2_, page 191."
```

```encounter-table
name: Hippopotamus
creatures:
  - 1: Hippopotamus
```
