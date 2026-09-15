---
noteType: pf2eMonster
aliases: "Akizendri"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/monitor
  - pf2e/creature/trait/protean
  - pf2e/creature/trait/small
statblock: inline
name: "Akizendri"
level: 3
source: "Monster Core 2"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4517"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Akizendri"
level: "Creature 3"
size: "Small"
trait_01: "Monitor"
trait_02: "Protean"
modifier: 8
perception:
  - name: "Perception"
    desc: "+8; darkvision, entropy sense (imprecise) 30 feet"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Chthonian|Chthonian]], [[srd/pf2e/compendium/rules-elements/Languages#Empyrean|Empyrean]], Protean; telepathy (touch only)"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +9, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +9, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +10, [[srd/pf2e/compendium/rules-elements/skills/Occultism|Occultism]] +11, [[srd/pf2e/compendium/rules-elements/skills/Society|Society]] +10, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +9, [[srd/pf2e/compendium/rules-elements/skills/Thievery|Thievery]] +9"
abilityMods: [3, 4, 1, 4, 3, 1]
abilities_top:
  - name: "Entropy Sense"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Prediction|prediction]]) An akizendri can anticipate the most likely presence of a creature through a supernatural insight into chaotic probabilities and chance. This grants them the ability to sense creatures within the listed range. [[srd/pf2e/compendium/spells/rank-3/Veil of Privacy|_Veil of privacy_]] prevents a creature from being detected via entropy sense automatically (without a counteract check)."
ac: 19
armorclass:
  - name: "AC"
    desc: "19; __Fort__: +6; __Ref__: +11; __Will__: +10"
hp: 40
health:
  - name: "HP"
    desc: "40 (fast healing 1); __Resistances__ precision 3, protean anatomy 6"
abilities_mid:
  - name: "Protean Anatomy"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]]) A protean's vital organs shift and change shape and position constantly. Immediately after the protean takes acid, electricity, or sonic damage, they gain the listed amount of resistance to that damage type. This lasts for 1 hour or until the next time the protean takes damage of one of the other types (in which case their resistance changes to match that type), whichever comes first. The protean is immune to polymorph effects unless they're a willing target. If [[srd/pf2e/compendium/rules-elements/Conditions#Blinded|blinded]] or [[srd/pf2e/compendium/rules-elements/Conditions#Deafened|deafened]], the protean automatically recovers at the end of their next turn as new sensory organs grow to replace the compromised ones."
speed: "25 feet, fly 25 feet, swim 25 feet; unfettered movement"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +12 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]]) __Damage__ 2d8+3 piercing plus garbled thoughts"
  - name: "Melee"
    desc: "⬻ tail +12 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]]) __Damage__ 2d6+3 bludgeoning plus Grab"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Polymorph|Polymorph]]) The akizendri takes on the appearance of any Small or smaller creature (page 360). This doesn't change its Speed or its attack and damage bonuses with its Strikes, but might change the damage type its Strikes deal."
  - name: "Constrict"
    desc: "⬻ 1d8+3 bludgeoning, DC 20"
  - name: "Garbled Thoughts"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|Mental]]) A creature hit by the akizendri's bite Strike must attempt a DC 20 Will save."
  - name: "Success"
    desc: "The creature is unaffected."
  - name: "Failure"
    desc: "The creature is [[srd/pf2e/compendium/rules-elements/Conditions#Stupefied|stupefied 1]] for 1d4 rounds."
  - name: "Critical Failure"
    desc: "As failure, but the creature is also [[srd/pf2e/compendium/rules-elements/Conditions#Confused|confused]] for 1 round."
  - name: "Text Immersion"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]]) As a 1-minute activity, the akizendri physically immerses itself in a page of text it's touching, changing the message of the text in the process. It can exit the book at any point by Dismissing this ability, at which point it appears in a space adjacent to the text. If it does so to begin combat, it rolls a [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] check for initiative. As long as it remains immersed in the text, the akizendri has no body. It can communicate telepathically with a creature as long as the creature touches the book or scroll that contains it. It can sense nearby creatures using its entropy sense, but not in any other way, nor can it use any [[srd/pf2e/compendium/rules-elements/traits/player-core/Attack|attack]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Manipulate|manipulate]], or [[srd/pf2e/compendium/rules-elements/traits/player-core/Move|move]] actions or speak aloud. If the object it's immersed in is destroyed, the akizendri reappears in an adjacent square and is [[srd/pf2e/compendium/rules-elements/Conditions#Stunned|stunned 1]]. Andals Of Chaos Those who seek secret knowledge beyond their means can bargain with akizendris to provide them with rare tomes in exchange for delivering the immersed akizendri into a library via another book. From there, the akizendri can vandalize books to its heart's content without being detected."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 20, attack +12 - __Cantrips (2nd)__ [[srd/pf2e/compendium/spells/cantrips/Caustic Blast|Caustic Blast]], [[srd/pf2e/compendium/spells/cantrips/Daze|Daze]], [[srd/pf2e/compendium/spells/cantrips/Figment|Figment]], [[srd/pf2e/compendium/spells/cantrips/Sigil|Sigil]], [[srd/pf2e/compendium/spells/cantrips/Telekinetic Hand|Telekinetic Hand]] - __3rd__ [[srd/pf2e/compendium/spells/rank-2/Dispel Magic|Dispel Magic]] - __Constant (4th)__ [[srd/pf2e/compendium/spells/rank-4/Unfettered Movement|Unfettered Movement]]"
sourcebook: "_Monster Core 2_, page 258."
```

```encounter-table
name: Akizendri
creatures:
  - 1: Akizendri
```
