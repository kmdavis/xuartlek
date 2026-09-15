---
noteType: pf2eMonster
aliases: "Weaver Of Webs"
tags:
  - pf2e/creature/level/15
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/mythic
  - pf2e/creature/trait/unique
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Weaver Of Webs"
level: 15
source: "War of Immortals"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3410"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "WoI"
name: "Weaver Of Webs"
level: "Creature 15"
size: "Gargantuan"
trait_01: "Beast"
trait_02: "Mythic"
trait_03: "Unique"
modifier: 32
perception:
  - name: "Perception"
    desc: "+32; all-around vision, greater darkvision, tremorsense (imprecise)"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Aklo|Aklo]], [[srd/pf2e/compendium/rules-elements/Languages#Chthonian|Chthonian]], [[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/Languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/Languages#Dwarven|Dwarven]], [[srd/pf2e/compendium/rules-elements/Languages#Empyrean|Empyrean]], [[srd/pf2e/compendium/rules-elements/Languages#Jotun|Jotun]], [[srd/pf2e/compendium/rules-elements/Languages#Sakvroth|Sakvroth]]; truespeech"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +25, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +30, [[srd/pf2e/compendium/rules-elements/skills/Crafting|Crafting]] +21, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +30, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +27, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +30, [[srd/pf2e/compendium/rules-elements/skills/Nature|Nature]] +25, [[srd/pf2e/compendium/rules-elements/skills/Occultism|Occultism]] +27, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +27, [[srd/pf2e/compendium/rules-elements/skills/Society|Society]] +27, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +30"
abilityMods: [6, 4, 6, 8, 6, 6]
abilities_top:
  - name: "Countless Eyes"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Scrying|scrying]]) The Weaver of Webs can see through the eyes of any spider, living or dead, in one of her many lairs. When the Weaver casts her [[srd/pf2e/compendium/spells/rank-6/Scrying|_scrying_]] spell and targets a spider in her lair, the spell is not expended, and the spider automatically critically fails its saving throw."
  - name: "Greater Web Sense"
    desc: "The Weaver of Webs' tremorsense also extends to any of her webs, regardless of distance or area, and her tremorsense is a precise sense against any creature in contact with one of her webs."
ac: 36
armorclass:
  - name: "AC"
    desc: "36; __Fort__: +26; __Ref__: +23; __Will__: +29"
hp: 335
health:
  - name: "HP"
    desc: "335 , regeneration 10 (deactivated by bright light); __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|poison]]; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Cold|cold]] 10, mythic resistance 15, [[srd/pf2e/compendium/rules-elements/traits/player-core/Void|void]] 10"
abilities_mid:
  - name: "Mythic Resistance"
    desc: "The Weaver of Webs has resistance 15 to all attacks made with non-[[srd/pf2e/compendium/rules-elements/traits/war-of-immortals/Mythic|mythic]] weapons and unarmed attacks made by non-mythic creatures."
  - name: "Spilled Secrets"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]]) 60 feet. Any creature that speaks within this aura must succeed at a DC 34 Will save or divulge some kind of secret instead of whatever speech they intended. [[srd/pf2e/compendium/rules-elements/traits/player-core/Linguistic|Linguistic]] spells and effects gain the [[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|concentrate]] trait if they didn't have it already and are wasted if the creature fails this save. On a critical failure, the character betrays a secret they least want to reveal to the Weaver or those present."
  - name: "Adopted Brood"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature deals precision damage to the Weaver"
  - name: "Effect"
    desc: "A spray of smaller spiders pours out of the open wound. These spiders deal 3d6 piercing damage to a single creature within 15 feet of the Weaver and expose that creature to Weaver venom before skittering away."
speed: "60 feet, climb 60 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fangs +28 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 10 feet]]) __Damage__ 2d8+16 piercing plus Weaver venom"
  - name: "Melee"
    desc: "⬻ tarsal claw +28 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 15 feet]]) __Damage__ 2d6+16 slashing plus Improved Grab"
  - name: "Ranged"
    desc: "⬻ web +24 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], range 120 feet) __Damage__ 4d4+10 bludgeoning plus nightmare cocoon and Weaver venom"
