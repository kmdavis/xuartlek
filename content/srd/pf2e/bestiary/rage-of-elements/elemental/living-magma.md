---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Living Magma"
tags:
  - pf2e/creature/level/13
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/fire
  - pf2e/creature/trait/huge
statblock: inline
name: "Living Magma"
level: 13
source: "Rage of Elements"
aon_id: "creature-2635"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2635"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "RoE"
name: "Living Magma"
level: "Creature 13"
size: "Huge"
trait_01: "Elemental"
trait_02: "Fire"
modifier: 22
perception:
  - name: "Perception"
    desc: "Perception +22; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Pyric|Pyric]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +27, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +23, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +22"
abilityMods: [8, 5, 5, 4, 5, 4]
ac: 35
armorclass:
  - name: "AC"
    desc: "35; __Fort__: +26; __Ref__: +20; __Will__: +22"
hp: 250
health:
  - name: "HP"
    desc: "250; __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/cold|cold]] 15"
abilities_mid:
  - name: "Molten Form"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]]) Any creature that hits the living magma with an [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|unarmed]] Strike or otherwise touches it takes 10 fire damage. If a gallon or more of water touches the living magma, or if it's affected by a [[srd/pf2e/compendium/rules-elements/traits/player-core/water|water]] effect, its outer layer of lava hardens to a rocky shell, deactivating its molten form and imposing weakness 15 to bludgeoning damage. Molten form reactivates if the living magma swims in lava for 1 minute."
  - name: "Volcanic Heat"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]]) 40 feet. Any creature that enters or starts its turn in the aura takes 15 fire damage (DC 33 basic Fortitude save). A creature that fails its save is also enfeebled 1 until it's no longer in the aura."
  - name: "Trap Weapon"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]])"
  - name: "Frequency"
    desc: "once per round"
  - name: "Trigger"
    desc: "A creature hits the living magma with a melee weapon"
  - name: "Effect"
    desc: "The living magma attempts an [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] check against the triggering creature's Athletics DC. On a success, the living magma traps the weapon in its body and pulls it from the attacker's grasp. A creature can Interact to retrieve the weapon, but the attempt fails unless the creature succeeds at an Athletics check against the living magma's Fortitude DC (typically 36). If the living magma uses Engulf, it also absorbs all trapped weapons, rendering them unreachable until it dies."
speed: "40 feet, swim 60 feet (in lava only)"
attacks:
  - name: "Melee"
    desc: "⬻ magma fist +27 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 20 feet]]) __Damage__ 3d8+11 bludgeoning plus 3d6 fire plus 2d4 persistent fire"
abilities_bot:
  - name: "Engulf"
    desc: "⬺ DC 33, 2d10 bludgeoning plus 4d6 fire, Escape DC 33, Rupture 25"
  - name: "Launch Lava"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/fire|Fire]]) The living magma hurls an exploding glob of lava up to 120 feet. Each creature in a 10-foot burst takes 7d6 fire damage (DC 33 basic Reflex save)."
  - name: "Reignite"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/fire|Fire]])"
  - name: "Requirements"
    desc: "The living magma is not in molten form"
  - name: "Effect"
    desc: "The living magma returns to molten form."
sourcebook: "_Rage of Elements_, page 129."
```

```encounter-table
name: Living Magma
creatures:
  - 1: Living Magma
```
