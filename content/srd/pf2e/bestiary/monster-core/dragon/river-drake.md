---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "River Drake"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/amphibious
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/water
  - pf2e/creature/trait/medium
statblock: inline
name: "River Drake"
level: 3
source: "Monster Core"
aon_id: "creature-2958"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2958"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "River Drake"
level: "Creature 3"
size: "Medium"
trait_01: "Amphibious"
trait_02: "Dragon"
trait_03: "Water"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9; darkvision, scent (imprecise) 30 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Draconic|Draconic]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +11, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +10, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +6, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +9, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +7"
abilityMods: [3, 4, 2, -1, 2, -1]
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +11; __Ref__: +9; __Will__: +7"
hp: 45
health:
  - name: "HP"
    desc: "45; __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/acid|acid]] 10"
abilities_mid:
  - name: "Tail Lash"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature within reach of the river drake's tail uses an action to Strike or attempt a skill check"
  - name: "Effect"
    desc: "The river drake attempts to Strike the triggering creature with their tail. If it hits, the target takes a –2 circumstance penalty to the triggering roll."
speed: "20 feet, fly 50 feet, swim 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fangs +12 __Damage__ 2d8+3 piercing"
  - name: "Melee"
    desc: "⬻ tail +12 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 2d6+3 bludgeoning"
abilities_bot:
  - name: "Caustic Mucus"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/acid|Acid]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]]) The river drake spits a ball of caustic mucus up to a range of 50 feet that explodes in a 10-foot burst. Creatures within the burst take 4d6 acid damage (DC 19 basic Reflex save). Those that fail this save also take 1d6 persistent acid damage and take a –5-foot status penalty to their Speed. This Speed reduction ends with the persistent acid damage. The river drake can't use Caustic Mucus again for 1d6 rounds."
  - name: "Draconic Frenzy"
    desc: "⬺ The river drake makes one fangs Strike and two tail Strikes in any order."
  - name: "Speed Surge"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/move|Move]])"
  - name: "Frequency"
    desc: "three times per day"
  - name: "Effect"
    desc: "The river drake Strides or Flies twice."
sourcebook: "_Monster Core_, page 129."
```

```encounter-table
name: River Drake
creatures:
  - 1: River Drake
```
