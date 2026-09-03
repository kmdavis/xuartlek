---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Sacristan"
tags:
  - pf2e/creature/level/10
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/velstrac
  - pf2e/creature/trait/medium
statblock: inline
name: "Sacristan"
level: 10
source: "Monster Core 2"
aon_id: "creature-4609"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4609"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Sacristan"
level: "Creature 10"
size: "Medium"
trait_01: "Fiend"
trait_02: "Unholy"
trait_03: "Velstrac"
modifier: 19
perception:
  - name: "Perception"
    desc: "Perception +19; greater darkvision, painsight"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/languages#Shadowtongue|Shadowtongue]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +19, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +22, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +18, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +21, [[srd/pf2e/compendium/rules-elements/skills/lore|Torture Lore]] +16"
abilityMods: [6, 5, 6, 0, 3, 2]
abilities_top:
  - name: "Painsight"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]]) A velstrac automatically knows whether a creature it sees has any of the [[srd/pf2e/compendium/rules-elements/conditions#Doomed|doomed]], [[srd/pf2e/compendium/rules-elements/conditions#Dying|dying]], and [[srd/pf2e/compendium/rules-elements/conditions#Wounded|wounded]] conditions as well as the value of those conditions."
ac: 30
armorclass:
  - name: "AC"
    desc: "30; __Fort__: +22; __Ref__: +19; __Will__: +17 +1 status to all saves vs. magic"
hp: 175
health:
  - name: "HP"
    desc: "175 , regeneration 10 (deactivated by [[srd/pf2e/compendium/rules-elements/traits/player-core/holy|holy]] or [[srd/pf2e/compendium/equipment/materials/silver-object-high-grade|silver]]); __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/cold|cold]]; __Weaknesses__ holy 10, silver 10"
abilities_mid:
  - name: "Staggering Servitude"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/visual|visual]]) 30 feet. When a creature ends its turn in the aura, it sees a vision of the sacristan groveling in pitiable servitude. The creature must succeed at a DC 27 Will save or become [[srd/pf2e/compendium/rules-elements/conditions#Stunned|stunned]] 1."
  - name: "Reactive Strike"
    desc: "⬲"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ barbed chain +22 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/trip|trip]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|unholy]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 2d8+9 piercing plus 1d6 spirit and 2d6 [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|persistent bleed]]"
abilities_bot:
  - name: "Focus Gaze"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/visual|visual]]) The sacristan eerily stares at a creature they can see within 30 feet. The creature must immediately attempt a Will save against staggering servitude. In addition, if the creature was already [[srd/pf2e/compendium/rules-elements/conditions#Stunned|stunned]], on a failed save, its revulsion toward the sacristan's presence causes it to be [[srd/pf2e/compendium/rules-elements/conditions#Stupefied|stupefied]] 2 for 1 minute. After attempting this save, the creature is then temporarily immune to Focus Gaze until the start of the sacristan's next turn."
  - name: "Shadow Scream"
    desc: "⬽ ([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|Aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/darkness|darkness]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/monster-core/oni|sonic]])"
  - name: "Frequency"
    desc: "once per hour"
  - name: "Effect"
    desc: "The sacristan opens their mouth to unloose the wailing howls and mind-twisting darkness of [[srd/pf2e/compendium/gm/planes#The Netherworld|the Netherworld]]. This creates a 30- foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Emanation|emanation]] of darkness and wailing sounds around the sacristan. Creatures with darkvision can't see through this darkness. The sacristan can [[srd/pf2e/compendium/rules-elements/actions/player-core#Sustain an Effect|Sustain]] Shadow Scream for up to 1 minute. Non-velstrac creatures in the area when the ability is used, as well as those who enter or start their turn in the area, must attempt a DC 28 Will save."
  - name: "Critical Success"
    desc: "The creature is unaffected and is then temporarily immune for 24 hours."
  - name: "Success"
    desc: "The creature is [[srd/pf2e/compendium/rules-elements/conditions#Deafened|deafened]] for 1 round."
  - name: "Failure"
    desc: "The creature is [[srd/pf2e/compendium/rules-elements/conditions#Confused|confused]] and deafened for 1 round."
  - name: "Critical Failure"
    desc: "The creature takes 20 mental damage, and is confused and deafened for 1 round."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 29 - __3rd__ [[srd/pf2e/compendium/spells/rank-1/fear|Fear]] - __5th__ [[srd/pf2e/compendium/spells/rank-3/chilling-darkness|Chilling Darkness]]"
sourcebook: "_Monster Core 2_, page 347."
```

```encounter-table
name: Sacristan
creatures:
  - 1: Sacristan
```
