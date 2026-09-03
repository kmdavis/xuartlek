---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Caligni Skulker"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/caligni
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/small
statblock: inline
name: "Caligni Skulker"
level: 2
source: "Monster Core"
aon_id: "creature-2863"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2863"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Caligni Skulker"
level: "Creature 2"
size: "Small"
trait_01: "Caligni"
trait_02: "Humanoid"
modifier: 8
perception:
  - name: "Perception"
    desc: "Perception +8; greater darkvision, light blindness"
languages: "Caligni"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +8, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +4, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +10, [[srd/pf2e/compendium/rules-elements/skills/thievery|Thievery]] +8"
abilityMods: [0, 4, 3, -1, 2, 1]
abilities_top:
  - name: "Items"
    desc: "darkening poison (3 doses), Dagger"
ac: 19
armorclass:
  - name: "AC"
    desc: "19; __Fort__: +9; __Ref__: +10; __Will__: +6"
hp: 30
health:
  - name: "HP"
    desc: "30 (final night)"
abilities_mid:
  - name: "Final Night"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/darkness|darkness]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|occult]]) When the caligni skulker dies, their remains dissolve into a 20-foot emanation of inky darkness before dissipating. The darkness extinguishes non-magical light sources and attempts to counteract magical [[srd/pf2e/compendium/rules-elements/traits/player-core/light|light]] as a 1st-rank effect with a +10 counteract modifier. The skulker's possessions are left in a pile where they died."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ dagger +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 1d4+4 piercing plus darkening poison"
  - name: "Ranged"
    desc: "⬻ dagger +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 1d4 piercing plus darkening poison"
abilities_bot:
  - name: "Sneak Attack"
    desc: "The caligni skulker deals 1d6 extra precision damage to [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] creatures."
  - name: "Tumble Behind"
    desc: "When the caligni skulker [[srd/pf2e/compendium/rules-elements/actions/player-core#Tumble Through|Tumbles Through]] a creature's space, that creature is [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] against the next attack the skulker makes against it before the end of its turn."
sourcebook: "_Monster Core_, page 48."
```

```encounter-table
name: Caligni Skulker
creatures:
  - 1: Caligni Skulker
```
