---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Nanoshard Swarm"
tags:
  - pf2e/creature/level/9
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/metal
  - pf2e/creature/trait/swarm
  - pf2e/creature/trait/huge
statblock: inline
name: "Nanoshard Swarm"
level: 9
source: "Rage of Elements"
aon_id: "creature-2651"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2651"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "RoE"
name: "Nanoshard Swarm"
level: "Creature 9"
size: "Huge"
trait_01: "Elemental"
trait_02: "Metal"
trait_03: "Swarm"
modifier: 18
perception:
  - name: "Perception"
    desc: "Perception +18; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Talican|Talican]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +21, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +19, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +21"
abilityMods: [6, 6, 4, 3, 3, 3]
ac: 28
armorclass:
  - name: "AC"
    desc: "28; __Fort__: +17; __Ref__: +21; __Will__: +16"
hp: 120
health:
  - name: "HP"
    desc: "120; __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], precision, [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]], swarm mind; __Resistances__ bludgeoning 5, electricity 10, piercing 10, slashing 10; __Weaknesses__ area damage 10, [[srd/pf2e/compendium/rules-elements/traits/gm-core/splash|splash]] damage 10"
abilities_mid:
  - name: "Electromagnetic Dispersal"
    desc: "When a nanoshard swarm takes electricity damage, they automatically shift into swarm form."
speed: "none (barrier), 15 feet (battle), or 25 feet (swarm)"
attacks:
  - name: "Melee"
    desc: "⬻ tendril +19 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 60 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile B]]) __Damage__ 2d8+9 piercing"
  - name: "Melee"
    desc: "⬻ limb +19 (reach 20 feet) __Damage__ 4d8+9 bludgeoning"
abilities_bot:
  - name: "Barrier Form"
    desc: "⬽ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/polymorph|Polymorph]])"
  - name: "Requirements"
    desc: "The nanoshard swarm is in swarm form"
  - name: "Effect"
    desc: "The nanoshard swarm forms a continuous 6-inch-thick solid wall, up to 60 feet long and 10 feet high, originating from any one square in its current space. The wall can follow any path, with each 5 feet being placed on the border between squares. It doesn't need to stand vertically, so it can form a bridge or set of stairs, for example. The wall must be formed in an unbroken open space where its edges don't pass through any creatures or objects. A single 5-foot-by-5-foot section of the wall can be destroyed by dealing 18 points of damage to it, which also reduces the swarm's total Hit Points. A nanoshard swarm can't be knocked [[srd/pf2e/compendium/rules-elements/conditions#Prone|prone]] or forcibly moved while in barrier form, nor can it voluntarily move. A nanoshard swarm in barrier form can originate tendril attacks from any square of its wall."
  - name: "Battle Form"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/polymorph|Polymorph]])"
  - name: "Requirements"
    desc: "The nanoshard swarm is in swarm form"
  - name: "Effect"
    desc: "The nanoshard swarm coalesces into a Huge shape that looks like a humanoid or beast and can hold items. In battle form, its Speed is 15 feet, it's clumsy 1, and it has the following Strike."
  - name: "Swarm Form"
    desc: "⭓ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]]) The nanoshard swarm collapses into its natural form: a Huge sea of tiny metal spheres. It drops anything it's holding. While in swarm form, the nanoshard swarm's Speed is 25 feet, it can move through any area large enough for a single sphere to fit through without having to Squeeze, and it gains Engulf. Engulf⬺ DC 27, 2d8+6 bludgeoning, Escape DC 27, Rupture 18 Some Reassembly Required Nanoshard swarms are notoriously difficult to permanently dismantle. Should even a single constituent of a swarm manage to escape destruction, the minuscule elemental immediately seeks out the nearest source of raw metal and begins extracting material in order to create as many exact duplicates of itself as possible. Each subsequent duplicate then dutifully repeats the same behavior, doubling the number of constituents every few minutes, until the entire swarm has been fully reconstituted."
sourcebook: "_Rage of Elements_, page 157."
```

```encounter-table
name: Nanoshard Swarm
creatures:
  - 1: Nanoshard Swarm
```
