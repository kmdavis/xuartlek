---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Deific Champion of Iomedae"
tags:
  - pf2e/creature/level/12
  - pf2e/creature/trait/holy
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/medium
statblock: inline
name: "Deific Champion of Iomedae"
level: 12
source: "NPC Core"
aon_id: "creature-3450"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3450"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Deific Champion of Iomedae"
level: "Creature 12"
size: "Medium"
trait_01: "Holy"
trait_02: "Human"
trait_03: "Humanoid"
trait_04: "Rare"
modifier: 19
perception:
  - name: "Perception"
    desc: "Perception +19"
languages: "Common, Empyrean"
skills:
  - name: "Skills"
    desc: "Athletics +25, Diplomacy +22, Intimidation +26, Religion +23"
abilityMods: [5, 2, 2, 0, 3, 4]
abilities_top:
  - name: "Blessed Shield"
    desc: "In the deific champion's hands, a shield gains the _moderate reinforcing rune_, giving it Hardness 8, 84 HP, and BT 42."
  - name: "Deific Reactions"
    desc: "At the start of each of their turns, the deific champion gains an additional reaction they can only use to make a Reactive Strike or to Shield Block."
  - name: "Items"
    desc: "_+1 striking crossbow_ (20 bolts), _+1 resilient full plate_, _+1 striking longsword_, _potion of flying_, religious symbol of Iomedae, Steel Shield"
ac: 33
armorclass:
  - name: "AC"
    desc: "33; __Fort__: +23; __Ref__: +19; __Will__: +22"
hp: 220
health:
  - name: "HP"
    desc: "220"
abilities_mid:
  - name: "Champion's Aura"
    desc: "(aura, divine) 15 feet. Any follower of Iomedae in the aura knows the champion is a champion of Iomedae. At the end of the champion's turn, each ally in the aura reduces its frightened value by 1. The aura can be suppressed or resumed with a single action, which has the concentrate trait, and ends if the champion falls unconscious."
  - name: "Champion's Courage"
    desc: "When the champion becomes frightened, they reduce the condition value by 1 (to a minimum of 0)."
  - name: "Exalted Retributive Strike"
    desc: "⬲ (divine)"
  - name: "Trigger"
    desc: "An enemy damages the deific champion's ally, and both are in the deific champion's aura"
  - name: "Effect"
    desc: "The ally gains resistance 14 to all damage against the triggering damage. If the enemy is within reach, the deific champion makes a melee Strike against it. Each ally in the champion's aura can spend a reaction to Strike the target with a –5 penalty."
  - name: "Reactive Strike"
    desc: "⬲"
  - name: "Shield Block"
    desc: "⬲"
  - name: "Will Not Fall"
    desc: "⭓ Trigger The deific champion's Hit Points are reduced to 0 for the first time that day; Effect The champion presses on, refusing to fail their god. They remain standing with 25 Hit Points."
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _longsword_ +26 (Magical, versatile P) __Damage__ 2d8+13 slashing"
  - name: "Melee"
    desc: "⬻ fist +25 (Agile, Nonlethal, Unarmed) __Damage__ 1d4+13 bludgeoning"
  - name: "Ranged"
    desc: "⬻ _crossbow_ +23 (Magical, range 120 feet, reload 1) __Damage__ 2d8+5 piercing"
abilities_bot:
  - name: "Champion Devotion Spells"
    desc: "DC 30, 2 Focus Points - __6th__ Champion's Sacrifice, Lay on Hands"
  - name: "Will Not Falter"
    desc: "⬺"
  - name: "Effect"
    desc: "The deific champion declares their devotion to their deity and their cause. They Stride, then make a melee Strike. If the Strike hits an enemy, all allies within their champion's aura gain a +2 status bonus to attack rolls and saving throws against fear until the start of the deific champion's next turn."
sourcebook: "_NPC Core_, page 36."
```

```encounter-table
name: Deific Champion of Iomedae
creatures:
  - 1: Deific Champion of Iomedae
```
