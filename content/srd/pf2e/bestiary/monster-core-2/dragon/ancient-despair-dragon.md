---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Ancient Despair Dragon"
tags:
  - pf2e/creature/level/18
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/occult
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Ancient Despair Dragon"
level: 18
source: "Monster Core 2"
aon_id: "creature-4353"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4353"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Ancient Despair Dragon"
level: "Creature 18"
size: "Gargantuan"
trait_01: "Dragon"
trait_02: "Occult"
trait_03: "Uncommon"
modifier: 31
perception:
  - name: "Perception"
    desc: "Perception +31; darkvision, fearsense (precise) 60 feet, scent (imprecise) 60 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Draconic|Draconic]]; telepathy 90 feet, [[srd/pf2e/compendium/spells/rank-5/truespeech|_truespeech_]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +31, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +33, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +32, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +32, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +35, [[srd/pf2e/compendium/rules-elements/skills/occultism|Occultism]] +29, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +29, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +33"
abilityMods: [9, 5, 4, 5, 5, 8]
abilities_top:
  - name: "Fearsense"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|occult]]) The dragon senses all creatures with the [[srd/pf2e/compendium/rules-elements/conditions#Frightened|frightened]] condition at the listed range."
ac: 41
armorclass:
  - name: "AC"
    desc: "41; __Fort__: +28; __Ref__: +30; __Will__: +32 +2 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|occult]]"
hp: 325
health:
  - name: "HP"
    desc: "325; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|fear]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]"
abilities_mid:
  - name: "Frightful Presence"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]]) 60 feet, DC 40"
  - name: "Consume Fear"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/occult|occult]])"
  - name: "Trigger"
    desc: "A creature within 60 feet loses the [[srd/pf2e/compendium/rules-elements/conditions#Frightened|frightened]] condition"
  - name: "Effect"
    desc: "The dragon feasts upon the fear that leaves the triggering creature's body, gaining 7d8 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/hit-points-healing-and-dying#Temporary Hit Points|temporary Hit Points]] that last for 1 minute."
  - name: "Unbidden Thoughts"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|occult]])"
  - name: "Trigger"
    desc: "The dragon is critically hit with a weapon or unarmed attack"
  - name: "Effect"
    desc: "The attacker's mind fills with visions of their worst fears that overwhelm their senses, and they must choose one of the following results: either the triggering attack becomes a normal success, or the critical hit is unaffected but the triggering creature becomes [[srd/pf2e/compendium/rules-elements/conditions#Frightened|frightened]] 2."
speed: "60 feet, fly 180 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +33 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 20 feet]]) __Damage__ 3d12+20 piercing"
  - name: "Melee"
    desc: "⬻ claws +33 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 3d10+20 slashing"
  - name: "Melee"
    desc: "⬻ tail +31 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 25 feet]]) __Damage__ 3d8+18 bludgeoning"
abilities_bot:
  - name: "Draconic Frenzy"
    desc: "⬺ The dragon makes two claw Strikes and one tail Strike in any order."
  - name: "Draconic Momentum"
    desc: "The dragon recharges their Shrieking Breath whenever they score a critical hit with a Strike."
  - name: "Look Behind You"
    desc: "⭓ ([[srd/pf2e/compendium/rules-elements/traits/player-core/occult|Occult]], [[srd/pf2e/compendium/rules-elements/traits/player-core/teleportation|teleportation]])"
  - name: "Trigger"
    desc: "The dragon successfully [[srd/pf2e/compendium/rules-elements/actions/player-core#Hide|Hides]] from a creature within 90 feet"
  - name: "Effect"
    desc: "The dragon teleports to a space directly behind the target creature. The dragon immediately becomes detected unless their chosen position has cover or another means to remain [[srd/pf2e/compendium/rules-elements/conditions#Hidden|hidden]]."
  - name: "Shrieking Breath"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|occult]], [[srd/pf2e/compendium/rules-elements/traits/monster-core/oni|sonic]]) The dragon lets out a cacophonous sound made of every scream the dragon has drawn from a terrified enemy, dealing 17d6 sonic damage in a 50-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Cone|cone]] (DC 40 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Will save). Creatures who fail their Will save must spend the first action of their next turn doing nothing but screaming. The dragon can't use Shrieking Breath again for 1d4 rounds."
  - name: "Tongue Decoy"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/manipulate|Manipulate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|occult]]) The despair dragon inflates several bladders at the end of its tongue to create the basic form of a creature. This process takes 1 minute to complete, during which the dragon is [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]]. If the dragon stops or is interrupted in this process, the bladders deflate, and the dragon must start over. Once the process is complete, the dragon can maintain the inflated bladders indefinitely, and can Dismiss to deflate the bladders and retract its tongue instantly. The inflated tongue takes the basic form of an animal or humanoid and can be inflated to be either Small or Medium. The form resembles the general silhouette of a creature, though closer inspection and success at a DC 35 [[srd/pf2e/books/player-core/chapter-1-introduction/character-creation#Perception|Perception]] check can determine the true nature of the tongue. While inflated, the dragon can send its voice through the decoy, though keeping its tongue inflated makes it difficult to speak, causing the dragon to take a –4 circumstance penalty to any checks related to speaking, such as [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] checks to [[srd/pf2e/compendium/rules-elements/actions/player-core#Lie|Lie]]. The dragon's tongue can extend up to 90 feet from the dragon's body and it can fully extend its tongue as part of the process to inflate the bladders. The dragon can move the inflated part of its tongue up to 15 feet at a time with an action, which has the concentrate, manipulate, and move traits. While extended, the inflated end of the tongue occupies space as a creature of the appropriate size, but the rest of the tongue doesn't impede or block movement in any way. The dragon's scent functions through cilia at the end of the tongue, but otherwise the dragon has no means of knowing what's near its tongue. Attacking the tongue is the same as attacking the dragon, except that the tongue is always off-guard. If the tongue takes any damage, it immediately deflates and remains out. The dragon remains off-guard as long as its tongue is out, but the dragon can retract its tongue with two consecutive [[srd/pf2e/compendium/rules-elements/actions/player-core#Interact|Interact]] actions. If the tongue takes damage, the dragon can't use its tongue decoy again for 1 day."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 40 - __7th__ [[srd/pf2e/compendium/spells/rank-1/fear|Fear]] (at will), [[srd/pf2e/compendium/spells/rank-5/wave-of-despair|Wave of Despair]] - __Constant (5th)__ [[srd/pf2e/compendium/spells/rank-5/truespeech|Truespeech]]"
sourcebook: "_Monster Core 2_, page 124."
```

```encounter-table
name: Ancient Despair Dragon
creatures:
  - 1: Ancient Despair Dragon
```
