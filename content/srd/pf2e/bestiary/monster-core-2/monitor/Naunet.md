---
noteType: pf2eMonster
aliases: "Naunet"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/monitor
  - pf2e/creature/trait/protean
  - pf2e/creature/trait/large
statblock: inline
name: "Naunet"
level: 7
source: "Monster Core 2"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4518"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Naunet"
level: "Creature 7"
size: "Large"
trait_01: "Monitor"
trait_02: "Protean"
modifier: 14
perception:
  - name: "Perception"
    desc: "+14; darkvision, entropy sense (imprecise) 30 feet"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Chthonian|Chthonian]], [[srd/pf2e/compendium/rules-elements/Languages#Empyrean|Empyrean]], Protean"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +14, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +16, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +16, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +14, [[srd/pf2e/compendium/rules-elements/skills/Survival|Survival]] +12"
abilityMods: [5, 3, 5, 0, 3, 3]
abilities_top:
  - name: "Entropy Sense"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Prediction|prediction]]) A protean can anticipate the most likely presence of a creature through a supernatural insight into chaotic probabilities and chance. This grants them the ability to sense creatures within the listed range. [[srd/pf2e/compendium/spells/rank-3/Veil of Privacy|_Veil of privacy_]] prevents a creature from being detected via entropy sense automatically (without a counteract check)."
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +18; __Ref__: +14; __Will__: +12 +1 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magic]]"
hp: 120
health:
  - name: "HP"
    desc: "120 (fast healing 2); __Resistances__ precision 5, protean anatomy 10"
abilities_mid:
  - name: "Protean Anatomy"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]]) A protean's vital organs shift and change shape and position constantly. Immediately after the protean takes acid, electricity, or sonic damage, they gain the listed amount of resistance to that damage type. This lasts for 1 hour or until the next time the protean takes damage of one of the other types (in which case their resistance changes to match that type), whichever comes first. The protean is immune to polymorph effects unless they're a willing target. If [[srd/pf2e/compendium/rules-elements/Conditions#Blinded|blinded]] or [[srd/pf2e/compendium/rules-elements/Conditions#Deafened|deafened]], the protean automatically recovers at the end of their next turn as new sensory organs grow to replace the compromised ones."
speed: "25 feet, fly 30 feet, swim 25 feet; unfettered movement"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +18 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 10 feet]]) __Damage__ 2d10+8 piercing"
  - name: "Melee"
    desc: "⬻ tail +18 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 15 feet]]) __Damage__ 2d8+8 bludgeoning plus Grab"
  - name: "Melee"
    desc: "⬻ tentacle +18 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 10 feet]]) __Damage__ 2d6+8 piercing plus confounding slam"
abilities_bot:
  - name: "Adaptive Strike"
    desc: "⭓ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Polymorph|Polymorph]]) The naunet chooses adamantine, cold iron, or silver; its melee Strikes count as that type for 1 minute or until it uses Adaptive Strike again."
  - name: "Change Shape"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Polymorph|Polymorph]]) The naunet can take the appearance of any Small, Medium, or Large [[srd/pf2e/compendium/rules-elements/traits/player-core/Animal|animal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Beast|beast]], or [[srd/pf2e/compendium/rules-elements/traits/player-core/Humanoid|humanoid]]. This doesn't change its Speed or its attack and damage bonuses with its Strikes but might change the damage type its Strikes deal."
  - name: "Confounding Slam"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|Mental]]) A creature hit by the naunet's tentacle Strike is [[srd/pf2e/compendium/rules-elements/Conditions#Stupefied|stupefied 2]] for 1d4 rounds (DC 25 Will negates). If the creature was already stupefied in this way, the duration extends by 1 round instead."
  - name: "Constrict"
    desc: "⬻ 1d8+8 bludgeoning, DC 22"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 25 - __2nd__ [[srd/pf2e/compendium/spells/rank-2/Mist|Mist]] (at will) - __3rd__ [[srd/pf2e/compendium/spells/rank-2/Shatter|Shatter]] (at will) - __4th__ [[srd/pf2e/compendium/spells/rank-2/Acid Grip|Acid Grip]], [[srd/pf2e/compendium/spells/rank-3/Vampiric Feast|Vampiric Feast]] - __5th__ [[srd/pf2e/compendium/spells/rank-4/Translocate|Translocate]] - __Constant (4th)__ [[srd/pf2e/compendium/spells/rank-4/Unfettered Movement|Unfettered Movement]]"
sourcebook: "_Monster Core 2_, page 259."
```

```encounter-table
name: Naunet
creatures:
  - 1: Naunet
```
