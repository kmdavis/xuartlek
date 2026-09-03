---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Phade"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/air
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/medium
statblock: inline
name: "Phade"
level: 7
source: "Monster Core"
aon_id: "creature-2975"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2975"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Phade"
level: "Creature 7"
size: "Medium"
trait_01: "Air"
trait_02: "Elemental"
modifier: 16
perception:
  - name: "Perception"
    desc: "Perception +16; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Sussuran|Sussuran]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +16, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +15, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +18, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +15"
abilityMods: [3, 6, 3, 2, 2, 0]
ac: 26
armorclass:
  - name: "AC"
    desc: "26; __Fort__: +14; __Ref__: +18; __Will__: +11"
hp: 70
health:
  - name: "HP"
    desc: "70; __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]"
abilities_mid:
  - name: "Naturally Invisible"
    desc: "The phade is [[srd/pf2e/compendium/rules-elements/conditions#Invisible|invisible]] at all times, though when it takes a hostile action of any kind, it is [[srd/pf2e/compendium/rules-elements/conditions#Hidden|hidden]] instead of [[srd/pf2e/compendium/rules-elements/conditions#Undetected|undetected]] until the start of its next turn, as the vague outline of its humanoid form is faintly visible for a short period of time."
speed: "25 feet, fly 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +18 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]]) __Damage__ 1d10+5 bludgeoning"
abilities_bot:
  - name: "Hush"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/air|Air]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]]) The phade calms the air in a 30-foot emanation until the beginning of its next turn, reducing sounds in it to a whisper that can't be heard outside the emanation. This doesn't prevent casting spells, but a phade attempts to counteract any [[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|auditory]] or [[srd/pf2e/compendium/rules-elements/traits/player-core/sonic|sonic]] effect originating in the area with a +17 counteract modifier. If the counteract attempt fails, Hush ends early."
  - name: "Sneak Attack"
    desc: "The phade deals 2d6 extra precision damage to [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] creatures."
sourcebook: "_Monster Core_, page 140."
```

```encounter-table
name: Phade
creatures:
  - 1: Phade
```
