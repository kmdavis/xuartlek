---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Air Wisp"
tags:
  - pf2e/creature/level/0
  - pf2e/creature/trait/air
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/tiny
statblock: inline
name: "Air Wisp"
level: 0
source: "Monster Core 2"
aon_id: "creature-4394"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4394"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Air Wisp"
level: "Creature 0"
size: "Tiny"
trait_01: "Air"
trait_02: "Elemental"
modifier: 6
perception:
  - name: "Perception"
    desc: "Perception +6; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Sussuran|Sussuran]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +7, [[srd/pf2e/compendium/rules-elements/skills/lore|Plane of Air Lore]] +4, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +7"
abilityMods: [0, 3, 1, 0, 2, 0]
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +3; __Ref__: +9; __Will__: +4"
hp: 12
health:
  - name: "HP"
    desc: "12; __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|bleed]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]"
abilities_mid:
  - name: "Resonance"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/air|air]]) 30 feet. All wisps vibrate at a frequency attuned to their element, resonating with and empowering all creatures and effects sharing that trait. Creatures in the area gain a +1 status bonus to attack and damage rolls for effects that have the [[srd/pf2e/compendium/rules-elements/traits/player-core/air|air]] trait; a creature with the [[srd/pf2e/compendium/rules-elements/traits/player-core/elemental|elemental]] and air traits gains this bonus to all attack and damage rolls."
  - name: "Accord Essence"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/air|air]])"
  - name: "Trigger"
    desc: "An ally within 30 feet that benefited from the wisp's resonance in the last hour is targeted by an attack"
  - name: "Effect"
    desc: "The wisp detonates themself in an elemental explosion. This grants [[srd/pf2e/books/player-core/chapter-8-playing-the-game/hit-points-healing-and-dying#Temporary Hit Points|temporary Hit Points]] equal to half the wisp's current Hit Points to allies within 30 feet who have benefited from the wisp's resonance in the last hour. These temporary Hit Points last 1 hour. A wisp that uses this reaction is permanently destroyed, and they can be restored by only a [[srd/pf2e/compendium/spells/rituals/wish|_wish_]] ritual or similarly powerful effect. If an ability would prevent the wisp's destruction (for instance, if the wisp is summoned and would merely be dismissed), Accord Essence has no effect."
speed: "fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ tendril +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 1d4 bludgeoning"
abilities_bot:
  - name: "In Concert"
    desc: "When an air wisp rolls a critical failure on a check to [[srd/pf2e/compendium/rules-elements/actions/player-core#Aid|Aid]], they get a failure instead, and when they roll a success, they get a critical success instead."
sourcebook: "_Monster Core 2_, page 152."
```

```encounter-table
name: Air Wisp
creatures:
  - 1: Air Wisp
```
