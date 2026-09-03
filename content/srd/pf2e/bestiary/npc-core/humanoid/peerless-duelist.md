---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Peerless Duelist"
tags:
  - pf2e/creature/level/12
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Peerless Duelist"
level: 12
source: "NPC Core"
aon_id: "creature-3512"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3512"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Peerless Duelist"
level: "Creature 12"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 24
perception:
  - name: "Perception"
    desc: "Perception +24; (27 for initiative) tremorsense 30 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +25, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +23, [[srd/pf2e/compendium/rules-elements/skills/crafting|Crafting]] +22, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +24, [[srd/pf2e/compendium/rules-elements/skills/lore|Dueling Lore]] +25, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +26"
abilityMods: [3, 5, 3, 0, 3, 2]
abilities_top:
  - name: "I See You"
    desc: "The peerless duelist's Perception checks and firearm Strikes ignore lesser cover and the [[srd/pf2e/compendium/rules-elements/conditions#Concealed|concealed]] condition."
  - name: "Items"
    desc: "[[srd/pf2e/compendium/equipment/worn-items/obsidian-goggles-major|_obsidian goggles_]], _+1 [[srd/pf2e/compendium/equipment/runes/striking-major|striking]] [[srd/pf2e/compendium/equipment/weapons/firearm/dueling-pistol-weapon-520|dueling pistol]]_ ( 2, 40 rounds)"
ac: 33
armorclass:
  - name: "AC"
    desc: "33; __Fort__: +21; __Ref__: +25; __Will__: +21"
hp: 200
health:
  - name: "HP"
    desc: "200"
abilities_mid:
  - name: "Threatening Aura"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]]) 60 feet, Will DC 30. The duelist's presence makes foes hesitate. Any enemy that enters or starts its turn in the aura must succeed at the Will save or be [[srd/pf2e/compendium/rules-elements/conditions#Stunned|stunned 1]]. Regardless of the result of its save, the creature is temporarily immune for 1 day."
  - name: "Shoot First"
    desc: "⬲"
  - name: "Trigger"
    desc: "An attacker the duelist can see targets them with a Strike or spell"
  - name: "Requirement"
    desc: "The duelist is holding a loaded firearm"
  - name: "Effect"
    desc: "The duelist makes a firearm Strike against the triggering creature. On a critical hit, they disrupt the triggering action."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +25 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+11 bludgeoning"
  - name: "Ranged"
    desc: "⬻ _dueling pistol_ +26 ([[srd/pf2e/compendium/rules-elements/traits/player-core/concealable|Concealable]], [[srd/pf2e/compendium/rules-elements/traits/npc-core/concussive|Concussive]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fatal|fatal d10]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], range increment 60 feet, reload 1) __Damage__ 3d6+13 piercing"
abilities_bot:
  - name: "Ace Shooter"
    desc: "The peerless duelist deals an extra die of damage on any firearm Strike they attempt. This extra damage is already included in their dueling pistol Strike."
  - name: "Disarming Shot"
    desc: "⬻ The duelist fires a dueling pistol to attempt a [[srd/pf2e/compendium/rules-elements/actions/player-core#Disarm|Disarm]] an enemy at range with the bullet. The duelist attempts an attack roll with the dueling pistol instead of an [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] check, taking any penalty appropriate for the firearm's range increment. The duelist doesn't have to meet the requirements of the Disarm action. Instead of Disarming, the duelist can use Disarming Shot to attempt an [[srd/pf2e/compendium/rules-elements/actions/player-core#Escape|Escape]] action for the benefit of themself or an ally within range."
  - name: "Double Reload"
    desc: "⬻"
  - name: "Requirements"
    desc: "The peerless duelist has an empty dueling pistol in each hand"
  - name: "Effect"
    desc: "The peerless duelist Interacts to reload both dueling pistols."
sourcebook: "_NPC Core_, page 80."
```

```encounter-table
name: Peerless Duelist
creatures:
  - 1: Peerless Duelist
```
