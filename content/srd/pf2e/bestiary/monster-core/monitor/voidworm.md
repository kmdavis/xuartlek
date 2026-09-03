---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Voidworm"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/monitor
  - pf2e/creature/trait/protean
  - pf2e/creature/trait/tiny
statblock: inline
name: "Voidworm"
level: 1
source: "Monster Core"
aon_id: "creature-3144"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3144"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Voidworm"
level: "Creature 1"
size: "Tiny"
trait_01: "Monitor"
trait_02: "Protean"
modifier: 4
perception:
  - name: "Perception"
    desc: "Perception +4; entropy sense (imprecise) 30 feet, darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Chthonian|Chthonian]], Protean"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +7, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +6, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +4, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +7"
abilityMods: [-1, 4, 0, -1, -1, 1]
abilities_top:
  - name: "Entropy Sense"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/prediction|prediction]]) A voidworm can anticipate the most likely presence of a creature through a supernatural insight into chaotic probabilities and chance. This grants them the ability to sense creatures within the listed range. [[srd/pf2e/compendium/spells/rank-3/veil-of-privacy|_Veil of privacy_]] prevents a creature from being detected via entropy sense automatically (without a counteract check)."
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +5; __Ref__: +9; __Will__: +6"
hp: 16
health:
  - name: "HP"
    desc: "16 (fast healing 1); __Resistances__ precision 3, protean anatomy 5"
abilities_mid:
  - name: "Protean Anatomy"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]]) A voidworm's vital organs shift and change shape and position constantly. Immediately after the voidworm takes acid, electricity, or sonic damage, they gain the listed amount of resistance to that damage type. This lasts for 1 hour or until the next time the protean takes damage of one of the other types (in which case their resistance changes to match that type), whichever comes first. The voidworm is immune to [[srd/pf2e/compendium/rules-elements/traits/player-core/polymorph|polymorph]] effects unless they're a willing target. If [[srd/pf2e/compendium/rules-elements/conditions#Blinded|blinded]] or [[srd/pf2e/compendium/rules-elements/conditions#Deafened|deafened]], the voidworm automatically recovers at the end of their next turn as new sensory organs grow to replace the compromised ones."
speed: "20 feet, fly 40 feet; unfettered movement"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 0 feet]]) __Damage__ 1d8+1 piercing"
  - name: "Melee"
    desc: "⬻ tail +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 0 feet]]) __Damage__ 1d4+1 slashing plus confounding lash"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/polymorph|Polymorph]]) The voidworm takes on the appearance of a Tiny [[srd/pf2e/compendium/rules-elements/traits/player-core/animal|animal]]. This doesn't change their Speed or their attack and damage bonuses with their Strikes but might change the damage type their Strikes deal."
  - name: "Confounding Lash"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]]) A creature hit by the voidworm's tail Strike is [[srd/pf2e/compendium/rules-elements/conditions#Stupefied|stupefied 1]] for 1 round (stupefied 2 on a critical hit). A successful DC 16 Will save negates this effect and grants temporary immunity to confounding lash for 1 minute."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 16 - __Cantrips (4th)__ [[srd/pf2e/compendium/spells/cantrips/figment|Figment]], [[srd/pf2e/compendium/spells/cantrips/light|Light]], [[srd/pf2e/compendium/spells/cantrips/prestidigitation|Prestidigitation]] - __2nd__ [[srd/pf2e/compendium/spells/rank-2/blur|Blur]] (self only), [[srd/pf2e/compendium/spells/rank-2/mist|Mist]] - __4th__ [[srd/pf2e/compendium/spells/rank-4/read-omens|Read Omens]] - __Constant (4th)__ [[srd/pf2e/compendium/spells/rank-4/unfettered-movement|Unfettered Movement]]"
sourcebook: "_Monster Core_, page 270."
```

```encounter-table
name: Voidworm
creatures:
  - 1: Voidworm
```
