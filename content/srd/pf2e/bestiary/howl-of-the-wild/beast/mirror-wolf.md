---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Mirror Wolf"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/incorporeal
  - pf2e/creature/trait/spirit
  - pf2e/creature/trait/medium
statblock: inline
name: "Mirror Wolf"
level: 7
source: "Howl of the Wild"
aon_id: "creature-3312"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3312"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Mirror Wolf"
level: "Creature 7"
size: "Medium"
trait_01: "Beast"
trait_02: "Incorporeal"
trait_03: "Spirit"
modifier: 18
perception:
  - name: "Perception"
    desc: "Perception +18; low-light vision, scent (imprecise) 30 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]; [[srd/pf2e/compendium/spells/rank-5/truespeech|_truespeech_]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +15, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +12, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +11, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +19, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +17"
abilityMods: [3, 6, 2, 1, 3, -2]
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +14; __Ref__: +19; __Will__: +15"
hp: 117
health:
  - name: "HP"
    desc: "117; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], precision; __Resistances__ all damage 7 (except [[srd/pf2e/compendium/rules-elements/traits/player-core/force|force]], [[srd/pf2e/compendium/equipment/runes/ghost-touch|_ghost touch_]], [[srd/pf2e/compendium/rules-elements/traits/player-core/spirit|spirit]], or [[srd/pf2e/compendium/rules-elements/traits/player-core/vitality|vitality]]; double resistance vs. non-magical)"
abilities_mid:
  - name: "Visage Strike"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature adjacent to the mirror wolf's visages damages mirror wolf's ally"
  - name: "Effect"
    desc: "The mirror wolf teleports to the visage's spot, destroying the visage, and makes a jaws Strike."
speed: "35 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +17 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]]) __Damage__ 2d8+8 force plus Knockdown"
abilities_bot:
  - name: "Bond with Mortal"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]])"
  - name: "Frequency"
    desc: "once per day"
  - name: "Effect"
    desc: "The spirit guide spends 10 minutes to form a bond with a mortal creature. While the bond exists, the spirit guide increases their current and maximum Hit Points by 14, gains a +2 status bonus to their attack and damage rolls, and can communicate telepathically with the bonded mortal as long as the two beings are on the same plane. The spirit guide can only be bonded with one mortal at a time, and they can take this action again to end the bond or to form a new bond (which also ends the old bond). The bond also ends if the spirit guide or the mortal dies. This bond strengthens the spirit guide's connection to [[srd/pf2e/compendium/gm/planes#The Universe|the Universe]]. While bonded, the spirit guide loses the [[srd/pf2e/compendium/rules-elements/traits/gm-core/incorporeal|incorporeal]] and [[srd/pf2e/compendium/rules-elements/traits/player-core/spirit|spirit]] traits, loses their immunity to disease, paralysis, and poison, along with their resistance to all damage, and changes their Strikes to deal the appropriate amount of physical damage (typically piercing or slashing) instead of force damage."
  - name: "Strafing Strike"
    desc: "⬺ The mirror wolf makes a jaws Strike against a creature within range. The mirror wolf can then Stride and make a second jaws Strike against the same creature."
  - name: "Bonded Strike"
    desc: "⬺"
  - name: "Requirements"
    desc: "The mirror wolf is currently Bonded with a Mortal"
  - name: "Effect"
    desc: "The mirror wolf makes a jaws Strike. If this attack hits, the bonded mortal can spend their reaction to Strike the same target."
  - name: "Lingering Assailant"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/illusion|Illusion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/visual|Visual]]) The mirror wolf attacks with such speed it leaves a visage of itself behind. When the mirror wolf Strikes, they leave behind a visage in an adjacent square. The visage is treated as an ally for effects such as flanking and pack attack. A visage has AC 10 and 1 HP and lasts for 1 round."
  - name: "Pack Attack"
    desc: "The mirror wolf's Strikes deal 1d8 extra damage to creatures within reach of at least two of the mirror wolf's allies."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 22 - __3rd__ [[srd/pf2e/compendium/spells/rank-2/revealing-light|Revealing Light]] - __Constant (5th)__ [[srd/pf2e/compendium/spells/rank-5/truespeech|Truespeech]]"
sourcebook: "_Howl of the Wild_, page 183."
```

```encounter-table
name: Mirror Wolf
creatures:
  - 1: Mirror Wolf
```
