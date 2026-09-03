---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Thanatotic Titan"
tags:
  - pf2e/creature/level/22
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/titan
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Thanatotic Titan"
level: 22
source: "Monster Core 2"
aon_id: "creature-4582"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4582"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Thanatotic Titan"
level: "Creature 22"
size: "Gargantuan"
trait_01: "Humanoid"
trait_02: "Rare"
trait_03: "Titan"
modifier: 36
perception:
  - name: "Perception"
    desc: "Perception +36; darkvision, [[srd/pf2e/compendium/spells/rank-6/truesight|_truesight_]]"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Chthonian|Chthonian]], [[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Empyrean|Empyrean]]; telepathy 100 feet (page 362)"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +45, [[srd/pf2e/compendium/rules-elements/skills/crafting|Crafting]] +41, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +36, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +38, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +38, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +36"
abilityMods: [10, 4, 9, 8, 6, 8]
abilities_top:
  - name: "Items"
    desc: "_[[srd/pf2e/compendium/equipment/armor/magic-armor-3-major-resilient|+2 greater resilient]] [[srd/pf2e/compendium/equipment/armor#Full Plate|full plate]]_, _[[srd/pf2e/compendium/equipment/weapons/magic-weapon-3-major-striking|+3 greater striking]] [[srd/pf2e/compendium/equipment/weapons/polearm/halberd|halberd]]_"
ac: 46
armorclass:
  - name: "AC"
    desc: "46; __Fort__: +37; __Ref__: +34; __Will__: +35 +4 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]] or divine"
hp: 540
health:
  - name: "HP"
    desc: "540; __Immunities__ [[srd/pf2e/books/player-core/chapter-8-playing-the-game/hit-points-healing-and-dying#Death Effects|death effects]], [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]]"
abilities_mid:
  - name: "Impossible Stature"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/illusion|illusion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]]) 100 feet. Titans warp perception and distance around them to seem even larger and more imposing. A creature that enters or begins its turn within the emanation must succeed at a DC 45 Will save or its movement toward the titan is movement over [[srd/pf2e/books/player-core/chapter-8-playing-the-game/movement#Difficult Terrain|difficult terrain]] (greater difficult terrain on a critical failure) for 1 round."
  - name: "Reactive Strike"
    desc: "⬲ The titan can use their Reactive Strike when a creature within their reach uses a concentrate action, in additional to its normal trigger. They disrupt actions on any hit, not just a critical hit—including triggering [[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|concentrate]] actions."
speed: "40 feet, fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _halberd_ +42 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 40 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 4d10+25 piercing"
  - name: "Melee"
    desc: "⬻ foot +39 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 30 feet]]) __Damage__ 4d8+20 bludgeoning"
  - name: "Ranged"
    desc: "⬻ void chunk +39 (Brutal, range increment 200 feet, [[srd/pf2e/compendium/rules-elements/traits/player-core/void|void]]) __Damage__ 3d12+10 bludgeoning plus 2d10 void and void explosion"
abilities_bot:
  - name: "Divine Rituals"
    desc: "DC 45 - __5th__ [[srd/pf2e/compendium/spells/rituals/planar-servitor|Planar Servitor]], [[srd/pf2e/compendium/spells/rituals/resurrect|Resurrect]]"
  - name: "Godslayer"
    desc: "⭓ ([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]])"
  - name: "Trigger"
    desc: "The titan damages a creature capable of using divine spells or abilities"
  - name: "Effect"
    desc: "The creature must attempt a DC 45 Will save."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature can't use divine spells or abilities for 1 round and is [[srd/pf2e/compendium/rules-elements/conditions#Frightened|frightened]] 2. Only powerful non-divine magic, such as [[srd/pf2e/compendium/spells/rank-10/manifestation|_manifestation_]], can undo this effect."
  - name: "Failure"
    desc: "As success, but the duration is 1 minute."
  - name: "Critical Failure"
    desc: "As success, but the duration is unlimited."
  - name: "Titanic Charge"
    desc: "⬺ The titan Strides twice and makes a melee Strike. If the Strike hits, the titan can cast [[srd/pf2e/compendium/spells/rank-8/earthquake|_earthquake_]] centered on the target as a free action."
  - name: "Trample"
    desc: "⬽ Huge or smaller, foot, DC 45"
  - name: "Void Explosion"
    desc: "If the titan's void chunk Strike isn't a critical failure, the chunk explodes, dealing 10d6 void damage to all creatures in a 20-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Burst|burst]] (DC 45 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save)."
  - name: "Wide Cleave"
    desc: "⬺ The titan makes a melee weapon Strike against each foe within their reach. This counts as three attacks for the titan's multiple attack penalty, but the penalty doesn't increase until all attacks have been made."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 45 - __5th__ [[srd/pf2e/compendium/spells/rank-5/sending|Sending]] - __6th__ [[srd/pf2e/compendium/spells/rank-6/scrying|Scrying]] (×3) - __7th__ [[srd/pf2e/compendium/spells/rank-7/spell-riposte|Spell Riposte]] - __8th__ [[srd/pf2e/compendium/spells/rank-2/dispel-magic|Dispel Magic]] (at will), [[srd/pf2e/compendium/spells/rank-8/spiritual-epidemic|Spiritual Epidemic]] (at will), [[srd/pf2e/compendium/spells/rank-4/suggestion|Suggestion]] (at will) - __10th__ [[srd/pf2e/compendium/spells/rank-9/falling-stars|Falling Stars]], [[srd/pf2e/compendium/spells/rank-9/massacre|Massacre]] - __Constant (10th)__ [[srd/pf2e/compendium/spells/rank-6/truesight|Truesight]]"
sourcebook: "_Monster Core 2_, page 320."
```

```encounter-table
name: Thanatotic Titan
creatures:
  - 1: Thanatotic Titan
```
