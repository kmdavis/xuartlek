---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Toady"
tags:
  - pf2e/creature/level/0
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Toady"
level: 0
source: "NPC Core"
aon_id: "creature-3607"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3607"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Toady"
level: "Creature 0"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 3
perception:
  - name: "Perception"
    desc: "Perception +3; (9 to eavesdrop)"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]; one additional language spoken by their boss"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +4, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +2, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +6, [[srd/pf2e/compendium/rules-elements/skills/thievery|Thievery]] +4"
abilityMods: [2, 2, 3, -1, 1, 0]
abilities_top:
  - name: "Master Sends Their Regards"
    desc: "A toady can deliver a message from their boss to [[srd/pf2e/compendium/rules-elements/actions/player-core#Demoralize|Demoralize]] using their boss's Intimidation modifier instead of their own."
  - name: "Items"
    desc: "Sap, supplies for the boss"
ac: 14
armorclass:
  - name: "AC"
    desc: "14; __Fort__: +9; __Ref__: +6; __Will__: +3"
hp: 20
health:
  - name: "HP"
    desc: "20; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]] 2"
abilities_mid:
  - name: "Human Shield"
    desc: "⬲"
  - name: "Trigger"
    desc: "The toady's boss takes damage from an attack, and the toady is adjacent to them"
  - name: "Effect"
    desc: "The toady takes the damage instead, along with any secondary effects of attack. This damage can't be reduced in any way."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ sap +6 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]]) __Damage__ 1d6+2 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +6 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+2 bludgeoning"
abilities_bot:
  - name: "Scurry"
    desc: "⬻ The toady Strides, then can [[srd/pf2e/compendium/rules-elements/actions/player-core#Hide|Hide]]. They can attempt to Hide from creatures without cover or being [[srd/pf2e/compendium/rules-elements/conditions#Concealed|concealed]], but at a –2 circumstance penalty."
  - name: "Throw Cargo"
    desc: "⬺ A toady carries a heavy load of supplies at their boss's behest. They hurl a heavy item they're carrying, which explodes on impact to deal 1d10 bludgeoning damage to all creatures in a 5-foot burst with a DC 14 basic Reflex save. Perks Of The Job A toady who works for a powerful boss may be granted special abilities or gifts. For example, a high-level spellcaster might give them a [[srd/pf2e/compendium/spells/rank-5/sending|_wand of sending_]], or an assassin may give them a single dose of a deadly poison to use on a problematic enemy."
sourcebook: "_NPC Core_, page 152."
```

```encounter-table
name: Toady
creatures:
  - 1: Toady
```
