---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Elder Outcrop"
tags:
  - pf2e/creature/level/13
  - pf2e/creature/trait/earth
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/huge
statblock: inline
name: "Elder Outcrop"
level: 13
source: "Rage of Elements"
aon_id: "creature-2626"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2626"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "RoE"
name: "Elder Outcrop"
level: "Creature 13"
size: "Huge"
trait_01: "Earth"
trait_02: "Elemental"
modifier: 26
perception:
  - name: "Perception"
    desc: "Perception +26; darkvision, tremorsense 120 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Fey|Fey]], [[srd/pf2e/compendium/rules-elements/languages#Petran|Petran]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +29, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +25, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +26, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +26"
abilityMods: [8, -2, 8, 1, 5, 4]
ac: 33
armorclass:
  - name: "AC"
    desc: "33; __Fort__: +29; __Ref__: +19; __Will__: +26"
hp: 295
health:
  - name: "HP"
    desc: "295; __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]"
abilities_mid:
  - name: "Dust Eternal"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/earth|earth]]) 30 feet. Dust swirls about the outcrop, rendering everything within its aura (including the outcrop) [[srd/pf2e/compendium/rules-elements/conditions#Concealed|concealed]]. In addition, the dust at the outcrop's base creates difficult terrain on the ground within the aura. The outcrop can activate or deactivate this aura using a single action, which has the [[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|concentrate]] trait."
  - name: "Unstoppable"
    desc: "The elder outcrop's [[srd/pf2e/compendium/rules-elements/conditions#Slowed|slowed]] condition can't exceed slowed 1, and it ignores penalties to its Speeds and the [[srd/pf2e/compendium/rules-elements/conditions#Immobilized|immobilized]] condition."
speed: "30 feet, burrow 30 feet; earth glide"
attacks:
  - name: "Melee"
    desc: "⬻ column +27 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 3d10+14 bludgeoning plus Knockdown"
  - name: "Ranged"
    desc: "⬻ rock +27 (Brutal, range increment 120 feet) __Damage__ 3d6+14 bludgeoning plus call of earth"
abilities_bot:
  - name: "Call of Earth"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]]) A flying creature hit by the elder outcrop's rock ranged strike is affected by a 7th-rank _earthbind_ spell (DC 33)."
  - name: "Earth Glide"
    desc: "The elder outcrop can Burrow through any earthen matter, including rock. When it does so, the elder outcrop moves at its full burrow Speed, leaving no tunnels or signs of its passing."
  - name: "Natural Formation"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]]) Until the next time it acts, the elder outcrop appears to be a natural terrain feature. It has an automatic result of 47 on [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] checks and DCs to pass as a natural outcropping of rock. The outcrop's dust eternal aura is deactivated while Natural Formation is being used."
  - name: "Stone Grip"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/earth|Earth]], [[srd/pf2e/compendium/rules-elements/traits/player-core/incapacitation|Incapacitation]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]]) Great fingers of stone arise to grasp up to two Medium or smaller creatures on the ground in the outcrop's aura. Each target must succeed at a DC 33 Reflex save or be [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] by the stone hand (or [[srd/pf2e/compendium/rules-elements/conditions#Restrained|restrained]] on a critical failure; Escape DC 33). A creature grabbed or restrained by a stone hand at the end of its turn becomes slowed 1 or increases its existing slowed condition by 1. When a creature is unable to act due to the slowed condition from this effect, the creature is permanently [[srd/pf2e/compendium/rules-elements/conditions#Petrified|petrified]]."
  - name: "Throw Rock"
    desc: "⬻ Wisdom of Stone Elder outcrops learn a lesson for every grain of rock eroded away, every squall and freeze that has shaped their craggy bodies. As wizened advisors and tutors, they have the respect and affection of other elementals, as well as from natural creatures. Druids of the stone order revere the wisdom of elder outcrops, always happy to receive their wide perspective, literal and philosophical."
sourcebook: "_Rage of Elements_, page 105."
```

```encounter-table
name: Elder Outcrop
creatures:
  - 1: Elder Outcrop
```
