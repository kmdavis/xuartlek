---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Ancient Resurrection Dragon"
tags:
  - pf2e/creature/level/17
  - pf2e/creature/trait/divine
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/huge
statblock: inline
name: "Ancient Resurrection Dragon"
level: 17
source: "Monster Core 2"
aon_id: "creature-4362"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4362"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Ancient Resurrection Dragon"
level: "Creature 17"
size: "Huge"
trait_01: "Divine"
trait_02: "Dragon"
trait_03: "Uncommon"
modifier: 32
perception:
  - name: "Perception"
    desc: "Perception +32; darkvision, scent (imprecise) 60 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/languages#Necril|Necril]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +28, [[srd/pf2e/compendium/rules-elements/skills/arcana|Arcana]] +28, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +33, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +31, [[srd/pf2e/compendium/rules-elements/skills/medicine|Medicine]] +33, [[srd/pf2e/compendium/rules-elements/skills/lore|Necromancy Lore]] +36, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +33, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +30"
abilityMods: [9, 5, 6, 5, 9, 6]
ac: 39
armorclass:
  - name: "AC"
    desc: "39; __Fort__: +28; __Ref__: +27; __Will__: +32"
hp: 320
health:
  - name: "HP"
    desc: "320; __Immunities__ [[srd/pf2e/books/player-core/chapter-8-playing-the-game/hit-points-healing-and-dying#Death Effects|death effects]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/spirit|spirit]] 20"
abilities_mid:
  - name: "Risen Commander"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]]) A resurrection dragon has a strong connection with its minions and can [[srd/pf2e/compendium/rules-elements/actions/player-core#Sustain|Sustain]] [[srd/pf2e/compendium/spells/rank-1/summon-undead|_summon undead_]] or [[srd/pf2e/compendium/spells/rank-5/invoke-spirits|_invoke spirits_]] as a free action once per turn. __Reawaken!__ ⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/spirit|spirit]], [[srd/pf2e/compendium/rules-elements/traits/player-core/vitality|vitality]])"
  - name: "Trigger"
    desc: "A living creature the resurrection dragon can see dies"
  - name: "Effect"
    desc: "The resurrection dragon uses divine and vital energy to retether the soul to its dead body. The willing creature is returned to life with half of their total Hit Points. A creature can be resurrected by this ability only once."
  - name: "Siphon Life"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/healing|healing]], [[srd/pf2e/compendium/rules-elements/traits/player-core/vitality|vitality]])"
  - name: "Trigger"
    desc: "A creature within 60 feet uses a [[srd/pf2e/compendium/rules-elements/traits/player-core/healing|healing]] effect that restores Hit Points"
  - name: "Effect"
    desc: "The resurrection dragon redirects vital energies away from the effect, minimizing its impact. The triggering effect results in the minimum amount on any dice rolls to restore Hit Points, and any flat values for restoring Hit Points (such as the additional Hit Points for a two-action [[srd/pf2e/compendium/spells/rank-1/heal|_heal_]] spell) are cut in half. The dragon then gains 3d8 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/hit-points-healing-and-dying#Temporary Hit Points|temporary Hit Points]] that last for 1 round."
speed: "50 feet, fly 200 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +33 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 3d12+15 piercing plus 1d6 void"
  - name: "Melee"
    desc: "⬻ claw +33 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 3d10+15 slashing"
  - name: "Melee"
    desc: "⬻ tail +31 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 20 feet]]) __Damage__ 3d12+15 bludgeoning"
abilities_bot:
  - name: "Draconic Frenzy"
    desc: "⬺ The dragon makes two claw strikes and one tail strike in any order."
  - name: "Draconic Momentum"
    desc: "The dragon recharges their Soul Siphoning Breath whenever they score a critical hit with a Strike."
  - name: "Necro Puppeteer"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/void|void]]) The dragon siphons energy into an undead creature, a [[srd/pf2e/compendium/rules-elements/conditions#Dying|dying]] creature, or a corpse they can see within 60 feet. The dragon moves the target creature 30 feet and causes it to unleash a wave of void energy in a 10-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Emanation|emanation]], dealing 6d8 void damage (DC 32 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save)."
  - name: "Soul Siphoning Breath"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/void|void]]) The dragon unleashes a torrent of divine energy, dealing 16d6 void damage in a 50-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Cone|cone]] (DC 38 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Fortitude save) that draws the life force from creatures within. The dragon gains fast healing 15 until their Soul Siphoning Breath recharges. The resurrection dragon can't use Soul Siphoning Breath again for 1d4 rounds."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 38 - __Cantrips (9th)__ [[srd/pf2e/compendium/spells/cantrips/guidance|Guidance]], [[srd/pf2e/compendium/spells/cantrips/stabilize|Stabilize]], [[srd/pf2e/compendium/spells/cantrips/void-warp|Void Warp]] - __4th__ [[srd/pf2e/compendium/spells/rank-4/talking-corpse|Talking Corpse]] (at will) - __9th__ [[srd/pf2e/compendium/spells/rank-1/harm|Harm]] (×2), [[srd/pf2e/compendium/spells/rank-5/invoke-spirits|Invoke Spirits]] (×2), [[srd/pf2e/compendium/spells/rank-6/raise-dead|Raise Dead]], [[srd/pf2e/compendium/spells/rank-1/summon-undead|Summon Undead]] (at will) __Arise!__ ([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/exploration|exploration]], [[srd/pf2e/compendium/rules-elements/traits/player-core/healing|healing]]) The resurrection dragon uses their mastery over life energy to cast their own soul into the Boneyard and pull a willing creature's soul back to its body in a process that takes 1 hour. This has the effects of [[srd/pf2e/compendium/spells/rank-6/raise-dead|_raise dead_]], except the maximum level of the target is 13th and the soul is tethered to the dragon's. Only one creature can be tethered to the dragon's soul at a time. If the creature and the dragon are no longer on the same plane or the dragon dies, the raised creature dies and can't be raised with Arise! again. The dragon can [[srd/pf2e/compendium/rules-elements/actions/player-core#Dismiss|Dismiss]] the connection at any time. Doing so doesn't prevent the dragon from raising the creature with Arise! again. While raised in this way, the creature is still a valid target for _raise dead_, [[srd/pf2e/compendium/spells/rituals/resurrect|_resurrection_]], and similar effects. Returning the creature to life in this way fully restores the creature, severing the connection to the dragon and allowing the dragon to establish a connection with a different creature."
sourcebook: "_Monster Core 2_, page 130."
```

```encounter-table
name: Ancient Resurrection Dragon
creatures:
  - 1: Ancient Resurrection Dragon
```
