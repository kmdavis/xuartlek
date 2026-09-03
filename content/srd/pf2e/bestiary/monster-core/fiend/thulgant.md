---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Thulgant"
tags:
  - pf2e/creature/level/18
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/qlippoth
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/large
statblock: inline
name: "Thulgant"
level: 18
source: "Monster Core"
aon_id: "creature-3157"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3157"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Thulgant"
level: "Creature 18"
size: "Large"
trait_01: "Fiend"
trait_02: "Qlippoth"
trait_03: "Uncommon"
trait_04: "Unholy"
modifier: 30
perception:
  - name: "Perception"
    desc: "Perception +30; darkvision, [[srd/pf2e/compendium/spells/rank-6/truesight|_truesight_]]"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Chthonian|Chthonian]]; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +32, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +35, [[srd/pf2e/compendium/rules-elements/skills/occultism|Occultism]] +33, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +32"
abilityMods: [9, 6, 6, 5, 6, 9]
ac: 42
armorclass:
  - name: "AC"
    desc: "42; __Fort__: +30; __Ref__: +28; __Will__: +32"
hp: 305
health:
  - name: "HP"
    desc: "305 (fast healing 10); __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Controlled|controlled]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|fear]]; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]] 15, physical 15 (except cold iron)"
speed: "30 feet, climb 30 feet, fly 50 feet; unfettered movement"
attacks:
  - name: "Melee"
    desc: "⬻ stinger +35 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|Unholy]]) __Damage__ 3d12+17 piercing plus 4d6 mental and thulgant venom"
  - name: "Melee"
    desc: "⬻ tentacle +35 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|Unholy]]) __Damage__ 3d8+17 bludgeoning plus 3d6 acid and Grab"
abilities_bot:
  - name: "Demon Hunter"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/occult|Occult]]) The thulgant causes a [[srd/pf2e/compendium/rules-elements/traits/player-core/demon|demon]] within 30 feet to suffer the effect of its sinful vulnerability."
  - name: "Greater Constrict"
    desc: "⬻ 2d6+17 bludgeoning and 1d6 acid, DC 40"
  - name: "Mind-Rending Sting"
    desc: "⬻"
  - name: "Requirement"
    desc: "The thulgant hits the same enemy with two consecutive sting Strikes in the same round"
  - name: "Effect"
    desc: "The thulgant deals 3d12+17 mental damage to the enemy. If the enemy is affected by thulgant venom, that poison gains the [[srd/pf2e/compendium/rules-elements/traits/gm-core/virulent|virulent]] trait."
  - name: "Stunning Display"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|Fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/incapacitation|Incapacitation]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|Occult]], [[srd/pf2e/compendium/rules-elements/traits/player-core/visual|Visual]]) The thulgant rises up on its twitching limbs and presents its numerous tentacles and stingers in a horrifying display of awfulness. Creatures in a 30-foot emanation must attempt a DC 40 Will save, after which they are temporarily immune to further Stunning Displays for 1 minute."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature is [[srd/pf2e/compendium/rules-elements/conditions#Stunned|stunned 1]]."
  - name: "Failure"
    desc: "The creature is stunned 4."
  - name: "Critical Failure"
    desc: "The creature is stunned 8."
  - name: "Thulgant Venom"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]])"
  - name: "Saving Throw"
    desc: "Fortitude DC 40"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "3d6 poison damage and the victim gains one of the following at random: [[srd/pf2e/compendium/rules-elements/conditions#Clumsy|clumsy 1]], [[srd/pf2e/compendium/rules-elements/conditions#Enfeebled|enfeebled 1]], or [[srd/pf2e/compendium/rules-elements/conditions#Stupefied|stupefied 1]] (1 round)"
  - name: "Stage 2"
    desc: "6d6 poison damage and the victim gains two of the following at random: clumsy 2, enfeebled 2, or stupefied 2 (1 round)"
  - name: "Stage 3"
    desc: "9d6 poison damage and the victim gains all three of the following: clumsy 3, enfeebled 3, and stupefied 3 (1 round)."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 40 - __Cantrips (9th)__ [[srd/pf2e/compendium/spells/cantrips/daze|Daze]], [[srd/pf2e/compendium/spells/cantrips/detect-magic|Detect Magic]] - __4th__ [[srd/pf2e/compendium/spells/rank-4/unfettered-movement|Unfettered Movement]] - __7th__ [[srd/pf2e/compendium/spells/rank-7/interplanar-teleport|Interplanar Teleport]] - __8th__ [[srd/pf2e/compendium/spells/rank-2/dispel-magic|Dispel Magic]], [[srd/pf2e/compendium/spells/rank-7/divine-decree|Divine Decree]], [[srd/pf2e/compendium/spells/rank-1/phantom-pain|Phantom Pain]] (×3), [[srd/pf2e/compendium/spells/rank-8/quandary|Quandary]] - __9th__ [[srd/pf2e/compendium/spells/rank-6/petrify|Petrify]] (×3), [[srd/pf2e/compendium/spells/rank-6/phantasmal-calamity|Phantasmal Calamity]] - __Constant (6th)__ [[srd/pf2e/compendium/spells/rank-6/truesight|Truesight]]"
  - name: "Rituals"
    desc: "DC 40 - __8th__ Imprisonment"
sourcebook: "_Monster Core_, page 283."
```

```encounter-table
name: Thulgant
creatures:
  - 1: Thulgant
```
