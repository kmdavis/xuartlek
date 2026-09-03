---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Veldenar"
tags:
  - pf2e/creature/level/11
  - pf2e/creature/trait/air
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/huge
statblock: inline
name: "Veldenar"
level: 11
source: "Rage of Elements"
aon_id: "creature-2621"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2621"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "RoE"
name: "Veldenar"
level: "Creature 11"
size: "Huge"
trait_01: "Air"
trait_02: "Elemental"
modifier: 24
perception:
  - name: "Perception"
    desc: "Perception +24; all-around vision, darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Sussuran|Sussuran]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +20, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +20, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +23"
abilityMods: [7, 5, 5, -2, 2, 0]
ac: 32
armorclass:
  - name: "AC"
    desc: "32; __Fort__: +24; __Ref__: +21; __Will__: +18"
hp: 190
health:
  - name: "HP"
    desc: "190; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/cold|cold]]; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/electricity|electricity]] 10; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]] 10"
abilities_mid:
  - name: "Natural Invisibility"
    desc: "A veldenar is naturally [[srd/pf2e/compendium/rules-elements/conditions#Invisible|invisible]] and only becomes visible when using a hostile action. Creatures it has engulfed remain visible within it, albeit slightly blurred by the veldenar's translucent skin."
  - name: "Viscous Breath"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/air|air]], [[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]]) 15 feet. The veldenar raises the viscosity of the surrounding air just by breathing it. Creatures who enter or start their turn within the emanation treat the area as difficult terrain and take a –2 status penalty to any non-magical physical attacks they attempt. This aura is suppressed whenever the veldenar has a creature engulfed."
  - name: "Reactive Strike"
    desc: "⬲"
speed: "25 feet, fly 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ tongue +25 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 2d10+10 bludgeoning plus 1d10 cold"
abilities_bot:
  - name: "Vacuum"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/air|Air]])"
  - name: "Requirements"
    desc: "The veldenar doesn't have a creature engulfed"
  - name: "Effect"
    desc: "The veldenar forcefully unlocks then expands its jaws to inhale the air in a 15-foot cone before it, pulling Large or smaller creatures into its cavernous maw. The veldenar Engulfs the creatures in the area (DC 27, 1d10+10 cold, Escape DC 27, Rupture 25). Paired Predators Veldenars bond in partnership for life, which can be well over a century. Utilizing their ambush pack tactics, one veldenar will often drive potential prey into their partner's clutches. Visitors to the [[srd/pf2e/compendium/gm/planes#Plane of Air|Plane of Air]] should keep in mind that if they happen to spot one veldenar, another is likely close by."
sourcebook: "_Rage of Elements_, page 85."
```

```encounter-table
name: Veldenar
creatures:
  - 1: Veldenar
```
