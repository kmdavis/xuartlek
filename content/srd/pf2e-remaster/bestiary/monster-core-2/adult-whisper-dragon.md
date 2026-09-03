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
    desc: "Perception +21; (23 to Sense Motive) darkvision, scent (imprecise) 60 feet"
languages: "Common, Draconic, Empyrean, Fey; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +17, Athletics +19, Deception +18, Diplomacy +20, Intimidation +18, Occultism +21, Society +23, Stealth +19, Underworld Lore +23"
abilityMods: [5, 3, 4, 7, 4, 6]
abilities_top:
  - name: "Information Network"
    desc: "The dragon can attempt a Society check to Recall Knowledge in place of a check to Gather Information, recalling intelligence from prior informants."
ac: 31
armorclass:
  - name: "AC"
    desc: "31; __Fort__: +21; __Ref__: +19; __Will__: +24 +2 status to all saves vs. occult"
hp: 190
health:
  - name: "HP"
    desc: "190; __Immunities__ confused, paralyzed, sleep"
abilities_mid:
  - name: "Diplomatic Solution"
    desc: "⭓ (emotion, incapacitation, mental, occult)"
  - name: "Trigger"
    desc: "The dragon rolls initiative"
  - name: "Effect"
    desc: "The dragon targets all enemies it can see within 60 feet with _calm_ heightened to a rank equal to half the dragon's level rounded up (DC 28 Will save). The dragon doesn't need to Sustain this effect, but if the dragon takes any hostile action against those affected, it breaks the effect for all creatures."
  - name: "Distracting Whisper"
    desc: "⬲ (mental, occult)"
  - name: "Trigger"
    desc: "The dragon is targeted with an attack"
  - name: "Effect"
    desc: "A mysterious voice whispers something disconcerting in the triggering creature's ear, inflicting a –2 circumstance penalty to the triggering attack."
speed: "50 feet, fly 170 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +24 (Magical, reach 10 feet) __Damage__ 2d12+11 piercing"
  - name: "Melee"
    desc: "⬻ claw +24 (Agile, magical) __Damage__ 2d10+11 slashing"
  - name: "Melee"
    desc: "⬻ tail +22 (Magical, reach 15 feet) __Damage__ 2d10+11 bludgeoning"
abilities_bot:
  - name: "Cogitation Breath"
    desc: "⬺ (Mental, occult) The dragon unleashes a befuddling miasma, dealing 10d6 mental damage in a 30-foot cone (DC 30 basic Will save). A creature that fails its save is stupefied 1 (stupefied 2 on a critical failure) for 1 minute. The dragon can't use Cogitation Breath again for 1d4 rounds."
  - name: "Draconic Frenzy"
    desc: "⬺ The dragon makes two claw Strikes and one tail Strike in any order."
  - name: "Draconic Momentum"
    desc: "The dragon recharges their Cogitation Breath whenever they score a critical hit with a Strike."
  - name: "Steal Knowledge"
    desc: "⬻ (Concentrate, mental, occult) The dragon plucks a fragment of knowledge from the mind of a creature within 60 feet, choosing a skill to affect. The creature must attempt a DC 28 Will save."
  - name: "Success"
    desc: "The creature is unaffected."
  - name: "Failure"
    desc: "For the next minute, the creature takes a –1 status penalty to checks using that skill, and the dragon gets a +1 status bonus to using that skill."
  - name: "Critical Failure"
    desc: "As failure, but the penalty is –2 and the bonus is +2."
  - name: "Unveil Secret"
    desc: "⬺ (Fear, mental, occult) The dragon delves into the mind of a creature within 60 feet to scour for secrets, learning something the creature would find embarrassing or shameful unless they succeed a DC 30 Will save. The target becomes frightened 1 and can't reduce their frightened condition for 1 minute or until the dragon reveals the secret. As a reaction when the affected creature attempts a check, the dragon can reveal their secret to discomfit them, requiring them to roll twice and take the lower result; this is a misfortune effect."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 30 - __Cantrips (6th)__ Daze, Message - __2nd__ Embed Message - __3rd__ Clairaudience (at will), Mind Reading, Ring of Truth - __4th__ Clairvoyance (at will) - __5th__ Mind Probe - __6th__ Charm, Suggestion"
sourcebook: "_Monster Core 2_, page 134."
```

```encounter-table
name: Adult Whisper Dragon
creatures:
  - 1: Adult Whisper Dragon
```
