---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Subaquatic Marauder"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/medium
statblock: inline
name: "Subaquatic Marauder"
level: 5
source: "NPC Core"
aon_id: "creature-3603"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3603"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Subaquatic Marauder"
level: "Creature 5"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: "Uncommon"
modifier: 12
perception:
  - name: "Perception"
    desc: "Perception +12"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +13, [[srd/pf2e/compendium/rules-elements/skills/crafting|Crafting]] +13, [[srd/pf2e/compendium/rules-elements/skills/lore|Ocean Lore]] +12"
abilityMods: [4, 2, 4, 2, 1, 0]
abilities_top:
  - name: "Sealed Diving Suit"
    desc: "The marauder's diving suit is a technological marvel. When sealed, it provides 1 hour of fresh air and protects the wearer from exposure to [[srd/pf2e/compendium/rules-elements/traits/gm-core/inhaled|inhaled]] threats. Personalized modifications and a need for constant tinkering mean that other creatures are unable to take advantage of the special abilities of the diving suit and treat it as an ordinary suit of half plate."
  - name: "Items"
    desc: "Chain (30 feet), diving suit (functions as [[srd/pf2e/compendium/equipment/armor#Half Plate|half plate]]), Gauntlet, Javelin"
ac: 23
armorclass:
  - name: "AC"
    desc: "23; __Fort__: +15; __Ref__: +7; __Will__: +12"
hp: 60
health:
  - name: "HP"
    desc: "60; __Immunities__ gases and other [[srd/pf2e/compendium/rules-elements/traits/gm-core/inhaled|inhaled]] effects"
speed: "20 feet, swim 20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ gauntlet +15 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/free-hand|Free-Hand]]) __Damage__ 1d4+8 bludgeoning"
  - name: "Ranged"
    desc: "⬻ javelin +15 (range 30 feet, [[srd/pf2e/compendium/rules-elements/traits/player-core-2/tethered|Tethered]]) __Damage__ 1d6+8 piercing"
abilities_bot:
  - name: "Depth Charge"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/air|Air]], [[srd/pf2e/compendium/rules-elements/traits/player-core/manipulate|Manipulate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sonic|Sonic]]) The marauder pulls a release valve on their suit, expelling a pressure wave that deals 3d6 sonic and 3d6 bludgeoning damage (DC 22 basic Fortitude save) to all creatures in a 10-foot emanation. Creatures that fail the save take a –2 circumstance penalty to [[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] checks to [[srd/pf2e/compendium/rules-elements/actions/player-core#Balance|Balance]] and [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] checks to [[srd/pf2e/compendium/rules-elements/actions/player-core#Swim|Swim]] for 1 minute as their inner ear is impaired. Creatures that critically fail the save are also [[srd/pf2e/compendium/rules-elements/conditions#Deafened|deafened]] for 1 minute. The marauder can't use Depth Charge again for 1d4 rounds."
  - name: "Retract"
    desc: "⬻"
  - name: "Requirements"
    desc: "The marauder's last action was a successful javelin strike"
  - name: "Effect"
    desc: "The marauder reels in a chain connected to the javelin, pulling the target up to 10 feet closer. They then Interact to return the javelin to their hand."
sourcebook: "_NPC Core_, page 149."
```

```encounter-table
name: Subaquatic Marauder
creatures:
  - 1: Subaquatic Marauder
```
