---
obsidianUIMode: preview
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
aon_id: "creature-4518"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4518"
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
    desc: "Perception +14; darkvision, entropy sense (imprecise) 30 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Chthonian|Chthonian]], [[srd/pf2e/compendium/rules-elements/languages#Empyrean|Empyrean]], Protean"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +14, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +16, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +16, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +14, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +12"
abilityMods: [5, 3, 5, 0, 3, 3]
abilities_top:
  - name: "Entropy Sense"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/prediction|prediction]]) A protean can anticipate the most likely presence of a creature through a supernatural insight into chaotic probabilities and chance. This grants them the ability to sense creatures within the listed range. [[srd/pf2e/compendium/spells/rank-3/veil-of-privacy|_Veil of privacy_]] prevents a creature from being detected via entropy sense automatically (without a counteract check)."
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +18; __Ref__: +14; __Will__: +12 +1 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magic]]"
hp: 120
health:
  - name: "HP"
    desc: "120 (fast healing 2); __Resistances__ precision 5, protean anatomy 10"
abilities_mid:
  - name: "Protean Anatomy"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]]) A protean's vital organs shift and change shape and position constantly. Immediately after the protean takes acid, electricity, or sonic damage, they gain the listed amount of resistance to that damage type. This lasts for 1 hour or until the next time the protean takes damage of one of the other types (in which case their resistance changes to match that type), whichever comes first. The protean is immune to polymorph effects unless they're a willing target. If [[srd/pf2e/compendium/rules-elements/conditions#Blinded|blinded]] or [[srd/pf2e/compendium/rules-elements/conditions#Deafened|deafened]], the protean automatically recovers at the end of their next turn as new sensory organs grow to replace the compromised ones."
speed: "25 feet, fly 30 feet, swim 25 feet; unfettered movement"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +18 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 2d10+8 piercing"
  - name: "Melee"
    desc: "⬻ tail +18 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 2d8+8 bludgeoning plus Grab"
  - name: "Melee"
    desc: "⬻ tentacle +18 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 2d6+8 piercing plus confounding slam"
abilities_bot:
  - name: "Adaptive Strike"
    desc: "⭓ ([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/polymorph|Polymorph]]) The naunet chooses adamantine, cold iron, or silver; its melee Strikes count as that type for 1 minute or until it uses Adaptive Strike again."
  - name: "Change Shape"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/polymorph|Polymorph]]) The naunet can take the appearance of any Small, Medium, or Large [[srd/pf2e/compendium/rules-elements/traits/player-core/animal|animal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/beast|beast]], or [[srd/pf2e/compendium/rules-elements/traits/player-core/humanoid|humanoid]]. This doesn't change its Speed or its attack and damage bonuses with its Strikes but might change the damage type its Strikes deal."
  - name: "Confounding Slam"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]]) A creature hit by the naunet's tentacle Strike is [[srd/pf2e/compendium/rules-elements/conditions#Stupefied|stupefied 2]] for 1d4 rounds (DC 25 Will negates). If the creature was already stupefied in this way, the duration extends by 1 round instead."
  - name: "Constrict"
    desc: "⬻ 1d8+8 bludgeoning, DC 22"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 25 - __2nd__ [[srd/pf2e/compendium/spells/rank-2/mist|Mist]] (at will) - __3rd__ [[srd/pf2e/compendium/spells/rank-2/shatter|Shatter]] (at will) - __4th__ [[srd/pf2e/compendium/spells/rank-2/acid-grip|Acid Grip]], [[srd/pf2e/compendium/spells/rank-3/vampiric-feast|Vampiric Feast]] - __5th__ [[srd/pf2e/compendium/spells/rank-4/translocate|Translocate]] - __Constant (4th)__ [[srd/pf2e/compendium/spells/rank-4/unfettered-movement|Unfettered Movement]]"
sourcebook: "_Monster Core 2_, page 259."
```

```encounter-table
name: Naunet
creatures:
  - 1: Naunet
```