abilities_bot:
  - name: "Mythic Power"
    desc: "3 Mythic Points _Remove a Condition_ ⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|concentrate]])"
  - name: "Cost"
    desc: "1 Mythic Point"
  - name: "Effect"
    desc: "The Weaver removes any one condition currently affecting her."
  - name: "Nightmare Cocoon"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Incapacitation|Incapacitation]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|Mental]]) A creature struck by the Weaver's web Strike must succeed at a DC 34 Reflex save or become [[srd/pf2e/compendium/rules-elements/Conditions#Immobilized|immobilized]] ([[srd/pf2e/compendium/rules-elements/actions/player-core#Escape|Escape]] DC 34). If the Weaver spends 1 Mythic Point as a free action when a creature fails this save, the creature is also [[srd/pf2e/compendium/rules-elements/Conditions#Paralyzed|paralyzed]], experiencing terrible nightmares of their deepest-held anxieties. The Weaver can view these dreams using a Sustain action, which imparts a –2 circumstance penalty to any Will saves the target attempts against the Weaver's spells until the beginning of the Weaver's next turn. At the end of a paralyzed victim's turn, they can attempt a DC 34 Will save to end the paralyzed condition (though they are still immobilized until they Escape)."
  - name: "Weaver Venom"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|Poison]])"
  - name: "Saving Throw"
    desc: "DC 34"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "2d10 poison (1 round)"
  - name: "Stage 2"
    desc: "2d10 poison and [[srd/pf2e/compendium/rules-elements/Conditions#Slowed|slowed 1]] (2 rounds)"
  - name: "Stage 3"
    desc: "3d10 poison and slowed 2 (1 round)"
  - name: "Stage 4"
    desc: "4d10 poison (1 round) and the target permanently forgets the Weaver exists, including any previous mention of her."
  - name: "Webbed Conveyance"
    desc: "⬻"
  - name: "Requirements"
    desc: "The Weaver is within 15 feet of a creature [[srd/pf2e/compendium/rules-elements/Conditions#Paralyzed|paralyzed]] in her nightmare cocoon"
  - name: "Effect"
    desc: "The Weaver grabs the paralyzed target, webs them to her back or one of her legs, and then Strides. As long as the creature is immobilized by the Weaver's nightmare cocoon, it shares the Weaver's space and moves with her. The DC to Escape the nightmare cocoon increases to 36."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 36, attack +28 - __2nd__ [[srd/pf2e/compendium/spells/rank-2/See the Unseen|See the Unseen]] (at will) - __3rd__ [[srd/pf2e/compendium/spells/rank-3/Dream Message|Dream Message]], [[srd/pf2e/compendium/spells/rank-1/Fear|Fear]], [[srd/pf2e/compendium/spells/rank-3/Mind Reading|Mind Reading]] - __4th__ [[srd/pf2e/compendium/spells/rank-2/Darkness|Darkness]] (at will), [[srd/pf2e/compendium/spells/rank-2/Invisibility|Invisibility]], [[srd/pf2e/compendium/spells/rank-4/Nightmare|Nightmare]], [[srd/pf2e/compendium/spells/rank-4/Read Omens|Read Omens]], [[srd/pf2e/compendium/spells/rank-2/Web|Web]] (at will) - __5th__ [[srd/pf2e/compendium/spells/rank-5/Sending|Sending]] (at will) - __6th__ [[srd/pf2e/compendium/spells/rank-6/Phantasmal Calamity|Phantasmal Calamity]], [[srd/pf2e/compendium/spells/rank-6/Repulsion|Repulsion]], [[srd/pf2e/compendium/spells/rank-6/Scrying|Scrying]], [[srd/pf2e/compendium/spells/rank-6/Teleport|Teleport]] - __7th__ [[srd/pf2e/compendium/spells/rank-7/Retrocognition|Retrocognition]], [[srd/pf2e/compendium/spells/rank-7/Warp Mind|Warp Mind]] - __8th__ [[srd/pf2e/compendium/spells/rank-8/Dream Council|Dream Council]] - __Constant (7th)__ [[srd/pf2e/compendium/spells/rank-5/Truespeech|Truespeech]]"
sourcebook: "_War of Immortals_, page 214."
```

```encounter-table
name: Weaver Of Webs
creatures:
  - 1: Weaver Of Webs
```
