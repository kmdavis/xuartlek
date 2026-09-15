---
noteType: pf2eMonster
aliases: "Choral"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/angel
  - pf2e/creature/trait/celestial
  - pf2e/creature/trait/holy
  - pf2e/creature/trait/small
statblock: inline
name: "Choral"
level: 6
source: "Monster Core"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2815"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Choral"
level: "Creature 6"
size: "Small"
trait_01: "Angel"
trait_02: "Celestial"
trait_03: "Holy"
modifier: 14
perception:
  - name: "Perception"
    desc: "+14; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/Languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/Languages#Empyrean|Empyrean]]; [[srd/pf2e/compendium/spells/rank-5/Truespeech|_truespeech_]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +12, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +15, [[srd/pf2e/compendium/rules-elements/skills/Performance|Performance]] +17, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +14"
abilityMods: [1, 4, 2, 3, 4, 5]
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +10; __Ref__: +14; __Will__: +16 +1 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magic]]"
hp: 100
health:
  - name: "HP"
    desc: "100; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Sonic|sonic]] 5; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|unholy]] 5"
abilities_mid:
  - name: "Harmonizing Aura"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Sonic|sonic]]) 20 feet. Allies in the aura gain a +2 status bonus to sonic damage rolls and a +1 status bonus to AC and all saves against effects with the [[srd/pf2e/compendium/rules-elements/traits/player-core/Auditory|auditory]] or [[srd/pf2e/compendium/rules-elements/traits/player-core/Sonic|sonic]] trait. Enemies in the aura take a –2 status penalty to sonic damage rolls and a –1 status penalty to AC and all saves against sonic and auditory effects."
speed: "30 feet, fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|Holy]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]]) __Damage__ 2d6+5 bludgeoning"
  - name: "Ranged"
    desc: "⬻ piercing hymn +17 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|Holy]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], range 90 feet, [[srd/pf2e/compendium/rules-elements/traits/player-core/Sonic|Sonic]]) __Damage__ 4d6 sonic damage plus deafening aria"
abilities_bot:
  - name: "Deafening Aria"
    desc: "On a critical hit with piercing hymn, the target is [[srd/pf2e/compendium/rules-elements/Conditions#Deafened|deafened]] for 1 minute."
  - name: "Harmonize"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Sonic|Sonic]]) The choral angel lends their harmony to a choral angel ally within their harmonizing aura. The ally can, on their next turn, expend their 3rd-rank [[srd/pf2e/compendium/spells/rank-2/Noise Blast|_noise blast_]] to instead cast [[srd/pf2e/compendium/spells/rank-2/Calm|_calm_]], [[srd/pf2e/compendium/spells/rank-3/Heroism|_heroism_]], or 4th-rank _noise blast_. If the ally is benefiting from 5 or more chorals' Harmonize actions, they can instead choose [[srd/pf2e/compendium/spells/rank-7/Divine Decree|_divine decree_]]."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 23, attack +15 - __Cantrips (3rd)__ [[srd/pf2e/compendium/spells/cantrips/Courageous Anthem|Courageous Anthem]], [[srd/pf2e/compendium/spells/cantrips/Uplifting Overture|Uplifting Overture]] - __1st__ [[srd/pf2e/compendium/spells/focus/Counter Performance|Counter Performance]] (at will) - __2nd__ [[srd/pf2e/compendium/spells/rank-2/Invisibility|Invisibility]] (at will; self only), [[srd/pf2e/compendium/spells/rank-2/Noise Blast|Noise Blast]] (at will) - __3rd__ [[srd/pf2e/compendium/spells/rank-2/Cleanse Affliction|Cleanse Affliction]], [[srd/pf2e/compendium/spells/rank-2/Clear Mind|Clear Mind]] (at will), [[srd/pf2e/compendium/spells/rank-1/Heal|Heal]], [[srd/pf2e/compendium/spells/rank-2/Noise Blast|Noise Blast]] - __Constant (5th)__ [[srd/pf2e/compendium/spells/rank-5/Truespeech|Truespeech]]"
  - name: "Rituals"
    desc: "DC 23 - __1st__ [[srd/pf2e/compendium/spells/rituals/Angelic Messenger|Angelic Messenger]]"
sourcebook: "_Monster Core_, page 15."
```

```encounter-table
name: Choral
creatures:
  - 1: Choral
```
