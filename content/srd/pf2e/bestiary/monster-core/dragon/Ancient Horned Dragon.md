---
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
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2949"
socialImage: og-image.png
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
    desc: "+30; darkvision, scent (imprecise) 60 feet"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Chthonian|Chthonian]], [[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/Languages#Elven|Elven]], [[srd/pf2e/compendium/rules-elements/Languages#Fey|Fey]], [[srd/pf2e/compendium/rules-elements/Languages#Jotun|Jotun]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +25, [[srd/pf2e/compendium/rules-elements/skills/Arcana|Arcana]] +32, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +30, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +27, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +31, Forest Lore +31, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +31, [[srd/pf2e/compendium/rules-elements/skills/Nature|Nature]] +28, [[srd/pf2e/compendium/rules-elements/skills/Occultism|Occultism]] +34, [[srd/pf2e/compendium/rules-elements/skills/Society|Society]] +31, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +29"
abilityMods: [7, 4, 5, 6, 5, 6]
abilities_top:
  - name: "Camouflage"
    desc: "The dragon can [[srd/pf2e/compendium/rules-elements/actions/player-core#Hide|Hide]] in natural environments even if they don't have cover."
ac: 41
armorclass:
  - name: "AC"
    desc: "41; __Fort__: +30; __Ref__: +29; __Will__: +32 +1 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/Primal|primal]]"
hp: 315
health:
  - name: "HP"
    desc: "315; __Immunities__ [[srd/pf2e/compendium/rules-elements/Conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Sleep|sleep]]"
abilities_mid:
  - name: "Frightful Presence"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Fear|fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]]) 90 feet, DC 37"
  - name: "Miasma"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|poison]]) 20 feet. After the dragon uses their Poison Breath, a cloud of poison gas continues to emanate from their body for 1 round. Any creature that ends its turn in the miasma takes 4d6 poison damage (DC 37 basic Fortitude save). Any creature in the miasma is [[srd/pf2e/compendium/rules-elements/Conditions#Concealed|concealed]] and treats other creatures as concealed. The dragon can see through this concealment."
  - name: "Twisting Tail"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature within reach of the dragon's tail uses a [[srd/pf2e/compendium/rules-elements/traits/player-core/Move|move]] action or leaves a square during a move action it's using"
  - name: "Effect"
    desc: "The dragon makes a tail Strike at the creature with a –2 penalty. If the Strike hits, the dragon disrupts the creature's action."
speed: "50 feet, fly 200 feet, swim 50 feet; forest passage, trackless journey"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +33 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|Poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 20 feet]]) __Damage__ 3d12+15 piercing plus 4d4 poison"
  - name: "Melee"
    desc: "⬻ claw +33 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 15 feet]]) __Damage__ 3d10+15 slashing"
  - name: "Melee"
    desc: "⬻ tail +31 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 25 feet]]) __Damage__ 3d10+13 bludgeoning"
  - name: "Melee"
    desc: "⬻ horn +31 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 20 feet]]) __Damage__ 2d10+13 piercing"
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
    desc: "The dragon attempts to gore a foe. They Stride, then attempt a horn Strike. On a hit, the target becomes impaled on the dragon's horn. The creature is [[srd/pf2e/compendium/rules-elements/Conditions#Grabbed|grabbed]] while on the horn (and can attempt to [[srd/pf2e/compendium/rules-elements/actions/player-core#Escape|Escape]] as normal). The dragon doesn't need to use additional actions to keep the impaled creature grabbed. If the dragon moves, they bring the grabbed creature along with them."
  - name: "Poison Breath"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Primal|Primal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|Poison]]) The dragon breathes a toxic cloud that deals 18d6 poison damage in a 60-foot cone (DC 37 basic Fortitude save). They can't use Poison Breath again for 1d4 rounds."
  - name: "Trackless Journey"
    desc: "The horned dragon always gains the benefits of [[srd/pf2e/compendium/rules-elements/actions/player-core#Cover Tracks|Cover Tracks]] in natural surroundings, even while moving at full speed."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 39 - __2nd__ [[srd/pf2e/compendium/spells/rank-2/Entangling Flora|Entangling Flora]] (at will) - __4th__ [[srd/pf2e/compendium/spells/rank-1/Charm|Charm]] (at will), [[srd/pf2e/compendium/spells/rank-4/Suggestion|Suggestion]] - __6th__ [[srd/pf2e/compendium/spells/rank-6/Dominate|Dominate]]"
sourcebook: "_Monster Core_, page 121."
```

```encounter-table
name: Ancient Horned Dragon
creatures:
  - 1: Ancient Horned Dragon
```
