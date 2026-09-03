---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Adult Whisper Dragon"
tags:
  - pf2e/creature/level/11
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/occult
  - pf2e/creature/trait/large
statblock: inline
name: "Adult Whisper Dragon"
level: 11
source: "Monster Core 2"
aon_id: "creature-4367"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4367"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Adult Whisper Dragon"
level: "Creature 11"
size: "Large"
trait_01: "Dragon"
trait_02: "Occult"
modifier: 21
perception:
  - name: "Perception"
    desc: "Perception +21; (23 to [[srd/pf2e/compendium/rules-elements/actions/player-core#Sense Motive|Sense Motive]]) darkvision, scent (imprecise) 60 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/languages#Empyrean|Empyrean]], [[srd/pf2e/compendium/rules-elements/languages#Fey|Fey]]; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +17, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +19, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +18, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +20, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +18, [[srd/pf2e/compendium/rules-elements/skills/occultism|Occultism]] +21, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +23, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +19, [[srd/pf2e/compendium/rules-elements/skills/lore|Underworld Lore]] +23"
abilityMods: [5, 3, 4, 7, 4, 6]
abilities_top:
  - name: "Information Network"
    desc: "The dragon can attempt a [[srd/pf2e/compendium/rules-elements/skills/society|Society]] check to [[srd/pf2e/books/gm-core/chapter-1-running-the-game/difficulty-classes#Recall Knowledge|Recall Knowledge]] in place of a check to [[srd/pf2e/compendium/rules-elements/actions/player-core#Gather Information|Gather Information]], recalling intelligence from prior informants."
ac: 31
armorclass:
  - name: "AC"
    desc: "31; __Fort__: +21; __Ref__: +19; __Will__: +24 +2 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|occult]]"
hp: 190
health:
  - name: "HP"
    desc: "190; __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Confused|confused]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]"
abilities_mid:
  - name: "Diplomatic Solution"
    desc: "⭓ ([[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/incapacitation|incapacitation]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|occult]])"
  - name: "Trigger"
    desc: "The dragon rolls initiative"
  - name: "Effect"
    desc: "The dragon targets all enemies it can see within 60 feet with [[srd/pf2e/compendium/spells/rank-2/calm|_calm_]] heightened to a rank equal to half the dragon's level rounded up (DC 28 Will save). The dragon doesn't need to [[srd/pf2e/compendium/rules-elements/actions/player-core#Sustain an Effect|Sustain this effect]], but if the dragon takes any [[srd/pf2e/books/player-core/chapter-7-spells/hostile-actions|hostile action]] against those affected, it breaks the effect for all creatures."
  - name: "Distracting Whisper"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|occult]])"
  - name: "Trigger"
    desc: "The dragon is targeted with an attack"
  - name: "Effect"
    desc: "A mysterious voice whispers something disconcerting in the triggering creature's ear, inflicting a –2 circumstance penalty to the triggering attack."
speed: "50 feet, fly 170 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +24 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 2d12+11 piercing"
  - name: "Melee"
    desc: "⬻ claw +24 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]]) __Damage__ 2d10+11 slashing"
  - name: "Melee"
    desc: "⬻ tail +22 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 2d10+11 bludgeoning"
abilities_bot:
  - name: "Cogitation Breath"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|occult]]) The dragon unleashes a befuddling miasma, dealing 10d6 mental damage in a 30-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Cone|cone]] (DC 30 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Will save). A creature that fails its save is [[srd/pf2e/compendium/rules-elements/conditions#Stupefied|stupefied]] 1 (stupefied 2 on a critical failure) for 1 minute. The dragon can't use Cogitation Breath again for 1d4 rounds."
  - name: "Draconic Frenzy"
    desc: "⬺ The dragon makes two claw Strikes and one tail Strike in any order."
  - name: "Draconic Momentum"
    desc: "The dragon recharges their Cogitation Breath whenever they score a critical hit with a Strike."
  - name: "Steal Knowledge"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|occult]]) The dragon plucks a fragment of knowledge from the mind of a creature within 60 feet, choosing a skill to affect. The creature must attempt a DC 28 Will save."
  - name: "Success"
    desc: "The creature is unaffected."
  - name: "Failure"
    desc: "For the next minute, the creature takes a –1 status penalty to checks using that skill, and the dragon gets a +1 status bonus to using that skill."
  - name: "Critical Failure"
    desc: "As failure, but the penalty is –2 and the bonus is +2."
  - name: "Unveil Secret"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/fear|Fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|occult]]) The dragon delves into the mind of a creature within 60 feet to scour for secrets, learning something the creature would find embarrassing or shameful unless they succeed a DC 30 Will save. The target becomes [[srd/pf2e/compendium/rules-elements/conditions#Frightened|frightened]] 1 and can't reduce their frightened condition for 1 minute or until the dragon reveals the secret. As a reaction when the affected creature attempts a check, the dragon can reveal their secret to discomfit them, requiring them to roll twice and take the lower result; this is a [[srd/pf2e/compendium/rules-elements/traits/player-core/misfortune|misfortune]] effect."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 30 - __Cantrips (6th)__ [[srd/pf2e/compendium/spells/cantrips/daze|Daze]], [[srd/pf2e/compendium/spells/cantrips/message|Message]] - __2nd__ [[srd/pf2e/compendium/spells/rank-2/embed-message|Embed Message]] - __3rd__ [[srd/pf2e/compendium/spells/rank-3/clairaudience|Clairaudience]] (at will), [[srd/pf2e/compendium/spells/rank-3/mind-reading|Mind Reading]], [[srd/pf2e/compendium/spells/rank-3/ring-of-truth|Ring of Truth]] - __4th__ [[srd/pf2e/compendium/spells/rank-4/clairvoyance|Clairvoyance]] (at will) - __5th__ [[srd/pf2e/compendium/spells/rank-5/mind-probe|Mind Probe]] - __6th__ [[srd/pf2e/compendium/spells/rank-1/charm|Charm]], [[srd/pf2e/compendium/spells/rank-4/suggestion|Suggestion]]"
sourcebook: "_Monster Core 2_, page 134."
```

```encounter-table
name: Adult Whisper Dragon
creatures:
  - 1: Adult Whisper Dragon
```
