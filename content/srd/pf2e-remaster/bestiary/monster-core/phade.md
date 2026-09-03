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
languages: "Sussuran"
skills:
  - name: "Skills"
    desc: "Acrobatics +16, Nature +15, Stealth +18, Survival +15"
abilityMods: [3, 6, 3, 2, 2, 0]
ac: 26
armorclass:
  - name: "AC"
    desc: "26; __Fort__: +14; __Ref__: +18; __Will__: +11"
hp: 70
health:
  - name: "HP"
    desc: "70; __Immunities__ bleed, paralyzed, poison, sleep"
abilities_mid:
  - name: "Naturally Invisible"
    desc: "The phade is invisible at all times, though when it takes a hostile action of any kind, it is hidden instead of undetected until the start of its next turn, as the vague outline of its humanoid form is faintly visible for a short period of time."
speed: "25 feet, fly 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +18 (Agile, Finesse) __Damage__ 1d10+5 bludgeoning"
abilities_bot:
  - name: "Hush"
    desc: "⬻ (Air, Primal) The phade calms the air in a 30-foot emanation until the beginning of its next turn, reducing sounds in it to a whisper that can't be heard outside the emanation. This doesn't prevent casting spells, but a phade attempts to counteract any auditory or sonic effect originating in the area with a +17 counteract modifier. If the counteract attempt fails, Hush ends early."
  - name: "Sneak Attack"
    desc: "The phade deals 2d6 extra precision damage to off-guard creatures."
sourcebook: "_Monster Core_, page 140."
```

```encounter-table
name: Phade
creatures:
  - 1: Phade
```
