---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Ancient Horned Dragon"
tags:
  - pf2e/creature/level/17
  - pf2e/creature/trait/amphibious
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/primal
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Ancient Horned Dragon"
level: 17
source: "Monster Core"
aon_id: "creature-2949"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2949"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Ancient Horned Dragon"
level: "Creature 17"
size: "Gargantuan"
trait_01: "Amphibious"
trait_02: "Dragon"
trait_03: "Primal"
trait_04: "Uncommon"
modifier: 30
perception:
  - name: "Perception"
    desc: "Perception +30; darkvision, scent (imprecise) 60 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Chthonian|Chthonian]], [[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/languages#Elven|Elven]], [[srd/pf2e/compendium/rules-elements/languages#Fey|Fey]], [[srd/pf2e/compendium/rules-elements/languages#Jotun|Jotun]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +25, [[srd/pf2e/compendium/rules-elements/skills/arcana|Arcana]] +32, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +30, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +27, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +31, Forest Lore +31, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +31, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +28, [[srd/pf2e/compendium/rules-elements/skills/occultism|Occultism]] +34, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +31, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +29"
abilityMods: [7, 4, 5, 6, 5, 6]
abilities_top:
  - name: "Camouflage"
    desc: "The dragon can [[srd/pf2e/compendium/rules-elements/actions/player-core#Hide|Hide]] in natural environments even if they don't have cover."
ac: 41
armorclass:
  - name: "AC"
    desc: "41; __Fort__: +30; __Ref__: +29; __Will__: +32 +1 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|primal]]"
hp: 315
health:
  - name: "HP"
    desc: "315; __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]"
abilities_mid:
  - name: "Frightful Presence"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]]) 90 feet, DC 37"
  - name: "Miasma"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]]) 20 feet. After the dragon uses their Poison Breath, a cloud of poison gas continues to emanate from their body for 1 round. Any creature that ends its turn in the miasma takes 4d6 poison damage (DC 37 basic Fortitude save). Any creature in the miasma is [[srd/pf2e/compendium/rules-elements/conditions#Concealed|concealed]] and treats other creatures as concealed. The dragon can see through this concealment."
  - name: "Twisting Tail"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature within reach of the dragon's tail uses a [[srd/pf2e/compendium/rules-elements/traits/player-core/move|move]] action or leaves a square during a move action it's using"
  - name: "Effect"
    desc: "The dragon makes a tail Strike at the creature with a –2 penalty. If the Strike hits, the dragon disrupts the creature's action."
speed: "50 feet, fly 200 feet, swim 50 feet; forest passage, trackless journey"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +33 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 20 feet]]) __Damage__ 3d12+15 piercing plus 4d4 poison"
  - name: "Melee"
    desc: "⬻ claw +33 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 3d10+15 slashing"
  - name: "Melee"
    desc: "⬻ tail +31 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 25 feet]]) __Damage__ 3d10+13 bludgeoning"
  - name: "Melee"
    desc: "⬻ horn +31 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 20 feet]]) __Damage__ 2d10+13 piercing"
abilities_bot:
  - name: "Draconic Frenzy"
    desc: "⬺ The dragon makes two claw Strikes and one horn Strike in any order."
  - name: "Draconic Momentum"
    desc: "The dragon recharges their Poison Breath whenever they score a critical hit with a Strike."
  - name: "Forest Passage"
    desc: "The horned dragon ignores any difficult terrain caused by plants, such as bushes, vines, and undergrowth. Even plants manipulated by magic don't impede their progress."
  - name: "Impaling Charge"
    desc: "⬺"
  - name: "Requirements"
    desc: "The dragon doesn't have a creature impaled on their horn"
  - name: "Effect"
    desc: "The dragon attempts to gore a foe. They Stride, then attempt a horn Strike. On a hit, the target becomes impaled on the dragon's horn. The creature is [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] while on the horn (and can attempt to [[srd/pf2e/compendium/rules-elements/actions/player-core#Escape|Escape]] as normal). The dragon doesn't need to use additional actions to keep the impaled creature grabbed. If the dragon moves, they bring the grabbed creature along with them."
  - name: "Poison Breath"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]]) The dragon breathes a toxic cloud that deals 18d6 poison damage in a 60-foot cone (DC 37 basic Fortitude save). They can't use Poison Breath again for 1d4 rounds."
  - name: "Trackless Journey"
    desc: "The horned dragon always gains the benefits of [[srd/pf2e/compendium/rules-elements/actions/player-core#Cover Tracks|Cover Tracks]] in natural surroundings, even while moving at full speed."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 39 - __2nd__ [[srd/pf2e/compendium/spells/rank-2/entangling-flora|Entangling Flora]] (at will) - __4th__ [[srd/pf2e/compendium/spells/rank-1/charm|Charm]] (at will), [[srd/pf2e/compendium/spells/rank-4/suggestion|Suggestion]] - __6th__ [[srd/pf2e/compendium/spells/rank-6/dominate|Dominate]]"
sourcebook: "_Monster Core_, page 121."
```

```encounter-table
name: Ancient Horned Dragon
creatures:
  - 1: Ancient Horned Dragon
```
