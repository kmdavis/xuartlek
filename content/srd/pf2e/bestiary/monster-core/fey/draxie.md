---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Draxie"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/fey
  - pf2e/creature/trait/sprite
  - pf2e/creature/trait/tiny
statblock: inline
name: "Draxie"
level: 3
source: "Monster Core"
aon_id: "creature-3211"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3211"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Draxie"
level: "Creature 3"
size: "Tiny"
trait_01: "Fey"
trait_02: "Sprite"
modifier: 8
perception:
  - name: "Perception"
    desc: "Perception +8; low-light vision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Fey|Fey]]; telepathy (touch)"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +9, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +10, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +8, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +6, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +11"
abilityMods: [-1, 4, 1, 3, 1, 3]
ac: 19
armorclass:
  - name: "AC"
    desc: "19; __Fort__: +6; __Ref__: +11; __Will__: +8"
hp: 45
health:
  - name: "HP"
    desc: "45; __Weaknesses__ cold iron 5"
speed: "15 feet, fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +11 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 0 feet]]) __Damage__ 1d8+3 piercing"
  - name: "Ranged"
    desc: "⬻ euphoric spark +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], range 20 feet) __Damage__ 2d4+3 mental"
abilities_bot:
  - name: "Draxie Dust"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/incapacitation|Incapacitation]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]]) The draxie breathes magical dust in a 15-foot cone. Roll 1d4 to determine the effect. Each creature in the area must succeed at a DC 17 Will save or be affected. The draxie can't use Draxie Dust again for 1d4 rounds. The target takes the effects of the [[srd/pf2e/compendium/spells/rank-1/charm|_charm_]] spell.The target loses its last 5 minutes of memory.The target takes the effects of a [[srd/pf2e/compendium/spells/rank-1/sleep|_sleep_]] spell.For 1 minute, the target is in a state of euphoria that makes it [[srd/pf2e/compendium/rules-elements/conditions#Stupefied|stupefied 2]] and [[srd/pf2e/compendium/rules-elements/conditions#Slowed|slowed 1]]."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 20 - __Cantrips (1st)__ [[srd/pf2e/compendium/spells/cantrips/light|Light]], [[srd/pf2e/compendium/spells/cantrips/figment|Figment]], [[srd/pf2e/compendium/spells/cantrips/prestidigitation|Prestidigitation]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/illusory-disguise|Illusory Disguise]] (×3) - __2nd__ [[srd/pf2e/compendium/spells/rank-2/invisibility|Invisibility]], [[srd/pf2e/compendium/spells/rank-2/revealing-light|Revealing Light]]"
sourcebook: "_Monster Core_, page 322."
```

```encounter-table
name: Draxie
creatures:
  - 1: Draxie
```
