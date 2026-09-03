---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Ancient Whisper Dragon"
tags:
  - pf2e/creature/level/16
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/occult
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/huge
statblock: inline
name: "Ancient Whisper Dragon"
level: 16
source: "Monster Core 2"
aon_id: "creature-4368"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4368"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Ancient Whisper Dragon"
level: "Creature 16"
size: "Huge"
trait_01: "Dragon"
trait_02: "Occult"
trait_03: "Uncommon"
modifier: 28
perception:
  - name: "Perception"
    desc: "Perception +28; (30 to Sense Motive) darkvision, scent (imprecise) 60 feet"
languages: "Common, Draconic, Empyrean, Fey; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +27, Athletics +29, Deception +28, Diplomacy +30, Intimidation +28, Occultism +31, Society +35, Stealth +29, Underworld Lore +35"
abilityMods: [7, 5, 6, 9, 6, 8]
abilities_top:
  - name: "Information Network"
    desc: "The dragon can attempt a Society check to Recall Knowledge in place of a check to Gather Information, recalling intelligence from prior informants."
ac: 39
armorclass:
  - name: "AC"
    desc: "39; __Fort__: +28; __Ref__: +26; __Will__: +30 +2 status to all saves vs. occult, _hidden mind_"
hp: 290
health:
  - name: "HP"
    desc: "290; __Immunities__ confused, paralyzed, sleep"
abilities_mid:
  - name: "Diplomatic Solution"
    desc: "⭓ (emotion, incapacitation, mental, occult)"
  - name: "Trigger"
    desc: "The dragon rolls initiative"
  - name: "Effect"
    desc: "The dragon targets all enemies it can see within 60 feet with _calm_ heightened to a rank equal to half the dragon's level rounded up (DC 35 Will save). The dragon doesn't need to Sustain this effect, but if the dragon takes any hostile action against those affected, it breaks the effect for all creatures."
  - name: "Distracting Whisper"
    desc: "⬲ (mental, occult)"
  - name: "Trigger"
    desc: "The dragon is targeted with an attack"
  - name: "Effect"
    desc: "A mysterious voice whispers something disconcerting in the triggering creature's ear, inflicting a –2 circumstance penalty to the triggering attack."
speed: "60 feet, fly 200 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +32 (Magical, reach 15 feet) __Damage__ 3d12+15 piercing"
  - name: "Melee"
    desc: "⬻ claw +32 (Agile, magical, reach 10 feet) __Damage__ 3d10+15 slashing"
  - name: "Melee"
    desc: "⬻ tail +30 (Magical, reach 20 feet) __Damage__ 3d10+15 bludgeoning"
abilities_bot:
  - name: "Cogitation Breath"
    desc: "⬺ (Mental, occult) The dragon unleashes a befuddling miasma, dealing 15d6 mental damage in a 50-foot cone (DC 37 basic Will save). A creature that fails its save is stupefied 1 (stupefied 2 on a critical failure) for 1 minute. The dragon can't use Cogitation Breath again for 1d4 rounds."
  - name: "Draconic Frenzy"
    desc: "⬺ The dragon makes two claw Strikes and one tail Strike in any order."
  - name: "Draconic Momentum"
    desc: "The dragon recharges their Cogitation Breath whenever they score a critical hit with a Strike."
  - name: "Steal Knowledge"
    desc: "⬻ (Concentrate, mental, occult) The dragon plucks a fragment of knowledge from the mind of a creature within 60 feet, choosing a skill to affect. The creature must attempt a DC 35 Will save."
  - name: "Success"
    desc: "The creature is unaffected."
  - name: "Failure"
    desc: "For the next minute, the creature takes a –1 status penalty to checks using that skill, and the dragon gets a +1 status bonus to using that skill."
  - name: "Critical Failure"
    desc: "As failure, but the penalty is –2 and the bonus is +2."
  - name: "Thought Whispers"
    desc: "⬺ (Mental, occult)"
  - name: "Frequency"
    desc: "once per minute"
  - name: "Effect"
    desc: "The dragon sends their mind out to seek others' thoughts, affecting all creatures within 60 feet with _mind reading_ (Will DC 37)."
  - name: "Unveil Secret"
    desc: "⬺ (Fear, mental, occult) The dragon delves into the mind of a creature within 60 feet to scour for secrets, learning something the creature would find embarrassing or shameful unless they succeed a DC 37 Will save. The target becomes frightened 1 and can't reduce their frightened condition for 1 minute or until the dragon reveals the secret. As a reaction when the affected creature attempts a check, the dragon can reveal their secret to discomfit them, requiring them to roll twice and take the lower result; this is a misfortune effect."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 37 - __Cantrips (8th)__ Daze, Message - __2nd__ Embed Message - __3rd__ Clairaudience (at will), Mind Reading (at will), Ring of Truth - __4th__ Clairvoyance (at will) - __5th__ Mind Probe - __6th__ Retrocognition - __8th__ Charm, Suggestion - __Constant (8th)__ Hidden Mind"
sourcebook: "_Monster Core 2_, page 135."
```

```encounter-table
name: Ancient Whisper Dragon
creatures:
  - 1: Ancient Whisper Dragon
```
