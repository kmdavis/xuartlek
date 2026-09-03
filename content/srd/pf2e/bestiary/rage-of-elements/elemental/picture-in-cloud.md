---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Picture-in-Cloud"
tags:
  - pf2e/creature/level/13
  - pf2e/creature/trait/air
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/huge
statblock: inline
name: "Picture-in-Cloud"
level: 13
source: "Rage of Elements"
aon_id: "creature-2619"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2619"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "RoE"
name: "Picture-in-Cloud"
level: "Creature 13"
size: "Huge"
trait_01: "Air"
trait_02: "Elemental"
modifier: 20
perception:
  - name: "Perception"
    desc: "Perception +20; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Sussuran|Sussuran]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +26, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +24"
abilityMods: [4, 8, 5, 4, 4, 4]
ac: 35
armorclass:
  - name: "AC"
    desc: "35; __Fort__: +21; __Ref__: +26; __Will__: +19"
hp: 175
health:
  - name: "HP"
    desc: "175; __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]"
abilities_mid:
  - name: "High Winds"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/air|air]], [[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]]) 60 feet. Air within the emanation is difficult terrain for Flying creatures that don't have the [[srd/pf2e/compendium/rules-elements/traits/player-core/air|air]] trait."
  - name: "Disperse"
    desc: "⬲"
  - name: "Trigger"
    desc: "The picture-in-clouds takes damage from a hostile action"
  - name: "Effect"
    desc: "The picture-inclouds disperses. Until the end of the current turn, they can't be attacked or targeted, they don't take up space, and any auras or emanations they have are suppressed. At the end of the turn, the picture-in-clouds re-forms in any sufficient space within 150 feet of where they dispersed; any auras or emanations they have are restored as long as the duration didn't run out while the elemental was dispersed."
speed: "fly 100 feet; swiftness"
attacks:
  - name: "Melee"
    desc: "⬻ gust +26 ([[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 20 feet]]) __Damage__ 3d10+10 bludgeoning plus Push 15 feet"
  - name: "Ranged"
    desc: "⬻ lightning lash +26 (range increment 100 feet) __Damage__ 3d12 electricity"
abilities_bot:
  - name: "Cloudgaze"
    desc: "⬻ The picture-in-clouds shifts into their choice of an eagle shape, elephant shape, or sword shape."
  - name: "Elephant Blast"
    desc: "⬺"
  - name: "Requirements"
    desc: "The picture-in-clouds is in elephant shape"
  - name: "Effect"
    desc: "The picture-in-clouds breathes out a 30-foot cone of air from their cloudy trunk. Creatures in the area must attempt a DC 30 Fortitude save to stand their ground. A creature pushed into a solid object stops moving and takes 4d10 bludgeoning damage."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature is pushed 20 feet."
  - name: "Failure"
    desc: "The creature is pushed 40 feet."
  - name: "Critical Failure"
    desc: "The creature is pushed 40 feet and knocked [[srd/pf2e/compendium/rules-elements/conditions#Prone|prone]]."
  - name: "Feather Storm"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/move|Move]])"
  - name: "Requirements"
    desc: "The picture-in-clouds is in eagle shape"
  - name: "Effect"
    desc: "The picture-in-clouds Flies 125 feet, flapping their wings and creating a barrier along their path. This barrier has the effects of _wall of wind_ (DC 30) and lasts until the end of the picture-in-clouds's next turn."
  - name: "Slicing Wind"
    desc: "⬻"
  - name: "Requirements"
    desc: "The picture-in-clouds is in sword shape"
  - name: "Effect"
    desc: "The picture-in-clouds spins, forming a whirlwind that deals 5d8 slashing damage in a 15-foot emanation (DC 30 basic Reflex save)."
  - name: "Swiftness"
    desc: "The picture-in-clouds's movement doesn't trigger reactions."
sourcebook: "_Rage of Elements_, page 83."
```

```encounter-table
name: Picture-in-Cloud
creatures:
  - 1: Picture-in-Cloud
```
