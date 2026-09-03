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
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +13, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +12, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +12, [[srd/pf2e/compendium/rules-elements/skills/lore|Heraldry Lore]] +14, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +14, [[srd/pf2e/compendium/rules-elements/skills/lore|Warfare Lore]] +14"
abilityMods: [3, 2, 0, 2, 3, 2]
abilities_top:
  - name: "Items"
    desc: "Dagger, Half Plate, _+1 [[srd/pf2e/compendium/equipment/weapons/sword/longsword|longsword]]_, signet ring"
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
    desc: "The first time each day the veteran noble would be reduced to 0 HP, they remain at 1 HP and are [[srd/pf2e/compendium/rules-elements/conditions#Enfeebled|enfeebled 2]] for the rest of the day."
  - name: "Noble Pride"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]])"
  - name: "Trigger"
    desc: "An opponent attempts to [[srd/pf2e/compendium/rules-elements/actions/player-core#Demoralize|Demoralize]] the veteran noble or one of the noble's allies within 30 feet"
  - name: "Effect"
    desc: "The veteran noble attempts to Demoralize the triggering opponent before the opponent rolls. On a critical success, the triggering action is [[srd/pf2e/books/player-core/chapter-8-playing-the-game/actions#Disrupting Actions|disrupted]] as well."
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _longsword_ +16 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile P]]) __Damage__ 1d8+11 slashing"
  - name: "Melee"
    desc: "⬻ dagger +15 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 1d4+11 piercing"
  - name: "Melee"
    desc: "⬻ gauntlet +15 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/free-hand|Free-Hand]]) __Damage__ 1d4+11 bludgeoning"
  - name: "Ranged"
    desc: "⬻ dagger +15 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 1d4+11 piercing"
abilities_bot:
  - name: "Tactical Command"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/linguistic|Linguistic]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]])"
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
