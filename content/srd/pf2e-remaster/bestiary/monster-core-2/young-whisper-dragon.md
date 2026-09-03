---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Young Whisper Dragon"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/occult
  - pf2e/creature/trait/large
statblock: inline
name: "Young Whisper Dragon"
level: 7
source: "Monster Core 2"
aon_id: "creature-4366"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4366"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Young Whisper Dragon"
level: "Creature 7"
size: "Large"
trait_01: "Dragon"
trait_02: "Occult"
modifier: 15
perception:
  - name: "Perception"
    desc: "Perception +15; (17 to Sense Motive) darkvision, scent (imprecise) 60 feet"
languages: "Common, Draconic, Empyrean, Fey; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +12, Athletics +14, Deception +13, Diplomacy +15, Intimidation +13, Occultism +15, Society +17, Stealth +14, Underworld Lore +17"
abilityMods: [4, 2, 3, 3, 2, 3]
abilities_top:
  - name: "Information Network"
    desc: "The dragon can attempt a Society check to Recall Knowledge in place of a check to Gather Information, recalling intelligence from prior informants."
ac: 25
armorclass:
  - name: "AC"
    desc: "25; __Fort__: +15; __Ref__: +13; __Will__: +18 +2 status to all saves vs. occult"
hp: 110
health:
  - name: "HP"
    desc: "110; __Immunities__ confused, paralyzed, sleep"
abilities_mid:
  - name: "Diplomatic Solution"
    desc: "⭓ (emotion, incapacitation, mental, occult)"
  - name: "Trigger"
    desc: "The dragon rolls initiative"
  - name: "Effect"
    desc: "The dragon targets all enemies it can see within 60 feet with _calm_ heightened to a rank equal to half the dragon's level rounded up (DC 23 Will save). The dragon doesn't need to Sustain this effect, but if the dragon takes any hostile action against those affected, it breaks the effect for all creatures."
  - name: "Distracting Whisper"
    desc: "⬲ (mental, occult)"
  - name: "Trigger"
    desc: "The dragon is targeted with an attack"
  - name: "Effect"
    desc: "A mysterious voice whispers something disconcerting in the triggering creature's ear, inflicting a –2 circumstance penalty to the triggering attack."
speed: "40 feet, fly 140 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +18 (Magical, reach 10 feet) __Damage__ 2d10+6 piercing"
  - name: "Melee"
    desc: "⬻ claw +18 (Agile, magical) __Damage__ 2d8+6 slashing"
  - name: "Melee"
    desc: "⬻ tail +16 (Magical, reach 15 feet) __Damage__ 2d8+6 bludgeoning"
abilities_bot:
  - name: "Cogitation Breath"
    desc: "⬺ (Mental, occult) The dragon unleashes a befuddling miasma, dealing 6d6 mental damage in a 30-foot cone (DC 25 basic Will save). A creature that fails its save is stupefied 1 (stupefied 2 on a critical failure) for 1 minute. The dragon can't use Cogitation Breath again for 1d4 rounds."
  - name: "Draconic Frenzy"
    desc: "⬺ The dragon makes two claw Strikes and one tail Strike in any order."
  - name: "Steal Knowledge"
    desc: "⬻ (Concentrate, mental, occult) The dragon plucks a fragment of knowledge from the mind of a creature within 60 feet, choosing a skill to affect. The creature must attempt a DC 23 Will save."
  - name: "Success"
    desc: "The creature is unaffected."
  - name: "Failure"
    desc: "For the next minute, the creature takes a –1 status penalty to checks using that skill, and the dragon gets a +1 status bonus to using that skill."
  - name: "Critical Failure"
    desc: "As failure, but the penalty is –2 and the bonus is +2."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 25 - __Cantrips (4th)__ Daze, Message - __2nd__ Embed Message - __3rd__ Clairaudience (at will) - __4th__ Charm, Clairvoyance (at will), Suggestion"
sourcebook: "_Monster Core 2_, page 133."
```

```encounter-table
name: Young Whisper Dragon
creatures:
  - 1: Young Whisper Dragon
```
