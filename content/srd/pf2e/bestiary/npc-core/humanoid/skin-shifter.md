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
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Wildsong|Wildsong]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +12, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +14, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +13, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +11, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +18, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +12, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +18"
abilityMods: [4, 2, 3, 0, 4, 1]
abilities_top:
  - name: "Animal Empathy"
    desc: "The skin shifter can ask questions of, receive answers from, and use the [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] skill with [[srd/pf2e/compendium/rules-elements/traits/player-core/animal|animals]]."
  - name: "Items"
    desc: "Hide Armor, _+1 [[srd/pf2e/compendium/equipment/runes/striking-major|striking]] [[srd/pf2e/compendium/equipment/weapons/bow/longbow|longbow]]_ (20 arrows), Spiked Gauntlet"
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
    desc: "⬻ spiked gauntlet +18 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/free-hand|Free-Hand]]) __Damage__ 1d4+10 piercing"
  - name: "Ranged"
    desc: "⬻ _longbow_ +17 ([[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly d10]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], range increment 100 feet, reload 0, [[srd/pf2e/compendium/rules-elements/traits/player-core/volley|volley 30 feet]]) __Damage__ 2d8+6 piercing"
abilities_bot:
  - name: "Gift of the Wild Spirits"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]])"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The skin shifter casts their choice of a 4th-rank [[srd/pf2e/compendium/spells/rank-4/aerial-form|_aerial form_]], [[srd/pf2e/compendium/spells/rank-2/animal-form|_animal form_]], [[srd/pf2e/compendium/spells/rank-4/dinosaur-form|_dinosaur form_]], or [[srd/pf2e/compendium/spells/rank-1/pest-form|_pest form_]] spell. They must transform into an animal of a kind they've seen within the last 24 hours. They can't gain temporary HP again from a spell cast with Gift of the Wild Spirits for 10 minutes. Their Strikes for forms other than _pest form_ have [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach]] 10 feet, a +20 attack modifier, and a +13 damage bonus (or a +9 damage bonus for aerial form). Most other changes to their statistics are listed above. While polymorphed, the skin shifter can still use Gift of the Wild Spirits, though they're still prevented from casting other spells as normal."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 26 - __Cantrips (4th)__ [[srd/pf2e/compendium/spells/cantrips/gouging-claw|Gouging Claw]], [[srd/pf2e/compendium/spells/cantrips/know-the-way|Know the Way]]"
sourcebook: "_NPC Core_, page 134."
```

```encounter-table
name: Skin Shifter
creatures:
  - 1: Skin Shifter
```
