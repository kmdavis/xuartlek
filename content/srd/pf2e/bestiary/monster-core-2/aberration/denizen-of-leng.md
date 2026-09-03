---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Denizen Of Leng"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/aberration
  - pf2e/creature/trait/dream
  - pf2e/creature/trait/medium
statblock: inline
name: "Denizen Of Leng"
level: 8
source: "Monster Core 2"
aon_id: "creature-4323"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4323"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Denizen Of Leng"
level: "Creature 8"
size: "Medium"
trait_01: "Aberration"
trait_02: "Dream"
modifier: 17
perception:
  - name: "Perception"
    desc: "Perception +17; darkvision"
languages: "Aklo; _truespeech_"
skills:
  - name: "Skills"
    desc: "Acrobatics +15, Athletics +15, Deception +19, Occultism +18, Sailing Lore +20, Stealth +17, Thievery +17"
abilityMods: [3, 3, 4, 6, 3, 5]
abilities_top:
  - name: "Items"
    desc: "_+1 striking kukri_, Leng ruby worth 30 gp"
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +16; __Ref__: +19; __Will__: +17"
hp: 100
health:
  - name: "HP"
    desc: "100 (planar fast healing 5); __Immunities__ cold; __Resistances__ critical hits 10, precision 10"
abilities_mid:
  - name: "No Breath"
    desc: "Denizens of Leng don't need to breathe."
  - name: "Planar Fast Healing"
    desc: "A denizen of Leng maintains a connection to Leng at all times, and when away from Leng, they have fast healing 5. They lose this ability in Leng or in areas where planar connections do not function. If killed, their body dissolves into nothingness in 1d4 rounds, leaving behind their equipment. A slain denizen reforms in Leng; they can be permanently killed only when their planar fast healing doesn't function."
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _kukri_ +18 (Agile, finesse, magical, trip) __Damage__ 2d6+6 slashing plus 1d6 persistent bleed"
  - name: "Melee"
    desc: "⬻ jaws +17 (Agile, finesse) __Damage__ 2d10+6 piercing plus debilitating bite"
abilities_bot:
  - name: "Debilitating Bite"
    desc: "(Curse, occult) A creature that takes damage from a denizen's bite must succeed at a DC 25 Fortitude save or become clumsy 1. Each time a target fails an additional save against this ability, the condition value increases by 1 (to a maximum of clumsy 4). This condition value decreases by 1 every 24 hours."
  - name: "Leng Ruby"
    desc: "(Occult) Many denizens of Leng carry strange rubies mined from quarries in Leng. As long as a creature holds a Leng ruby that it willingly accepted as a gift or payment from a denizen of Leng, any denizen of Leng can target that creature with _mind reading_, _outcast's curse_, or _phantom pain_ at a range of 1 mile, and the bearer uses an outcome one degree of success worse than the result of its saving throw against outcast's curse. Leng Known variously as the Nightmare Realm or the Terror Beyond Dreams, the frozen Plateau of Leng looms physically and spiritually above the Dreamlands. Both a part of that dimension and a corruption of it, Leng is a realm inhabited by eldritch horrors and ruled by the horrors' ancient gods."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 26 - __Cantrips (4th)__ Detect Magic, Telekinetic Hand, Message, Read Aura, Void Warp - __2nd__ Blur - __3rd__ Hypnotize, Levitate, Locate, Mind Reading - __4th__ Outcast's Curse, Phantom Pain, Suggestion - __Constant (5th)__ Truespeech"
sourcebook: "_Monster Core 2_, page 96."
```

```encounter-table
name: Denizen Of Leng
creatures:
  - 1: Denizen Of Leng
```
