---
noteType: pf2eMonster
aliases: "Young Resurrection Dragon"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/divine
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/large
statblock: inline
name: "Young Resurrection Dragon"
level: 8
source: "Monster Core 2"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4360"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Young Resurrection Dragon"
level: "Creature 8"
size: "Large"
trait_01: "Divine"
trait_02: "Dragon"
modifier: 19
perception:
  - name: "Perception"
    desc: "+19; darkvision, scent (imprecise) 60 feet"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/Languages#Necril|Necril]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +15, [[srd/pf2e/compendium/rules-elements/skills/Arcana|Arcana]] +15, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +18, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +18, [[srd/pf2e/compendium/rules-elements/skills/Medicine|Medicine]] +18, [[srd/pf2e/compendium/rules-elements/skills/Lore|Necromancy Lore]] +19, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +18, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +17"
abilityMods: [6, 3, 4, 3, 6, 4]
ac: 26
armorclass:
  - name: "AC"
    desc: "26; __Fort__: +15; __Ref__: +14; __Will__: +19"
hp: 140
health:
  - name: "HP"
    desc: "140; __Immunities__ [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Hit Points, Healing, and Dying#Death Effects|death effects]], [[srd/pf2e/compendium/rules-elements/Conditions#Paralyzed|paralyzed]], sleep; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Spirit|spirit]] 10"
abilities_mid:
  - name: "Risen Commander"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]]) A resurrection dragon has a strong connection with its minions and can [[srd/pf2e/compendium/rules-elements/actions/player-core#Sustain|Sustain]] [[srd/pf2e/compendium/spells/rank-1/Summon Undead|_summon undead_]] or [[srd/pf2e/compendium/spells/rank-5/Invoke Spirits|_invoke spirits_]] as a free action once per turn. __Reawaken!__ ⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Spirit|spirit]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Vitality|vitality]])"
  - name: "Trigger"
    desc: "A living creature the resurrection dragon can see dies"
  - name: "Effect"
    desc: "The resurrection dragon uses divine and vital energy to retether the soul to its dead body. The willing creature is returned to life with the [[srd/pf2e/compendium/rules-elements/Conditions#Dying|dying]] 1 condition at the start of its next turn. A creature can be resurrected by this ability only once."
  - name: "Siphon Life"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Healing|healing]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Vitality|vitality]])"
  - name: "Trigger"
    desc: "A creature within 60 feet uses a [[srd/pf2e/compendium/rules-elements/traits/player-core/Healing|healing]] effect that restores Hit Points"
  - name: "Effect"
    desc: "The resurrection dragon redirects vital energies away from the effect, minimizing its impact. The triggering effect results in the minimum amount on any dice rolls to restore Hit Points, and any flat values for restoring Hit Points (such as the additional Hit Points for a two-action [[srd/pf2e/compendium/spells/rank-1/Heal|_heal_]] spell) are cut in half. The dragon then gains 1d8 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Hit Points, Healing, and Dying#Temporary Hit Points|temporary Hit Points]] that last for 1 round."
speed: "30 feet, fly 120 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +20 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 10 feet]]) __Damage__ 2d10+9 piercing plus 1d6 void"
  - name: "Melee"
    desc: "⬻ claw +20 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magical]]) __Damage__ 2d8+9 slashing"
  - name: "Melee"
    desc: "⬻ tail +18 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 15 feet]]) __Damage__ 2d10+9 bludgeoning"
abilities_bot:
  - name: "Draconic Frenzy"
    desc: "⬺ The dragon makes two claw strikes and one tail strike in any order."
  - name: "Draconic Momentum"
    desc: "The dragon recharges their Soul Siphoning Breath whenever they score a critical hit with a Strike."
  - name: "Soul Siphoning Breath"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Void|void]]) The dragon unleashes a torrent of divine energy, dealing 7d6 void damage in a 30-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Area#Cone|cone]] (DC 26 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Checks#Basic Saving Throws|basic]] Fortitude save) that draws the life force from creatures within. The dragon gains fast healing 5 until their Soul Siphoning Breath recharges. The resurrection dragon can't use Soul Siphoning Breath again for 1d4 rounds."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 26 - __Cantrips (4th)__ [[srd/pf2e/compendium/spells/cantrips/Guidance|Guidance]], [[srd/pf2e/compendium/spells/cantrips/Stabilize|Stabilize]], [[srd/pf2e/compendium/spells/cantrips/Void Warp|Void Warp]] - __4th__ [[srd/pf2e/compendium/spells/rank-1/Harm|Harm]] (×2), [[srd/pf2e/compendium/spells/rank-1/Summon Undead|Summon Undead]] (at will), [[srd/pf2e/compendium/spells/rank-4/Talking Corpse|Talking Corpse]]"
sourcebook: "_Monster Core 2_, page 129."
```

```encounter-table
name: Young Resurrection Dragon
creatures:
  - 1: Young Resurrection Dragon
```
