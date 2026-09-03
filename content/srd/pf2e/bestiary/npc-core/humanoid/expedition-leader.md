---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Expedition Leader"
tags:
  - pf2e/creature/level/9
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Expedition Leader"
level: 9
source: "NPC Core"
aon_id: "creature-3478"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3478"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Expedition Leader"
level: "Creature 9"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 21
perception:
  - name: "Perception"
    desc: "Perception +21"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], Erutaki, [[srd/pf2e/compendium/rules-elements/languages#Skald|Skald]], [[srd/pf2e/compendium/rules-elements/languages#Tien|Tien]], Varki"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +20, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +20, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +18, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +19, [[srd/pf2e/compendium/rules-elements/skills/lore|Scouting Lore]] +21, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +18"
abilityMods: [4, 2, 4, 2, 3, 0]
abilities_top:
  - name: "Familiarity with the Land"
    desc: "The expedition leader isn't affected by [[srd/pf2e/books/gm-core/chapter-2-building-games/environment#Climate|severe weather]] and ignores difficult terrain."
  - name: "On Guard"
    desc: "When the expedition leader [[srd/pf2e/compendium/rules-elements/actions/player-core#Scout|Scouts]], they grant their party a +2 circumstance bonus to their initiative rolls."
  - name: "Items"
    desc: "Compass, four-person tent, _+1 [[srd/pf2e/compendium/equipment/armor#Hide Armor|hide armor]]_, hooded lantern, _+1 [[srd/pf2e/compendium/equipment/runes/striking-major|striking]] [[srd/pf2e/compendium/equipment/weapons/sword/machete-weapon-516|machete]]_, [[srd/pf2e/compendium/equipment/adventuring-gear/repair-toolkit-superb|Repair Toolkit]], Shortbow (20 arrows), Spyglass, [[srd/pf2e/compendium/equipment/adventuring-gear/sun-goggles|Sun Goggles]], Survey Map"
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +21; __Ref__: +18; __Will__: +15"
hp: 160
health:
  - name: "HP"
    desc: "160"
abilities_mid:
  - name: "Reactive Strike"
    desc: "⬲"
  - name: "Memories of Expeditions Past"
    desc: "⬲"
  - name: "Frequency"
    desc: "once per day"
  - name: "Trigger"
    desc: "The expedition leader fails a [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] check"
  - name: "Effect"
    desc: "The expedition leader rethinks their choices based on prior experience. The degree of success increases by one step, from critical failure to failure or from failure to success."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _machete_ +21 ([[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly d8]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sweep|Sweep]]) __Damage__ 2d6+10 slashing"
  - name: "Melee"
    desc: "⬻ fist +20 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+10 bludgeoning"
  - name: "Ranged"
    desc: "⬻ shortbow +19 ([[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly d10]], range increment 60 feet) __Damage__ 1d6+6 piercing"
abilities_bot:
  - name: "Quick Draw"
    desc: "⬻ The expedition leader Interacts to take out their machete or shortbow, then Strikes with the weapon. __Think Fast!__ ⬻"
  - name: "Requirements"
    desc: "The expedition leader has a hand free"
  - name: "Effect"
    desc: "The expedition leader scoops up a handful of rubble and throws it. Each creature in a 15-foot cone must succeed at a DC 27 Reflex save or be [[srd/pf2e/compendium/rules-elements/conditions#Dazzled|dazzled]] and [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] until the start of the expedition leader's next turn."
sourcebook: "_NPC Core_, page 58."
```

```encounter-table
name: Expedition Leader
creatures:
  - 1: Expedition Leader
```
