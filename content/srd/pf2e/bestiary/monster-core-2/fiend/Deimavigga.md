---
noteType: pf2eMonster
aliases: "Deimavigga"
tags:
  - pf2e/creature/level/17
  - pf2e/creature/trait/devil
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Deimavigga"
level: 17
source: "Monster Core 2"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4330"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Deimavigga"
level: "Creature 17"
size: "Medium"
trait_01: "Devil"
trait_02: "Fiend"
trait_03: "Unholy"
modifier: 32
perception:
  - name: "Perception"
    desc: "+32; (36 to [[srd/pf2e/compendium/rules-elements/actions/player-core#Sense Motive|Sense Motive]]) greater darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Chthonian|Chthonian]], [[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/Languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/Languages#Empyrean|Empyrean]]; indomitable oration, telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +29, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +34, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +36, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +30, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +30, [[srd/pf2e/compendium/rules-elements/skills/Society|Society]] +27, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +33"
abilityMods: [7, 8, 6, 4, 7, 9]
abilities_top:
  - name: "Indomitable Oration"
    desc: "Any creature capable of comprehending speech understands the deimavigga, as if they constantly spoke in all languages at once."
  - name: "Items"
    desc: "_[[srd/pf2e/compendium/equipment/armor/Magic Armor|+2 resilient]] [[srd/pf2e/compendium/equipment/runes/Raiment|raiment]] [[srd/pf2e/compendium/equipment/Armor#Full Plate|full plate]]_"
ac: 40
armorclass:
  - name: "AC"
    desc: "40; __Fort__: +27; __Ref__: +29; __Will__: +32 +1 status to all saves vs. magic"
hp: 285
health:
  - name: "HP"
    desc: "285; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Fire|fire]]; __Resistances__ physical 15 (except [[srd/pf2e/compendium/equipment/materials/Silver|silver]]); __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|holy]] 15"
abilities_mid:
  - name: "Whispers of Discord"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature within 60 feet is targeted by a spell that would restore Hit Points or provide a status bonus (the deimavigga automatically recognizes such effects)"
  - name: "Effect"
    desc: "The deimavigga whispers disturbing lies, audible only to the target, to shake the target's faith in the spell's caster. The target must attempt a DC 38 Will save."
  - name: "Critical Success"
    desc: "The target disbelieves the lies and receives the intended benefit of the spell; the target becomes temporarily immune to Whispers of Discord for 24 hours."
  - name: "Success"
    desc: "As critical success, but the target isn't temporarily immune."
  - name: "Failure"
    desc: "The spell fails to affect the target. The target refuses all [[srd/pf2e/compendium/rules-elements/actions/player-core#Aid|aid]] from that caster for 1 round and doesn't count as the caster's ally."
  - name: "Critical Failure"
    desc: "As failure, but the duration is 1 minute."
speed: "30 feet, fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +33 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|unholy]]) __Damage__ 3d8+18 slashing"
abilities_bot:
  - name: "Boundless Reach"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Teleportation|teleportation]]) A deimavigga's razor-sharp claws can slice through reality, allowing them to make claw Strikes and use spells with a range of touch against any creature they can see directly or via magic. A creature targeted in this way can retaliate until the start of the deimavigga's next turn; it can target the devil's claws as if the devil were physically present and adjacent to the target, though the claws are [[srd/pf2e/compendium/rules-elements/Conditions#Concealed|concealed]]."
  - name: "Change Shape"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Polymorph|polymorph]]) The deimavigga can take on the appearance of any humanoid. This doesn't change their Speed or attack and damage bonuses with Strikes, but it might change the damage type their Strikes deal (typically to bludgeoning)."
  - name: "Whisper Earworm"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]]) The deimavigga whispers a terrifying multiversal truth to one adjacent creature, shaking its faith in reality and divinity. The target must attempt a DC 38 Will save. [[srd/pf2e/compendium/rules-elements/traits/player-core/Celestial|Celestials]] and [[srd/pf2e/compendium/rules-elements/traits/player-core/Fiend|fiends]] gain a +2 status bonus to this save."
  - name: "Critical Success"
    desc: "The target is unaffected and temporarily immune to Whisper Earworm for 24 hours."
  - name: "Success"
    desc: "The target is unaffected."
  - name: "Failure"
    desc: "The next time the target rests, it ruminates on the deimavigga's words instead of sleeping or otherwise resting and awakens fatigued. The target also becomes [[srd/pf2e/compendium/rules-elements/Conditions#Drained|drained]] 1 and [[srd/pf2e/compendium/rules-elements/Conditions#Stupefied|stupefied]] 1 until it's no longer fatigued."
  - name: "Critical Failure"
    desc: "As failure, but drained 2. After this rest, the target must attempt another DC 38 Will save. On a failure, the target becomes stupefied 2 and takes a –4 status penalty to Will saves against effects from unholy creatures. These effects last until the target unlearns the truth spoken by the deimavigga, requiring a rewrite memory spell, other means of modifying their memory, or powerful magic such as a [[srd/pf2e/compendium/spells/rituals/Wish|_wish_]] ritual. Lore Operators While most devils perform a specialized role within a complex infernal machine, deimaviggas work almost exclusively alone, as they find even the most obedient minions a hindrance to their stratagems."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 38, attack +34 - __3rd__ [[srd/pf2e/compendium/spells/rank-3/Dream Message|Dream Message]] (at will) - __4th__ [[srd/pf2e/compendium/spells/rank-4/Translocate|Translocate]] (at will) - __7th__ [[srd/pf2e/compendium/spells/rank-1/Illusory Disguise|Illusory Disguise]], [[srd/pf2e/compendium/spells/rank-6/Scrying|Scrying]], [[srd/pf2e/compendium/spells/rank-2/Stupefy|Stupefy]] (at will), [[srd/pf2e/compendium/spells/rank-4/Translocate|Translocate]], [[srd/pf2e/compendium/spells/rank-7/Warp Mind|Warp Mind]] - __9th__ [[srd/pf2e/compendium/spells/rank-7/Divine Decree|Divine Decree]], [[srd/pf2e/compendium/spells/rank-6/Dominate|Dominate]], [[srd/pf2e/compendium/spells/rank-5/Illusory Scene|Illusory Scene]] (at will)"
  - name: "Rituals"
    desc: "DC 43 - __1st__ [[srd/pf2e/compendium/spells/rituals/Diabolic Pact|Diabolic Pact]]"
sourcebook: "_Monster Core 2_, page 102."
```

```encounter-table
name: Deimavigga
creatures:
  - 1: Deimavigga
```
