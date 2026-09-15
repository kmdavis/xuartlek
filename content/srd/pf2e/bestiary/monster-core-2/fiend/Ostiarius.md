---
noteType: pf2eMonster
aliases: "Ostiarius"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/velstrac
  - pf2e/creature/trait/medium
statblock: inline
name: "Ostiarius"
level: 5
source: "Monster Core 2"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4607"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Ostiarius"
level: "Creature 5"
size: "Medium"
trait_01: "Fiend"
trait_02: "Unholy"
trait_03: "Velstrac"
modifier: 15
perception:
  - name: "Perception"
    desc: "+15; greater darkvision, painsight, sense portal"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/Languages#Shadowtongue|Shadowtongue]]; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +13, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +12, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +12, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +16, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +11, [[srd/pf2e/compendium/rules-elements/skills/Lore|Torture Lore]] +11"
abilityMods: [0, 4, 2, 2, 4, 5]
abilities_top:
  - name: "Painsight"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]]) A velstrac automatically knows whether a creature it sees has any of the [[srd/pf2e/compendium/rules-elements/Conditions#Doomed|doomed]], [[srd/pf2e/compendium/rules-elements/Conditions#Dying|dying]], and [[srd/pf2e/compendium/rules-elements/Conditions#Wounded|wounded]] conditions as well as the value of those conditions."
  - name: "Sense Portal"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]]) The ostiarius always knows the direction and distance to the closest portal between [[srd/pf2e/compendium/gm/Planes#The Netherworld|the Netherworld]] and [[srd/pf2e/compendium/gm/Planes#The Universe|the Universe]]. This sense functions only on these two planes."
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +9; __Ref__: +15; __Will__: +13 +1 status to all saves vs. magic"
hp: 65
health:
  - name: "HP"
    desc: "65 , regeneration 5 (deactivated by [[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|holy]] or [[srd/pf2e/compendium/equipment/materials/Silver|silver]]); __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Cold|cold]]; __Weaknesses__ holy 5, silver 5"
abilities_mid:
  - name: "Whispering Wounds"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Visual|visual]]) 30 feet. When a creature ends its turn in the aura, it hears the wounds on the ostiarius's body whisper obscene truths. The creature must succeed at a DC 21 Will save or become [[srd/pf2e/compendium/rules-elements/Conditions#Sickened|sickened]] 1."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +13 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|unholy]]) __Damage__ 2d6+2 slashing plus 2d6 [[srd/pf2e/compendium/rules-elements/Conditions#Persistent Damage|persistent bleed]]"
abilities_bot:
  - name: "Compel Courage"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Linguistic|linguistic]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]]) The ostiarius inspires their willing allies and themself by whispering words of courage from their wounds. The ostiarius and their allies in a 50-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Area#Emanation|emanation]] gain a +1 status bonus to attack rolls, damage rolls, and saves against fear effects. The ostiarius can [[srd/pf2e/compendium/rules-elements/actions/player-core#Sustain an Effect|Sustain]] Compel Courage. Non-velstracs who accept this compelled courage find bleeding wounds opening on their own bodies to whisper in thanks. They take 1 [[srd/pf2e/compendium/rules-elements/Conditions#Persistent Damage|persistent bleed damage]] and can't attempt a flat check to end this damage as long as they're compelled."
  - name: "Focus Gaze"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Fear|fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Visual|visual]]) The ostiarius stares at a creature they can see within 30 feet. The creature must immediately attempt a Will save against whispering wounds. In addition, if the creature was already [[srd/pf2e/compendium/rules-elements/Conditions#Sickened|sickened]] and fails its save, the creature is [[srd/pf2e/compendium/rules-elements/Conditions#Fascinated|fascinated]] by the ostiarius and can't use [[srd/pf2e/books/player-core/chapter-7-spells/Hostile Actions|hostile actions]]. This fascination lasts for 1 round or until the ostiarius takes any hostile action against the creature or the creature's allies. Whether the creature succeeds at or fails the save, it's temporarily immune to Focus Gaze for 1 hour."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 24 - __Cantrips (3rd)__ [[srd/pf2e/compendium/spells/cantrips/Shield|Shield]] - __2nd__ [[srd/pf2e/compendium/spells/rank-2/Calm|Calm]] (at will), [[srd/pf2e/compendium/spells/rank-2/Darkness|Darkness]], [[srd/pf2e/compendium/spells/rank-2/Silence|Silence]] - __3rd__ [[srd/pf2e/compendium/spells/rank-3/Enthrall|Enthrall]], [[srd/pf2e/compendium/spells/rank-3/Safe Passage|Safe Passage]]"
  - name: "Rituals"
    desc: "DC 22 - __2nd__ [[srd/pf2e/compendium/spells/rituals/Inveigle|Inveigle]]"
sourcebook: "_Monster Core 2_, page 345."
```

```encounter-table
name: Ostiarius
creatures:
  - 1: Ostiarius
```
