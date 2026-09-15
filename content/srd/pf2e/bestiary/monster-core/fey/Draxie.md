---
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
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3211"
socialImage: og-image.png
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
    desc: "+8; low-light vision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Fey|Fey]]; telepathy (touch)"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +9, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +10, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +8, [[srd/pf2e/compendium/rules-elements/skills/Nature|Nature]] +6, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +11"
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
    desc: "⬻ jaws +11 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 0 feet]]) __Damage__ 1d8+3 piercing"
  - name: "Ranged"
    desc: "⬻ euphoric spark +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], range 20 feet) __Damage__ 2d4+3 mental"
abilities_bot:
  - name: "Draxie Dust"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Incapacitation|Incapacitation]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|Mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Primal|Primal]]) The draxie breathes magical dust in a 15-foot cone. Roll 1d4 to determine the effect. Each creature in the area must succeed at a DC 17 Will save or be affected. The draxie can't use Draxie Dust again for 1d4 rounds. The target takes the effects of the [[srd/pf2e/compendium/spells/rank-1/Charm|_charm_]] spell.The target loses its last 5 minutes of memory.The target takes the effects of a [[srd/pf2e/compendium/spells/rank-1/Sleep|_sleep_]] spell.For 1 minute, the target is in a state of euphoria that makes it [[srd/pf2e/compendium/rules-elements/Conditions#Stupefied|stupefied 2]] and [[srd/pf2e/compendium/rules-elements/Conditions#Slowed|slowed 1]]."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 20 - __Cantrips (1st)__ [[srd/pf2e/compendium/spells/cantrips/Light|Light]], [[srd/pf2e/compendium/spells/cantrips/Figment|Figment]], [[srd/pf2e/compendium/spells/cantrips/Prestidigitation|Prestidigitation]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/Illusory Disguise|Illusory Disguise]] (×3) - __2nd__ [[srd/pf2e/compendium/spells/rank-2/Invisibility|Invisibility]], [[srd/pf2e/compendium/spells/rank-2/Revealing Light|Revealing Light]]"
sourcebook: "_Monster Core_, page 322."
```

```encounter-table
name: Draxie
creatures:
  - 1: Draxie
```
