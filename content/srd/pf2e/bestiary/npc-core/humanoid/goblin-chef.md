---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Goblin Chef"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/goblin
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/small
statblock: inline
name: "Goblin Chef"
level: 1
source: "NPC Core"
aon_id: "creature-3640"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3640"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Goblin Chef"
level: "Creature 1"
size: "Small"
trait_01: "Goblin"
trait_02: "Humanoid"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Goblin|Goblin]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/lore|Cooking Lore]] +10, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +7, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +4, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +6, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +7"
abilityMods: [1, 1, 3, 2, 2, 0]
abilities_top:
  - name: "Good Enough to Eat"
    desc: "The goblin chef can turn otherwise inedible items into meals for others. They can provide food for any number of creatures without using the [[srd/pf2e/compendium/rules-elements/actions/player-core#Subsist|Subsist]] downtime activity as long as garbage is readily available. A non-[[srd/pf2e/compendium/rules-elements/traits/player-core/goblin|goblin]] who eats the goblin chef's food must attempt a DC 14 Fortitude save. On a failure, they suffer an upset stomach for 1 day; if they attempt to willingly ingest anything else during that period, they must first succeed at a DC 4 flat check or the action is [[srd/pf2e/books/player-core/chapter-8-playing-the-game/actions#Disrupting Actions|disrupted]]."
  - name: "Kitchen Specialist"
    desc: "For encounters involving cooking, a goblin chef is a 3rd-level challenge."
  - name: "Items"
    desc: "cleaver (functions as [[srd/pf2e/compendium/equipment/weapons/sword/dogslicer|dogslicer]]), leather apron (functions as [[srd/pf2e/compendium/equipment/armor#Leather Armor|leather armor]]), pickles (6)"
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +10; __Ref__: +6; __Will__: +5 +2 circumstance bonus against [[srd/pf2e/compendium/rules-elements/traits/gm-core/ingested|ingested]] [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poisons]]"
hp: 24
health:
  - name: "HP"
    desc: "24; __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Sickened|sickened]]"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d6+1 piercing"
  - name: "Melee"
    desc: "⬻ cleaver +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/backstabber|Backstabber]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]]) __Damage__ 1d4+1 slashing"
abilities_bot:
  - name: "Eat a Pickle"
    desc: "⬺"
  - name: "Effect"
    desc: "The goblin chef draws a pickle and eats it or feeds it to an adjacent ally. The chef or ally gains 4 temporary Hit Points and ignores any penalties from [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|emotion]] effects or [[srd/pf2e/compendium/rules-elements/conditions#Fatigued|fatigued]] for 1 round."
sourcebook: "_NPC Core_, page 186."
```

```encounter-table
name: Goblin Chef
creatures:
  - 1: Goblin Chef
```
